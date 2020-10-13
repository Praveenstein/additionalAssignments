# -*- coding: utf-8 -*-
""" Module for counting the occurrences of words in a sentence

Problem Statement:
Given a sentence find the number of unique words in the input, and its
corresponding count. The output is expected in the form of a dictionary where
the key represents the word and value represents the corresponding count. The
keys should be in the same order as appeared in the input.

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations

This script contains the following function
    * check_for_piling - Checks if the rows of cube could be piled up vertically
"""

# Standard imports
import logging
__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def count_words(sentence):
    """
    Function used to count the occurrences of all words in a given sentence
    :param sentence: The sentence in which the occurrences need to be counted
    :type sentence: str
    :return: Nothing
    :rtype: None
    """
    try:
        # Checking if the cubes is a list
        if not issubclass(type(sentence), str):
            raise ValueError("The sentence should be a string")

        # Splitting the string into a list of words
        words = sentence.split()

        # Converting all the words to lower case and stripping of any trailing
        # comma or period
        words = list(map(lambda arg: (arg.lower()).rstrip(",."), words))

        word_count = dict()
        for word in words:
            # Looping over all the words

            # The get method is used to get the value from dictionary
            # and incremented by one if the key already exist
            # If the key does not exist, then it returns the default value
            # Of zero and then it is incremented by one
            word_count[word] = word_count.get(word, 0) + 1

        for word, count in word_count.items():
            LOGGER.info("Word: %s   Count: %s", word, count)
    except ValueError as err:
        LOGGER.exception(err)
