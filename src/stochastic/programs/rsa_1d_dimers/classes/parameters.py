"""
    Contains the different classes for storing the parameters.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from typing import Any

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

        - self.loaded: A boolean flag indicating whether the simulation was
          loaded or it has not been loaded. True, if the simulation has been
          loaded from an external file; False, otherwise. Set initially to
          False.

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
        # Auxiliary variables.
        parameters: dict = {
            "history": self.history,
            "output": self.output,
            "simulation": self.simulation
        }

        return f"{parameters}"

    def __str__(self) -> str:
        """
            Prints the current dictionary parameters in a friendly format.
        """
        # Auxiliary variables.
        indent: str = " " * 4
        string: str = "{\n"
        entries: tuple = (
            ("history", self.history),
            ("output", self.output),
            ("simulation", self.simulation)
        )

        # Print every dictionary.
        for key, dictionary in entries:
            string = f"{string}{indent}'{key}': " + "{\n"

            for subkey, value in dictionary.items():
                value: Any = f"'{value}'" if isinstance(value, str) else value
                string = f"{string}{indent * 2}'{subkey}': {value},\n"

            # More strings.
            string = f"{string}{indent}" + "},\n"

        return f"{string}" + "}"

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
        self.output: dict = final["output"]
        self.simulation: dict = final["simulation"]

        # Current iteration and repetition.
        self.current_attempts: int = 0
        self.current_repetition: int = 0
