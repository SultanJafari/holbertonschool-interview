#!/usr/bin/python3
"""
Module for Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing 
    the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(len(triangle[-1]) - 1):
            row.append(triangle[-1][j] + triangle[-1][j + 1])
        row.append(1)
        triangle.append(row)

    return triangle
