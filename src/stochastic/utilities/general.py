"""
    Contains the function for validating the parameters.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import copy as cp

from typing import Any


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Main
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def convert_dict_to_str(dictionary: dict) -> str:
    """
        Recursively prints the dictionary to a string.

        :param dictionary: The dictionary to be converted into a string.

        :return: The dictionary converted into a string.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Auxiliary Functions
    # /////////////////////////////////////////////////////////////////////////

    def to_str_(object_: Any, level_: int = 0) -> str:
        """
            Recursively converts the current dictionary entry to a string.

            :param object_: The object to be turned into a string.

            :param level_: The depth level of the recursion.

            :return: The string with the dictionary.
        """
        # Auxiliary variables.
        indent0_: str = " " * (4 * level_)
        indent1_: str = " " * (4 * (level_ + 1))

        string_: str = "{\n"

        for key_, val_ in object_.items():
            key_ = f"\"{key_}\"" if isinstance(key_, str) else f"{key_}"
            string_ += f"{indent1_}{key_}: "

            if isinstance(val_, dict):
                string_ += to_str_(val_, level_ + 1)
                continue

            val_ = f"\"{val_}\"" if isinstance(val_, str) else f"{val_}"
            string_ += f"{val_},\n"

        character: str = "" if level_ == 0 else ","

        return string_ + f"{indent0_}" + "}" + f"{character}\n"

    # /////////////////////////////////////////////////////////////////////////
    # Implementation
    # /////////////////////////////////////////////////////////////////////////

    return to_str_(dictionary)


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

            :param main_: The dictionary that needs to be updated.

            :param parameters_: The dictionary with which to update the main_
             dictionary.

            :raise KeyError: If the key does not exist in the main dictionary.
        """
        # Scan the items.
        for key_, value_ in parameters_.items():
            # Key must be present!
            if key_ not in main_.keys():
                raise KeyError(f"The key {key_} does not exist in main_.")

            # End of the dictionary.
            if not isinstance(value_, dict):
                main_[key_] = value_
                continue

            # Recursive step.
            recursive_(main_[key_], value_)

    # /////////////////////////////////////////////////////////////////////////
    # Implementation
    # /////////////////////////////////////////////////////////////////////////

    # Dictionary copy.
    results: dict = cp.deepcopy(main)

    # Fix the main dictionary.
    recursive_(results, parameters)

    return results
