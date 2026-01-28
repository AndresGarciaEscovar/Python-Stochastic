"""
    File that contains the class where to store the lattice.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class RSA1DDimersLattice:
    """
        Contains the variables to store the lattice of the simulation.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    # Possible site states.
    EMPTY: int = 0
    OCCUPIED: int = 1

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(self, parameters: dict) -> None:
        """
            Builds a new statistics object.

            :param parameters: The simulation parameters that contains all the
             information to create the lattice, and perform the lattice
             operations.
        """