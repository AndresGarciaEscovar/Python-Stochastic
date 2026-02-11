"""
    Contains the unit tests for the general utilities.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
import copy as cp
import unittest

# User.
from stochastic.utilities.general import format_dictionary


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


class TestUtilitiesGeneral(unittest.TestCase):
    """
        Contains the tests for the utilities.
    """
    # /////////////////////////////////////////////////////////////////////////
    # Tests
    # /////////////////////////////////////////////////////////////////////////

    def test_format_dictionary(self) -> None:
        """
            Tests that replacing the dictionary values works correctly.
        """
        # Auxiliary variables.
        expected: dict = cp.deepcopy(DICTIONARY)
        current: dict = cp.deepcopy(DICTIONARY)

        # ---------------------------------------------------------------------
        # Just change one entry.
        # ---------------------------------------------------------------------

        msg: str = "The parameters must be equal."

        del current["one"]
        del current[4]["five"]

        current[4]["six"] = 7.0

        # Setup the parameters.
        final: dict = format_dictionary(expected, current)

        # Validate the quantities.
        self.assertEqual(expected["one"]["two"], final["one"]["two"], msg)
        self.assertEqual(expected["one"]["three"], final["one"]["three"], msg)
        self.assertEqual(expected[4]["five"], final[4]["five"], msg)
        self.assertEqual(current[4]["six"], final[4]["six"], msg )

        self.assertNotEqual(expected[4]["six"], final[4]["six"], msg )

        # ---------------------------------------------------------------------
        # Key error must be generated.
        # ---------------------------------------------------------------------

        current["five"] = "Nine"

        with self.assertRaises(KeyError, msg="Key should not exist."):
            format_dictionary(expected, current)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    unittest.main()
