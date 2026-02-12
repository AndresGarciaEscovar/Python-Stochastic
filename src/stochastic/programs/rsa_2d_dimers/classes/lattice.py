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

        - self.lattice: The 2D array that contains the particles with "length"
          rows of "width" number of entries.

        - self.dimensions: A dictionary with the "length" and the "width" of
          the 2D lattice.

        - self.periodic: A dictionary with the periodicity of the "length" and
          the "width" of the 2D lattice.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Class Variables
    # /////////////////////////////////////////////////////////////////////////

    # Possible site states.
    EMPTY: int = 0
    OCCUPIED: int = 1

    # Adsorption directions.
    DIRECTIONS: tuple =  "up", "down", "left", "right"

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Auxiliary
    # /////////////////////////////////////////////////////////////////////////

    def _get_site(self, site: list, direction: str) -> list:
        """
            Gets the site where the particle will be attempted to be adsorbed.

            :param site: The current adsorption site.

            :param direction: The direction where the particles are meant to be
             adsorbed.

            :return: A list with the place where a particle is meant to be
             adsorbed.
        """
        # Check the direction is valid.
        if direction not in Lattice.DIRECTIONS:
            raise ValueError(
                f"The direction value must take only one of these values: "
                f"{Lattice.DIRECTIONS}; current value: \"{direction}\"."
            )

        # Auxiliary variables.
        length: int = self.dimensions["length"]
        width: int = self.dimensions["width"]

        # Determine the direction.
        if direction in Lattice.DIRECTIONS[:2]:
            # Flip the site up or down.
            site[0] += 1 if direction == "up" else -1

            if self.periodic["length"]:
                site[0] = length - 1 if site[0] < 0 else site[0] % length

        else:
            # Flip the left or right.
            site[1] += 1 if direction == "right" else -1

            if self.periodic["width"]:
                site[1] = width - 1 if site[1] < 0 else site[1] % width

        return site

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

    def particle_adsorb(
        self,
        site_length: list,
        site_width: list,
        direction: str
    ) -> bool:
        """
            Attempts to adsorb the particles at the given sites.

            :param site_length: The site along the length of the lattice where
             the adsorption is inteded to take place.

            :param site_width: The site along the width of the lattice where
             the adsorption is inteded to take place.

            :param direction: A string with the direction in wich the
             adsorption will take place. Must be "up", "down", "left", or
             "right".

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
                f"(0 <= site_length < {length}); {site_length = }."
            )

        if not 0 <= site_width < width:
            raise ValueError(
                f"The column adsorption site for a particle to adsorb is not "
                f"in the proper range; the site must be inside the lattice "
                f"(0 <= site_width < {width}); {site_width = }."
            )

        # Neighboring sites.
        sites: list = [
            [site_length, site_width],
            self._get_site([site_length, site_width], direction)
        ]

        # Check all the sites.
        for site in sites:
            flag = flag and (0 <= site[0] < length or 0 <= site[1] < width)
            flag = flag and self.lattice[site[0]][site[1]] == Lattice.EMPTY

            if not flag:
                break

        else:
            # Set the sites to occupied.
            for site in sites:
                self.lattice[site[0]][site[1]] = Lattice.OCCUPIED

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
