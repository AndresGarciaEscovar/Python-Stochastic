"""
    File that contains the class to run and manage the simulation.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# User.
from stochastic.programs.rsa_1d_dimers.validation.parameters import validate
from stochastic.programs.rsa_1d_dimers.classes.lattice import (
    RSA1DDimersLattice
)
from stochastic.programs.rsa_1d_dimers.classes.results import (
    RSA1DDimersResults
)
from stochastic.programs.rsa_1d_dimers.classes.statistics import (
    RSA1DDimersStatistics
)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class RSA1DDimersSimulation:
    """
        Contains the methods and variables to run a complete simulation and
        get the proper statistics.

        PARAMETERS:
        ___________

        - self.lattice: The lattice specific to the simulation; contains all
          the methods to run the simulation.

        - self.results: The object where the results of the simulation will be
          stored.

        - self.statistics: The object where the statistics of a single
          simulation will be stored.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(self, parameters: dict) -> None:
        """
            Constructor for the object.

            :param parameters: The simulation parameters that contains all the
             information to record the statistics.
        """
        # Validate the parameters.
        final: dict = validate(parameters)

        # Other parameters.
        self.lattice: RSA1DDimersLattice = RSA1DDimersLattice(final)
        self.results: RSA1DDimersResults = RSA1DDimersResults(final)
        self.statistics: RSA1DDimersStatistics = RSA1DDimersStatistics(final)
