# -*- coding: utf-8 -*-
""" Module for filtering words
This scripts is used to filter out words in a given string
into categories such as lower case, upper case, mixed case
alpha numeric and digits

This script requires the following modules be installed in the python environment
    * re - Python built-in Regular expression module
    * logging - to perform logging operations

This script contains the following function
    * compile_regex - uses the re module to find all the substring
                        that match the pattern in the given text
    * categorize_words - Takes a string as input and categorized
                        the words in the string
"""

# Standard imports
import re
import logging

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def compile_regex(pattern, text):
    """
    Funciton to perform the string matching operations
    :param pattern: A regex string pattern to be searched for
    :type pattern: str
    :param text: The string from which the pattern has to be searched
    :type text: str
    :return: result- list of words from the text that matches the pattern
    :rtype: list
    """
    result = re.findall(pattern, text)
    return result


def categorize_words(string):
    """
    Function to perform the categorization of words in the given string
    :param string: The string from which the words need to be categorized
    :type string: str
    :return: Nothing
    :rtype: None
    """
    try:
        if not issubclass(type(string), str):
            raise ValueError("The input should be string")

        # The pattern string for getting only lower case words are done using
        # Positive and negative lookahead.
        # (?=.*[a-z]) Makes sure that at least one lower case letter exists
        # and (?!.*[A-Z])(?!.*[0-9]) Makes sure that no upper case or digit is present
        # .* is used to absorb the sub string as the lookahead is just an assertion
        lower_case_pattern = "\\b(?=.*[a-z])(?!.*[A-Z])(?!.*[0-9])\\b.*"
        lower_case_words = compile_regex(lower_case_pattern, string)
        LOGGER.info("Lower Case Words: %s", lower_case_words)

        # The pattern string for getting only upper case words are done using
        # Positive and negative lookahead.
        # (?=.*[A-Z]) Makes sure that at least one upper case letter exists
        # and (?!.*[a-z])(?!.*[0-9]) Makes sure that no lower case or digit is present
        # .* is used to absorb the sub string as the lookahead is just an assertion
        upper_case_pattern = "\\b(?!.*[a-z])(?=.*[A-Z])(?!.*[0-9])\\b.*"
        upper_case_words = compile_regex(upper_case_pattern, string)
        LOGGER.info("Upper Case Words: %s", upper_case_words)

        # The pattern string for getting only upper case words are done using
        # Positive and negative lookahead.
        # (?=.*[A-Z]) Makes sure that at least one upper case letter exists
        # (?=.*[a-z] Makes sure that at least one lower case letter exists
        # (?!.*[0-9]) Makes sure that no digits exist
        # .* is used to absorb the sub string as the lookahead is just an assertion
        mixed_case_pattern = "\\b(?=.*[a-z])(?=.*[A-Z])(?!.*[0-9])\\b.*"
        mixed_case_words = compile_regex(mixed_case_pattern, string)
        LOGGER.info("Mixed Case Words: %s", mixed_case_words)

        # The pattern string for getting only upper case words are done using
        # Positive and negative lookahead.
        # (?=.*[a-zA-Z]) Makes sure that at least one upper case letter or lower case exists
        # (?=.*[0-9]) Makes sure that at least one digit exist
        # .* is used to absorb the sub string as the lookahead is just an assertion
        alphanumeric_pattern = "\\b(?=.*[a-zA-Z])(?=.*[0-9])\\b.*"
        alphanumeric_words = compile_regex(alphanumeric_pattern, string)
        LOGGER.info("AlphaNumeric Words: %s", alphanumeric_words)

        # The pattern string for getting only upper case words are done using
        # Positive and negative lookahead.
        # (?!.*[A-Z]) Makes sure that no upper case exist
        # (?!.*[a-z] Makes sure that no lower case exist
        # (?=.*[0-9]) Makes sure that at least one digit exist
        # .* is used to absorb the sub string as the lookahead is just an assertion
        digit_pattern = "\\b(?!.*[a-z])(?!.*[A-Z])(?=.*[0-9])\\b.*"
        digits = compile_regex(digit_pattern, string)
        LOGGER.info("Digits: %s", digits)
    except ValueError as err:
        LOGGER.exception(err)
