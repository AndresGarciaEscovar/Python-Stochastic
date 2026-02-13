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
from stochastic_kmc.programs.rsa_2d_dimers.classes.lattice import (
    Lattice
)
from stochastic_kmc.programs.rsa_2d_dimers.classes.parameters import (
    Parameters
)
from stochastic_kmc.programs.rsa_2d_dimers.classes.results import (
    Results
)
from stochastic_kmc.programs.rsa_2d_dimers.classes.statistics import (
    Statistics
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Name of the program.
PROGRAM: str = "RSA 2D Dimers"


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _get_banner(text: str) -> str:
    """
        Gets the banner for the section.

        :param text: The text to be placed in the header banner.

        :return: The banner with the required text.
    """
    # Auxiliary variables.
    base: str = f"# {'$' * 78}"

    return f"{base}\n# {text}\n{base}\n"


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
    # Methods - Auxiliary
    # /////////////////////////////////////////////////////////////////////////

    def _get_info_string(self) -> str:
        """
            Gets the simulation class specific parameters as a string.

            :return: A string specific with the simulation class parameters
             that are not nested in classes.
        """
        # Auxiliary variables.
        string: str = f"\n{_get_banner('Simulation')}\n"
        string += f"current repetition: {self.parameters.current_repetition}\n"
        string += f"current attempts: {self.parameters.current_attempts}\n"
        string += f"loaded: {self.loaded}\n"

        return string

    def _run_simulation(self) -> None:
        """
            Runs the simulations.
        """
        # Auxiliary variables.
        attempts: int = self.parameters.simulation["attempts"]
        length: int = self.parameters.simulation["dimensions"]["length"]
        width: int = self.parameters.simulation["dimensions"]["width"]

        total_sites: int = length * width
        total_sites -= 1

        # Start the simulation.
        for attempt in range(self.parameters.current_attempts, attempts):
            # Periodically save the simulation.
            self._save_simulation(False, attempt)
            self._save_lattice(False, attempt)

            # Make the move.
            side: str = self.generator.choice(Lattice.DIRECTIONS)
            site: int = self.generator.randint(0, total_sites)

            site_x: int = site // width
            site_y: int = site % width

            successful: bool = self.lattice.particle_adsorb(
                site_x,
                site_y,
                side
            )

            # Take the statistics and update the counter.
            self.statistics.update_statistics(self.lattice.lattice, successful)
            self.parameters.current_attempts += 1

    def _save_lattice(self, end: bool, attempts: int) -> None:
        """
            Saves the lattice to a text file.

            :param end: A boolean flag indicating whether the save is performed
             at the end of the simulation. True, if the save is being attempted
             at the end of the simulation; False, if the simulation is intended
             to be saved in the course of the simulation.

            :param attempts: The current number of attempts; zero by default.
        """
        # Save if needed.
        if self._validate_save_lattice(end, attempts):
            # Get the working directory.
            directory: Path = Path(self.parameters.output["working"])
            file: str = self.parameters.history_lattice["file"]
            file_text: str = f"{directory / file}"

            # Check the directory exists.
            if not directory.is_dir():
                raise ValueError(
                    f"Select a valid directory, current directory is not "
                    f"valid: {directory}"
                )

            # Write the simulation state.
            with open(file_text, encoding="utf-8", mode="a") as stream:
                attempts: int = self.parameters.current_attempts
                stream.write(f"Current attempts: {attempts}\n")
                stream.write(f"{self.lattice.get_lattice_string(True)}\n\n")

    def _save_simulation(self, end: bool, attempts: int = 0) -> None:
        """
            Saves the simulation to a binary file.

            :param end: A boolean flag indicating whether the save is performed
             at the end of the simulation. True, if the save is being attempted
             at the end of the simulation; False, if the simulation is intended
             to be saved in the course of the simulation.

            :param attempts: The current number of attempts; zero by default.
        """
        # Save if needed.
        if self._validate_save_simulation(end, attempts):
            # Get the working directory.
            directory: Path = Path(self.parameters.output["working"])
            file: str = self.parameters.history["file"]
            file_pickle: str = f"{directory / file}"

            # Check the directory exists.
            if not directory.is_dir():
                raise ValueError(
                    f"Select a valid directory, current directory is not "
                    f"valid: {directory}"
                )

            # Extract the parameters in the dictionary.
            dictionary: dict = {
                "_metadata": {
                    "name": PROGRAM,
                    "save_date": datetime.now().strftime("%Y%m%d%H%M%S")
                },
                "simulation": self
            }

            # Pickle the simulation state.
            with open(file_pickle, mode="wb") as stream:
                pickle.dump(dictionary, stream)

    def _set_simulation(self) -> None:
        """
            Sets a simulation before starting to run a single simulation.
        """
        # Set the simulation.
        self.lattice.reset()
        self.statistics.reset()

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

    def _validate_save_lattice(self, end: bool, attempts: int) -> bool:
        """
            Validates the lattice is to be saved.

            :param end: A boolean flag indicating whether the save is performed
             at the end of the simulation. True, if the save is being attempted
             at the end of the simulation; False, if the simulation is intended
             to be saved in the course of the simulation.

            :param attempts: The current number of attempts.

            :return: A boolean flag indicating whether the simulation must be
             saved. True, if the simulation must be saved; False, otherwise.
        """
        # Auxiliary variables.
        total_attempts: int = self.parameters.simulation["attempts"]
        frequency: int = self.parameters.history_lattice["frequency"]
        flag: bool = frequency > 0

        # Check the end condition and frequency condition.
        if flag:
            cond: bool = total_attempts == frequency

            flag = end and cond
            flag = flag or (not end and not cond and attempts % frequency == 0)

        return flag

    def _validate_save_simulation(self, end: bool, attempts: int) -> bool:
        """
            Validates the simulation is to be saved.

            :param end: A boolean flag indicating whether the save is performed
             at the end of the simulation. True, if the save is being attempted
             at the end of the simulation; False, if the simulation is intended
             to be saved in the course of the simulation.

            :param attempts: The current number of attempts.

            :return: A boolean flag indicating whether the simulation must be
             saved. True, if the simulation must be saved; False, otherwise.
        """
        # Auxiliary variables.
        total_attempts: int = self.parameters.simulation["attempts"]
        frequency: int = self.parameters.history["frequency"]
        flag: bool = frequency > 0

        # Check the end condition and frequency condition.
        if flag:
            cond: bool = total_attempts == frequency

            flag = end and cond
            flag = flag or (not end and not cond and attempts % frequency == 0)

        return flag

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Dunder
    # /////////////////////////////////////////////////////////////////////////

    def __str__(self) -> str:
        """
            The string representation of the simulation class with the current
            state at the time it is invoked.

            :return: The string with the class representation.
        """
        # Append all the strings.
        string: str = self._get_info_string()
        string += f"\n{_get_banner('Parameters')}\n{self.parameters}\n"
        string += f"\n{_get_banner('Lattice')}\n{self.lattice}\n"
        string += f"\n{_get_banner('Statistics')}\n{self.statistics}\n"
        string += f"\n{_get_banner('Results')}\n{self.results}\n"

        return string

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def run_simulations(self) -> None:
        """
            Runs the simulations.
        """
        # Auxiliary variables.
        attempts: int = self.parameters.simulation["attempts"]
        repetitions: int = self.parameters.simulation["repetitions"]

        for _ in range(self.parameters.current_repetition, repetitions):
            # Run the simulation.
            self._run_simulation()
            self.results.statistics_add(self.statistics)

            # Save the lattice.
            self._save_lattice(True, attempts)

            # Try to save the simulation at the end.
            self.parameters.current_attempts = 0
            self.parameters.current_repetition += 1

            # Reset the variables.
            self._set_simulation()
            self._save_simulation(True, attempts)

        # Process the statistics.
        self.results.statistics_process()

        # Save the results.
        self.save_results()

        # Print the location of the saved results.
        directory: str = self.parameters.output["working"]

        print(
            f"Simulation results have been saved in the directory: "
            f"{directory}"
        )

    def save_results(self) -> None:
        """
            Saves the final simulation results to the working directory.
        """
        # Auxiliary variables.
        path: Path = Path(self.parameters.output["working"])
        file: Path = path / self.parameters.output["file"]

        # Check the directory exists.
        if not path.is_dir():
            raise ValueError(
                f"Select a valid directory, current directory is not "
                f"valid: {path}"
            )

        # Name of the file.
        with open(f"{file}", encoding="utf-8", mode="w") as stream:
            stream.write(f"{PROGRAM}\n\n")
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
