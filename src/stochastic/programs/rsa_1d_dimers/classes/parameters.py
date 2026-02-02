"""
    Contains the different classes for storing the parameters.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import copy as cp

# User.
from stochastic.programs.rsa_1d_dimers.validation.parameters import validate


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
    # Constructor
    # /////////////////////////////////////////////////////////////////////////

    def __init__(self, parameters: dict) -> None:
        """
            Initializes the parameters object.
        """
        # Validate the parameters.
        final: dict = validate(parameters)

        # Extract the dictionaries.
        self.history: dict = final["history"]
        self.output: dict = final["output"]
        self.simulation: dict = final["simulation"]
