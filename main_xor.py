# -*- coding: utf-8 -*-
""" Module for testing out the XOR operations"""

# Built-In Imports
import logging.config
import json
import argparse

# User Imports
from solutions.xor_operation.testing_xor import checking_xor

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
        data = file.read()

    data = data.split()
    data = list(map(lambda arg: int(arg.rstrip(",.")), data))
    return data


def main():
    """
    Main function to get inputs and call function to check xor operations
    :return: Nothing
    :rtype: None
    """
    arguments = get_input_arguments()
    configure_logging(arguments.logfile)

    elements = get_input_data(arguments.inputfile)
    LOGGER.info(elements)
    LOGGER.info("Starting to check the XOR operations")
    checking_xor(elements)
    LOGGER.info("Done Checking")


if __name__ == '__main__':
    main()
