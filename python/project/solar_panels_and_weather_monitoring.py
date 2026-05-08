#### RENAME THIS FILE
# Rename `project.py` to `(your_project_short_name).py`
# Example: `orbit_simulation.py`, `wave_packet.py`, `two_body_problem.py`

# -----------------------------------------------------------------------------
# PROJECT FILE STRUCTURE (CONTEMPORARY PYTHON BEST PRACTICES)
# -----------------------------------------------------------------------------
# The goal is clarity, testability, and “import safety” (importing your module
# should NOT start the simulation or pop up plots).
#
# Recommended top-to-bottom order:
# 1) Module docstring (100–200 words): what the project does, key assumptions,
#    inputs/outputs, and how to run it.
# 2) Imports (grouped per PEP 8).
# 3) Module-level constants (only if truly global and stable).
# 4) Function definitions (each with a PEP 257-compliant docstring).
# 5) main() function: the single clear entry point for running the program.
# 6) Script guard: if __name__ == "__main__": main()
#
# References:
# - PEP 8 (imports and general style): https://peps.python.org/pep-0008/  (see “Imports”)
# - SciPy physical constants (use inside functions when appropriate):
#   https://docs.scipy.org/doc/scipy/reference/constants.html
#
# -----------------------------------------------------------------------------
# IMPORTS: ORDER + PRACTICES (PEP 8)
# -----------------------------------------------------------------------------
# Put imports at the top, after the module docstring, before constants.
# Group imports in THIS order, separated by blank lines:
#   1) Standard library imports (e.g., math, pathlib, dataclasses)
#   2) Third-party imports (e.g., numpy, scipy, matplotlib, plotly)
#   3) Local/project imports (your own modules in this repo/package)






#
# Examples:
#   # 1) Standard library
#   from __future__ import annotations
#   from dataclasses import dataclass
#   from pathlib import Path
#
#   # 2) Third-party
#   import numpy as np
#   from scipy import constants as scipy_constants
#
#   # 3) Local imports (if your project is a package)
#   # from .helpers import integrate
#
# Avoid:
# - wildcard imports: `from module import *`
# - hiding heavy work at import time (reading big files / launching plots)
#
# -----------------------------------------------------------------------------
# SIMULATION / VISUALIZATION FUNCTIONS (FUNCTIONAL STYLE)
# -----------------------------------------------------------------------------
# Keep “work” inside functions. This makes your code testable and reusable.
#
# Typical breakdown:
# - read_data(...): load/validate input data

#file locations stored in tuple
# - compute_derived_parameters(...): compute values that depend on inputs
# - simulate(...): compute arrays / time series (no plotting)
# - build_figure(...): create a plot/animation object (no file I/O)
# - save_outputs(...): optional, write files if required
#
# Each function must have:
# - clear, full-word parameter names (PEP 8: lower_case_with_underscores)
# - units in comments or docstrings (meters, seconds, kg, etc.)
# - a docstring describing: parameters, returns, and assumptions
#
# -----------------------------------------------------------------------------
# SciPy CONSTANTS: WHERE TO USE THEM
# -----------------------------------------------------------------------------
# Prefer importing SciPy constants inside the function that uses them, so the
# dependency is obvious and to keep module import fast/lightweight.
#
# Example pattern (inside a function):
#   from scipy import constants as scipy_constants
#   speed_of_light = scipy_constants.c
#
# Docs: https://docs.scipy.org/doc/scipy/reference/constants.html
#
# -----------------------------------------------------------------------------
# main(): THE STANDARD ENTRY POINT
# -----------------------------------------------------------------------------
# It is now standard practice to put the “run the program” logic in a main()
# function and call it under the script guard. This prevents side effects when
# importing your module.
#
# Skeleton:
#   def main() -> None:
#       """Run the simulation and display/save results."""
#       # 1) Define simulation parameters (with units)
#       # 2) Compute derived parameters
#       # 3) Call read_data / simulate / build_figure
#       # 4) Show or save outputs
#
#   if __name__ == "__main__":
#       main()
#
# -----------------------------------------------------------------------------
# PRIMARY SIMULATION FUNCTION STRUCTURE (SUGGESTED)
# -----------------------------------------------------------------------------
# Inside your primary simulation function (often called by main()):
# 1) Parameters (named clearly, units documented)
# 2) Derived parameters (computed from inputs)
# 3) Call helpers for:
#    - data read-in / validation
#    - simulation computation
#    - visualization creation
# 4) Return results (arrays, figure objects) instead of printing everything
#
# Keep plotting separate from physics/math wherever INGr_.(i)ntEDees ng NCON 



def create_data_array(file_location):
    """
    imports data in csv files and converts the data to arrays, 
    uses those arrays to store time values as strptime values for easy access and consistent data
    stores arrays in dictionaries 
    """

    import numpy as np
    import datetime as datetime
    from datetime import datetime
    from astropy.time import Time

    arr = np.genfromtxt(file_location, delimiter=',',dtype=str)

    
    headings = arr[0]

    data = arr[1:]


    # DATE FUNCTIONS

    if headings[0] == "Date":

        times = Time([
            datetime.strptime(d, "%Y-%m-%d")
            for d in data[:,0]
        ])

    
    elif headings[0] == "YEAR":

       times = Time([
           datetime(int(y), int(m), int(d))
           for y, m, d in data[:, :3]
       ])


    elif "Site Time" in headings[0]:

        times = Time([
            datetime.strptime(t, "%m-%d-%Y %H:%M:%S")
            for t in data[:,0]
        ])

    else:
        raise ValueError("unknown file format")

    #--------------------------------------------------------

    # VALUE FUNCTIONS

    if headings[0] == "YEAR": 
        headings = headings[3:]
        raw_values = data[:, 3:]

    elif headings[0] == 'Date':
        headings = headings[1:]
        raw_values = data[:, 1:]

        
    else:
        headings = headings[1:]
        raw_values = data[:, 1:]
    

    clean_values = np.array([
        [x.strip().replace('"', '') for x in row]
        for row in raw_values
    ])

    clean_values[clean_values == ''] = np.nan
    clean_values[clean_values == 'M'] = -1
    clean_values[clean_values == 'T'] = 0
    clean_values[clean_values == '-999'] = np.nan

    values = clean_values.astype(float)

    return times, values, headings
            

#-------------------------------------------------------------------------
#DECIMAL TO TIME FUNCTION

def convert_decimals_to_time(arr):
    import numpy as np

    arr = np.mod(arr, 24)

    hours = np.floor(arr).astype(int)
    minutes = np.floor((arr-hours)*60).astype(int)

    vectorized = np.vectorize(lambda h, m: f'{h:02d}:{m:02d}')

    return vectorized(hours, minutes)


#-------------------------------------------------------------------------------
#STORING DATA NEEDED FOR GRAPHING AS SEPERATE ARRAYS 

def pull_and_store_data(values, headings, name, default = None):
    """
    pulls out specific data from column names by searching for the given name 
    then grouping the data and name together in an array,
    also "cleans" the headers by removing quotes so as to 
    not break the function. 
    """
    def clean_strings(heading):
        return heading.strip().replace("'","")
    
    clean_headings = [clean_strings(h) for h in headings]
    clean_name = clean_strings(name)

    for i, h in enumerate(clean_headings):
        if clean_name in h:
            return values[:, i]
    
    return default
    

#----------------------------------------------------------------------------

#calculating and storing solar geometry constants


def calculate_equation_of_time(N):
    import numpy as np

    B = np.radians((360/364.)*(N-81))

    ET = 9.87*np.sin(2*B)-7.53*np.cos(B)-1.5*np.sin(B)

    return ET



def calculate_hour_angles(solar_time_hours):
    import numpy as np
    return np.radians(15*(solar_time_hours - 12))



def calculate_declination_angles(n):
    import numpy as np

    return np.radians(
        23.45 * np.sin(np.radians((360/365)*  (284 + n)))
    )



def calculate_solar_altitudes(declination_angle, hour_angle, latitude):
    import numpy as np
    SA = np.arcsin(
        np.sin(declination_angle) * np.sin(latitude) + 
        np.cos(declination_angle) * np.cos(latitude) * np.cos(hour_angle)
    )
    return SA


def calculate_solar_zenith_angles(altitude):
    import numpy as np
    ZA = np.pi/2 - altitude

    return ZA


#CALCULATING IDEAL IRRADIANCE/POWER

def calculate_ideal_irradiances(altitude, I0=1361):
    import numpy as np
    IR = I0 * np.maximum(np.sin(altitude), 0)

    return IR



def compute_daily_average_daily_values(times, values):
    import numpy as np
    import datetime as datetime

    datetimes = times.to_datetime()

    dates = np.array([DT.date() for DT in datetimes])

    unique_dates = np.unique(dates)

    daily_average = []

    for date in unique_dates:
        matching_dates = dates == date

        daily_average.append(np.nanmean(values[matching_dates]))
    
    return unique_dates, np.array(daily_average)




#-----------------------------------------------------------------------------------------
# DEVELOPING FUNCTIONS TO PREVENT GRAPHING BUGS!!!!!!!!!
def compute_daily_average_values(times, values):
    """
    calculates daily average for data with hourly sets and makes
    sure that dates align through the use of a boolean function.
    stores averages in a list and then converts the list
    to an array for easy graphing
    """
    import numpy as np 
    import datetime as datetime

    datetimes = times.to_datetime()

    values = np.array(values).flatten()

    dates = np.array([dt.date() for dt in datetimes])

    unique_dates = np.unique(dates)

    if len(dates) == len(unique_dates):
        return dates, values

    daily_average = []

    for date in unique_dates:
        matching_dates = dates == date

        computable_dates = values[matching_dates]

        if computable_dates.size == 0 or np.all(np.isnan(computable_dates)):
            daily_average.append(np.nan)
        else:
            daily_average.append(np.nanmean(computable_dates))
    
    return unique_dates, np.array(daily_average)


def align_different_datasets_by_time(time_set1, time_set2, data_set1, data_set2):
    """
    aligns times in datasets for easy graphing 
    """
    times1 = np.array(time_set1)
    times2 = np.array(time_set2)

    common_times_for_computing = np.intersect1d(times1, times2)

    frame1 = np.isin(times1, common_times_for_computing)
    frame2 = np.isin(times2, common_times_for_computing)

    aligned_times = times1[frame1]

    aligned_values1 = data_set1[frame1]
    aligned_values2 = data_set2[frame2]

    return aligned_times, aligned_values1, aligned_values2

def normalize_arrays(arr):
    min_val = np.nanmin(arr)
    max_val = np.nanmax(arr)

    if max_val == min_val:
        return arr

    return (arr-min_val) / (max_val-min_val)

def align_three_sets_of_data(date_1, date_2, date_3, values_1, values_2, values_3):
    common_dates = np.intersect1d(np.intersect1d(date_1, date_2), date_3)

    frame_1 = np.isin(date_1, common_dates)
    frame_2 = np.isin(date_2, common_dates)
    frame_3 = np.isin(date_3, common_dates)

    return(
        common_dates,
        values_1[frame_1],
        values_2[frame_2],
        values_3[frame_3]
    )

def align_four_sets_of_data(date_1, date_2, date_3, date_4, values_1, values_2, values_3, values_4):
    common_dates = np.intersect1d(
        np.intersect1d(date_1, date_2),
        np.intersect1d(date_3, date_4)
    )

    frame_1 = np.isin(date_1, common_dates)
    frame_2 = np.isin(date_2, common_dates)
    frame_3 = np.isin(date_3, common_dates)
    frame_4 = np.isin(date_4, common_dates)

    return(
        common_dates,
        values_1[frame_1],
        values_2[frame_2],
        values_3[frame_3],
        values_4[frame_4]
    )

def align_all_data(date_1, date_2, date_3, date_4, date_5, values_1, values_2, values_3, values_4, values_5):
    common_dates = np.intersect1d(
        np.intersect1d(
            np.intersect1d(date_1, date_2), 
            np.intersect1d(date_3, date_4)
        ),
        date_5)

    frame_1 = np.isin(date_1, common_dates)
    frame_2 = np.isin(date_2, common_dates)
    frame_3 = np.isin(date_3, common_dates)
    frame_4 = np.isin(date_4, common_dates)
    frame_5 = np.isin(date_5, common_dates)

    return(
        common_dates,
        values_1[frame_1],
        values_2[frame_2],
        values_3[frame_3],
        values_4[frame_4],
        values_5[frame_5]
    )
#---------------------------------------------------------------------------------------------------------

def get_aligned_data(variable1, variable2):
    set1 = all_data[variable1]
    set2 = all_data[variable2]

    return align_different_datasets_by_time(set1["dates"], set2["dates"], set1["values"], set2["values"])

#use np.corrcoef to compute coorelation. store r values and graph them. (dotted line with first graph (color indigo or red/purple mustard?))

def find_graphable_data(year, month, irradiance_key, power_key, variable_key1, variable_key2 = None, variable_key3 = None):
    import numpy as np

    irradiance_dates = all_data[irradiance_key]["dates"]
    irradiance_values = all_data[irradiance_key]["values"]
    power_dates = all_data[power_key]["dates"]
    power_values = all_data[power_key]["values"]

    variable_dates1 = all_data[variable_key1]["dates"]
    variable_values1 = all_data[variable_key1]["values"]

    if variable_key2 == None and variable_key3 == None:

        dates_aligned, irradiance_aligned, variable_aligned, power_aligned = align_three_sets_of_data(
            irradiance_dates, variable_dates1, power_dates,
            irradiance_values, variable_values1, power_values
        )
    
        year = int(year)

        filtered_date = np.array([
            (d.year == year and d.month == month)
            for d in dates_aligned
        ])

        dates = dates_aligned[filtered_date]
        irradiance = irradiance_aligned[filtered_date]
        power = power_aligned[filtered_date]
        weather1 = variable_aligned[filtered_date]

        return dates, irradiance, power, weather1
    
    elif variable_key3 == None:
        variable_dates2 = all_data[variable_key2]["dates"]
        variable_values2 = all_data[variable_key2]["values"]

        dates_aligned, irradiance_aligned, variable_aligned1, variable_aligned2, power_aligned = align_four_sets_of_data(
            irradiance_dates, variable_dates1, variable_dates2, power_dates,
            irradiance_values, variable_values1, variable_values2, power_values
        )

        year = int(year)

        filtered_date = np.array([
            (d.year == year and d.month == month)
            for d in dates_aligned
        ])

        dates = dates_aligned[filtered_date]
        irradiance = irradiance_aligned[filtered_date]
        power = power_aligned[filtered_date]
        weather1 = variable_aligned1[filtered_date]
        weather2 = variable_aligned2[filtered_date]

        return dates, irradiance, power, weather1, weather2
    
    else:
        variable_dates2 = all_data[variable_key2]["dates"]
        variable_values2 = all_data[variable_key2]["values"]
        variable_dates3 = all_data[variable_key3]["dates"]
        variable_values3 = all_data[variable_key3]["values"]

        dates_aligned, irradiance_aligned, variable_aligned1, variable_aligned2, variable_aligned3, power_aligned = align_all_data(
            irradiance_dates, variable_dates1, variable_dates2, variable_dates3, power_dates,
            irradiance_values, variable_values1, variable_values2, variable_values3, power_values
        )

        year = int(year)

        filtered_date = np.array([
            (d.year == year and d.month == month)
            for d in dates_aligned
        ])

        dates = dates_aligned[filtered_date]
        irradiance = irradiance_aligned[filtered_date]
        power = power_aligned[filtered_date]
        weather1 = variable_aligned1[filtered_date]
        weather2 = variable_aligned2[filtered_date]
        weather3 = variable_aligned3[filtered_date]

        return dates, irradiance, power, weather1, weather2, weather3



def compute_correlation(weather, irr):
    import numpy as np
    r = np.corrcoef(weather, irr)[0, 1]
    return r


def graph_datasets(year, month, irradiance_key, power_key, variable_key1, variable_key2 = None, variable_key3 = None):
    import matplotlib.pyplot as plt 

    irradiance_unit = all_data[irradiance_key]["unit"]
    weather1_unit = all_data[variable_key1]["unit"]
    power_unit = all_data[power_key]["unit"]

    def graph_weather1(dates, irradiances, weather1):
        ax[0].set_title(f"{variable_key1.capitalize()} vs. Irradiance")

        line1, = ax[0].plot(dates, irradiances, label = f"Irradiance ({irradiance_unit})", color = 'cyan')
        ax[0].set_ylabel(f"Irradiance ({irradiance_unit})")

        line2, = first_shared_axes.plot(dates, weather1, label = f"{variable_key1.capitalize()} ({weather1_unit})", color = 'orange')
        first_shared_axes.set_ylabel(f"{variable_key1.capitalize()} ({weather1_unit})")


        lines = [line1, line2]
        labels = [line.get_label() for line in lines]

        fig.subplots_adjust(right=0.75)

        ax[0].legend(lines, labels, loc = 'upper left', bbox_to_anchor=(1.055, 1))
        #ax1.legend(lines, labels, loc = 'upper right', bbox_to_anchor=(1.01, 1))
        ax[0].tick_params(axis='x', rotation=45)

    def graph_weather2(dates, irradiances, weather2):
        ax[2].set_title(f"{variable_key2.capitalize()} vs. Irradiance")

        print(irradiances)

        line1, = ax[2].plot(dates, irradiances, label = f"Irradiance ({irradiance_unit})", color = 'cyan')
        ax[2].set_ylabel(f"Irradiance ({irradiance_unit})")

        line2, = second_shared_axis.plot(dates, weather2, label = f"{variable_key2.capitalize()} ({weather2_unit})", color = 'lime')
        second_shared_axis.set_ylabel(f"{variable_key2.capitalize()} ({weather2_unit})")

        lines = [line1, line2]
        labels = [line.get_label() for line in lines]

        fig.subplots_adjust(right=0.75)
        
        ax[2].legend(lines, labels, loc = 'upper left', bbox_to_anchor=(1.055, 1))
        ax[2].tick_params(axis='x', rotation=45)

        
    

    def graph_correlation(irradiance, weather, weather_key, weather_unit, axis_index):
        ax[axis_index].scatter(weather, irradiance)

        coefficients= np.polyfit(weather, irradiance, 1)
        trend = np.poly1d(coefficients)

        indices = np.argsort(weather)
        ax[axis_index].plot(weather[indices], trend(weather[indices]), color='red', linestyle='--', label="Trendline")
        ax[axis_index].set_xlabel(f"{weather_key.capitalize()} ({weather_unit})")
        ax[axis_index].set_ylabel(f"Irradiance ({irradiance_unit})")

        correlation = compute_correlation(weather, irradiance)

        ax[axis_index].set_title(f"{weather_key.capitalize()} vs Irradiance Correlation: r = {correlation:.3f}")
        ax[axis_index].legend(loc = 'upper left', bbox_to_anchor=(1.055, 1))
        print(f'graphing coorelation on ax[{axis_index}]')

    if variable_key2 == None and variable_key3 == None:

        dates_input, irradiance_input, power_input, weather_input1 = find_graphable_data(year, month, irradiance_key, power_key, variable_key1)

        fig, ax = plt.subplots(
            3, 1, 
            figsize=(12.5, 10),
            gridspec_kw={"height_ratios": [2, 2, 2]}
            )
        first_shared_axes = ax[0].twinx()

        fig.suptitle(f'Monthly Weather/Irradiance Data and Power Output', x=0.39,fontsize=16)

        graph_weather1(dates_input, irradiance_input, weather_input1)

        graph_correlation(irradiance_input, weather_input1, variable_key1, weather1_unit, 1)

        ax[2].set_title("Power Output")

        ax[2].plot(dates_input, power_input, label = f"Power output {power_unit}")
        ax[2].set_ylabel(f"Power Output {power_unit}")

        ax[2].legend(loc = 'upper left', bbox_to_anchor=(1.055, 1))
        ax[2].tick_params(axis = 'x', rotation=45)

        fig.tight_layout()

        filename = f"{variable_key1}_{year}_{month}.png"
        fig.savefig(filename)

        print(f"Graph saved as {filename}")
        print(f"In workbook, run")
        print(f"from IPython.display import Image")
        print(f"Image(filename='{filename}')")

        plt.close()

    
    elif variable_key3 == None:
        dates_input, irradiance_input, power_input, weather_input1, weather_input2 = find_graphable_data(year, month, irradiance_key, power_key, variable_key1, variable_key2)

        weather2_unit = all_data[variable_key2]["unit"]

        fig, ax = plt.subplots(
            5, figsize=(12.5, 16.6),
            gridspec_kw={"height_ratios":[2, 2, 2, 2, 2]}
        )
        first_shared_axes = ax[0].twinx()

        fig.suptitle(f'Monthly Weather/Irradiance Data and Power Output', x=0.39, fontsize=16)

        graph_weather1(dates_input, irradiance_input, weather_input1)

        graph_correlation(irradiance_input, weather_input1, variable_key1, weather1_unit, 1)

        print(irradiance_input)

        second_shared_axis = ax[2].twinx()

        graph_weather2(dates_input, irradiance_input, weather_input2)

        print(irradiance_input)

        graph_correlation(irradiance_input, weather_input2, variable_key2, weather2_unit, 3)

        ax[4].set_title("Power Output")

        ax[4].plot(dates_input, power_input, label = f"Power output {power_unit}")
        ax[4].set_ylabel(f"Power Output ({power_unit})")

        ax[4].legend(loc = 'upper left', bbox_to_anchor=(1.055, 1))
        ax[4].tick_params(axis='x', rotation = 45)

        fig.tight_layout()

        filename = f"{variable_key1}_{variable_key2}_{year}_{month}.png"
        fig.savefig(filename)

        print(f"Graph saved as {filename}")
        print(f"In workbook, run")
        print(f"from IPython.display import Image")
        print(f"Image(filename='{filename}')")

        plt.close()



    else:
        dates_input, irradiance_input, power_input, weather_input1, weather_input2, weather_input3 = find_graphable_data(
            year, month, irradiance_key,
            power_key, variable_key1,
            variable_key2, variable_key3
        )

        weather2_unit = all_data[variable_key2]["unit"]
        weather3_unit = all_data[variable_key3]["unit"]

        fig, ax = plt.subplots(
            7, figsize=(12.5, 23.24),
            gridspec_kw = {"height_ratios":[2, 2, 2, 2, 2, 2, 2]}
            )

        fig.suptitle(f'Monthly Weather/Irradiance Data and Power Output', x = 0.39, y=0.995, fontsize=16)

        first_shared_axes = ax[0].twinx()
        graph_weather1(dates_input, irradiance_input, weather_input1)

        graph_correlation(irradiance_input, weather_input1, variable_key1, weather1_unit, 1)


        second_shared_axis = ax[2].twinx()

        graph_weather2(dates_input, irradiance_input, weather_input2)

        graph_correlation(irradiance_input, weather_input2, variable_key2, weather2_unit, 3)


        last_shared_axis = ax[4].twinx()

        ax[4].set_title(f"{variable_key3.capitalize()} vs Irradiance")

        line1, = ax[4].plot(dates_input, irradiance_input, label = f"Irradiance ({irradiance_unit})", color = 'cyan')
        ax[4].set_ylabel(f"Irradiance ({irradiance_unit})")

        line2, = last_shared_axis.plot(dates_input, weather_input3, label = f"{variable_key3.capitalize()} ({weather3_unit})", color = (0/255, 128/255, 255/255))

        last_shared_axis.set_ylabel(f"{variable_key3.capitalize()} ({weather3_unit})")

        lines = [line1, line2]
        labels = [line.get_label() for line in lines]

        ax[4].legend(lines, labels, loc='upper left', bbox_to_anchor=(1.055, 1))
        ax[4].tick_params(axis = 'x', rotation=45)

        graph_correlation(irradiance_input, weather_input3, variable_key3, weather3_unit, 5)

        ax[6].set_title("Power Output")

        ax[6].plot(dates_input, power_input, label = f"Power output ({power_unit})")
        ax[6].set_ylabel(f"Power Output ({power_unit})")
        ax[6].legend(loc = 'upper left', bbox_to_anchor=(1.055, 1))
        ax[6].tick_params( axis = 'x', rotation = 45)

        fig.tight_layout(rect=[0,0,0.78,0.96])
        fig.subplots_adjust(hspace=0.65)

        filename = f"{variable_key1}_{variable_key2}_{variable_key3}_{year}_{month}.png"
        fig.savefig(filename, bbox_inches="tight")

        print(f"Graph saved as {filename}")
        print(f"In workbook, run")
        print(f"from IPython.display import Image")
        print(f"Image(filename='{filename}')")

        plt.close()

    




years = ["2024","2025","2026"]

months = list(range(1, 13))

if __name__ == '__main__':

    import numpy as np 
    import datetime as datetime

    weather_files = "/work/scientific_programming_rosaliehelgeland/python/project/data/2026-kenosha-regional-airport-weather-data.csv"

    solar_file = "/work/scientific_programming_rosaliehelgeland/python/project/data/daily_solar_data_2026.csv"

    site_file = "/work/scientific_programming_rosaliehelgeland/python/project/data/2026-power-irradiance-weather.csv"



    solar_times, solar_values, solar_headings = create_data_array(solar_file)

    weather_times, weather_values, weather_headings = create_data_array(weather_files)

    site_times, site_values, site_headings = create_data_array(site_file)


    actual_irradiance = pull_and_store_data(solar_values, solar_headings, "ALLSKY_SFC_SW_DWN")
    

    needed_weather_names = [
        "Precipitation"
    ]

    weather_data = {
        name: pull_and_store_data(weather_values, weather_headings, name)
        for name in needed_weather_names
    }


    needed_site_names = [
        "Weather station rain Inches",
        "Weather station Humidity Relative humidity (%)",
        "Production meter active power Kilowatts",
        "Weather station ambient temperature Degrees Fahrenheit"
    ]

    site_data = {
        name: pull_and_store_data(site_values, site_headings, name)
        for name in needed_site_names
    }



    times = solar_times.datetime

    days_of_the_year = np.array([t.timetuple().tm_yday for t in times])

    hours = np.array([t.hour + t.minute/60 for t in times])

    latitude = np.radians(42.647228)


    declination_angles = calculate_declination_angles(days_of_the_year)

    hour_angles = calculate_hour_angles(hours)

    solar_altitudes = calculate_solar_altitudes(declination_angles, hour_angles, latitude)

    zenith_angles = calculate_solar_zenith_angles(solar_altitudes)

    ideal_irradiances = calculate_ideal_irradiances(solar_altitudes)



    #SOLAR DATA

    average_irradiance_dates, average_irradiance_values = compute_daily_average_values(solar_times, actual_irradiance)
    ideal_irradiance_dates, ideal_irradiance_values = compute_daily_average_values(solar_times, ideal_irradiances)

    #WEATHER DATA

    rain = weather_data["Precipitation"]
    rain_dates, average_rain = compute_daily_average_values(weather_times, rain)

    #SITE DATA

    humidity = site_data["Weather station Humidity Relative humidity (%)"]
    humidity_dates, average_humidity = compute_daily_average_values(site_times, humidity)

    temperature = site_data["Weather station ambient temperature Degrees Fahrenheit"]
    temperature_dates, average_temperatures = compute_daily_average_values(site_times, temperature)
    

    power_output = site_data["Production meter active power Kilowatts"]
    power_dates, average_power = compute_daily_average_values(site_times, power_output)

    
    all_data = {
        "real_irradiance": {
            "dates":average_irradiance_dates, 
            "values":average_irradiance_values,
            "unit": "W/m^2"
        } ,
        "ideal_irradiance": {

            "dates":ideal_irradiance_dates, 
            "values":ideal_irradiance_values,
            "unit:": "W/m^2"
        },
        "temperatures": {
            "dates": temperature_dates,
            "values": average_temperatures,
            "unit": "°F"
        },
        "rain": { 
            "dates": rain_dates,
            "values": average_rain,
            "unit": "in"
        },
        "humidity": { 
            "dates": humidity_dates, 
            "values": average_humidity,
            "unit": "Relative humidity %"
        },
        "power_output": {
            "dates": power_dates,
            "values": average_power,
            "unit": "kW"
        }
    }

    
    years = ["2024","2025","2026"]

    months = list(range(1, 13))

    #graph_datasets(years[2], months[1], "humidity", "real_irradiance", "power_output")

    #dates, irradiance, power, rain_test, humidity_test, temperature_test = find_graphable_data(years[2], months[1], "real_irradiance", "power_output", "rain", "humidity", "temperatures")

    graph_datasets(years[2], months[1], "real_irradiance", "power_output", "temperatures", "humidity", "rain")
