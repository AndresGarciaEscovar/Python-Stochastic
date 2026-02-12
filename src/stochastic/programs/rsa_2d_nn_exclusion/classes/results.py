"""
    Contains the class that processes the results.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from datetime import datetime

# User.
from stochastic.programs.rsa_2d_nn_exclusion.classes.statistics import (
    Statistics
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Date format
DFORMAT: str = "%Y-%m-%d %H:%M:%S"


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


def _get_string_dictionary(parameters: dict) -> str:
    """
        From the parameters dictionary gets the string representing the
        simulation parameters.

        :param parameters: The dictionary with the simulation parameters.

        :return: A string with the simulation parameters.
    """
    # Auxiliary variables .
    date: str = f"{datetime.now().strftime(DFORMAT)}"
    string: str = f"{_get_header('Parameters')}\n"

    # Extract the key and variables.
    string += "\n".join((
        f"Date (YYYY-MM-DD hh:mm:ss): {date}",
        f"Attempts: {parameters['attempts']}",
        "Dimensions:",
        f"    Length: {parameters['dimensions']['length']}",
        f"    Width: {parameters['dimensions']['width']}",
        "Periodic:",
        f"    Length: {parameters['periodic']['length']}",
        f"    Width: {parameters['periodic']['width']}",
        f"Repetitions: {parameters['repetitions']}",
        f"Seed: {parameters['seed']}",
    ))

    return f"{string}\n\n"


def _get_string_table(table: list) -> str:
    """
        Gets the string for the given table.

        :param array: The table for which the string must be obtained.

        :return: A list of the widths of each table column entry.
    """
    # Auxiliary variables.
    string: str = ""
    tostr: callable = "{:>{width}}".format

    # Set the string.
    if len(table) <= 1:
        # No data to show.
        string += "No data to show.\n"

    else:
        # Table dimensions
        table_length: int = len(table)
        table_width: int = len(table[0])

        # List of widths.
        widths: list = _get_widths(table)

        for i in range(table_width):
            string += " | ".join(
                tostr(table[j][i], width=w)
                for j, w in zip(range(table_length), widths)
            ) + "\n"

    return f"{string}\n"


def _get_widths(table: list) -> tuple:
    """
        Gets the maximum width for each column of the given table.

        :param array: The table for which the column widths must be obtained.

        :return: A list of the widths of each table column entry.
    """
    # Auxiliary variables.
    if len(table) == 0:
        return tuple()

    return tuple(max(len(f"{x}") for x in entry) for entry in table)


def _update_results(target: list, current: list) -> None:
    """
        Updates the target with the current list.

        :param target: The target list to update with the current list.

        :param current: The list with which to update the current list.

        :raise ValueError: If the time stamps in the current list are different
         from those in the target list.
    """
    # Validate the lists have similar number of time stamps.
    if len(target) != len(current):
        raise ValueError(
            f"The target list length is different from the current list "
            f"length; target list length: {len(target)}, current list length: "
            f"{len(current)}."
        )

    # Attempt to merge the statistics.
    for i, (x, y) in enumerate(zip(target, current)):
        # No need to update the header.
        if i == 0:
            continue

        # Time stamps must be the same.
        if x[0] != y[0]:
            raise ValueError(
                f"There are time stamps that do not match; time stamp of "
                f"current: {x[0]}, time stamp of current: {y[0]}."
            )

        # Update the entries for each time stamp.
        target[i][1] += y[1]


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class Results:
    """
        Contains the methods and variables to process the results.

        PARAMETERS:
        ___________

        - self.attempts: The array with the statistics of the number of
          attempts and successful attempts.

        - self.coverage: The array with the total number of particles and the
          inverse elapsed time, i.e., the number of attempts.

        - self.simulations: The number of simulations stored.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def get_dictionary(self) -> dict:
        """
            Returns a dictionary with the COMPLETE parameters of the
            simulation.
        """
        return {
            "simulations": self.simulations,
            "attempts": self.attempts,
            "coverage": self.coverage,
        }

    def statistics_add(self, statistics: Statistics) -> None:
        """
            Adds more statistics to the results before they are processed. For
            this method to process, the statistics arrays must contain the same
            time stamps.

            :param statistics: A Statistics object that contains the
             statistiscs of a SINGLE run.
        """
        # Extract the statistics.
        if self.simulations == 0:
            # Initialize the statistics.
            self.attempts = [list(x) for x in statistics.attempts]
            self.coverage = [list(x) for x in statistics.coverage]

        else:
            # Update the statistics.
            _update_results(self.attempts, statistics.attempts)
            _update_results(self.coverage, statistics.coverage)

        # Upgrade the number of simulation.
        self.simulations += 1

    def statistics_process(self) -> None:
        """
            Processes the statistics to give the final results.
        """
        # Auxiliary variables.
        header_0: str = "Time Elapsed"
        pore_length: int = self.parameters["dimensions"]["length"]
        pore_width: int = self.parameters["dimensions"]["width"]

        length_stat: int = len(self.attempts)
        total_sites: int = pore_length * pore_width
        denominator: int = self.simulations * total_sites

        # For each quantity.
        for i in range(length_stat):
            # Fix the elapsed time.
            if i == 0:
                self.attempts[i][0] = header_0
                self.coverage[i][0] = header_0

                self.attempts[i][1] += " / Attempts"
                self.coverage[i][1] += " / (Length * Width)"

                continue

            # Average the simulations.
            number: int = self.attempts[i][0] * self.simulations

            self.attempts[i][1] /= number if number != 0 else 1
            self.coverage[i][1] /= denominator

            # Turn attempts into elapsed time.
            self.attempts[i][0] /= total_sites
            self.coverage[i][0] /= total_sites

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Dunder
    # /////////////////////////////////////////////////////////////////////////

    def __str__(self) -> str:
        """
            The string representation of the class at the time it is invoked.

            :return: The string with the class representation.
        """
        # Parameters.
        string: str = _get_string_dictionary(self.parameters)

        # Append the strings.
        string += f"{_get_header('Attempts')}\n"
        string += _get_string_table(self.attempts)

        string += f"{_get_header('Coverage')}\n"
        string += _get_string_table(self.coverage)

        return f"{string.strip()}\n"

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(self, parameters: dict) -> None:
        """
            Constructor for the object.

            :param parameters: The simulation parameters that contains all the
             information to record the results of a simulation.
        """
        # Simulation information.
        self.parameters: dict = parameters

        # Initialize the parameters.
        self.simulations: int = 0
        self.attempts: list = []
        self.coverage: list = []
