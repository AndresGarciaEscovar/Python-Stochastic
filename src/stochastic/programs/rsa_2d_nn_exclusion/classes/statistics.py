"""
    File that contains the class where to store the statistics.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# User.
from stochastic.programs.rsa_2d_nn_exclusion.classes.lattice import Lattice


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables.
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Headers.
HEADER_ATTEMPTS: tuple = ("Attempts", "Successful")
HEADER_COVERAGE: tuple = ("Attempts", "Occupied")
HEADER_EMPTYSTS: tuple = ("Attempts", "Free")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _get_coverage(lattice: list) -> int:
    """
        Gets the number of sites that are not empty. The lattice must only
        be made of zeros and ones, where zero (0) is empty and one (1) is
        occupied.

        :param lattice: The lattice with the particles.

        :return: An integer number that represents the lattice coverage.
    """
    # Auxiliary variables.
    coverage: int = 0

    for row in lattice:
        coverage += sum(1 for x in row if x != Lattice.EMPTY)

    return coverage


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
        string += "No data to show."

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


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class Statistics:
    """
        Contains the variables to take the statistics of the simulation.

        PARAMETERS:
        ___________

        - self.attempts: The array with the statistics of the number of
          attempts and successful attempts.

        - self.coverage: The array with the total number of particles and the
          inverse elapsed time, i.e., the number of attempts.

        - self.length: The length of the 1D lattice, a number  greater than
          zero.

        - self.periodic: A boolean flag indicating whether the lattice is
          periodic. True, if the lattice is periodic; False, otherwise.
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
            "attempts": self.attempts,
            "coverage": self.coverage,
            "length": self.length,
            "periodic": self.periodic
        }

    def reset(self) -> None:
        """
            Resets ALL the statistics to their original value.
        """
        # Reset the parameters.
        self.attempts = [HEADER_ATTEMPTS, (0, 0)]
        self.coverage = [HEADER_COVERAGE, (0, 0)]

    def update_statistics(self, lattice: list, successful: bool) -> None:
        """
            From the given lattice, updates the statistics, i.e., increases the
            number of attempts by one and the corresponding quantities.

            :param lattice: The lattice with the particles.

            :param successful: A boolean flag indicating whether the adsorption
             attempt was successful. True, if the attempt was successful in
             adsorbing a particle; False, otherwise.
        """
        # Update the coverage.
        attempts: int = self.coverage[-1][0] + 1
        self.coverage.append((attempts, _get_coverage(lattice)))

        # Update the number of successful attempts.
        nsuccessful: int = self.attempts[-1][1] + (1 if successful else 0)
        self.attempts.append((attempts, nsuccessful))

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Dunder
    # /////////////////////////////////////////////////////////////////////////

    def __str__(self) -> str:
        """
            The string representation of the class at the time it is invoked.

            :return: The string with the class representation.
        """
        # Parameters.
        string: str = "\n    ".join([
            "Parameters:",
            f"length: {self.length}",
            f"periodic: {self.periodic}"
        ]) + "\n\n"

        # Append the strings.
        string += "Attempts:\n\n"
        string += _get_string_table(self.attempts)

        string += "Coverage:\n\n"
        string += _get_string_table(self.coverage)

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
        self.attempts: list = [HEADER_ATTEMPTS, (0, 0)]
        self.coverage: list = [HEADER_COVERAGE, (0, 0)]

        # Useful parameters.
        self.length: int = parameters["length"]
        self.periodic: bool = parameters["periodic"]
