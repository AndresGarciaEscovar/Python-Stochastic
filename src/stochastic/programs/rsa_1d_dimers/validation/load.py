"""
    Contains the validation of the load parameters.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from datetime import datetime
from typing import Any

# User.
from stochastic.programs.rsa_1d_dimers.simulation import PROGRAM, Simulation


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Base dictionary with which to compare.
BASE: dict = {
    "_metadata": {
        "attempts": 0,
        "name": PROGRAM,
        "save_date": "%Y%m%d%H%M%S"
    },
    "simulation": None,
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

    print("HERE")


def _validate_form_keys(dictionary: dict) -> None:
    """
        Validates that the dictionary has the proper base keys.

        :param dictionary: The dictionary to be validated.

        :raise KeyError: If the keys of the dictionary do not match the
         required keys.
    """
    # Auxiliary variables.
    current: set = set(dictionary.keys())
    expected: set = set(REQUIRED_KEYS)

    # Validate the keys.
    if current != expected:
        raise KeyError(
            f"The key of the loaded dictionary do not match the required "
            f"keys. Current keys: {current or '{}'}, expected keys: "
            f"{expected or '{}'}."
        )


def _validate_values(dictionary: dict) -> None:
    """
        Validates that the dictionary values are consistent with what is
        expected.

        :param dictionary: The dictionary to be validated.
    """
    # Validate the different entries.
    _validate_values__metadata(dictionary["_metadata"])


def _validate_values__metadata(dictionary: dict) -> None:
    """
        Validates that the dictionary values are consistent with what is
        expected.

        :param dictionary: The dictionary of metadata values to be validated.
    """
    # Auxiliary variables.
    metadata: dict = BASE["_metadata"]

    expected: set = set(metadata.keys())
    current: set = set(dictionary.keys())

    # Validate the keys.
    if current != expected:
        raise KeyError(
            f"The key of the metadata dictionary do not match the required "
            f"keys. Current keys: {current or '{}'}, expected keys: "
            f"{expected or '{}'}."
        )

    # Validate the attempts.
    attempts: Any = dictionary["attempts"]

    if not isinstance(attempts, int) or attempts < metadata["attempts"]:
        raise ValueError(
            f"The number of \"attempts\" must be a number greater than or "
            f"equal to zero; current type: {type(attempts)}, current value: "
            f"{attempts}."
        )

    # Validate that the date has the correct form.
    if dictionary["name"] != metadata["name"]:
        raise ValueError(
            f"The name of the simulation must be \"{metadata['name']}\", this "
            f"does not correspond to a {metadata['name']} simulation."
        )

    # Try to load the date.
    datetime.strptime(dictionary["save_date"], metadata["save_date"])


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
