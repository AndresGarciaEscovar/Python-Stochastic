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
# Main Function
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def run(parameters: dict) -> RSA1DDimersResults:
    """
        Runs the main simulation.

        :param parameters: The parameters to run the simulation.

        :return: The results of the simulation.
    """
    # Import the objects.
    statistics: RSA1DDimersStatistics = RSA1DDimersStatistics(parameters)
    lattice: RSA1DDimersLattice = RSA1DDimersLattice(parameters)
    results: RSA1DDimersResults = RSA1DDimersResults(parameters)

    return results
