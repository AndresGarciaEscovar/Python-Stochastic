"""
    Contains the class that processes the results.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from datetime import datetime

# User.
from stochastic.programs.rsa_1d_dimers.simulation.classes.statistics import (
    RSA1DDimersStatistics
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Date format
DFORMAT: str = "%Y-%m-%d %H:%M:%S"


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _get_lengths(table: list) -> tuple:
    """
        Gets the maximum width for each column of the given table.

        :param array: The table for which the column widths must be obtained.

        :return: A list of the widths of each table column entry.
    """
    # Auxiliary variables.
    if len(table) == 0:
        return tuple()

    # Get the length.
    length: int = len(table[0])

    return tuple(max(len(f"{x[i]}") for x in table) for i in range(length))


def _get_string_dictionary(parameters: dict) -> str:
    """
        From the parameters dictionary gets the string representing the
        simulation parameters.

        :param parameters: The dictionary with the simulation parameters.

        :return: A string with the simulation parameters.
    """
    # Auxiliary variables.
    date: str = f"{datetime.now().strftime(DFORMAT)}"

    string: str = "Parameters:\n"
    string += f"    date (YYYY-MM-DD hh:mm:ss): {date}\n"

    # Extract the key and variables.
    for key, value in parameters.items():
        string += f"    {key}: {value}\n"

    return f"{string}\n"


def _get_string_table(table: list) -> str:
    """
        Gets the string for the given table.

        :param array: The table for which the string must be obtained.

        :return: A list of the widths of each table column entry.
    """
    # Auxiliary variables.
    lengths: list = _get_lengths(table)
    string: str = ""
    temp: callable = "{:>{length}}".format

    # Get each row.
    for i, entries in enumerate(table):
        # For each entry.
        string += " | ".join(
            temp(x, length=lengths[i]) for i, x in enumerate(entries)
        ) + "\n"

        # Header separator.
        if i == 0:
            string = f"{string}{' | '.join('-' * x for x in lengths)}\n"

    return f"{string}\n\n"


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


class RSA1DDimersResults:
    """
        Contains the methods and variables to process the results.

        PARAMETERS:
        ___________

        - self.attempts: The array with the statistics of the number of
          attempts and successful attempts.

        - self.coverage: The array with the total number of particles and the
          inverse elapsed time, i.e., the number of attempts.

        - self.empty_double: The number of sites that have an empty neighbor
          to the left.

        - self.empty_single: The number of sites that are empty.

        - self.empty_triple: The number of sites that have two empty neighbors
          to the left.

        - self.length: The length of the 1D lattice, a number  greater than
          zero.

        - self.periodic: A boolean flag indicating whether the lattice is
          periodic. True, if the lattice is periodic; False, otherwise.

        - self.simulations: The number of simulations stored.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def statistics_add(self, statistics: RSA1DDimersStatistics) -> None:
        """
            Adds more statistics to the results before they are processed. For
            this method to process, the statistics arrays must contain the same
            time stamps.

            :param statistics: A RSA1DDimersStatistics object that contains the
             statistiscs of a SINGLE run.
        """
        # Extract the statistics.
        if self.simulations == 0:
            # Initialize the statistics.
            self.attempts = [list(x) for x in statistics.attempts]
            self.coverage = [list(x) for x in statistics.coverage]

            self.empty_single = [list(x) for x in statistics.empty_single]
            self.empty_double = [list(x) for x in statistics.empty_double]
            self.empty_triple = [list(x) for x in statistics.empty_triple]

        else:
            # Update the statistics.
            _update_results(self.attempts, statistics.attempts)
            _update_results(self.coverage, statistics.coverage)

            _update_results(self.empty_single, statistics.empty_single)
            _update_results(self.empty_double, statistics.empty_double)
            _update_results(self.empty_triple, statistics.empty_triple)

        # Upgrade the number of simulation.
        self.simulations += 1

    def statistics_process(self) -> None:
        """
            Processes the statistics to give the final results.
        """
        # Auxiliary variables.
        header_0: str = "Time Elapsed"
        length_pore: int = self.information["simulation"]["length"]
        length_stat: int = len(self.attempts)
        denominator: int = self.simulations * length_pore

        # For each quantity.
        for i in range(length_stat):
            # Fix the elapsed time.
            if i == 0:
                self.attempts[i][0] = header_0
                self.coverage[i][0] = header_0

                self.empty_single[i][0] = header_0
                self.empty_double[i][0] = header_0
                self.empty_triple[i][0] = header_0

                continue

            # Average the simulations.
            number: int = self.attempts[i][0] * self.simulations

            self.attempts[i][1] /= number if number != 0 else 1
            self.coverage[i][1] /= denominator

            self.empty_single[i][1] /= denominator
            self.empty_double[i][1] /= denominator
            self.empty_triple[i][1] /= denominator

            # Turn attempts into elapsed time.
            self.attempts[i][0] /= length_pore
            self.coverage[i][0] /= length_pore

            self.empty_single[i][0] /= length_pore
            self.empty_double[i][0] /= length_pore
            self.empty_triple[i][0] /= length_pore

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Dunder
    # /////////////////////////////////////////////////////////////////////////

    def __str__(self) -> str:
        """
            The string representation of the class at the time it is invoked.

            :return: The string with the class representation.
        """
        # Parameters.
        string: str = _get_string_dictionary(self.information["simulation"])

        # Append the strings.
        string += "Attempts:\n\n"
        string += _get_string_table(self.attempts)

        string += "Coverage:\n\n"
        string += _get_string_table(self.coverage)

        string += "Empties - Single:\n\n"
        string += _get_string_table(self.empty_single)

        string += "Empties - Double:\n\n"
        string += _get_string_table(self.empty_double)

        string += "Empties - Triple:\n\n"
        string += _get_string_table(self.empty_triple)

        return string.strip()

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(self, parameters: dict) -> None:
        """
            Constructor for the object.

            :param parameters: The simulation parameters that contains all the
             information to record the statistics.
        """
        # Initialize the parameters.
        self.simulations: int = 0
        self.attempts: list = []
        self.coverage: list = []

        self.empty_single: list = []
        self.empty_double: list = []
        self.empty_triple: list = []

        # Simulation information.
        self.information: dict = parameters
