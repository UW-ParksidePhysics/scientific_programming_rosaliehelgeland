"""
Make a fit curve using polynomial coefficients, NumPy's polynomial, and minimum and maximum x-values
"""

__author__ = "Rosie"

import numpy as np 
from numpy.polynomial import Polynomial

def fit_curve_array(quadratic_coefficients, minimum_x, maximum_x, number_of_points=100):
    """
    Parameters:
        quadratic_coefficients: ndarray, shape (3,)
            Quadratic polynomial coefficients, ordered constant term first, then linear term, and quadratic term last.
        minimum_x: float
            Starting value for the fit curve array.
        maximum_x: float
            Ending value for the fit curve array.
        number_of_points: int, optional
            Number of points N to return for final fit curve. Default is 100.
    Returns:
        fit_curve: ndarray, shape (2, N)
            x-y data created by the coefficients of the fit function. N is the number of function evaluation points.
    Raises:
        ArithmeticError
            When maximum_x < minimum_x.
        IndexError
            When number_of_points <= 2.
    """
    if maximum_x < minimum_x:
        raise ArithmeticError(f"The maximum_x input ({maximum_x}) is smaller than the minimum_x input ({minimum_x})!")
    if number_of_points <= 2:
        raise IndexError (f"invalid number of points ({number_of_points}), number_of_points must be above 2!")

    else:
        x_polynomial = Polynomial(quadratic_coefficients)

        x_values = np.linspace(minimum_x, maximum_x, number_of_points)
    
        y_values = x_polynomial(x_values)

        fit_curve = np.array([x_values, y_values])

        return fit_curve

if __name__ == "__main__":
    """
    Test:
    Pass quadratic coefficients of [0, 0, 1], a minimum x-value of -2, 
    and a maximum x-value of 2 and show that the resulting array matches y = x2.
    """
    quadratic_coefficients_test = np.array([0, 0, 1])

    #print(quadratic_coefficients_test.shape)

    test_fit_curve = fit_curve_array(quadratic_coefficients_test, -2, 2)

    #print(test_fit_curve)
    #print(test_fit_curve.shape)

    print(
        f"When inputting {quadratic_coefficients_test} as quadratic_coefficient and minimum_x = -2, maximum_x = 2,\n"
        f"the function returns {test_fit_curve[0, :3]} as the first 3 x-values \n and {test_fit_curve[1, :3]} as the first 3 y-values.\n"
        f"To check that y = x^2, we manually calculate y for our first 3 x-values: \n"
        f"x={test_fit_curve[0, 0]}, y = {test_fit_curve[0, 0]}**2 = {test_fit_curve[0, 0]**2}\n"
        f"x={test_fit_curve[0, 1]}, y = {test_fit_curve[0,1]}**2 = {test_fit_curve[0, 1]**2}\n" 
        f"x={test_fit_curve[0, 2]}, y = {test_fit_curve[0, 2]}**2 = {test_fit_curve[0, 2]**2}\n"
        f"when compared, our manually computed y-values are the same as the y-values the function returns"
    )