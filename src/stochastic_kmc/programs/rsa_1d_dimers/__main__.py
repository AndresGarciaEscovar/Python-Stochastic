"""
    Contains the functions to run the program from the console.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import json

from argparse import ArgumentParser, Namespace
from importlib.resources import files as ifiles

# User.
from stochastic_kmc.programs.rsa_1d_dimers import configs
from stochastic_kmc.programs.rsa_1d_dimers.simulation import Simulation


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _get_arguments() -> dict:
    """
        Gets the options from the command line arguments.

        :return: A dictionary with the command line arguments properly
         formatted.
    """
    # Auxiliary variables.
    parser: ArgumentParser = ArgumentParser(
        prog=Simulation.PROGRAM,
        description=f"Runs a simulation for the {Simulation.PROGRAM}",
    )

    # Arguments: Positional.
    parser.add_argument(
        "file",
        default="",
        nargs="?",
        type="str",
        help="The name of the file where the configuration options are stored."
    )

    # Arguments: Optional.
    parser.add_argument(
        "-p",
        "--print",
        action="store_true",
        help=(
            "Flag that indicates whether the default configuration options "
            "must be printed."
        )
    )

    # Get the arguments and validate them.
    arguments: Namespace = parser.parse_args()

    if arguments.file is not None and arguments.print:
        raise ValueError(
            "Two arguments are being simultaneosly used, use one at a time."
        )

    return {
        "path": arguments.file,
        "print": arguments.print
    }


def _get_parameters(name: str) -> dict:
    """
        Gets the options from the command line arguments.

        :param name: The name of the file where the configuration is being
         stored.

        :return: A dictionary with the command line arguments properly
         formatted.
    """
    # Auxiliary variables.
    parameters: dict = {}

    # Read the parameters, if required.
    if name.strip() != "":
        with open(name, encoding="uft-8", mode="r") as stream:
            parameters = json.load(stream)

    return parameters


def _print_parameters() -> None:
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


def _run(path: str) -> dict:
    """
        Runs the main simulation.

        :param path: The path to the file where the configuration is stored.
    """
    # Auxiliary variables.
    parameters: dict = _get_parameters(path)

    # Create and run the simulation.
    simulation: Simulation = Simulation(parameters)
    simulation.run_simulations()


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Main
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def main() -> None:
    """
        Runs the main function of the program.
    """
    # Auxiliary variables.
    arguments: dict = _get_arguments()

    if arguments["print"]:
        # Print the default parameters.
        _print_parameters()

    else:
        # Create and run the simulation.
        _run(arguments["path"])
