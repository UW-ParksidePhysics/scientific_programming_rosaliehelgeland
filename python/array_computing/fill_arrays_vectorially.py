import numpy as np

from numpy import exp, sqrt, pi

def compute_gaussian_function(position):
    gaussian_values = 1/sqrt(2*pi)*(exp(-(position)**2)/2)
    return gaussian_values

if __name__ == '__main__':
    
    positions = np.linspace(-4, 4, 41)

    gaussian_values = compute_gaussian_function(positions)


    #table header
    print(f'{"x":>3} {"g(x)":>9}')
    print(f'{"-----":>2} {"-------":>9}')

    for x, gx in zip(positions, gaussian_values):
        print (f'{x:>3.2} {gx:>10.2}')