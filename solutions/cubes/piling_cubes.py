# -*- coding: utf-8 -*-
""" Module for check if row of cubes could be piled vertically

Problem Statement:
There is a horizontal row of n cubes. The length of each cube is given. You need
to create a new vertical pile of cubes. The new pile should follow these
directions: if cube(i) is on top of cube(j) then sideLength(j) >= sideLength(i).
When stacking the cubes, you can only pick up either the leftmost or the
rightmost cube each time. Print "Yes" if it is possible to stack the cubes.
Otherwise, print "No".

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations
    * collection - to store and traverse in an efficient and quick way

This script contains the following function
    * check_for_piling - Checks if the rows of cube could be piled up vertically
"""

# Standard imports
import logging
from collections import deque

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def check_for_piling(cubes):
    """
    Function to check if given rows of cube could be piled up vertically
    :param cubes: array consisting of the length of cubes in the row
    :type cubes: list
    :return: Nothing
    :rtype: None
    """

    try:
        # Checking if the cubes is a list
        if not issubclass(type(cubes), list):
            raise ValueError("The input should be a list")

        # Checking if all the items of cubes is either int or float
        check_type = map(lambda arg: issubclass(type(arg), int) or
                         issubclass(type(arg), float),
                         cubes)
        if not all(check_type):
            raise ValueError("The list items should be integer or float")

        # deque are easier to pop elements from both sides
        rows = deque(cubes)
        while True:

            # Running the loop forever until the deque becomes empty (Meaning that
            # the rows could be piled up vertically) or if the piling condition fails

            # If the left most element is greater than the right most elements
            # Then it is taken as the biggest_number, while on other conditions
            # The biggest number is taken as the left most element
            biggest_number = rows.popleft() if rows[0] > rows[-1] else rows.pop()
            if not rows:
                # If the rows become empty, it means the rows could be piled
                # Up vertically
                LOGGER.info("Yes")
                return
            if rows[-1] > biggest_number or rows[0] > biggest_number:
                # Checking if either the leftmost or rightmost element is greater
                # Then the biggest number, if yes, then it fails to satisfy the
                # Piling condition, hence it logs "No"
                LOGGER.info("No")
                return
    except ValueError as err:
        LOGGER.error(err)
