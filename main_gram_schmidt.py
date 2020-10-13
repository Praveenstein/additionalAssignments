# -*- coding: utf-8 -*-
""" Main Module for implementiong the gram_schmidt orthogonaliztion of given vectors

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations
    * json - to load json files

This script contains the following function
    * configure_logging - to configure logging
    * main - main function to perform the operations
"""

# Built-In Imports
import logging.config
import json
import argparse

# User Imports
from solutions.orthogonalization.gram_schmidt import orthogonalize_vectors

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
            line = list(map(lambda arg: float(arg.rstrip(",.\\n")), line))
            data.append(line)
    return data


def main():
    """
    Main function to perform orthogonalization
    :return: Nothing
    :rtype: None
    """
    arguments = get_input_arguments()
    configure_logging(arguments.logfile)

    vectors = get_input_data(arguments.inputfile)

    orthogonalized_vectors = orthogonalize_vectors(vectors)

    for row in orthogonalized_vectors:
        print(row)


if __name__ == '__main__':
    main()
