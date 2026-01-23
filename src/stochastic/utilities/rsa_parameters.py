"""
    File that contains the RSAParameters class.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports.
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import time

from dataclasses import dataclass


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes.
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


@dataclass
class RSA1DParameters:
    """
        A data class where the parameters of the system are defined.
    """

    # Lattice save file path.
    lattice_file: str = "lattice.txt"

    # Defines the length of the lattice.
    length: int = 1

    # File name to save the lattice.
    results_file: str = "results.txt"

    # The seed with which the generator is seeded (i.e., the system time).
    seed: int = int(time.time())

    # Define the maximum simulation time.
    maximum_time: float = 0.1

    # Flags if the lattice is periodic.
    periodic: bool = False

    # Define the number of times the simulation must be executed.
    repetitions: int = 1000

    # Defines the tolerance, i.e., how close two numbers must be, to be equal.
    tolerance: float = 1.0*10**(-5)


@dataclass
class RSA2DParameters:
    """
        A data class where the parameters of the system are defined.
    """

    # Defines the dimensions of the lattice.
    dimensions: int = (1, 1)

    # Lattice save file path.
    lattice_file: str = "lattice.txt"

    # File name to save the lattice.
    results_file: str = "results.txt"

    # The seed with which the generator is seeded (i.e., the system time).
    seed: int = int(time.time())

    # Define the maximum simulation time.
    maximum_time: float = 0.1

    # Flags if the lattice is periodic.
    periodic: tuple[bool, bool] = (False, False)

    # Define the number of times the simulation must be executed.
    repetitions: int = 1000

    # Defines the tolerance, i.e., how close two numbers must be, to be equal.
    tolerance: float = 1.0*10**(-5)
