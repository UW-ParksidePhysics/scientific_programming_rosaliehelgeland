import numpy as np

matrix_A = np.diagflat(2*np.ones(10)) #practicing using diagflat 
matrix_B = np.diagflat(-1*np.ones(9), 1)
matrix_C = np.diagflat(-1*np.ones(9), -1)

matrix_dimension = 10

matrix_H = (
    np.diagflat(2*np.ones(matrix_dimension))
    + np.diagflat(-1*np.ones(matrix_dimension-1), 1)
    + np.diagflat(-1*np.ones(matrix_dimension-1), -1)
)


h = 1/(matrix_dimension+1)

matrix = (1 / (2 * h )**2) * matrix_H

print(matrix)

eighen_values, eighen_vectors = np.linalg.eig(matrix)

all_sorted_eighen =  np.argsort(eighen_values)

eighen_values = eighen_values[all_sorted_eighen]
eighen_vectors=eighen_vectors[:, all_sorted_eighen]

tenth_eighen_vector = eighen_vectors[:, matrix_dimension-1]

x_values = np.linspace(
    h,
    matrix_dimension*h,
    matrix_dimension
)

sin_values = np.sqrt(2) * np.sin(np.pi * x_values)

if __name__ == '__main__':
    import matplotlib.pyplot as plt

    plt.plot(x_values, tenth_eighen_vector, "o-", label="tenth eighen vector")
    plt.plot(x_values, sin_values, label = r"$\sqrt{2}*(\pi x)$")
    plt.xlabel = ("x")
    plt.ylabel =("y")
    plt.legend()

    from IPython.display import Image

    plt.savefig("tenth_eighen.png")