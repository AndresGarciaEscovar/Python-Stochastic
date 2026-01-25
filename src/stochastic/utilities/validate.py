"""
    Several validation functions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from typing import Any


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def validate_subdictionary(
    base: dict,
    dictionary: dict,
    error: bool = False
) -> bool:
    """
        Validates that the given dictionary is a sub dictionary of the base
        dictionary.

        :param base: The base dictionary with which to compare the other
         dictionary.

        :param dictionary: The dictionary to be validated.

        :param error: A boolean flag indicating whether an error must be thrown
         if validation fails. True, if an error must be thrown if validation
         fails; False, otherwise.

        :raise TypeError: If the base object is not a dictionary.

        :raise ValueError: If the dictionary to be validated contains an
         invalid entry.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Auxiliary Variables
    # /////////////////////////////////////////////////////////////////////////

    def recursive_(base_: dict, current_: dict, path_: str) -> None:
        """
            Recursively checks if the current dictionary is a sub dictionary of
            the base dictionary; including the types.
        """
        # Local variables.
        nonlocal message

        # Check the types.
        flag0_: bool = isinstance(base_, dict)
        flag1_: bool = isinstance(current_, type(base_))

        # Check the types match.
        if not flag1_:
            message += (
                f"The \"{path_}\" variable is not of the expected type; "
                f"current: {type(current_)}, expected: {type(base_)}. "
            )

        # No need to continue.
        if not flag0_ or (flag0_ and not flag1_):
            return

        # The keys of the current dictionary are a subset of the base ones.
        keys_base_: set = set(base_.keys())
        keys_current_: set = set(current_.keys())
        excess: set = keys_current_ - keys_base_

        if keys_current_ == set() or excess != set():
            message += (
                f"The keys of the \"{path_}\" dictionary are not a subset of "
                f"the expected keys, or is empty. Expected: {keys_base_}, "
                f"current: {keys_current_ or '{}'}, excess: {excess or '{}'}."
            )

            return

        # Recursive step.
        for key_, value_ in current_.items():
            tkey_: Any = f"\"{key_}\"" if isinstance(key_, str) else key_
            recursive_(base_[key_], value_, f"{path_}.{tkey_}")

    # /////////////////////////////////////////////////////////////////////////
    # Implementation
    # /////////////////////////////////////////////////////////////////////////

    # Auxiliary variables.
    flag: bool = isinstance(base, dict)
    message: str = ""

    # Check the correct type is being checked.
    if not flag or base == {}:
        raise TypeError(
            f"The \"base\" object must be a non-empty dictionary; current "
            f"type \"{type(base).__name__}\"{' is empty' if flag else ''}."
        )

    # Check recursively.
    recursive_(base, dictionary, "\"base\"")

    # Validate if errors were found.
    flag = flag and message == ""

    if error and not flag:
        raise ValueError(message.strip())

    return flag


if __name__ == "__main__":
    dict0__ = 2

    dict1__ = {
        "more": {
        },
        "less": {
            "be friends": "op"
        }
    }

    print(validate_subdictionary(dict0__, dict1__,  True))
