"""
    File that contains the class to run and manage the simulation.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import random

from datetime import datetime
from pathlib import Path

# User.
from stochastic.programs.rsa_1d_dimers.classes.history import History
from stochastic.programs.rsa_1d_dimers.classes.lattice import Lattice
from stochastic.programs.rsa_1d_dimers.classes.parameters import Parameters
from stochastic.programs.rsa_1d_dimers.classes.results import Results
from stochastic.programs.rsa_1d_dimers.classes.statistics import Statistics


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Name of the program.
PROGRAM: str = "RSA 1D Dimers"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _get_header(text: str) -> str:
    """
        Gets the header for the given section.

        :param text: The name of the header, must be a relatively short string.

        :return: The string that represents the header of the section.
    """
    # Auxiliary variables.
    header: str = f"# {'-' * 78}"

    return f"{header}\n# {text}\n{header}\n"


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

            :param reset: A boolean flag indicating whether the statistics
             and the lattice must be reset. True, if the statistics and lattice
             must be reset; False, otherwise. True, by default.
        """
        # Auxiliary variables.
        attempts: int = self.parameters.simulation["attempts"]
        length: int = self.parameters.simulation["length"] - 1

        # Get a new lattice and statistics.
        self.lattice.reset()
        self.statistics.reset()

        for _ in range(attempts):
            site: int = self.generator.randint(0, length)
            successful: bool = self.lattice.particle_adsorb([site, site + 1])
            self.statistics.update_statistics(self.lattice.lattice, successful)

    def _set_working_directory(self) -> None:
        """
            Sets the working directory to the place where the results will
            be stored.
        """
        # Auxiliary variables.
        date: str = datetime.now().strftime("%Y%m%d%H%M%S")
        directory: str = f"{PROGRAM.replace(' ', '-')}_{date}"
        path: Path = Path(self.parameters.output["working"]) / directory

        # Set and create the working directory.
        path.mkdir(exist_ok=True, parents=False)
        self.parameters.output["working"] = f"{path}"

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
            self.results.statistics_add(self.statistics)

        # Process the statistics.
        self.results.statistics_process()

        # Save the results.
        self.save_results()

    def save_results(self) -> None:
        """
            Saves the final simulation results to the working directory.
        """
        # Auxiliary variables.
        path: Path = Path(self.parameters.output["working"])
        file: Path = path / self.parameters.output["file"]

        # Name of the file.
        with open(f"{file}", encoding="utf-8", mode="w") as stream:
            stream.write(f"{self.results}")

    def save_history(self) -> None:
        """
            Saves the state of the lattice to the given file, if requested.
        """
        # Auxiliary variables.
        flag: bool = self.parameters.history["save"]
        flag = flag and self.parameters.history["frequency"] > 0

        # Only save if requested.
        if flag:
            # Get the file where the lattice will be saved.
            working: Path = Path(self.parameters.output["working"])
            file: str = f"{working / self.parameters.history['file']}"

            with open(file, encoding="utf-8", mode="w") as stream:
                stream.write(_get_header("Parameters\n"))
                stream.write(f"{self.parameters}")

                stream.write(_get_header("Lattice\n"))
                stream.write(f"{self.lattice}")

                stream.write(_get_header("Statistics\n"))
                stream.write(f"{self.statistics}")

                stream.write(_get_header("Results\n"))
                stream.write(f"{self.results}")

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(self, parameters: dict) -> None:
        """
            Constructor for the object.

            :param parameters: The simulation parameters that contains all the
             information needed for the simulation.
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

        # Finish setting other quantities.
        self._set_working_directory()

        # Initialize the history.
        self.history: History = History(
            self.parameters,
            self.lattice,
            self.results,
            self.statistics
        )
