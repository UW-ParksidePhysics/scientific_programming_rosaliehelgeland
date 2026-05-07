"""
Create a combined scatter and curve plot for the data and the fit polynomial respectively using Pyplot's plot function
"""

__author__ = 'Rosie'

import numpy as np
import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_format='o', fit_format=''):
    """
    Parameters:
        data: ndarray, shape (2, M)
            x-y data that was fit. M is the number of data points.
        fit_curve: ndarray, shape (2, N)
            x-y data created by the coefficients of the fit function. N is the number of function evaluation points, usually much greater than M.
        data_format: str, optional
            Optional formatting specification for the style of the scatter plot data points. Default is 'o'. See Pyplot's plotLinks to an external site. for specifications. Use Pyplot's plot, not scatter, for this.
        fit_format: str, optional
            Optional formatting specification for the curve of the fit function. Default is '', an empty string. See Pyplot's plotLinks to an external site. for specifications.
    Returns:
        combined_plot
            A list of Line2DLinks to an external site. objects representing the plotted data. This is the default return type from Pyplot's plot.
    """

    if data.shape[0] != 2:
        raise IndexError(f'Data has {data.shape[0]} rows, must have 2 rows.')
    if fit_curve.shape[0] != 2:
        raise IndexError(f'Fit curve has {fit_curve.shape[0]} rows, must have 2 rows.')    
    if len(data.shape) != 2:
        raise IndexError(f'Data has shape {data.shape}, but should have shape (2, M)')
    if len(fit_curve.shape) != 2:
        raise IndexError(f'Fit curve has shape {fit_curve.shape}, but should have shape (2, N)')

    
    combined_plot = [] 
    combined_plot.append(ax.plot(data[0], data[1], data_format))
    combined_plot.append(ax.plot(fit_curve[0], fit_curve[1], fit_format))

    return combined_plot


if __name__ == '__main__':
    test_data = np.array([
        [-2, -1, 0, 1, 2],
        [4, 1, 0, 1, 4]
        ])
    test_curve = np.array([
        np.linspace(-2, 2), 
        np.linspace(-2, 2)**2
        ])
    fig, ax = plt.subplots()
    test_plot = plot_data_with_fit(test_data, test_curve, data_format='x', fit_format='--')

    plt.savefig('plot_data_with_fit.png')
