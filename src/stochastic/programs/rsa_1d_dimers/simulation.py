"""
    File that contains the class to run and manage the simulation.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import json
import random

from datetime import datetime
from pathlib import Path

# User.
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
        self._set_simulation()

        for _ in range(attempts):
            site: int = self.generator.randint(0, length)
            successful: bool = self.lattice.particle_adsorb([site, site + 1])
            self.statistics.update_statistics(self.lattice.lattice, successful)

        # Save the complete simulation.
        self._simulation_save("complete")

    def _set_simulation(self) -> None:
        """
            Sets a simulation before starting to run a single simulation.
        """
        # For the moment, set the simulation.
        self.lattice.reset()
        self.statistics.reset()

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

    def _simulation_save(self, stype: str) -> None:
        """
            Saves the simulation to a json file.

            :param stype: The type of simulation to be saved.
        """
        # Get the working directory.
        directory: Path = Path(self.parameters.output["working"])
        file: str = f"{directory / 'save.json'}"

        # State variables.
        if stype == "partial":
            state: dict = {
                "parameters": self.parameters.get_dictionary(),
                "results": self.results.get_dictionary(),
            }

        elif stype == "complete":
            state: dict = {
                "parameters": self.parameters.get_dictionary(),
                "lattice": self.lattice.get_dictionary(),
                "results": self.results.get_dictionary(),
                "statistics": self.statistics.get_dictionary(),
            }

        else:
            raise ValueError(
                f"The requested save type is not valid; must be either "
                f"'complete' or 'partial'; current value of {stype = }."
            )

        # Save the dictionary.
        with open(file, encoding="utf-8", mode="w") as stream:
            json.dump(state, stream, indent=4)

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

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(self, parameters: dict) -> None:
        """
            Constructor for the object.

            :param parameters: The simulation parameters that contains all the
             information needed for the simulation.

            :param file: A string with the path to the file to load a
             simulation. If the string is "None", the simulation starts from
             scratch.
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
