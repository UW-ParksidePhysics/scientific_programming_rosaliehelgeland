#IMPORTS

import numpy as np 
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt 
from scipy import stats
from datetime import date

#PARAMETERS

display_graph = False
today = date.today().isoformat()
equation_of_state = 'vinet'
fit_point_number = 110

#FUNCTIONS

def parse_file_name(file_name):

    file_name_array = np.array(file_name, dtype = str)

    split_array = file_name.split('.')

    chemical_symbol = split_array[0]
    crystal_symmetry_symbol = split_array[1]
    density_functional_exchange_acronym = split_array[2]
    
    return chemical_symbol, crystal_symmetry_symbol, density_functional_exchange_acronym


__author__ = "rosie"

def read_two_columns_text(filename: str) -> np.ndarray:
    try:
        data = np.loadtxt(filename)
        return data
    except OSError as error:
        print(f"{filename} not found!")


__author__ = "Rosie"

def calculate_bivariate_statistics(data):
    """
    Parameters:
        data: ndarray, shape (2, M)
            x-y data to be characterized. M is the number of data points.
    Returns:
        statistics: ndarray, shape (6,)
            Mean of y, standard deviation of y, minimum x-value, maximum x-value, minimum y-value, maximum y-value. 
            Use scipy.stats.describe to obtain the descriptive statistics for the y-values, 
            but return only these six requested values in this order.
            Use the square root of the sample variance returned by stats.describe for the standard deviation.
    Raises:
        IndexError
            When the data array has inappropriate dimensions, including anything other than 2 rows or fewer than 2 columns.
    """
    if data.ndim != 2:
       raise ValueError("Data must be 2D!")

    row_number, column_number = data.shape

    if row_number != 2:
        raise IndexError(f"Number of rows ({row_number}) does not equal 2!")
    
    if column_number <2:
        raise IndexError(f"This code needs at least 2 columns! You have {column_number} columns!")
    
    else:

        x_statistics = stats.describe(data[0])
        y_statistics = stats.describe(data[1])


        def calculate_standard_deviation(sample_variance):
            standard_deviation = np.sqrt(sample_variance)
            return standard_deviation
    

        statistics = np.array([
            y_statistics.mean,
            calculate_standard_deviation(y_statistics.variance),
            x_statistics.minmax[0],
            x_statistics.minmax[1],
            y_statistics.minmax[0],
            y_statistics.minmax[1]
        ])

        return statistics



__author__ = "Fabian"

def calculate_quadratic_fit(data):
    """
    Parameters:
        data: ndarray, shape (2, M)
            x-y data to be fit. M is the number of data points.
    Returns:
        quadratic_coefficients: ndarray, shape (3,)
            Quadratic polynomial coefficients, ordered constant term first, then linear term, and quadratic term last.
    Raises:
        IndexError
            When the data array has inappropriate dimensions, including anything other than 2 rows or too few columns to fit a quadratic polynomial. 
    """

    if len(data) != 2:
        raise IndexError(f'Data has incorrect length of {len(data)}')
    elif len(data[0]) < 3:
        raise IndexError(f'Data has too short a length of {len(data[0])}')


    import numpy.polynomial.polynomial as polynomial

    return polynomial.polyfit(data[0], data[1], 2)    



def fit_equation_of_state(volumes, energies, quadratic_coefficients, equation_of_state='vinet', number_of_points=50):
    """
    Returns a NumPy array of values evaluated to an equation of state fit
    :param volumes:                 NumPy array(N) :: volumes (x-values) to be fit
    :param energies:                NumPy array(N) :: energies (y-values) to be fit
    :param quadratic_coefficients:  list(3) :: coefficients of the quadratic polynomial already fit to the data
    :param equation_of_state:                     str :: equation of state name ('murnaghan', 'birch-murnaghan', 'vinet')
    :param number_of_points:        int, optional :: number of points to evaluate fit function on
    :return:                        NumPy array(number_of_points) :: equation of state fit evaluated on grid,

    starting at volumes[0] and ending at volume[-1]
    """
    from scipy.optimize import curve_fit

    # Dictionary holding lambda functions from current module.
    lambda_dictionary = {
        'vinet': globals()['vinet'],
        'murnaghan': globals()['murnaghan'],
        'birch-murnaghan': globals()['birch_murnaghan']
    }

    # Get extremes of data and calculate range

    minimum_volume = np.amin(volumes)
    maximum_volume = np.amax(volumes)

    # for y = c0 + c1 x + c2 x^2
    #   axis of symmetry: x = -c1 / (2 c2)
    quadratic_axis_of_symmetry = -quadratic_coefficients[1] / (2 * quadratic_coefficients[2])
    #   minimum: y = -c1^2 / (4 c2)  + c0
    quadratic_minimum = -quadratic_coefficients[1] ** 2 / (4 * quadratic_coefficients[2]) + quadratic_coefficients[0]
    #   bulk modulus: K_0 = 2 * a / V_0 for E(V) = c2*V^2 + c1*V + E0
    quadratic_bulk_modulus = 2. * quadratic_coefficients[2] / quadratic_axis_of_symmetry

    bulk_modulus_derivative = 3.7

    # Get realistic equation of state fit

    initial_parameters = [quadratic_minimum, quadratic_bulk_modulus,
                          bulk_modulus_derivative, quadratic_axis_of_symmetry]

    equation_parameters, equation_covariances = curve_fit(lambda_dictionary[equation_of_state.lower()], volumes, energies,
                                                p0=initial_parameters, method='trf')  # ,
    # x_scale=[10**np.floor(np.log10(np.amin(np.abs(energies)))), 100, 1,
    #         10**np.floor(np.log10(np.amin(np.abs(volumes))))])
    fit_curve_volumes = np.linspace(minimum_volume, maximum_volume, num=number_of_points)
    equation_fit_curve = lambda_dictionary[equation_of_state.lower()](fit_curve_volumes,
                                                                 equation_parameters[0], equation_parameters[1], equation_parameters[2],
                                                                 equation_parameters[3])

    return fit_curve_volumes, equation_fit_curve, equation_parameters


def murnaghan(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume):
    """
    Murnaghan equation of state: E(V) = E_0 + K_0 V_0 [ (1 / (K_0' (K_0' - 1))) (V / V_0)^(-(K_0' - 1)) +
                                                        (1 / K_0') (V / V_0) -

                                                        (1 / (K_0' - 1)) ]

    :param volumes:                 NumPy array of volumes per atom

    :param equilibrium_energy:      equilibrium energy E_0

    :param bulk_modulus:            bulk modulus K_0 = ∂^E/(∂V)^2 / V_0

    :param bulk_modulus_derivative: pressure derivative of bulk modulus ∂K_0/∂P

    :param equilibrium_volume:      equilibrium volume V_0

    :return:                        NumPy array of Murnaghan equation of state values at input volumes
    """
    k0pm1 = bulk_modulus_derivative - 1.0  # K_0' - 1
    return equilibrium_energy + (bulk_modulus * equilibrium_volume *
                                 (((1.0 / (bulk_modulus_derivative * k0pm1)) *
                                   np.power((volumes / equilibrium_volume), (-k0pm1))) +
                                  (volumes / (bulk_modulus_derivative * equilibrium_volume)) - (1.0 / k0pm1)))


def birch_murnaghan(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume):
    """
    Birch-Murnaghan equation of state: E(V) = E_0 + (9/16) K_0 V_0 {[ (V / V_0)^(-(2/3)) - 1 ]^3 K_0' +
                                                                    [ (V / V_0)^(-(2/3)) - 1]^2 *
                                                                    [ 6 - 4 (V / V_0)^(-(2/3)) ]}

    :param volumes:                 NumPy array of volumes per atom

    :param equilibrium_energy:      equilibrium energy E_0

    :param bulk_modulus:            bulk modulus K_0 = ∂^E/(∂V)^2 / V_0

    :param bulk_modulus_derivative: pressure derivative of bulk modulus ∂K_0/∂P

    :param equilibrium_volume:      equilibrium volume V_0

    :return:                        NumPy array of the Birch-Murnaghan equation of state values at input volumes
    """
    reduced_volume_area = np.power(volumes / equilibrium_volume, -2. / 3.)
    return equilibrium_energy + (9. * bulk_modulus * equilibrium_volume / 16.) * (
            np.power(reduced_volume_area - 1., 3.) * bulk_modulus_derivative +
            np.power(reduced_volume_area - 1., 2.) * (6. - 4. * reduced_volume_area))


def vinet(volumes, equilibrium_energy, bulk_modulus, bulk_modulus_derivative, equilibrium_volume):
    """
    Vinet equation of state: E(V) = E_0 + (2 K_0 V_0 / (K_0' - 1)^2) *
                                        - {2 - [5 + 3 (V / V_0)^(1/3) (K_0' - 1) - 3 K_0']
                                               exp(- (3/2) (K_0' - 1) (1 - (V / V_0)^(1/3))})

    :param volumes:                 NumPy array of volumes per atom

    :param equilibrium_energy:      equilibrium energy E_0

    :param bulk_modulus:            bulk modulus K_0 = ∂^E/(∂V)^2 / V_0

    :param bulk_modulus_derivative: pressure derivative of bulk modulus ∂K_0/∂P

    :param equilibrium_volume:      equilibrium volume V_0

    :return: NumPy array of the Vinet equation of state values at input volumes
    """
    k0pm1 = bulk_modulus_derivative - 1  # K_0' - 1
    k0pm1_squared = np.power(k0pm1, 2)
    reduced_volume_lengths = np.cbrt(volumes / equilibrium_volume)

    exponential_argument = -1.5 * k0pm1 * (reduced_volume_lengths - 1.)
    try:
        exponential_factor = np.exp(exponential_argument)
        vinet_eos = equilibrium_energy + \
                    (2. * bulk_modulus * equilibrium_volume / k0pm1_squared) * \
                    (2. - (5. + 3. * reduced_volume_lengths * k0pm1 - 3 * bulk_modulus_derivative) *
                     exponential_factor)
    except:
        # assuming the failure is the exponential factor
        vinet_eos = equilibrium_energy + \
                    (2. * bulk_modulus * equilibrium_volume / k0pm1_squared) * \
                    (2. - (5. + 3. * reduced_volume_lengths * k0pm1 - 3 * bulk_modulus_derivative))

    return vinet_eos

from scipy import constants

def convert_units(value, starting_unit, desired_unit):
    """
    Convert that data and fit from atomic units 
        (cubic bohr per atom, #Bohr radius
        rydberg per atom, #Rydberg constant times hc in eV
        and rydberg per cubic bohr)
    to these units using a module you write called convert_units (use SciPy constants to get the values):
        volume: cubic angstroms / atom   
        energy: electron volts / atom 
        bulk modulus(second parameter in fit): gigapascals
    This function should take three arguments: 
        the value to be converted, 
        the units of the value to be converted from, 
        the units to be converted to, 
    the function should return the value in the requested units. 
    Show in the test cases in the if __name__ ==  "__main__": block that:
        1.  1 cubic bohr per atom equals 0.14818471147216278 cubic angstroms per atom, #angstrom
        2.  1 rydberg per atom equals 13.605693122994 electron volts per atom, and
        3.  1 rydberg per cubic bohr equals 14710.507848260711 gigapascals.
    """
    if starting_unit == "bohr^3" and desired_unit=="angstrom^3":

        bohr = float(constants.physical_constants["Bohr radius"][0])
        angstrom = float(constants.angstrom)

        conversion_ratio = bohr/angstrom

        return value * conversion_ratio**3

    elif starting_unit == "rydberg" and desired_unit == "eV":

        conversion_ratio = constants.physical_constants["Rydberg constant times hc in eV"][0]

        return value * conversion_ratio
    
    elif starting_unit == 'rydberg/bohr^3' and desired_unit == 'GPa':

        joules_from_rydberg = constants.physical_constants["Rydberg constant times hc in J"][0]

        bohr = constants.physical_constants["Bohr radius"][0]

        pascals_conversion = joules_from_rydberg/(bohr**3)

        gigapascals_conversion = pascals_conversion / 10**9 #GPa

        return gigapascals_conversion * value
    
    else:
        raise ValueError("unsupported conversion!")
    

__author__ = "rosie"


def annotate_plot(annotations: dict) -> list:
    annotate_objects = []
    try:
        for label, value in annotations.items():
            position = value["position"]
            alignment= value["alignment"]
            fontsize = value["fontsize"]

            annotation = plt.text(
                position[0],
                position[1],
                label,
                ha = alignment[0],
                va = alignment[1],
                fontsize = fontsize
            )

            annotate_objects.append(annotation)

        return annotate_objects
    except KeyError as error:
        print(f"required key missing from annotation dictionary!")

    



if __name__ == '__main__':
    test_data_path = "/work/scientific_programming_rosaliehelgeland/python/Si.Fd-3m.GGA-PBE.volumes_energies.dat"

    test_file_name = "Si.Fd-3m.GGA-PBE.volumes_energies.dat"

    chemical_symbol, crystal_symmetry_symbol, density_functional_exchange_acronym = parse_file_name(test_file_name)

    test_data = read_two_columns_text(test_data_path)
    test_data_column_by_row = test_data.transpose()

    dataset_statistics = calculate_bivariate_statistics(test_data_column_by_row)
    dataset_statistics_row_by_column = dataset_statistics.transpose()


    datas_quadratic_polynomial = calculate_quadratic_fit(test_data_column_by_row)

    volumes = test_data[:, 0] #bohr^3/atom
    energies = test_data[:, 1] #rydberg/atom
    
    
    fit_curve_volumes, equation_fit_curve, equation_parameters = fit_equation_of_state(
        volumes, energies, datas_quadratic_polynomial, 
        equation_of_state, fit_point_number
    )

    equilibrium_volume = equation_parameters[3]

    bulk_modulus = equation_parameters[1] #rydberg/bohr

    print(f'1 cubic bohr per atom equals 0.14818471147216278 cubic angstroms per atom, and my function returns: {convert_units(1, "bohr^3", "angstrom^3")} cubic angstroms per atom.')
    print(f'1 rydberg per atom equals 13.605693122994 electron volts per atom, and my function returns: {convert_units(1, "rydberg", "eV")} electron volts per atom.')
    print(f'1 rydberg per cubic bohr equals 14710.507848260711 gigapascals, and my function returns: {convert_units(1, "rydberg/bohr^3", "GPa")} gigapascals.')

    converted_volumes = convert_units(volumes, "bohr^3", "angstrom^3")
    converted_energies = convert_units(energies, "rydberg", "eV")
    converted_bulk_modulus = convert_units(bulk_modulus, "rydberg/bohr^3", "GPa")
    converted_fit_volumes = convert_units(fit_curve_volumes, "bohr^3","angstrom^3")
    converted_fit_curve = convert_units(equation_fit_curve, "rydberg", "eV")
    converted_equilibrium_volumes = convert_units(equilibrium_volume, "bohr^3", "angstrom^3")


    fig, ax = plt.subplots(figsize = (8, 6))

    ax.scatter(converted_volumes, converted_energies, color='blue')
    ax.plot(converted_fit_volumes, converted_fit_curve, color='black')

    minimum_volume = np.min(converted_volumes) #x-minimum
    maximum_volume = np.max(converted_volumes) #x-max

    minimum_energy = np.min(converted_energies) #y-minimum
    maximum_energy = np.max(converted_energies) #y-maximum

    volume_range = maximum_volume - minimum_volume
    energy_range = maximum_energy - minimum_energy

    volume_padding = volume_range * 0.10
    energy_padding = energy_range * 0.10

    ax.vlines(converted_equilibrium_volumes, minimum_energy - energy_padding, np.min(converted_fit_curve), colors = 'black', linestyle = 'dashed')

    ax.set_xlim(
        minimum_volume - volume_padding,
        maximum_volume + volume_padding
    )

    ax.set_ylim(
        minimum_energy - energy_padding,
        maximum_energy + energy_padding
    )

    ax.set_xlabel(r"$V$ ($\mathrm{\AA^3/atom}$)")
    ax.set_ylabel(r"$E$ ($\mathrm{eV/atom}$)")


    x_left = minimum_volume - volume_padding + 0.02 * volume_range
    x_center = np.median(converted_fit_volumes)

    y_top = maximum_energy + energy_padding - 0.02 * energy_range
    y_bottom = minimum_energy - energy_padding + 0.02 * energy_range
    y_curve_top = np.max(converted_fit_curve)

    formatted_symmetry = crystal_symmetry_symbol.replace("-3", r"\bar{3}")

    annotations = {
        f"{chemical_symbol}":{
            "position": np.array([x_left, y_top]),
            "alignment": ("left", "top"),
            "fontsize": 10
        },

        f"${formatted_symmetry}$":{
            "position": np.array([x_center, y_curve_top]),
            "alignment": ("center", "bottom"),
            "fontsize": 10
        },
    
        f"$K_0$ = {converted_bulk_modulus:.1f} GPa":{
            "position": np.array([x_center, y_curve_top + 0.05 * energy_range]),
            "alignment": ("center", "bottom"),
            "fontsize": 10
        },

        f"Created by Rosie Helgeland on {today}":{
            "position": np.array([x_left, y_bottom]),
            "alignment": ("left", "bottom"),
            "fontsize": 10
        }
    
    }

    annotate_plot(annotations)

    ax.set_title(f"Vinet Equation of State for {chemical_symbol} in DFT {density_functional_exchange_acronym}", pad = 15)

    plt.tight_layout()

    if display_graph:
        plt.show()
    else:
        plt.savefig(f"Helgeland.{chemical_symbol}.{crystal_symmetry_symbol}.{density_functional_exchange_acronym}.{equation_of_state}EquationOfState.png", bbox_inches = "tight")
