"""
    Contains the class for saving the lattice history.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from pathlib import Path
from typing import Union

# User.
from stochastic.programs.rsa_1d_dimers.classes.lattice import Lattice
from stochastic.programs.rsa_1d_dimers.classes.parameters import Parameters
from stochastic.programs.rsa_1d_dimers.classes.results import Results
from stochastic.programs.rsa_1d_dimers.classes.statistics import Statistics


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class History:
    """
        Contains the methods and variables to save and keep the history of a
        simulation.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Methods - Private
    # /////////////////////////////////////////////////////////////////////////

    def _set_path(self) -> None:
        """
            Sets the path of the file where the simulation is to be saved.
        """
        # Set up only if needed.
        if self.parameters.history["save"]:
            # Working directory.
            working: Path = Path(self.parameters.output["working"])
            working.mkdir(exist_ok=True, parents=False)

            # Create the file.

    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(
        self,
        parameters: Parameters,
        lattice: Lattice,
        results: Results,
        statistics: Union[None, Statistics],
    ) -> None:
        """
            Constructor for the object.

            :param parameters: The simulation history parameters that contains
             all the information needed to save the lattice to the correct
             place.

            :param lattice: A lattice object that represents the current state
             of the lattice.

            :param results: A reference to the results object.

            :param statistics: A reference to the current statistics object, it
             can be None.
        """
        # Set the parameters.
        self.lattice: Lattice = lattice
        self.parameters: Parameters = parameters
        self.results: Results = results
        self.statistics: Statistics = statistics

        # Finish setting the object.
        self._set_path()
