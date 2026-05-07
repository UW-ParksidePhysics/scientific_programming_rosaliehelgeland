"""
Identify eigenvectors witht he smallest K eigenvalues for an input matirx using NumPy's eig function
"""

__author__ = 'Rosie'

import numpy as np


def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    """
    Parameters:
        square_matrix: ndarray, shape (M, M)
            Matrix to be characterized. Must be a square matrix of M rows and M columns where M is at least 1.
        number_of_eigenvectors: int, optional
            Number of eigenvectors K with eigenvalues to return. Default is 3.
    Returns:
        eigenvalues: ndarray, shape (K,)
            Array of the K lowest-value eigenvalues ordered from lowest to highest.
        eigenvectors: ndarray, shape (K, M)
            Array of K eigenvectors with M components arranged in order corresponding to their eigenvalues. The first index should correspond to the eigenvalue index in the eigenvalues array. The order of the components in each eigenvector should remain the same as output by NumPy's eig.
    Raises:
        IndexError
            When square_matrix is not square or when number_of_eigenvectors is less than 1 or greater than the number of rows in the matrix.
    """
    if number_of_eigenvectors < 1:
        raise IndexError(f'Number of eigenvectors ({number_of_eigenvectors}) is less than 1.')

    # Get M from the matrix
    row_number, column_number = square_matrix.shape

    if row_number != column_number:
        raise IndexError(f'Number of rows ({row_number}) does not equal number of columns ({column_number}).')

    if number_of_eigenvectors > row_number:
        raise IndexError(f'Number of eigenvectors ({number_of_eigenvectors}) is greater than the number of rows ({row_number}).')
    
    # Use linalg.eig to calculate eigenvalues and eigenvectors
    values, vectors = np.linalg.eig(square_matrix)

    # Get the indices of the sorted eigenvalues
    sorted_value_indices = np.argsort(values)

    # Construct the lists of sorted eigenvalues and eigenvectors
    eigenvalues, eigenvectors = [], []     
    for value_index in sorted_value_indices:
        eigenvalues.append(values[value_index])
        eigenvectors.append(vectors[:, value_index])

    return (
        np.array(eigenvalues[:number_of_eigenvectors]), 
        np.array(eigenvectors[:number_of_eigenvectors])
        )  


if __name__ == '__main__':
    test_matrix = np.array([[2, -1], [-1, 2]])
    test_values, test_vectors = calculate_lowest_eigenvectors(test_matrix, number_of_eigenvectors=2)

    for value, vector in zip(test_values, test_vectors):
        print(f'{value}: {vector}')
