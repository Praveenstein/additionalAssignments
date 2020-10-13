# -*- coding: utf-8 -*-
""" Module for generating a toeplitz matrix"""

# Built-In Imports
import logging.config
import json
import argparse

# User Imports
from solutions.toeplitz.generate_matrix import generate_toeplitz_matrix

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def get_input_arguments():
    """
    Function to get the input arguments from command line
    :return: args - arguments from the command line
    :rtype: argparse.Namespace
    """

    my_parser = argparse.ArgumentParser(allow_abbrev=False)
    my_parser.add_argument('--logfile', action='store', type=str, required=True)
    my_parser.add_argument('--inputfile', action='store', type=str, required=True)

    args = my_parser.parse_args()
    return args


def configure_logging(filepath):
    """
    Function to configure logging
    :return: None
    """
    with open(filepath, 'r') as file_object:
        config_data = json.load(file_object)
    logging.config.dictConfig(config_data)
    LOGGER.info("Configured Logging")


def get_input_data(filepath):
    """
    Function to load file having input data
    :param filepath: path of file consisting of input data
    :type filepath: str
    :return: data
    :rtype: list
    """

    with open(filepath) as file:
        data = []
        for line in file.readlines():
            line = line.split()

            # Stripping of comma, periods and new line and converting it to int
            line = list(map(lambda arg: int(arg.rstrip(",.\\n")), line))
            data.append(line)
    return data


def main():
    """
    Main function generate a toeplitz matrix
    :return: Nothing
    :rtype: None
    """
    arguments = get_input_arguments()
    configure_logging(arguments.logfile)

    elements = get_input_data(arguments.inputfile)
    if len(elements) > 1:
        matrix = generate_toeplitz_matrix(elements[0], elements[1])
    else:
        matrix = generate_toeplitz_matrix(elements[0])

    for row in matrix:
        print(row)


if __name__ == '__main__':
    main()
