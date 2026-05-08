"""
Calculate statistical characteristics of a data set using SciPy's stats.describe function
"""

__author__ = "Rosie"

import numpy as np 
from scipy import stats

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


if __name__ == "__main__":
    """
    Test:
        Create an array centered around zero with x values in the range [-10, 10], calculate y = x2, 
        and show that the returned values come out as expected.
    """
    x_values_test = np.arange(-10, 11, 1)
    def calculate_y_values(x_values):
        y_values = x_values**2
        return y_values

    
    y_values = []
    for x in x_values_test:
        y_value = calculate_y_values(x)
        y_values.append(y_value)
    
    y_values_arr = np.array(y_values)

    test_data = np.array([x_values_test, y_values_arr])

    #print(test_data.shape)
    #print(test_data)

    statistics = calculate_bivariate_statistics(test_data)

    print(statistics.shape)
    print(statistics)

    error_test_data = np.array([
        [1],
        [2] 
        ])

    calculate_bivariate_statistics(error_test_data)
