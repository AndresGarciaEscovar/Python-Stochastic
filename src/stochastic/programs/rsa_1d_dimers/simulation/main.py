"""
    File that contains the main point of entry to the simulation.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports.
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# User.
from stochastic.programs.rsa_1d_dimers.simulation.classes.statistics import (
    RSA1DDimersStatistics
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Function
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def run(parameters: dict) -> RSA1DDimersStatistics:
    """
        Runs the main simulation.

        :param parameters: The parameters to run the simulation.

        :return: The results of the simulation.
    """

    print(parameters["simulation"])

    statistics: RSA1DDimersStatistics = RSA1DDimersStatistics(parameters)
    # lattice:

    return statistics
