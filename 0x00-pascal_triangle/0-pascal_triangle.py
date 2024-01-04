#!/usr/bin/python3
"""
Pascal Trangle
"""


def pascal_triangle(n):
    '''
    Creates a list of lists of integers in a Pascal's triangle
    of a given integer.
    '''
    if n <= 0:
        return []
    else:
        rows_of_triangle = []
        for i in range(n):
            if len(rows_of_triangle) == 0:
                rows_of_triangle.append([1])
            else:
                row = [1]
                for j in range(1, len(rows_of_triangle[-1])):
                    row.append(rows_of_triangle[-1][j] + rows_of_triangle[-1][j - 1])
                row.append(1)
                rows_of_triangle.append(row)
        return rows_of_triangle
