"""
    File that contains the class where to store the statistics.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# User.
from stochastic.programs.rsa_1d_dimers.simulation.classes.lattice import (
    RSA1DDimersLattice
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables.
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Headers.
HEADER_ATTEMPTS: tuple = ("Attempts", "Successful")
HEADER_COVERAGE: tuple = ("Attempts", "Occupied")
HEADER_EMPTYSTS: tuple = ("Attempts", "Free")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def _get_continuous_empty(lattice: list, number: int, periodic: bool) -> int:
    """
        Gets the number of sites that have N (represented by the "number"
        variable) empty sites. It will consider if the variable is periodic.
        The lattice must only be made of zeros and ones, where zero (0) is
        empty and one (1) is busy.

        :param lattice: The lattice with the particles.

        :param number: The number of consecutive empty sites to check.

        :param periodic: A boolean flag indicating whether the lattice is
         periodic, i.e., site n = n + N, where N is the length of the lattice.
         True, if the lattice is periodic; False otherwise.
    """
    # Auxiliary variables.
    count: int = 0
    length: int = len(lattice)

    # Cannot take these statistics.
    if number >= length:
        raise ValueError(
            "The number of contiguous empty sites cannot be greater than that "
            "of the lattice length."
        )

    # Scan the lattice.
    for site in range(length):
        # Sites to be examined.
        sites: list = [
            (site + i) % length if periodic else (site + i)
            for i in range(number)
        ]

        # Reached the end of the lattice.
        if any(x >= length for x in sites):
            break

        # Check ALL consecutive sites are empty.
        if any(lattice[x] != RSA1DDimersLattice.EMPTY for x in sites):
            count += 1

    return count


def _get_coverage(lattice: list) -> int:
    """
        Gets the number of sites that are not empty. The lattice must only
        be made of zeros and ones, where zero (0) is empty and one (1) is busy.

        :param lattice: The lattice with the particles.

        :return: An integer number that represents the lattice coverage.
    """
    return sum(1 for x in lattice if x != 0)


def _get_lengths(table: list) -> list:
    """
        Gets the maximum width for each column of the given table.

        :param array: The table for which the column widths must be obtained.

        :return: A list of the widths of each table column entry.
    """
    # Auxiliary variables.
    length: int = len(table[0])

    return tuple(max(len(f"{x[i]}") for x in table) for i in range(length))


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


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class RSA1DDimersStatistics:
    """
        Contains the variables to take the statistics of the simulation.

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
    """
    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def update_coverage(self, lattice: list, successful: bool) -> None:
        """
            From the given lattice, updates the coverage. Increases the number
            of attempts by one.

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

        # Alias for function.
        emp: callable = lambda x, y: _get_continuous_empty(x, y, self.periodic)

        # Update the other quantities.
        self.empty_single.append((attempts, emp(lattice, 1)))
        self.empty_double.append((attempts, emp(lattice, 2)))
        self.empty_triple.append((attempts, emp(lattice, 3)))

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
            Builds a new statistics object.

            :param parameters: The simulation parameters that contains all the
             information to record the statistics.
        """
        # Initialize the parameters.
        self.attempts: list = [HEADER_ATTEMPTS, (0, 0)]
        self.coverage: list = [HEADER_COVERAGE, (0, 0)]

        self.empty_single: list = [HEADER_EMPTYSTS, (0, 0)]
        self.empty_double: list = [HEADER_EMPTYSTS, (0, 0)]
        self.empty_triple: list = [HEADER_EMPTYSTS, (0, 0)]

        # Useful parameters.
        self.length: int = parameters["simulation"]["length"]
        self.periodic: bool = parameters["simulation"]["periodic"]
