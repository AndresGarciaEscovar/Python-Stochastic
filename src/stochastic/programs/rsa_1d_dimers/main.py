"""
    Code to run random sequential adsorption of dimers into a 1D lattice.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from importlib.resources import files as ifiles


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# User.
from stochastic.programs.rsa_1d_dimers import configs
from stochastic.programs.rsa_1d_dimers.validation.parameters import validate


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Main
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def print_parameters() -> None:
    """
        Prints the default parameters for the simulation.
    """
    # Auxiliary variables.
    file: str = "parameters.json"
    parameters: dict = {
        "encoding": "utf-8",
        "mode": "r"
    }

    # Open the file.
    with ifiles(configs).joinpath(file).open(**parameters) as stream:
        print(f"\n{stream.read()}", end="\n")


def run(parameters: dict) -> dict:
    """
        Runs the main simulation.

        :param parameters: A dictionary with the simulation parameters.

        :return: A dictionary with the results to be plotted.
    """
    # Get the simulation parameters.
    final: dict = validate(parameters)
