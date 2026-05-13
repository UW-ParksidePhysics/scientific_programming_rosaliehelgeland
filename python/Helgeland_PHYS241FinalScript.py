#IMPORTS

import numpy as np 
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt 
from scipy import stats
from datetime import date
from scipy import constants
from read_two_columns_text import read_two_columns_text
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from equations_of_state import fit_equation_of_state, murnaghan, birch_murnaghan, vinet
from annotate_plot import annotate_plot


#PARAMETERS

display_graph = False

today = date.today().isoformat()

equation_of_state = 'vinet'

fit_point_number = 110

test_data_path = "/work/scientific_programming_rosaliehelgeland/python/Si.Fd-3m.GGA-PBE.volumes_energies.dat"

test_file_name = "Si.Fd-3m.GGA-PBE.volumes_energies.dat"

#FUNCTIONS


def parse_file_name(file_name):

    file_name_array = np.array(file_name, dtype = str)

    split_array = file_name.split('.')

    chemical_symbol = split_array[0]
    crystal_symmetry_symbol = split_array[1]
    density_functional_exchange_acronym = split_array[2]
    
    return chemical_symbol, crystal_symmetry_symbol, density_functional_exchange_acronym



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
    




if __name__ == '__main__':

    chemical_symbol, crystal_symmetry_symbol, density_functional_exchange_acronym = parse_file_name(test_file_name)

    test_data = read_two_columns_text(test_data_path)
    test_data_column_by_row = test_data.transpose()

    dataset_statistics = calculate_bivariate_statistics(test_data_column_by_row)
    dataset_statistics_row_by_column = dataset_statistics.transpose()


    datas_quadratic_polynomial = calculate_quadratic_fit(test_data_column_by_row)

    volumes = test_data[:, 0] #bohr^3/atom
    energies = test_data[:, 1] #rydberg/atom
    
    
    equation_fit_curve, equation_parameters = fit_equation_of_state(
        volumes, energies, datas_quadratic_polynomial, 
        equation_of_state, fit_point_number
    )

    fit_curve_volumes = np.linspace(
        np.min(volumes),
        np.max(volumes),
        num=fit_point_number
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
