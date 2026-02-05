"""
    Contains the validation of the load parameters.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Base dictionary with which to compare.
BASE: dict = {
    "_metadata": {
        "name": "RSA 1D Dimers",
        "save_date": "YYYYMMDDhhmmss"
    },
    "lattice": {
        "lattice": [],
        "length": 0,
        "periodic": False
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


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _validate_form(dictionary: dict) -> None:
    """
        Validates the form of the dictionary.

        :param dictionary: The dictionary to be validated.
    """


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
