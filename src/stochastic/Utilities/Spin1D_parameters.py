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
class Spin1DParameters:
    """ A data class where the parameters of the system are defined."""

    # Lattice save file path.
    lattice_file: str = "spin_lattice.txt"

    # Defines the length of the lattice.
    length: int = 1

    # File name to save the lattice.
    results_file: str = "results.txt"   

    # Define the seed with which the generator must be seeded (i.e., the system time by default).
    seed: int = int(time.time())

    # Define the maximum number of attempts.
    maximum_attempts: int = length * 5

    # Flags if the lattice is periodic.
    periodic: bool = False

    # Defines the tolerance, i.e., how close two numbers must be, to be equal.
    tolerance: float = 1.0*10**(-5)
