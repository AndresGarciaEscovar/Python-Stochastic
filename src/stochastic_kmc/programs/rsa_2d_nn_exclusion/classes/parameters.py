"""
    Contains the different classes for storing the parameters.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# User.
from stochastic_kmc.programs.rsa_2d_nn_exclusion.validation.parameters import (
    validate
)
from stochastic_kmc.utilities.general import convert_dict_to_str


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class Parameters:
    """
        Class that contains the parameters of the simulation.

        PARAMETERS:
        ___________

        - self.history: A dictionary with the history parameters.

        - self.output: A dictionary with the output parameters.

        - self.simulation: A dictionary with the simulation parameters.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Methods
    # /////////////////////////////////////////////////////////////////////////

    def get_dictionary(self):
        """
            Returns a dictionary with the COMPLETE parameters of the
            simulation.
        """
        return {
            "history": self.history,
            "history_lattice": self.history_lattice,
            "output": self.output,
            "simulation": self.simulation,
        }

    # /////////////////////////////////////////////////////////////////////////
    # Methods - Dunder
    # /////////////////////////////////////////////////////////////////////////

    def __repr__(self) -> str:
        """
            Prints the current dictionary parameters in a reproducible way.
        """
        return f"{self.get_dictionary()}"

    def __str__(self) -> str:
        """
            Prints the current dictionary parameters in a friendly format.
        """
        return convert_dict_to_str(self.get_dictionary())

    # /////////////////////////////////////////////////////////////////////////
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(self, parameters: dict) -> None:
        """
            Constructor for the object.

            :param parameters: The simulation parameters that contains all the
             information needed for the simulation.
        """
        # Validate the parameters.
        final: dict = validate(parameters)

        # Extract the dictionaries.
        self.history: dict = final["history"]
        self.history_lattice: dict = final["history_lattice"]
        self.output: dict = final["output"]
        self.simulation: dict = final["simulation"]

        # Current iteration and repetition.
        self.current_attempts: int = 0
        self.current_repetition: int = 0
