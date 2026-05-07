""" 
Read in two columns of data from a text file of arbitrary length
Module name:
read_two_columns_text
Parameters:
filename: str
Name of file to be read in.

Returns:
data: ndarray, shape (2, M)
x-y data read in from file. M is the number of data points.
Raises:
OSError
When filename cannot be found for reading.
Test:
Read in volumes_energies.dat and print out the data array with its shape using:
print(f'{data=}, shape={data.shape}')
"""

__author__ = "rosie"
import numpy as np 


def read_two_columns_text(filename: str) -> np.ndarray:
    try:
        data = np.loadtxt(filename)
        return data
    except OSError as error:
        print(f"{filename} not found!")
   

if __name__ == '__main__':
    volumes_energies = "/work/scientific_programming_rosaliehelgeland/python/volumes_energies.dat"
    data = read_two_columns_text(volumes_energies).transpose()
    print(f'{data=}, shape={data.shape}')

    