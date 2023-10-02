#!/usr/bin/python3

"""
This script defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    :param n: The number of rows in Pascal's triangle to generate.
    :type n: int
    :return: A list of lists representing Pascal's triangle.
    :rtype: list[list[int]]
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        if i == 0:
            row.append(1)
        else:
            prev_row = triangle[i - 1]
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(prev_row[j - 1] + prev_row[j])
        triangle.append(row)

    return triangle
