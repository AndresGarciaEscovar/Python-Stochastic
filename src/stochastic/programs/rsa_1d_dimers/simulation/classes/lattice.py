"""
    File that contains the class where to store the lattice.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import copy as cp


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class RSA1DDimersLattice:
    """
        Contains the variables to store the lattice of the simulation.

        PARAMETERS:
        ___________

        - self.lattice: The array that contains the particles.

        - self.length: The length of the lattice.

        - self.periodic: A boolean flag indicating whether the lattice is
          periodic. True, if the lattice is periodic; False, otherwise.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    # Possible site states.
    EMPTY: int = 0
    OCCUPIED: int = 1

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def get_lattice_string(self, partial: bool = False) -> str:
        """
            The string representation of the lattice at the given time. The
            partial representation of the lattice is the state of the lattice
            without the site numbering.

            :param partial: A boolean flag indicating whether the lattice
             string to be returned is the full representation of the lattice,
             or the partial representation of the lattice. True, if the partial
             representation of the lattice is requested; False, if the full
             representation of the lattice is requested. False, by default.

            :return: The string representation of the lattice.
        """
        # Auxiliary variables.
        string: str = ""
        ents: tuple = tuple(f"{part}" for part in self.lattice)
        sites: tuple = tuple(f"{site}" for site in range(self.length))
        widths: tuple = tuple(max(len(x), len(y)) for x, y in zip(ents, sites))

        # Determine if partial full lattice needs to be returned.
        if not partial:
            for i, (site, length) in enumerate(zip(sites, widths)):
                char: str = " | " if i > 0 else ""
                string += f"{char}{site:>{length}}"

            string += "\n"

        # Get the particles in the site.
        for i, (ent, length) in enumerate(zip(ents, widths)):
            char: str = " | " if i > 0 else ""
            string += f"{char}{ent:>{length}}"

        return string + "\n"

    def particle_adsorb(self, sites: list) -> bool:
        """
            Attempts to adsorb the particles at the given sites.

            :param sites: A list of sites where to adsorb the particles.

            :return: A boolean flag that indicates whether ALL the particles
             were adsorbed, i.e., the requested sites are within the lattice
             and empty.
        """
        # All sites must be valid.
        if any(x < 0 for x in sites):
            raise ValueError(
                "One the sites for a particle to adsorb is a negative number;"
                "the site must be inside the lattice."
            )

        # Auxliary variables.
        occupied: int = RSA1DDimersLattice.OCCUPIED

        # Check the sites.
        fsites: list = cp.deepcopy(sites)

        if self.periodic:
            fsites = [x % self.length for x in fsites]

        flag: bool = all(
            x < self.length and self.lattice[x] != occupied
            for x in fsites
        )

        # Update the particles in the sites.
        if flag:
            for site in sites:
                self.lattice[site] = occupied

        return flag

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Dunder
    # /////////////////////////////////////////////////////////////////////////

    def __str__(self) -> str:
        """
            The string representation of the lattice class with the current
            state at the time it is invoked.

            :return: The string with the class representation.
        """

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
        # Auxiliary variables.
        empty: int = RSA1DDimersLattice.EMPTY

        # Initialize the parameters.
        self.length: int = parameters["simulation"]["length"]
        self.periodic: bool = parameters["simulation"]["periodic"]

        # Update the lattice.
        self.lattice: list = [empty for _ in range(self.length)]
