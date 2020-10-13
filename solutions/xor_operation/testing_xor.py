# -*- coding: utf-8 -*-
""" Module for generating the toeplitz matrix
This script contains the following function
    * generate_toeplitz_matrix: It is used to generate a toeplitz matrix of given dimension
"""
from functools import reduce
import logging
__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def finding_xor(elements):
    """
    Function used to find the xor of all the items in the given array

    :param elements: array of integers for which the Xor operation has to be done
    :type elements: [list, generator]
    :return: results
    :rtype: int
    """

    # The xor operation is done by taking the first two items
    # of the iterable and performing xor operation between them
    # and then the resultant of the operation is taken to perform
    # xor operation with the next element in the iterable,and so on
    # Until the iterable is exhausted
    result = reduce(lambda num1, num2: num1 ^ num2, elements)
    return result


def finding_xor_odd_even(elements):
    """
    Function to find two xor,
    i) items of elements at even index
    ii) items of elements at odd index

    :param elements: array of integers for which the Xor operation has to be done
    :type: elements: list
    :return: xor_of_even, xor_of_odd
    :rtype: int, int
    """

    # The even items of the elements are created using a generator expression
    # For even index the starting value of range should be 0, with a step of 2
    even_elements = (elements[i] for i in range(0, len(elements), 2))

    # The odd items of the elements are created using a generator expression
    # For odd index the starting value of range should be 1, with a step of 2
    odd_elements = (elements[i] for i in range(1, len(elements), 2))

    # The xor of items at even index are found by calling the finding_xor function
    # with the even_elements
    xor_of_even = finding_xor(even_elements)

    # The xor of items at odd index are found by calling the finding_xor function
    # with the odd_elements
    xor_of_odd = finding_xor(odd_elements)
    return xor_of_even, xor_of_odd


def checking_xor(elements):
    """
    Function which finds the
    a) xor of the given array
    b) xor of the elements in odd index of given array
    c) xor of elements in  even index
    d) xor of (b) and (c)
    and check if (a) is same as (d)

    :param elements: The array of integers for which the xor operations need to be done
    :type elements: list
    :return: Nothing
    :rtype: None
    """
    try:
        # Checking if the cubes is a list
        if not issubclass(type(elements), list):
            raise ValueError("The input should be a list")

        # Checking if all the items of elements is int
        check_type = map(lambda arg: issubclass(type(arg), int), elements)
        if not all(check_type):
            raise ValueError("The list items should be integer")
        if len(elements) < 2:
            raise ValueError("The length of elements should not be less than 2")

        # Finding the XOR of all elements
        xor_of_all = finding_xor(elements)
        LOGGER.info("The Xor of all elements of array: %s", xor_of_all)

        # Finding the XOR of elements at even and odd index
        xor_even, xor_odd = finding_xor_odd_even(elements)
        LOGGER.info("The Xor of elements at even index: %s", xor_even)
        LOGGER.info("The Xor of elements at odd index: %s", xor_odd)

        # Finding the XOR of the result from odd and even xor operations
        xor_of_even_odd = finding_xor([xor_even, xor_odd])
        LOGGER.info("The Xor of both even and odd: %s", xor_of_even_odd)

        # Checking if the results are same
        LOGGER.info("Checking if both are same: %s", xor_of_all == xor_of_even_odd)
    except ValueError as err:
        LOGGER.exception(err)
