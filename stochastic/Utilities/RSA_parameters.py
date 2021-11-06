""" File that contains the RSAParameters class."""

# ------------------------------------------------------------------------------
# Imports.
# ------------------------------------------------------------------------------

# Imports: General.
import time

from dataclasses import dataclass

# ------------------------------------------------------------------------------
# Classes.
# ------------------------------------------------------------------------------


@dataclass
class RSAParameters:
    """ A data class where the parameters of the system are defined."""

    # Lattice save file path.
    lattice_file: str = "lattice.txt"

    # Defines the length of the lattice.
    length: int = 1

    # Define the seed with which the generator must be seeded (i.e., the system time by default).
    seed: int = int(time.time())

    # Define the maximum simulation time.
    maximum_time: float = 0.1

    # Flags if the lattice is periodic.
    periodic: bool = False

    # Define the number of times the simulation must be executed.
    repetitions: int = 1000

    # Defines the tolerance, i.e., how close two numbers must be, to be equal.
    tolerance = 1.0*10**(-5)
