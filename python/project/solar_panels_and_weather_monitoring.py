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
import matplotlib.pyplot as plt
from datetime import datetime
from math import sin, cos, pi
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

file_locations = (
    "/work/scientific_programming_rosaliehelgeland/python/project/data/chicago_airport_data.csv",
    "/work/scientific_programming_rosaliehelgeland/python/project/data/hourly_solar_data_2024_2026.csv",
    "/work/scientific_programming_rosaliehelgeland/python/project/data/2024-power-irradiance-weather.csv",
    "/work/scientific_programming_rosaliehelgeland/python/project/data/2025-power-irradiance-weather.csv",
    "/work/scientific_programming_rosaliehelgeland/python/project/data/2026-power-irradiance-weather.csv"
    )








def create_data_array(file_location):
    """
    imports data in csv files and converts the data to arrays, 
    uses those arrays to store time values as strptime values for easy access and consistent data
    stores arrays in dictionaries 
    """

    arr = np.genfromtxt(file_location, delimiter=',',dtype=str)

    
    start_index = 0


    for line in arr:
        if len(line[1]) == 0:
            start_index +=1

        else:
            continue
    print(arr[start_index])
    
    headings = arr[start_index]

    data = arr[start_index+1]

    data = []


    if headings[0] == "DATE":

        for line in data:

            date_time = datetime.strptime(line[0], "%m/%d/%Y")

            dates.append(date_time)

    
    elif headings[0] == "YEAR":

        for line in data:
        
            date_string = f"{line[1]}/{line[2]}/{line[0]}/{line[3]}"
            

            date_time = datetime.strptime(date_string, "%m/%d/%Y/%H")

            dates.append(date_time)

    elif header[0] == "Site Time":

        for line in data:
            
            date_time = datetime.strptime(line[0], "%d-%m-%Y")

            dates.append(date_time)
    

    return np.array(dates), headers, data
            





#if __name__ == '__main__':
    #for file in file_locations:
       # dates_and_data = create_data_array(file)

       # print(dates_and_data)

#-------------------------------------------------------------------------
#DECIMAL TO TIME FUNCTION

def convert_decimals_to_time(arr):
    arr = np.mod(arr, 24)

    hours = np.floor(arr).astype(int)
    minutes = np.floor((arr-hours)*60).astype(int)

    vectorized = np.vectorize(lambda h, m: f'{h:02d}:{m:02d}')

    return vectorized(hours, minutes)





#calculating and storing solar geometry constants

days_of_the_year = np.arange(1, 366)

def equation_of_time(N):
    B = np.radians((360/364.)*(N-81))

    ET = 9.87*sin(2*B)-7.53*cos(B)-1.5*sin(B)

    return ET

equation_of_time_results = []

for N in days_of_the_year:
    equation_of_time_results.append(equation_of_time(N))





time_difference_greenwich= 5 #hours

standard_meridian = time_difference_greenwich*15 #degrees

hours_in_the_day = np.arange(1, 25)





#standard time function 

def calculate_standard_time(H):
    standard_time = H+time_difference_greenwich

    if standard_time > 24:
        return standard_time-24

    else:
        return standard_time

standard_times = []

for H in hours_in_the_day:
    standard_time = calculate_standard_time(H)

    standard_times.append(standard_time)





#apparent solar time function

local_longitude = -87.851997

local_latitude = 42.647228


ET = np.array(equation_of_time_results)[:, None]

LST = np.array(standard_times)[None, :]

apparent_solar_times = LST + (ET + 4*(standard_meridian - local_longitude)) /60

#print(apparent_solar_times)




#DECLINATION ANGLE 

declination_angles = []

for N in days_of_the_year:
    inner_function = np.radians((360/365.)*(284+N))

    DA = 23.45*sin(inner_function)

    declination_angles.append(DA)

#print(declination_angles)



#HOUR ANGLES

hour_angles = (apparent_solar_times - 12)*15



if __name__ == '__main__':
    #EQUATION OF TIME FORMATTING 
    formatted_equation_of_time_results = convert_decimals_to_time(np.array(equation_of_time_results) / 60)
    
    print(f'equation of time: {formatted_equation_of_time_results}')

    #STANDARD TIME FORMATTING
    formatted_standard_times = convert_decimals_to_time(standard_times)

    print(f'standard times: {formatted_standard_times}')

    #APPARENT SOLAR TIME FORMATTING
    formated_apparent_solar_times = convert_decimals_to_time(apparent_solar_times)

    print(f'apparent solar times: {formated_apparent_solar_times}')


times = Time([
    f"{year}-{day:03d}T{hour:02d}:00:00"
    for year in range(2024,2025)
    for day in range(1, 366)
    for hour in range(24)
    ],format = 'yday'
)
    
location = EarthLocation(
    lat = local_latitude * u.deg,
    lon = local_longitude * u.deg
)

altaz = AltAz(obstime=times, location=location)

sun = get_sun(times).transform_to(altaz)

azimuth_angle = sun.az.deg
altitude_angle = sun.alt.deg

print(azimuth_angle, altitude_angle, sun, altaz)

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
# Keep plotting separate from physics/math wherever pmit n snsntegnT(h)p