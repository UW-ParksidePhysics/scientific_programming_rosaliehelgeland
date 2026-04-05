import numpy as np

from numpy import exp, sqrt, pi

def compute_gaussian_function(position):
    gaussian_values = 1/sqrt(2*pi)*(exp(-(position)**2)/2)
    return gaussian_values

if __name__ == '__main__':
    
    number_of_points = 41
    
    positions = np.zeros(number_of_points)
    gaussian_values = np.zeros(number_of_points)

    step = 8./40
    start = -4

    for i in range(number_of_points):
        x_values = start + i * step
        positions[i] = x_values
        gaussian_values[i] = compute_gaussian_function(x_values)
    

    #table headers
    print (f'{"x":>3} {"g(x)":>9}')
    print (f'{"-----":>2} {"-------":>9}')


    for x, gx in zip(positions, gaussian_values):
        print (f'{x:>3.2} {gx:>10.2}')
        