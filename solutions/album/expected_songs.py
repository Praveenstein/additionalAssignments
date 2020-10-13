# -*- coding: utf-8 -*-
""" Module for finding the expected number of songs

Problem Statement:
There are N songs in the album. After some song is over the next one is chosen
randomly and independently of what has been played before. Determine the
expected number of songs to listen to until every song is played at least once.

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * find_expected_songs - finds the dot product of given two vectors
"""

# Standard imports
import logging
import math

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def find_expected_songs(length):
    """
    Function to find the expected number of songs

    The expected number of songs to be played before each song is played at least once
    Is given by:
                    Length * H(n) ....... Where H(n) is the nth harmonic number
    This is further simplified to :
                    Length * [log(n) + GAMMA + (0.5 / length)] ...... Where GAMMA = Euler–Mascheroni constant
                                                                                  = 0.577245
    :param length: Number of songs in the album
    :type length: int
    :return: Nothing
    :rtype: None
    """

    try:
        if not issubclass(type(length), int):
            raise ValueError("The number of songs in the album should be an integer")

        expected_value = round(length*(math.log(length) + 0.5772156649 + (0.5 / length)), 1)
        LOGGER.info("The expected number of songs are: %s", expected_value)
    except ValueError as err:
        LOGGER.error(err)
