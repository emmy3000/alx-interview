#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.

    Parameters:
       matrix (list of lists): Input matrix to be rotated.
    """
    # Transpose the matrix (swap rows with columns)
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to get the final rotated matrix
    for i in range(len(matrix)):
        matrix[i].reverse()
