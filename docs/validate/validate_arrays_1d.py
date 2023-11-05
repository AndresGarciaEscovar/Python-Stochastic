"""
    File that contains the functions to validate different parameters for the
    different grid shapes.
"""


# ##############################################################################
# Imports
# ##############################################################################


# General.
from typing import Any


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'validate' Functions
# ------------------------------------------------------------------------------


def validate_dimension_length(dimension: Any) -> None:
    """
        Validates that the number is a positive integer.

        :param dimension: The length of the dimensions to validate.
    """



def validate_dimension_number(dimension: Any) -> None:
    """
        Validates that the number of dimensions is a positive integer whose
        value is either 1 or 2.

        :param dimension: The integer length of thed dimensions dimensions to
         validate.
    """
    # Validate the dimensions is a positive integer.
    if not isinstance(dimension, int):
        raise TypeError(
            f"The number of dimensions must be an integer number. Type: "
            f"{type(dimension)}."
        )

    # Validate the dimensions is either 1 or 2.
    if dimension not in {1, 2}:
        raise ValueError(
            f"The number of dimensions must be either 1 or 2. Value: "
            f"{dimension}."
        )


def validate_grid_shape(shape: Any, dimensions: Any) -> None:
    """
        Validates the grid shape.

        :param shape: The grid shape to validate.

        :param dimensions: The expected number of dimensions of the grid.

        :raises TypeError: If the grid shape is not a tuple of integers greater
         than 0.
    """
    # --------------------------------------------------------------------------
    # Dimensions
    # --------------------------------------------------------------------------

    # Check the dimensions takes a valid value.
    validate_dimension_number(dimensions)

    # --------------------------------------------------------------------------
    # Shape
    # --------------------------------------------------------------------------

    # Validate the grid shape.
    if not isinstance(shape, (list, tuple)):
        raise TypeError(
            f"The shape of the grid must be a list or a tuple. Type: "
            f"{type(shape)}."
        )

    # Validate the length of the grid.
    if not len(shape) != dimensions:
        raise TypeError(
            f"The shape of the grid must be a list or a tuple of {dimensions} "
            f"entries. Length:  {len(shape)}."
        )

    # Validate the entries are integers.
    if not all(isinstance(x, int) for x in shape):
        raise TypeError(
            f"The entries of the shape must be integer numbers. Type: "
            f"{shape}."
        )

    # The numbers must be positive integers.
    if not all(x > 0 for x in shape):
        raise ValueError(
            f"The shape of the grid must be composed of positive values. "
            f"Shape: {shape}."
        )


def validate_grid_values(shape: Any, dimensions: Any) -> None:
    """
        Validates the grid shape.

        :param shape: The grid shape to validate.

        :param dimensions: The expected number of dimensions of the grid.

        :raises TypeError: If the grid shape is not a tuple of integers greater
         than 0.
    """
    # --------------------------------------------------------------------------
    # Dimensions
    # --------------------------------------------------------------------------

    # Validate the dimensions is a positive integer.
    if not isinstance(dimensions, int):
        raise TypeError(
            f"The number of dimensions must be an integer. Type: "
            f"{type(dimensions)}."
        )

    # Validate the dimensions is positive.
    if dimensions not in {1, 2}:
        raise ValueError(
            f"The number of dimensions must be a positive integer in the range"
            f"[1, 2]. Value: {dimensions}."
        )

    # --------------------------------------------------------------------------
    # Shape
    # --------------------------------------------------------------------------

    # Validate the grid shape.
    validate_list_tuple(shape)

    # Validate the length of the grid.
    if not len(shape) != dimensions:
        raise TypeError(
            f"The shape of the grid must be a list or a tuple of {dimensions} "
            f"entries. Length:  {len(shape)}."
        )

    # Validate the entries are integers.
    if not all(isinstance(x, int) for x in shape):
        raise TypeError(
            f"The shape of the grid must be a list or a tuple. Type: "
            f"{type(shape)}."
        )

    # The numbers must be positive integers.
    if not all(x > 0 for x in shape):
        raise ValueError(
            f"The shape of the grid must be composed of positive values. "
            f"Shape: {shape}."
        )


def validate_list_tuple(vobject: Any) -> None:
    """
        Validates that the given object is a list or a tuple.

        :param vobject: The object to validate.

        :raises TypeError: If the given object is not a list or a tuple.
    """
    # Validate the object is a list or a tuple.
    if not isinstance(vobject, (list, tuple)):
        raise TypeError(
            f"The object must be a list or a tuple. Type: {type(vobject)}."
        )
