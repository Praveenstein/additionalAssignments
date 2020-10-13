# -*- coding: utf-8 -*-
""" Module for generating the toeplitz matrix
This script contains the following function
    * generate_toeplitz_matrix: It is used to generate a toeplitz matrix of given dimension
"""

__author__ = "praveen@gyandata.com"


def generate_toeplitz_matrix(rows, columns=None):
    """
    Function to generate a toeplitz matrix
    The generated matrix will have the first row and column equal to
    numbers from 1 till it's length.
    For example, for row = [1, 2, 3], column = [1, 2, 3, 4], the generated matrix would be:
            [1, 2, 3]
            [2, 1, 2]
            [3, 2, 1]
            [4, 3, 2]

    :param rows: first row
    :type rows: list
    :param columns: first column
    :type columns: list
    :return: matrix: The generated toeplitz matrix
    :rtype: list
    """

    # Setting the matrix variable to be an empty list
    matrix = []
    number_of_rows = len(columns) if columns else len(rows)
    for row in range(number_of_rows):
        # Looping to generate all row elements
        if row == 0:
            # If it is the first row, then we append a list
            # Consisting of elements from 1 to number of columns
            # E.g : [1, 2, 3, 4] for number of columns = 4
            matrix.append(rows)

            # Since all column elements are generated, we skip the
            # Remaining part of the code
            continue

        # If it is not the first row, then the first element
        # Would the the (row index + 1)
        if columns:
            _row = [columns[row]]
        else:
            _row = [rows[row]]

        # The remaining column elements are obtained from the
        # Previous row's elements, starting from first column,
        # till the column before the last item
        _row.extend(matrix[row - 1][:-1])

        # This row elements is appended to the matrix
        matrix.append(_row)

    return matrix
