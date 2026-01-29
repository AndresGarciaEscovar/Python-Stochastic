"""
    File that contains the main point of entry to the simulation.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports.
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# User.
from stochastic.programs.rsa_1d_dimers.simulation.classes.lattice import (
    RSA1DDimersLattice
)
from stochastic.programs.rsa_1d_dimers.simulation.classes.results import (
    RSA1DDimersResults
)
from stochastic.programs.rsa_1d_dimers.simulation.classes.statistics import (
    RSA1DDimersStatistics
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _run_simulation(parameters: dict) -> RSA1DDimersResults:
    """
        Runs the one time simulation the number of requested times.

        :param parameters: The parameters to run the simulations.

        :return: The processed results of the simulation.
    """
    attempts: int = parameters["simulation"]["attempts"]

    statistics: RSA1DDimersStatistics = RSA1DDimersStatistics(parameters)
    lattice: RSA1DDimersLattice = RSA1DDimersLattice(parameters)
    results: RSA1DDimersResults = RSA1DDimersResults(parameters)

    print(f"{results}")

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Function
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def run(parameters: dict) -> RSA1DDimersResults:
    """
        Runs the main simulation.

        :param parameters: The parameters to run the simulation.

        :return: The results of the simulation.
    """
    # Import the objects.
    results: RSA1DDimersResults = _run_simulation(parameters)

    print("HERE")

    return results
