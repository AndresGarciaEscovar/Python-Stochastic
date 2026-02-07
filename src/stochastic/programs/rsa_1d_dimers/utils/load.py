"""
    Contains the functions and routines to load a simulation.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import pickle

from pathlib import Path

# User.
from stochastic.programs.rsa_1d_dimers.simulation import Simulation
from stochastic.programs.rsa_1d_dimers.validation.load import (
    validate_parameters
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _load_simulation(file: str) -> dict:
    """
        Gets the dictionary loaded from the given JSON formatted file.

        :param file: The path to the JSON file where the general simulations
         are saved.

        :return: A dictionary with the loaded parameters.
    """
    # Auxiliary variables.
    dictionary: dict = {}

    # Load the file as is.
    with open(file, mode="rb") as stream:
        dictionary = pickle.load(stream)

    return dictionary


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Main
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def load_simulation(file_pickle: str) -> Simulation:
    """
        Loads a simulation from the given file.

        :param file_pickle: The path to the file where the saved pickled random
         generator is stored.

        :return: A consistent simulation object ready to be launched from the
         save point.
    """
    # Load the parameters and generator.
    parameters: dict = _load_simulation(file_pickle)

    # Validate the parameters before loading.
    validate_parameters(parameters)

    # Create the simulation, and mark it as loaded.
    simulation: Simulation = parameters["simulation"]
    simulation.loaded = True

    return simulation


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# TO DELETE!!
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def to_delete():
    """
        Runs the main program.
    """
    # Auxiliary variables.
    path_pickle: str = Path(
        "/home/andres/Projects/Python/Stochastic/temp/scripts",
        "RSA-1D-Dimers_20260206210439",
        'simulation.sim'
    )

    # Load the simulation.
    load_simulation(f"{path_pickle}")

    # Continue in this file!
    # raise NotImplementedError("Continue here!!!")


if __name__ == "__main__":
    to_delete()
