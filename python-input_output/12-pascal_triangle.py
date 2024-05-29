#!/usr/bin/python3
"""Module for the Pascal Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        start_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(start_row[j - 1] + start_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
