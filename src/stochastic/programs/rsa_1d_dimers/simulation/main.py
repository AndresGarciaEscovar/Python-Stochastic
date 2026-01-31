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

        :return: The averaged results of the simulation.
    """
    # Auxiliary variables.
    repetitions: int = parameters["simulation"]["repetitions"]
    results: RSA1DDimersResults = RSA1DDimersResults(parameters)

    # Run the simulation the given number of times.
    for _ in range(repetitions):
        # Get the statistics and process them.
        statistics: RSA1DDimersStatistics = run_simulation_single(parameters)
        results.statistics_add(statistics)

    # Process the statistics.
    results.statistics_process()

def run_simulation_single(parameters: dict) -> RSA1DDimersStatistics:
    """
        Runs a single simulation, that is, makes N attempts to adsorb a
        particle into a lattice and takes the statistics associated with it.

        :param parameters: The parameters of the simulation.
    """
    statistics: RSA1DDimersStatistics = RSA1DDimersStatistics(parameters)
    lattice: RSA1DDimersLattice = RSA1DDimersLattice(parameters)

    return statistics

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
