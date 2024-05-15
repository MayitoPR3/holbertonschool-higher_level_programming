#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return [[m**2 for m in row] for row in (matrix)]
