"""
    File that contains the class to run and manage the simulation.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import pickle
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

        # Start the simulation.
        for _ in range(self.parameters.current_attempts, attempts):
            self._simulation_save(False, self.parameters.current_attempts)

            site: int = self.generator.randint(0, length)
            successful: bool = self.lattice.particle_adsorb([site, site + 1])

            self.statistics.update_statistics(self.lattice.lattice, successful)
            self.parameters.current_attempts += 1

        # Update the simulations completed.
        self.parameters.current_attempts = 0
        self.parameters.current_repetition += 1

    def _set_simulation(self) -> None:
        """
            Sets a simulation before starting to run a single simulation.
        """
        # Set the simulation.
        self.lattice.reset()
        self.statistics.reset()

        # Mark as unloaded.
        self.parameters.loaded = False

    def _set_working_directory(self) -> None:
        """
            Sets the working directory to the place where the results will
            be stored.
        """
        date: str = datetime.now().strftime("%Y%m%d%H%M%S")
        directory: str = f"{PROGRAM.replace(' ', '-')}_{date}"
        path: Path = Path(self.parameters.output["working"]) / directory

        # Set and create the working directory.
        path.mkdir(exist_ok=True, parents=False)
        self.parameters.output["working"] = f"{path}"

    def _simulation_save(self, end: bool, attempts: int = 0) -> None:
        """
            Saves the simulation to a json file.

            :param end: A boolean flag indicating whether the save is performed
             at the end of the simulation. True, if the save is being attempted
             at the end of the simulation; False, if the simulation is intended
             to be saved in the course of the simulation.

            :param attempts: The current number of attempts; zero by default.
        """
        # Save if needed.
        if self._validate_save(end, attempts):
            # Get the working directory.
            directory: Path = Path(self.parameters.output["working"])
            file_pickle: str = f"{directory / 'simulation.sim'}"

            # Extract the parameters in the dictionary.
            dictionary: dict = {
                "_metadata": {
                    "attempts": attempts,
                    "name": PROGRAM,
                    "save_date": datetime.now().strftime("%Y%m%d%H%M%S")
                },
                "simulation": self
            }

            # Pickle the simulation state.
            with open(file_pickle, mode="wb") as stream:
                pickle.dump(dictionary, stream)

    def _validate_save(self, end: bool, attempts: int) -> bool:
        """
            Saves the simulation to a json file.

            :param end: A boolean flag indicating whether the save is performed
             at the end of the simulation. True, if the save is being attempted
             at the end of the simulation; False, if the simulation is intended
             to be saved in the course of the simulation.

            :param attempts: The current number of attempts.

            :return: A boolean flag indicating whether the simulation must be
             saved. True, if the simulation must be saved; False, otherwise.
        """
        # Auxiliary variables.
        flag: bool = self.parameters.history["save"]

        # Check the conditions are appropriate to save the simulation.
        if flag:
            frequency: int = self.parameters.history["frequency"]

            flag = not end and frequency > 0 and attempts % frequency == 0
            flag = flag or (end and frequency < 1)

        return flag

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def run_simulations(self) -> None:
        """
            Runs the simulations.
        """
        # Auxiliary variables.
        repetitions: int = self.parameters.simulation["repetitions"]

        for _ in range(self.parameters.current_repetition, repetitions):
            # Run the simulation.
            self._run_simulation()
            self.results.statistics_add(self.statistics)

            # Try to save the simulation at the end.
            self.parameters.current_attempts = 0
            self.parameters.current_repetition += 1

            # Reset the variables.
            self._set_simulation()
            self._simulation_save(end=True)

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

    def __init__(self, parameters: dict = None) -> None:
        """
            Constructor for the object.

            :param parameters: The simulation parameters that contains all the
             information needed for the simulation. If the "parameters"
             parameter is None, the default parameters are set.
        """
        # Extract the parameters.
        parameters = {} if parameters is None else parameters

        # Extract the parameters.
        self.loaded: bool = False
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

        # raise NotImplementedError("Need to finish loading the simulation properly")
