from matplotlib.pylab import *

def gaussian_function(position):
    gaussian_values = 1/sqrt(2*pi)*(exp(-(position)**2)/2)
    return gaussian_values

if __name__ == '__main__':

    positions = linspace(-4, 4, 41)

    gaussian_values = zeros(len(positions))

    for index in range(len(positions)):
        gaussian_values[index] = gaussian_function(positions[index])
    
    plot(positions, gaussian_values)
    show()
