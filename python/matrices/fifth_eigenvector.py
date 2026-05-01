import numpy as np 
(1/(2*(1/(5+1))**2))

matrix_a = np.diagflat(2*np.ones(4))
matrix_b = np.diagflat(-1*np.ones(3), 1)
matrix_c = np.diagflat(np.ones(3), -1)

matrix_H = (
    np.diagflat(2*np.ones(5))
    +np.diagflat(-1*np.ones(4), 1)
    +np.diagflat(-1*np.ones(4), -1)
)

n = 5
h = 1/(n+1)
matrix = (1 / (2 * h ** 2)) * matrix_H

print(matrix)

eighen_values, eighen_vectors = np.linalg.eig(matrix)

sorted_things = np.argsort(eighen_values)

eighen_values = eighen_values[sorted_things]
eighen_vectors = eighen_vectors[:, sorted_things]

fifth_eighen_vector = eighen_vectors[:, 4]

x_values = np.linspace(
    h,
    n*h,
    n
)

sine_values = np.sqrt(2) * np.sin(np.pi * x_values)


if __name__ == '__main__':
    import matplotlib.pyplot as plt 

    plt.plot(x_values, fifth_eighen_vector, "o-", label = "Fifth eigenvector")
    plt.plot(x_values, sine_values, label=r"$\sqrt{2}sin(\pi x)$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    
    from IPython.display import Image

    plt.savefig("matrix_plot.png")

    Image(filename="matrix_plot.png")

    