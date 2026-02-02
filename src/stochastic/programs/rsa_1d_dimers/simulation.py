"""
    File that contains the class to run and manage the simulation.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import random

# User.
from stochastic.programs.rsa_1d_dimers.classes.lattice import Lattice
from stochastic.programs.rsa_1d_dimers.classes.parameters import Parameters
from stochastic.programs.rsa_1d_dimers.classes.results import Results
from stochastic.programs.rsa_1d_dimers.classes.statistics import Statistics


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class Simulation:
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
    # Methods - Private
    # /////////////////////////////////////////////////////////////////////////

    def _run_simulation(self) -> None:
        """
            Runs the simulations.
        """
        # Auxiliary variables.
        attempts: int = self.parameters.simulation["attempts"]
        length: int = self.parameters.simulation["length"] - 1

        # Get a new lattice and statistics.
        self.lattice = Lattice(self.parameters.simulation)
        self.statistics = Statistics(self.parameters.simulation)

        for _ in range(attempts):
            site: int = self.generator.randint(0, length)
            successful: bool = self.lattice.particle_adsorb([site, site + 1])
            self.statistics.update_statistics(self.lattice.lattice, successful)

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def run_simulations(self) -> None:
        """
            Runs the simulations.
        """
        # Auxiliary variables.
        repetitions: int = self.parameters.simulation["repetitions"]

        for _ in range(repetitions):
            self._run_simulation()
            self.results.statistics_add(self.statistics)

        # Process the statistics.
        self.results.statistics_process()

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(self, parameters: dict) -> None:
        """
            Constructor for the object.

            :param parameters: The simulation parameters that contains all the
             information to record the statistics.
        """
        # Extract the parameters.
        self.parameters: Parameters = Parameters(parameters)
        seed: int = self.parameters.simulation["seed"]

        # Parameters.

        self.generator: random.Random = random.Random(seed)

        # Other parameters.
        self.lattice: Lattice = Lattice(self.parameters.simulation)
        self.results: Results = Results(self.parameters.simulation)
        self.statistics: Statistics = Statistics(self.parameters.simulation)

        self.run_simulations()
