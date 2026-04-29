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
from math import sin, cos

import numpy as np 
from datetime import datetime
from math import sin, cos, pi, radians
import astropy
from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, get_sun
import astropy.units as u 





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
            



#if __name__ == '__main__':
    #for file in file_locations:
        #results = create_data_array(file)
        #print(results)

#-------------------------------------------------------------------------
#DECIMAL TO TIME FUNCTION

def convert_decimals_to_time(arr):
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
    B = np.radians((360/364.)*(N-81))

    ET = 9.87*np.sin(2*B)-7.53*np.cos(B)-1.5*np.sin(B)

    return ET



def calculate_hour_angles(solar_time_hours):
    return np.radians(15*(solar_time_hours - 12))



def calculate_declination_angles(n):
    return np.radians(
        23.45 * np.sin(np.radians((360/365)*  (284 + n)))
    )



def calculate_solar_altitudes(declination_angle, hour_angle, latitude):
    SA = np.arcsin(
        np.sin(declination_angle) * np.sin(latitude) + 
        np.cos(declination_angle) * np.cos(latitude) * np.cos(hour_angle)
    )
    return SA


def calculate_solar_zenith_angles(altitude):
    ZA = np.pi/2 - altitude

    return ZA


#CALCULATING IDEAL IRRADIANCE/POWER

def calculate_ideal_irradiances(altitude, I0=1361):
    IR = I0 * np.maximum(np.sin(altitude), 0)

    return IR



def compute_daily_average_daily_values(times, values):
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
    datetimes = times.to_datetime()

    dates = np.array([DT.date() for DT in datetimes])

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

#---------------------------------------------------------------------------------------------------------

def get_aligned_data(variable1, variable2):
    set1 = all_data[variable1]
    set2 = all_data[variable2]

    return align_different_datasets_by_time(set1["dates"], set2["dates"], set1["values"], set2["values"])


def graph_datasets(year, month, variable, irradiance_key, power_key):
    import matplotlib.pyplot as plt 

    irradiance_dates = all_data[irradiance_key]["dates"]
    irradiance_values = all_data[irradiance_key]["values"]
    variable_dates = all_data[variable]["dates"]
    variable_values = all_data[variable]["values"]
    power_dates = all_data[power_key]["dates"]
    power_values = all_data[power_key]["values"]

    dates_aligned, irradiance_aligned, variable_aligned, power_aligned = align_three_sets_of_data(
        irradiance_dates, variable_dates, power_dates,
        irradiance_values, variable_values, power_values
    )

    year = int(year)

    filtered_date = np.array([
        (d.year == year and d.month == month)
        for d in dates_aligned
    ])
    
    dates = dates_aligned[filtered_date]
    irradiances = irradiance_aligned[filtered_date]
    weather_input = variable_aligned[filtered_date]
    power_output = power_aligned[filtered_date]

    unit1 = all_data[irradiance_key]["unit"]
    unit2 = all_data[variable]["unit"]
    unit3 = all_data[power_key]["unit"]


    fig, (ax1, ax3) = plt.subplots(2)
    ax2 = ax1.twinx()
    
    fig.suptitle(f'{variable} vs irradiance and power output')

    line1, = ax1.plot(dates, irradiances, label = f"Irradiance ({unit1})", color = 'cyan')
    ax1.set_ylabel(f"Irradiance ({unit1})")

    line2, = ax2.plot(dates, weather_input, label = f"{variable.capitalize()} ({unit2})", color = 'orange')
    ax2.set_ylabel(f"{variable.capitalize()}({unit2})")
    
    lines = [line1, line2]
    labels = [line.get_label() for line in lines]

    ax1.legend(lines, labels, loc='upper right')
    ax1.tick_params(axis='x', rotation=45)

    ax3.plot(dates, power_output, label = f"Power output {unit3}")
    ax3.legend()
    ax3.tick_params(axis='x', rotation=45)

    fig.tight_layout()
    
    filename = f"{variable}_{year}_{month}.png"
    fig.savefig(filename)

    print(f"Graph saved as {filename}")
    print(f"In workbook, run:")
    print(f"from IPython.display import Image")
    print(f"Image(filename='{filename}')")

    plt.close()


years = ["2024","2025","2026"]

months = list(range(1, 13))

if __name__ == '__main__':
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
    ideal_irradiance_dates, ideal_irradiance_values = compute_daily_average_daily_values(solar_times, ideal_irradiances)

    #WEATHER DATA

    rain = weather_data["Precipitation"]
    rain_dates, average_rain = compute_daily_average_daily_values(weather_times, rain)

    #SITE DATA

    humidity = site_data["Weather station Humidity Relative humidity (%)"]
    humidity_dates, average_humidity = compute_daily_average_values(site_times, humidity)

    temperature = site_data["Weather station ambient temperature Degrees Fahrenheit"]
    temperature_dates, average_temperatures = compute_daily_average_daily_values(site_times, temperature)
    

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

    graph_datasets(years[2], months[2], "rain", "real_irradiance", "power_output")
