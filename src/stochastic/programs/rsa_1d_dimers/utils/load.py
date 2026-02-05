"""
    Contains the functions and routines to load a simulation.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import json
import pickle
import random

from pathlib import Path

# User.
from stochastic.programs.rsa_1d_dimers.simulation import Simulation


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
    with open(file, encoding="utf-8", mode="r") as stream:
        dictionary = json.load(stream)

    return dictionary


def _load_generator(file: str) -> random.Random:
    """
        Gets the dictionary loaded from the given JSON formatted file.

        :param file: The path to the pickle file where the generator is saved.

        :return: A dictionary with the loaded parameters.
    """
    # Auxiliary variables.
    generator: random.Random = random.Random(0)

    # Load the file as is.
    with open(file, mode="rb") as stream:
        generator = pickle.load(stream)

    return generator


def _set_generator(simulation: Simulation, generator: random.Random) -> None:
    """
        Sets the random number generator of the simulation.

        :param simulation: The simulation object on which the generator is
         going to be set.

        :param generator: The already initialized random number generator,
         i.e., a non-None random.Random object that is already seeded and
         has (potentially) been running.
    """
    # Set the generator.
    simulation.generator = generator


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Main
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def load_simulation(file_json: str, file_pickle: str) -> Simulation:
    """
        Loads a simulation from the given file.

        :param file_json: The path to the file where the saved simulation is
         stored.

        :param file_pickle: The path to the file where the saved pickled random
         generator is stored.

        :return: A consistent simulation object ready to be launched from the
         save point.
    """
    # Load the parameters and generator.
    parameters: dict = _load_simulation(file_json)
    generator: random.Random = _load_generator(file_pickle)

    # Create the simulation.
    simulation: Simulation = Simulation()

    # Set the simulation.
    _set_generator(simulation, generator)

    return simulation


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# TO DELETE!!
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def to_delete():
    """
        Runs the main program.
    """
    # Auxiliary variables.
    main: str = Path(
        "/home/andres/Projects/Python/Stochastic/temp/scripts",
        "RSA-1D-Dimers_20260204204502"
    )

    path_json: str = f"{main / 'save.json'}"
    path_pickle: str = f"{main / 'generator.pkl'}"

    # Load the simulation.
    load_simulation(path_json, path_pickle)


if __name__ == "__main__":
    to_delete()
