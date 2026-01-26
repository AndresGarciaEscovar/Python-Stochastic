"""
    Contains the function for validating the parameters.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from typing import Any


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Main
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def format_dictionary(main: dict, parameters: dict) -> dict:
    """
        From the parameters dictionary, extracts the quantities into the
        main dictionary.

        :param main: The dictionary into which the parameters dictionary will
         be merged.

        :param parameters: The dictionary of parameters; with the pre condition
         that it has already been checked.

        :return: The main dictionary with the new parameters.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Auxiliary Functions
    # /////////////////////////////////////////////////////////////////////////

    def recursive_(main_: Any, parameters_: Any) -> None:
        """
            Recursively sets the keys of the main dictionary.
        """
        # Scan the items.
        for key_, value_ in parameters_.items():
            # End of the dictionary.
            if not isinstance(value_, dict):
                main_[key_] = value_
                continue

            # Recursive step.
            recursive_(main_[key_], value_)

    # /////////////////////////////////////////////////////////////////////////
    # Implementation
    # /////////////////////////////////////////////////////////////////////////

    # Fix the main dictionary.
    recursive_(main, parameters)

    return main
