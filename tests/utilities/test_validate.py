"""
    Contains the unit tests for the general validation functions.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import copy as cp
import unittest

# User.
from stochastic.utilities.validate import (
    validate_dictionary,
    validate_dictionary_sub
)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Dictionary to compare.
DICTIONARY: dict = {
    "one": {
        "two": 2,
        "three": "3",
    },
    4: {
        "five": 5,
        "six": 6.0
    }
}


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Classes
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


class TestUtilitiesValidate(unittest.TestCase):
    """
        Contains the tests for the utilities.

        Methods:
        ________

        - test_validate_dictionary.
        - test_validate_dictionary_sub
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_validate_dictionary(self) -> None:
        """
            Tests that equal dictionaries validate to True and dictionaries
            that are different evaluate to False, or throw an error.
        """
        # Auxiliary variables.
        expected: dict = cp.deepcopy(DICTIONARY)
        current: dict = cp.deepcopy(DICTIONARY)

        # ---------------------------------------------------------------------
        # Dictionaries have the same structure.
        # ---------------------------------------------------------------------

        current["one"]["two"] = 3
        current["one"]["three"] = "2"
        current[4]["five"] = 6
        current[4]["six"] = 5.0

        # The dictionaries should be the same.
        self.assertTrue(
            validate_dictionary(expected, current),
            "The dictionaries do not match in structure."
        )

        # ---------------------------------------------------------------------
        # Dictionaries have the same structure but different types.
        # ---------------------------------------------------------------------

        current["one"]["two"] = "3"

         # The dictionaries should NOT be the same.
        self.assertFalse(
            validate_dictionary(expected, current),
            "The dictionaries match in structure."
        )

        with self.assertRaises(
            ValueError,
            msg="False validation must raise an error"
        ):
            validate_dictionary(expected, current, error=True)

        # ---------------------------------------------------------------------
        # Dictionaries don't have the same structure.
        # ---------------------------------------------------------------------

        del current["one"]

         # The dictionaries should NOT be the same.
        self.assertFalse(
            validate_dictionary(expected, current),
            "The dictionaries match in structure."
        )

        with self.assertRaises(
            ValueError,
            msg="False validation must raise an error"
        ):
            validate_dictionary(expected, current, error=True)

    def test_validate_dictionary_sub(self) -> None:
        """
            Tests that if a dictionary is a sub dictionary of another
            dictionary it evaluates to True, otherwise it evaluates to False or
            throws an error.
        """
        # Auxiliary variables.
        expected: dict = cp.deepcopy(DICTIONARY)
        current: dict = cp.deepcopy(DICTIONARY)

        # ---------------------------------------------------------------------
        # Dictionaries have the same structure.
        # ---------------------------------------------------------------------

        current["one"]["two"] = 3
        current["one"]["three"] = "2"
        current[4]["five"] = 6
        current[4]["six"] = 5.0

        # The dictionaries should be the same.
        self.assertTrue(
            validate_dictionary_sub(expected, current),
            "The dictionaries do not match in structure."
        )

        # ---------------------------------------------------------------------
        # Dictionaries have the same structure.
        # ---------------------------------------------------------------------

        current["one"]["two"] = 3
        current["one"]["three"] = "2"
        del current[4]

        # The dictionaries should be the same.
        self.assertTrue(
            validate_dictionary_sub(expected, current),
            "The dictionary is not a subdictionary of the expected dictionary."
        )

        # ---------------------------------------------------------------------
        # Dictionaries have the same structure but different types.
        # ---------------------------------------------------------------------

        current["one"]["two"] = "3"

         # The dictionaries should NOT be the same.
        self.assertFalse(
            validate_dictionary_sub(expected, current),
            "The dictionaries match in structure."
        )

        with self.assertRaises(
            ValueError,
            msg="False validation must raise an error"
        ):
            validate_dictionary_sub(expected, current, error=True)

        # ---------------------------------------------------------------------
        # Dictionaries don't have the same structure.
        # ---------------------------------------------------------------------

        current["Four"] = 9

         # The dictionaries should NOT be the same.
        self.assertFalse(
            validate_dictionary_sub(expected, current),
            "The dictionaries match in structure."
        )

        with self.assertRaises(
            ValueError,
            msg="False validation must raise an error"
        ):
            validate_dictionary_sub(expected, current, error=True)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    unittest.main()
