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
from stochastic.programs.rsa_1d_dimers import configs
from stochastic.utilities.general import format_dictionary
from stochastic.utilities.validate import validate_dictionary_sub


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


def validate_parameters(parameters: dict) -> None:
    """
        Validates that the different quantities take appropriate values for the
        simulation.

        :param parameters: A dictionary with the complete simulation
         parameters.
    """
    # Auxiliary variables (LEAVE IN THIS ORDER).
    functions: dict = {
        "output": validate_parameters_output,
        "history": validate_parameters_history,
        "simulation": validate_parameters_simulation,
    }

    # Validate and updated the parameters.
    for name, function in functions.items():
        parameters[name] = function(parameters[name])

    return parameters


def validate_parameters_history(parameters: dict) -> None:
    """
        Validates the parameters specific to the history.

        :param parameters: The dictionary of parameters related to the
         "history" entry.

        :return: A dictionary with the history parameters.
    """
    return parameters


def validate_parameters_output(parameters: dict) -> None:
    """
        Validates the parameters specific to the output.

        :param parameters: The dictionary of parameters related to the
         "output" entry.

        :return: A dictionary with the output parameters.
    """
    return parameters


def validate_parameters_simulation(parameters: dict) -> None:
    """
        Validates the parameters specific to the simulation.

        :param parameters: The dictionary of parameters related to the
         "simulation" entry.

        :return: A dictionary with the simulation parameters.
    """
    return parameters


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

    # Validate the dictionary.
    if parameters != {}:
        # Validate the dictionary format and extract the parameters.
        validate_dictionary_sub(default, parameters, error=True)
        default = format_dictionary(default, parameters)

    # Validate the specific parameters.
    default = validate_parameters(default)

    return default
