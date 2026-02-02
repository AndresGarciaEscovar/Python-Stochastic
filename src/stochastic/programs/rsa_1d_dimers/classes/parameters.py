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

        - self.output: A dictionary with the output parameters.

        - self.simulation: A dictionary with the simulation parameters.
    """
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
        indent: str = " " * 4
        string: str = "{\n"
        entries: tuple = (
            ("history", self.history),
            ("output", self.output),
            ("simulation", self.simulation)
        )

        for key, dictionary in entries:
            string = f"{string}{indent}'{key}': " + "{\n"

            for subkey, value in dictionary.items():
                value: Any = f"'{value}'" if isinstance(value, str) else value
                string = f"{string}{indent * 2}'{subkey}': {value},\n"

            string = f"{string}{indent}" + "},\n"

        return f"{string}" + "}"

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

        print(f"{self}")
