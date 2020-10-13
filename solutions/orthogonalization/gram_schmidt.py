# -*- coding: utf-8 -*-
""" Module for implementing Gram_schmidt Orthogonalization

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * inner_product - finds the dot product of given two vectors
    * find_projection - Finds the vector project of v_vector on u_vector
    * orthogonalize_vectors - Given a set of vectors, it finds the orthogonalized vectors
"""

# Standard imports
import logging

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def inner_product(vector1, vector2):
    """
    Function used to find the dot product of two given vectors
    :param vector1: The first vector
    :type vector1: list
    :param vector2: The second vector
    :type vector2: list
    :return: dot product of two vectors
    :rtype: int, float
    """
    try:
        # Checking if the cubes is a list
        if not issubclass(type(vector1), list) and issubclass(type(vector2), list):
            raise ValueError("The vectors should be a list")

        # Zip function is used to tie the elements of same index together into a tuple
        # These individual tuples are sent as an argument to the lambda function inside
        # The map function, The lambda function return the product of the tuples
        # Finally the sum of all such products are found using sum function to get the
        # dot product
        return sum(map(lambda arg: arg[0] * arg[1], zip(vector1, vector2)))
    except ValueError as err:
        LOGGER.error(err)


def find_projection(v_vector, u_vector):
    """
    Function to find the vector project of v_vector on to u_vector
    The definition of projection of u_v on v_v is given by:
    Proj (v_v, u_u) = ((v_v inner_product u_v)/(u_v inner_product u_v))*u_u

    :param v_vector: The vector being projected
    :type v_vector: list
    :param u_vector: The vector on which the other vector is being projected
    :type u_vector: list
    :return: projection
    :rtype: list
    """
    try:
        # Checking if the cubes is a list
        if not issubclass(type(v_vector), list) and issubclass(type(u_vector), list):
            raise ValueError("The vectors should be a list")

        # The numerator of the multiplication factor for finding
        # The projection is given by inner product of v_vector and u_vector
        numerator = inner_product(v_vector, u_vector)

        # The denominator of the multiplication factor for finding
        # The projection is given by inner product of u_vector and u_vector
        denominator = inner_product(u_vector, u_vector)
        mul_factor = numerator / denominator

        # The projection vector is given by multiplying the multiplication
        # Factor (mul_factor) with each elements of the u_vector
        projection = list(map(lambda arg: arg * mul_factor, u_vector))
        return projection
    except ValueError as err:
        LOGGER.error(err)


def orthogonalize_vectors(vectors):
    """
    Function to orthogonalize a set of vectors
    The orthogonalzied vector is found by the following formula:

            u(k) = v(k) - sum( projection(v(k), u(j) ) ......where j = 1, 2, ....k-1

    :param vectors: The set of vectors for which orthogonal vectors need to be found
    :type vectors: list
    :return: ortho_vectors - The orthogonalized vectors
    :rtype: list
    """

    try:
        # Checking if the cubes is a list
        if not issubclass(type(vectors), list):
            raise ValueError("The vectors should be a list")

        if len(vectors) > len(vectors[0]):
            raise ValueError("The number of vectors cannot be greater than it's dimension")

        # Initially the orthogonalized vectors are set to an empty list
        ortho_vectors = []

        # Looping over each vectors
        for vector in vectors:
            if not ortho_vectors:
                # If the vector is the first vector, then we append
                # It to the ortho_vectors list and then skip remaining code
                ortho_vectors.append(vector)
                continue

            # The list of projection are found by using a map function, which calls the
            # find_projection function with the given vector and all the orthogonalized
            # Vectors found previously
            projections = list(map(lambda arg: find_projection(vector, arg), ortho_vectors))

            # Since vector sum means addition of individual elements, we find the transpose
            # of the projections list
            transpose_projection = [*zip(*projections)]

            # Now vector sum is done using map function
            sum_projection = map(sum, transpose_projection)

            # The vector subtraction of the given vector and sum_projection is found
            # The zip function ties the elements of vector and sum_projects in same index
            # Together into a tuple, and these are sent as argument to the lambda function
            # Which finds the difference and rounds up to 2 decimal places
            new_ortho_vector = list(map(lambda arg: round(arg[0]-arg[1], 2), zip(vector, sum_projection)))
            ortho_vectors.append(new_ortho_vector)
        return ortho_vectors
    except ValueError as err:
        LOGGER.exception(err)
