#!/usr/bin/python3
"""
Module to rotate an n x n 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix (list of lists): The 2D matrix to rotate.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = \
                matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        left = 0
        right = n - 1
        while left < right:
            matrix[i][left], matrix[i][right] = \
                matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
