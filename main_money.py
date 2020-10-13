# -*- coding: utf-8 -*-
""" Main Module for finding the number of transition to group the
money in wallet

This script requires the following modules be installed in the python environment
    * logging - to perform logging operations
    * json - to load json files

This script contains the following function
    * configure_logging - to configure logging
    * main - main function to find the number of transition
"""

# Built-In Imports
import logging.config
import json

# User Imports
from solutions.wallet.group_money import find_number_of_transition

__author__ = "praveen@gyandata.com"

LOGGER = logging.getLogger(__name__)


def configure_logging():
    """
    Function to configure logging
    :return: None
    """
    with open("configs\\log.json", 'r') as file_object:
        config_data = json.load(file_object)
    logging.config.dictConfig(config_data)
    LOGGER.info("Configured Logging")


def main():
    """
    Main function to find number of transitions to organize wallets
    :return: Nothing
    :rtype: None
    """
    configure_logging()

    wallet = [100, 200, 200, 500, 100, 100, 500, 100, 100]
    find_number_of_transition(wallet)
    LOGGER.info("Done")


if __name__ == '__main__':
    main()
