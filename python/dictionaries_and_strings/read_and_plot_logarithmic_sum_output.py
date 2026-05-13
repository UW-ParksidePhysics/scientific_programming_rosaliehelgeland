#redirect the output to a file (by python3 logarithmic_sum.py > logarithmic_sum.out) 
#include a function parse_sum_output that reads the file logarithmic_sum.out
#extract numbers corresponding to epsilon, exact error, and n
#return the numbers in three seperate arrays: tolerances, errors, maximum_indices

#write a function plot_logarithmic_sum_error that takes the three arrays as inputs,
#plots tolerance and the approximation error versus maximum index(n)

#use logarithmic scale on y-axis
#use semilogy: 
#semilogy([x], y, [fmt], data=None, **kwargs)
#semilogy([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)

import matplotlib.pyplot as plt


def parse_sum_output(filename):

    tolerances = []

    errors = []

    maximum_indices = []

    with open(filename, 'r') as f:
        for line in f:

            values = line.replace(",", " ").replace(":", " ").replace("=", " ").split()

            epsilon = float(values[1])

            exact_error = float(values[4])

            n = int(values[6])


            tolerances.append(epsilon)

            errors.append(exact_error)

            maximum_indices.append(n)
    
    return tolerances, errors, maximum_indices



#creating plot function

def plot_logarithmic_sum_error(tolerance, approximation_error, num_max):
    
    plt.semilogy(num_max, tolerance, 'o', label='Tolerance (ε)')

    plt.semilogy(num_max, approximation_error, '-', label = 'Approximation Error (△)')


    plt.xlabel("Maximum Indices (n)")

    plt.ylabel("Logarithmic Scale")


    plt.legend()


    plt.show()


if __name__ == '__main__':
    test_filename = "logarithmic_sum.out"

    with open(test_filename, 'w') as f:
        f.write(""" epsilon: 1e-04, exact error: 8.18e-04, n=55
        epsilon: 1e-06, exact error: 9.02e-06, n=97
        epsilon: 1e-04, exact error: 8.70e-08, n=142
        epsilon: 1e-10, exact error: 9.20e-10, n=187
        epsilon: 1e-12, exact error: 9.31e-12, n=233""")

    tolerances, errors, maximum_indices = parse_sum_output(test_filename)

    plot_logarithmic_sum_error(tolerances, errors, maximum_indices)