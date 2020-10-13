# -*- coding: utf-8 -*-
""" Module for finding the distinct prime factors of the product of elements of given array
Problem Statement:
Given a list of N elements, find the distinct prime factors of product of the
elements in the array.


This script requires the following modules be installed in the python environment
    * logging - to perform logging operations
    * math - to store and traverse in an efficient and quick way

This script contains the following function
    * get_prime_factors - Given a number, it return the prime factors
    * get_prime_factors_array - Given a array of number, will return the
                                prime factors of it's product
"""

import logging
import math


__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def get_prime_factors(number):
    """
    Function which finds the distinct prime factors of given number
    :param number: The number for which the prime factors are to be found
    :type number: int
    :return: prime_factors
    :rtype: set
    """

    try:
        if not issubclass(type(number), int):
            raise ValueError("The Number should be a integer")
        prime_factors = set()

        while number % 2 == 0:

            # If the number is divisible by two
            # Two is added to set of prime_factors
            prime_factors.add(2)

            # And the number is divided by 2
            number /= 2

        # Looping from 3 till square root of number
        # While skipping all even number, since it is taken
        # care in previous step
        for i in range(3, int(math.sqrt(number))+1, 2):
            while number % i == 0:
                # If the number is divisible i, it is added to prime_factors
                prime_factors.add(i)

                # And the number is divided by it
                number /= i

        if number > 2:
            # If the remaining number is greater the 2,
            # Then it is the one prime_factor that is greater than
            # Square root of the given number
            prime_factors.add(int(number))

        return prime_factors
    except ValueError as err:
        LOGGER.error(err)


def get_prime_factors_array(elements):
    """
    Function to find the prime_factors of the product of given elements
    :param elements: The array of elements, for which the prime_factors of
                    it's product has to be found
    :type elements: list
    :return: Nothing
    :rtype: None
    """
    try:
        # Checking if the elements is a list
        if not issubclass(type(elements), list):
            raise ValueError("The elements should be a list")

        # Checking if all the items of elements is int
        check_type = map(lambda arg: issubclass(type(arg), int), elements)
        if not all(check_type):
            raise ValueError("The list items should be integer")
        results = set()
        for element in elements:
            results.update(get_prime_factors(element))
        LOGGER.info("Prime Factors are: %s", results)
    except ValueError as err:
        LOGGER.error(err)
