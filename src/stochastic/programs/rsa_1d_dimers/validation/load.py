"""
    Contains the validation of the load parameters.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from datetime import datetime

# User.
from stochastic.programs.rsa_1d_dimers.simulation import PROGRAM
from stochastic.programs.rsa_1d_dimers.validation.parameters import (
    validate as vparameters
)
from stochastic.utilities.validate import validate_dictionary


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Base dictionary with which to compare.
BASE: dict = {
    "_metadata": {
        "name": PROGRAM,
        "save_date": "%Y%m%d%H%M%S"
    },
    "parameters": {
        "history": {
            "file": "",
            "frequency": 0,
            "save": False
        },
        "output": {
            "file": "",
            "working": ""
        },
        "simulation": {
            "attempts": 0,
            "length": 0,
            "periodic": False,
            "repetitions": 0,
            "seed": 0
        }
    },
    "results": {
        "simulations": 0,
        "attempts": [],
        "coverage": [],
        "empty_single": [],
        "empty_double": [],
        "empty_triple": []
    },
    "lattice": {
        "lattice": [],
        "length": 0,
        "periodic": False
    },
    "statistics": {
        "attempts": [],
        "coverage": [],
        "empty_single": [],
        "empty_double": [],
        "empty_triple": [],
        "length": 0,
        "periodic": False
    }
}

# Possible keys.
REQUIRED_KEYS: tuple = tuple(BASE.keys())


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _validate_form(dictionary: dict) -> None:
    """
        Validates the form of the dictionary.

        :param dictionary: The dictionary to be validated.
    """
    # Validate the different quantities.
    _validate_form_keys(dictionary)

    for key, value in dictionary.items():
        validate_dictionary(BASE[key], value, error=True)


def _validate_form_keys(dictionary: dict) -> None:
    """
        Validates that the dictionary has the proper base keys.

        :param dictionary: The dictionary to be validated.

        :raise KeyError: If the keys of the dictionary do not match the
         required keys.
    """
    # Auxiliary variables.
    current: set = set(dictionary.keys())
    expected_0: set =set(REQUIRED_KEYS)
    expected_1: set =set(REQUIRED_KEYS[:-2])

    # Validate the keys.
    if current not in (expected_0, expected_1):
        raise KeyError(
            f"The key of the loaded dictionary do not match the required "
            f"keys. Current keys: {current or '{}'}, expected keys: "
            f"{expected_0 or '{}'} or {expected_1 or '{}'}."
        )


def _validate_values(dictionary: dict) -> None:
    """
        Validates the values in the dictionary.

        :param dictionary: The dictionary to be validated.
    """
    # Validate the parameters.
    _: dict = vparameters(dictionary["parameters"])
    del _

    # Validate the other.
    _validate_values__metadata(dictionary["_metadata"])



def _validate_values__metadata(dictionary: dict) -> None:
    """
        Validates that the metadata is properly set.

        :param dictionary: The dictionary to be validated.

        :param ValueError: If any of the values are not properly set.
    """
    # Auxiliary variables.
    metadata: dict = BASE["_metadata"]

    # The names must match.
    key: str = "name"

    if dictionary[key] != metadata[key]:
        raise ValueError(
            f"The metadata \"{key}\" entry does not match the required value. "
            f"Required value: \"{metadata[key]}\", current value: "
            f"\"{dictionary[key]}\"."
        )

    # The date must be valid and have the proper format.
    key = "save_date"
    datetime.strptime(dictionary[key], metadata[key])


def _validate_values_parameters(dictionary: dict) -> None:
    """
        Validates that the parameters are properly set.

        :param dictionary: The dictionary to be validated.

        :param ValueError: If any of the values are not properly set.
    """
    # Auxiliary variables.
    metadata: dict = BASE["_metadata"]

    # The names must match.
    key: str = "name"

    if dictionary[key] != metadata[key]:
        raise ValueError(
            f"The metadata \"{key}\" entry does not match the required value. "
            f"Required value: \"{metadata[key]}\", current value: "
            f"\"{dictionary[key]}\"."
        )

    # The date must be valid and have the proper format.
    key = "save_date"
    datetime.strptime(dictionary[key], metadata[key])


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Main
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def validate_parameters(loaded: dict) -> None:
    """
        Validates that the parameters match for continuing the simulation.

        :param loaded: The parameters that were loaded from the simulation.
    """
    # Validate the dictionary.
    _validate_form(loaded)
    _validate_values(loaded)
