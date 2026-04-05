from math import exp, sqrt, pi

def compute_gaussian_function(position):
    gaussian_values = 1/sqrt(2*pi)*(exp(-(position)**2)/2)
    return gaussian_values

if __name__ == '__main__':
    positions = []
    gaussian_values = []

    number_of_points = 41
    step = (8./40)
    start = -4

    for index in range(number_of_points):
        x_values = start + index * step
        positions.append(x_values)
    
    for x in positions:
        gx = compute_gaussian_function(x)
        gaussian_values.append(gx)


    #table headers
    print (f'{"x":>3} {"g(x)":>9}')
    print (f'{"-----":>2} {"-------":>9}')

    for x, gx in zip(positions, gaussian_values):
        print (f'{x:>3.2}, {gx:>9.2}')