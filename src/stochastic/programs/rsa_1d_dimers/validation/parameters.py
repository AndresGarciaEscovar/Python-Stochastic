"""
    Contains the function for validating the parameters.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import json
import time

from importlib.resources import files as ifiles

# User.
import stochastic.programs.rsa_1d_dimers.configs as configs

# from stochastic.rsa_1d_dimers.validation.parameters import validate


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def load_base() -> dict:
    """
        From the json file, imports the base dictionary.

        :return: The dictionary with the default settings.
    """
    # Auxiliary variables.
    config: dict = {
        "encoding": "utf-8",
        "mode": "r"
    }

    # Read and return the default dictionary.
    with ifiles(configs).joinpath("parameters.json").open(**config) as stream:
        return json.load(stream)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Main
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def validate(parameters: dict) -> dict:
    """
        Validates the parameters that the user wants to override.

        :param parameters: The parameters to be overridden.

        :return: A dictionary with the complete simulation parameters.
    """
    # Auxiliary variables.
    default: dict = load_base()

    return {}

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# TO DELETE
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    print(int(100))
    print(int(time.time()))
