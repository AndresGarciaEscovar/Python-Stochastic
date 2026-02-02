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
from pathlib import Path

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
    # No need to check the parameters.
    if not parameters["save"]:
        return parameters

    # Check the output file path.
    file: Path = Path(parameters["file"])

    if len(file.parts) != 1:
        raise ValueError(
            f"The name of the history file must not have any addtional path, "
            f"i.e., it must only be the name of the file; current path: "
            f"{file}."
        )

    if f"{file.with_suffix('')}".strip() == "":
        raise ValueError("The name of the history file cannot be empty.")

    if file.suffix != ".txt":
        raise ValueError(
            f"The name of the history file must have a \".txt\" extension; "
            f"current extension: \"{file.suffix}\"."
        )

    # Validate the interval is a positive number.
    if parameters["interval"] < 0.0:
        raise ValueError(
            f"The saving interval must be greater than or equal to zero; "
            f"current interval setting: {parameters['interval']}."
        )

    return parameters


def validate_parameters_output(parameters: dict) -> None:
    """
        Validates the parameters specific to the output.

        :param parameters: The dictionary of parameters related to the
         "output" entry.

        :return: A dictionary with the output parameters.

        :raise ValueError: If the working directory does not exist. If the
         output file name has subdirectories. If the output file name is
         empty. If the output file name has a different extension than ".txt".
    """
    # Set the proper working directory.
    if parameters["working"].strip() == "":
        parameters["working"] = f"{Path.cwd()}"

    # Check the working directory.
    if not Path(parameters["working"]).is_dir():
        raise ValueError(
            f"The given path \"{parameters['working']}\" for the working "
            f"directory is not a directory; create the directory before "
            f"setting it."
        )

    # Check the output file path.
    file: Path = Path(parameters["file"])

    if len(file.parts) != 1:
        raise ValueError(
            f"The name of the file must not have any addtional path, i.e., it "
            f"must only be the name of the file; current path: {file}."
        )

    if f"{file.with_suffix('')}".strip() == "":
        raise ValueError("The name of the output file cannot be empty.")

    if file.suffix != ".txt":
        raise ValueError(
            f"The name of the output file must have a \".txt\" extension; "
            f"current extension: \"{file.suffix}\"."
        )

    return parameters


def validate_parameters_simulation(parameters: dict) -> None:
    """
        Validates the parameters specific to the simulation.

        :param parameters: The dictionary of parameters related to the
         "simulation" entry.

        :return: A dictionary with the simulation parameters.
    """
    # Set the seed.
    if parameters["seed"] < 0:
        parameters["seed"] = int(time.time())

    # Check the other values.
    message: str = ""
    skip: tuple = ("periodic",)

    for key, value in parameters.items():
        # No neeed to check these parameters.
        if key in skip:
            continue

        # Values must be positive, greater than zero.
        if value <= 0.0:
            message += (
                f"The value (for the \"simulation\".\"{key}\" parameter) is "
                f"negative, it must be a positive value, i.e., greater than "
                f"or equal to zero. "
            )

    # Check if an error must be thrown.
    if message != "":
        raise ValueError(message)

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

    # Validate the dictionary structure.
    if parameters != {}:
        # Validate the dictionary format and extract the parameters.
        validate_dictionary_sub(default, parameters, error=True)
        default = format_dictionary(default, parameters)

    # Validate the specific parameters.
    default = validate_parameters(default)

    return default
