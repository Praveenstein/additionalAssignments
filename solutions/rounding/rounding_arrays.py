# -*- coding: utf-8 -*-
""" Module for rounding off array of real numbers

Problem Statement:
Given an array of real numbers such that the real numbers sum to a whole
number, round off the real numbers while ensuring the sum remains the same
and the resultant real numbers are closest to the original number.

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations
    * itertools - To perform efficient iterating

This script contains the following function
    * round_off - function to round of the array of real numbers
"""

import logging
from itertools import cycle


__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def round_off(array):
    """
    Function to round off array of real numbers
    :param array: The array consisting of real numbers
    :type array: list
    :return: Nothing
    :rtype: None
    """

    try:

        if not issubclass(type(array), list):
            raise ValueError("The input should be a list")

        # Checking if all the items of array is either int or float
        check_type = map(lambda arg: issubclass(type(arg), int) or
                         issubclass(type(arg), float),
                         array)
        if not all(check_type):
            raise ValueError("The list items should be integer or float")

        # Getting the integer part of the real numbers
        new_array = [int(item) for item in array]

        # Getting all the index of items in the original array
        # and sorting them based on the precision of the numbers
        # That is modulo of the number with it's integer part

        # This is done by creating a list of index using range function
        # And sorting them using key function
        # That uses the uses the elements from original array
        sorted_index = sorted(list(range(len(array))), key=lambda arg: array[arg] % int(array[arg]), reverse=True)

        # Getting the sum of all decimal values
        sum_of_decimal = sum(map(lambda arg: arg % int(arg), array))

        # Once the sum of decimal value is obtained the value is distributed uniformly
        # Among the real numbers starting with the highest decimal value to lowest
        # This has to be done continuously until the sum_of_decimal becomes zero
        # Using cycle function from itertools to continuously loop over the sorted_index
        pool = cycle(sorted_index)
        while sum_of_decimal != 0:
            index = next(pool)
            new_array[index] += 1
            sum_of_decimal -= 1

        LOGGER.info("OLD ARRAY: %s", array)
        LOGGER.info("Sum of old array: %s", sum(array))
        LOGGER.info("New Array: %s", new_array)
        LOGGER.info("Sum of new array: %s", sum(new_array))

    except ValueError as err:
        LOGGER.error(err)
