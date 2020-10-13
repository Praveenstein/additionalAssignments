# -*- coding: utf-8 -*-
""" Module for determining the minimum number of transition
to organize the wallet

Problem Statement:
There are notes of denominations 10, 20, 50, 100, 200, 500, and 2000 rupees in a
wallet, but the notes are all messed up. Determine the minimum number of
transitions to organize the wallet so that all the notes of each denomination are
together. The notes need not necessarily be in sorted order.


This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * find_number_of_transition - function to find the number of transition
"""

# Standard imports
import logging
import numpy as np

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def find_number_of_transition(notes):
    """
    Function to find the number of transition required to group the wallet
    :param notes: An array denoting the money in wallet
    :type notes: list
    :return: Nothing
    :rtype: None
    """

    # Max Value of N - number of notes in the wallet
    max_n = int(1e5 + 9)

    # Table to store intermediate value in dynamic programming
    dp_table = np.zeros((max_n, 1 << 7, 7), dtype=np.int64)

    # Array denoting the notes in wallet
    notes_array = np.zeros(max_n, dtype=np.int64)

    # Bit value representation of the note denominations
    # Used for bit mapping
    converions = np.zeros(2001, dtype=np.int64)
    converions[10] = 0
    converions[20] = 1
    converions[50] = 2
    converions[100] = 3
    converions[200] = 4
    converions[500] = 5
    converions[2000] = 6

    for i in range(0, len(notes)):
        # Converting the original array to new one
        # Based on the integers defined previously
        notes_array[i] = converions[int(notes[i])]

    for i in range(0, len(notes)):
        for mask in range(0, 1 << 7):
            for j in range(0, 7):
                dp_table[i + 1][mask][j] = max(dp_table[i + 1][mask][j], dp_table[i][mask][j])
                if ((mask >> notes_array[i]) & 1) == False or (notes_array[i] == j):
                    dp_table[i + 1][mask | (1 << notes_array[i])][notes_array[i]] = max(dp_table[i + 1]
                                                                                        [mask | (1 << notes_array[i])]
                                                                                        [notes_array[i]],
                                                                                        dp_table[i][mask][j] + 1)
    ans = 0
    for mask in range(0, 1 << 7):
        for j in range(0, 7):
            ans = max(ans, dp_table[len(notes)][mask][j])

    number_of_transition = len(notes) - ans
    LOGGER.info("The number of transitions are: %s", number_of_transition)
