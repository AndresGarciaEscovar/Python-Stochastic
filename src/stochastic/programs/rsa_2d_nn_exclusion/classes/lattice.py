"""
    File that contains the class where to store the lattice.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class Lattice:
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

    def get_dictionary(self) -> dict:
        """
            Returns a dictionary with the COMPLETE parameters of the
            simulation.
        """
        return {
            "dimensions": self.dimensions,
            "lattice": self.lattice,
            "periodic": self.periodic,
        }

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
        array: list = [
            [
                "row\\column",
                *[f"{i}" for i in range(self.dimensions['width'])]
            ],
            *[
                [f"{i}", *[f"{x}" for x in row]]
                for i, row in enumerate(self.lattice)
            ]
        ]
        string: str = ""

        # Remove the entries, if neeeded.
        if partial:
            del array[0]

            for i, _ in enumerate(array):
                del array[i][0]

        # Get the column widths.
        widths: list = [len(x) for x in array[0]]

        for entry in array:
            widths = [max(x, len(y)) for x, y in zip(widths, entry)]

        # Update the string.
        for i, row in enumerate(array):
            string += " | ".join(
                f"{entry:^{width}}" for entry, width in zip(row, widths)
            ) + "\n"

            if i < len(array) - 1:
                string += "---".join(
                    f"{'-' * width:^{width}}"
                    for entry, width in zip(row, widths)
                ) + "\n"

        return string + "\n\n"

    def particle_adsorb(self, site_length: list, site_width: list) -> bool:
        """
            Attempts to adsorb the particles at the given sites.

            :param site: The site where the adsorption is inteded to take
             place.

            :return: A boolean flag that indicates whether ALL the particles
             were adsorbed, i.e., the requested sites are within the lattice
             and empty.
        """
        # Auxiliary variables.
        flag: bool = True
        length: int = self.dimensions["length"]
        width: int = self.dimensions["width"]

        # All sites must be valid.
        if not 0 <= site_length < length:
            raise ValueError(
                f"The row adsorption site for a particle to adsorb is not in "
                f"the proper range; the site must be inside the lattice "
                f"(0 <= site < {length}); {site_length = }."
            )

        if not 0 <= site_width < width:
            raise ValueError(
                f"The column adsorption site for a particle to adsorb is not "
                f"in the proper range; the site must be inside the lattice "
                f"(0 <= site < {width}); {site_width = }."
            )

        # Neighboring sites.
        sites: list = [
            [site_length, site_width],
            [site_length - 1, site_width],
            [site_length + 1, site_width],
            [site_length, site_width - 1],
            [site_length, site_width + 1]
        ]

        # Fix the sites.
        if self.periodic["length"]:
            sites[1][0] = length - 1 if sites[1][0] < 0 else sites[1][0]
            sites[2][0] = sites[2][0] % length

        if self.periodic["width"]:
            sites[3][1] = width - 1 if sites[3][1] < 0 else sites[3][1]
            sites[4][1] = sites[4][1] % width

        # Check all the sites.
        occupied: int = Lattice.OCCUPIED

        for site in sites:
            if site[0] not in range(length) or site[1] not in range(width):
                continue

            flag = flag and self.lattice[site[0]][site[1]] != occupied

        return flag

    def reset(self) -> None:
        """
            Resets the lattice to an empty lattice.
        """
        # Reset to an empty lattice.
        for i in range(self.dimensions["length"]):
            for j in range(self.dimensions["width"]):
                self.lattice[i][j] = Lattice.EMPTY

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Dunder
    # /////////////////////////////////////////////////////////////////////////

    def __str__(self) -> str:
        """
            The string representation of the lattice class with the current
            state at the time it is invoked.

            :return: The string with the class representation.
        """
        # Parameters.
        string: str = "\n    ".join([
            "Parameters:",
            "dimensions:",
            f"    length: {self.dimensions['length']}",
            f"     width: {self.dimensions['width']}",
            "periodic:",
            f"    length: {self.periodic['length']}",
            f"     width: {self.periodic['width']}"
        ]) + "\n\n"

        return f"{string}Lattice:\n\n{self.get_lattice_string(partial=False)}"

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(self, parameters: dict) -> None:
        """
            Constructor for the object.

            :param parameters: The simulation parameters that contains all the
             information to create the lattice, and perform the lattice
             operations.
        """
        # Initialize the parameters.
        self.dimensions: int = parameters["dimensions"]
        self.periodic: bool = parameters["periodic"]

        # Update the lattice.
        self.lattice: list = [
            [Lattice.EMPTY for _ in range(self.dimensions["width"])]
            for _ in range(self.dimensions["length"])
        ]
