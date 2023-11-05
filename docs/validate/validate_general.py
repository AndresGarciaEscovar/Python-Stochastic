"""
    Contains the functions for general validation.
"""


# ##############################################################################
# Imports
# ##############################################################################


# General.
from typing import Any, Union


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'validate' Functions
# ------------------------------------------------------------------------------


def validate_boolean(
    vobject: Any, name: str = None, rexception: bool = True
) -> bool:
    """
        Validates that the object is a boolean variable.

        :param vobject: The object to validate.

        :param name: The name of the variable. If none is provided,
         a blank space will be used.

        :param rexception: If an exception should be raised if a validation
         fails. True by default.

        :raise TypeError: If the object is not a boolean.
    """
    # Check that the object is a boolean variable.
    flag = isinstance(vobject, bool)

    if not flag and rexception:
        # Format the name.
        tname = " " if name is None else f" \"{name}\" "

        raise TypeError(
            f"The variable{tname}must be a boolean variable. Current "
            f"type: {type(vobject)}."
        )

    return flag


def validate_dictionary(
    vobject: Any, keys: tuple = None, name: str = None, rexception: bool = True
) -> bool:
    """
        Validates that the object is a dictionary with the given keys.

        :param vobject: The object to validate.

        :param keys: The valid keys that the dictionary can contain. None by
         default.

        :param name: The name of the dictionary. If None is provided, a blank
         space will be used. None by default.

        :param rexception: If an exception should be raised if a validation
         fails. True by default.

        :raise TypeError: If the dictionary is not a dictionary.

        :raise: ValueError if the dictionary does not contain the keys.
    """
    # Check it's a dictionary.
    flag = isinstance(vobject, dict)

    if not flag and rexception:
        # Format the name.
        tname = " " if name is None else f" \"{name}\" "

        raise TypeError(
            f"The object{tname}must be a dictionary. Current type: "
            f"{type(vobject)}."
        )

    # No need to keep validating.
    if keys is None or not flag:
        return flag

    # Check the keys are valid.
    flag = all(key in keys for key in vobject.keys())

    if not flag and rexception:
        # Format the variables.
        tname = " " if name is None else f" \"{name}\" "
        invalid = tuple(key for key in vobject.keys() if key not in keys)

        raise ValueError(
            f"The dictionary{tname}contains non-valid keys: {invalid}. The "
            f"only valid keys are: {keys}."
        )

    return flag


def validate_float(
    vobject: Any, name: str = None, rexception: bool = True
) -> bool:
    """
        Validates that the object is a floating point number or an integer.

        :param vobject: The object to validate.

        :param name: The name of the variable. If none is provided,
         a blank space will be used.

        :param rexception: If an exception should be raised if a validation
         fails. True by default.

        :raise TypeError: If the object is not a floating point number or an
         integer.
    """
    # Check that the object is an floating point number or an integer.
    flag = isinstance(vobject, (int, float))

    if not flag and rexception:
        # Format the name.
        tname = " " if name is None else f" \"{name}\" "

        raise TypeError(
            f"The variable{tname}must be an floating point number. Current "
            f"type: {type(vobject)}."
        )

    return flag


def validate_float_positive(
    vobject: Any, zero: bool = True, name: str = None, rexception: bool = True
) -> bool:
    """
        Validates that the object is a positive floating point number. If the
        zero parameter is True, the number can be zero.

        :param vobject: The object to validate.

        :param zero: If the number can be zero. True by default.

        :param name: The name of the variable. If None is provided,
         a blank space will be used. None by default.

        :param rexception: If an exception should be raised if a validation
         fails. True by default.

        :raise ValueError: If the object is not a positive floating point
         number.
    """
    # Validate it's a floating point number.
    if not (flag := validate_float(vobject, name, rexception)):
        return flag

    # Positive condition.
    flag = vobject >= 0 if zero else vobject > 0

    # Evaluate.
    if not flag and rexception:
        # Configure only if needed.
        tname = " " if name is None else f" \"{name}\" "
        statement = " greater than or equal to " if zero else " greater than "

        raise ValueError(
            f"The variable{tname}must be a floating point "
            f"number{statement}zero. Current value: {vobject}."
        )

    return flag


def validate_float_negative(
    vobject: Any, zero: bool = True, name: str = None, rexception: bool = True
) -> bool:
    """
        Validates that the object is a negative floating point number. If the
        zero parameter is True, the number can be zero.

        :param vobject: The object to validate.

        :param zero: If the number can be zero. True by default.

        :param name: The name of the variable. If None is provided,
         a blank space will be used. None by default.

        :param rexception: If an exception should be raised if a validation
         fails. True by default.

        :raise ValueError: If the object is not a negative floating point
         number.
    """
    # Validate it's a floating point number.
    if not (flag := validate_float(vobject, name, rexception)):
        return flag

    # Negative condition.
    flag = vobject <= 0 if zero else vobject < 0

    # Evaluate.
    if not flag and rexception:
        # Configure only if needed.
        tname = " " if name is None else f" \"{name}\" "
        statement = " less than or equal to " if zero else " less than "

        raise ValueError(
            f"The variable{tname}must be a floating point "
            f"number{statement}zero. Current value: {vobject}."
        )

    return flag


def validate_integer(
    vobject: Any, name: str = None, rexception: bool = True
) -> bool:
    """
        Validates that the object is an integer.

        :param vobject: The object to validate.

        :param name: The name of the variable. If none is provided,
         a blank space will be used.

        :param rexception: If an exception should be raised if a validation
         fails. True by default.

        :raise TypeError: If the object is not an integer.
    """
    # Check that the object is an integer.
    flag = isinstance(vobject, int)

    if not flag and rexception:
        # Format the name.
        tname = " " if name is None else f" \"{name}\" "

        raise TypeError(
            f"The variable{tname}must be an integer. Current type: "
            f"{type(vobject)}."
        )

    return flag


def validate_integer_positive(
    vobject: Any, zero: bool = True, name: str = None, rexception: bool = True
) -> bool:
    """
        Validates that the object is a positive integer. If the zero parameter
        is True, the integer can be zero.

        :param vobject: The object to validate.

        :param zero: If the integer can be zero. True by default.

        :param name: The name of the variable. If None is provided,
         a blank space will be used. None by default.

        :param rexception: If an exception should be raised if a validation
         fails. True by default.

        :raise ValueError: If the object is not a positive integer.
    """
    # Validate it's an integer.
    if not (flag := validate_integer(vobject, name, rexception)):
        return flag

    # Positive condition.
    flag = vobject >= 0 if zero else vobject > 0

    # Evaluate.
    if not flag and rexception:
        # Configure only if needed.
        tname = " " if name is None else f" \"{name}\" "
        statement = " greater than or equal to " if zero else " greater than "

        raise ValueError(
            f"The variable{tname}must be an integer{statement}zero. Current "
            f"value: {vobject}."
        )

    return flag


def validate_integer_negative(
    vobject: Any, zero: bool = True, name: str = None, rexception: bool = True
) -> bool:
    """
        Validates that the object is a negative integer. If the zero parameter
        is True, the integer can be zero.

        :param vobject: The object to validate.

        :param zero: If the integer can be zero. True by default.

        :param name: The name of the variable. If None is provided,
         a blank space will be used. None by default.

        :param rexception: If an exception should be raised if a validation
         fails. True by default.

        :raise ValueError: If the object is not a negative integer.
    """
    # Validate it's an integer.
    if not (flag := validate_integer(vobject, name, rexception)):
        return flag

    # Negative condition.
    flag = vobject <= 0 if zero else vobject < 0

    # Evaluate.
    if not flag and rexception:
        # Configure only if needed.
        tname = " " if name is None else f" \"{name}\" "
        statement = " greater than or equal to " if zero else " greater than "

        raise ValueError(
            f"The variable{tname}must be an integer{statement}zero. Current "
            f"value: {vobject}."
        )

    return flag


def validate_list_tuple(
    vobject: Any, length: int = None, name: str = None, rexception: bool = True
) -> bool:
    """
        Validates that the given object is a list or a tuple. If the
        length parameter is provided, it will check that the length of the
        list or tuple is the same as the given length.

        :param vobject: The object to validate.

        :param length: The requested length of the list or tuple. None by
         default.

        :param name: The name of the variable. If None is provided, a blank
         space will be used. None by default.

        :param rexception: If an exception should be raised. True by default.

        :raise TypeError: If the object is not a list or a tuple.

        :raise ValueError: If the length is not the same as the given length.
         If the length of the list or tuple is not the same as the given length.
    """
    # Check the condition.
    flag = isinstance(vobject, (list, tuple))

    # Check that the dictionary is a dictionary.
    if not flag and rexception:
        # Format the name.
        tname = " " if name is None else f" \"{name}\" "

        raise TypeError(
            f"The variable{tname}must be a list or a tuple. Current type: "
            f"{type(vobject)}."
        )

    # Return if the length is not provided.
    if length is None or not flag:
        return flag

    # Check that the length is an integer, this is non-negotiable.
    if not isinstance(length, int) and validate_integer_positive(length):
        raise TypeError(
            f"The provided length must be an integer. Current type: "
            f"{type(length)}."
        )

    # Set the length correctly.
    length = 0 if length < 0 else length

    if len(vobject) != length:
        # Format the name.
        tname = " " if name is None else f" \"{name}\" "

        raise ValueError(
            f"The variable{tname}must have a length of {length}. Current "
            f"length: {len(vobject)}."
        )


def validate_list_tuple_existence(
    vobject: Any, values: Union[list, tuple], name: str = None,
    rexception: bool = True
) -> bool:
    """
        Validates that the given object is a list or a tuple of integers.

        :param vobject: The object to validate.

        :param values: The tuple where the object must be.

        :param name: The name of the variable. If None is provided, a blank
         space will be used. None by default.

        :param rexception: If an exception should be raised. True by default.

        :raise TypeError: If the object is not a list or a tuple.

        :raise ValueError: If the length is not the same as the given length.
         If the length of the list or tuple is not the same as the given length.
    """
    # Validate the values are a list or a tuple.
    validate_list_tuple(values, length=None, name="values", rexception=True)

    # Validate the object is in the values.
    flag = vobject in values

    # Evaluate.
    if not flag and rexception:
        # Format the name.
        tname = " " if name is None else f" \"{name}\" "
        values = tuple(value for value in values)

        raise ValueError(
            f"The variable{tname}must be one of the following: {values}. "
            f"Current value: {vobject}."
        )

    return flag


def validate_list_tuple_floats(
    vobject: Any, length: int = None, name: str = None, rexception: bool = True
) -> bool:
    """
        Validates that the given object is a list or a tuple of floating point
        numbers.

        :param vobject: The object to validate.

        :param length: The requested length of the list or tuple. None by
         default.

        :param name: The name of the variable. If None is provided, a blank
         space will be used. None by default.

        :param rexception: If an exception should be raised. True by default.

        :raise TypeError: If the object is not a list or a tuple.

        :raise ValueError: If the length is not the same as the given length.
         If the length of the list or tuple is not the same as the given length.
    """
    # Validate it's a list or a tuple.
    if not (flag := validate_list_tuple(vobject, length, name, rexception)):
        return flag

    # Check that all the elements are integers or floats.
    flag = all(isinstance(element, (int, float)) for element in vobject)

    # Evaluate.
    if not flag and rexception:
        # Format the name.
        tname = " " if name is None else f" \"{name}\" "
        not_floats = []

        # Get the index of the elements that are not integers or floats.
        for i, element in enumerate(vobject):
            # No need to add this.
            if isinstance(element, (int, float)):
                continue

            # Add the index.
            not_floats.append(f"index = {i}, type = {type(element)}")

        raise TypeError(
            f"The variable{tname}must be a list, or a tuple, of integers or "
            f"floating point numbers. Current type: {tuple(not_floats)}."
        )

    return flag


def validate_list_tuple_integers(
    vobject: Any, length: int = None, name: str = None, rexception: bool = True
) -> bool:
    """
        Validates that the given object is a list or a tuple of integers.

        :param vobject: The object to validate.

        :param length: The requested length of the list or tuple. None by
         default.

        :param name: The name of the variable. If None is provided, a blank
         space will be used. None by default.

        :param rexception: If an exception should be raised. True by default.

        :raise TypeError: If the object is not a list or a tuple.

        :raise ValueError: If the length is not the same as the given length.
         If the length of the list or tuple is not the same as the given length.
    """
    # Validate it's a list or a tuple.
    if not (flag := validate_list_tuple(vobject, length, name, rexception)):
        return flag

    # Check that all the elements are integers.
    flag = all(isinstance(element, int) for element in vobject)

    # Evaluate.
    if not flag and rexception:
        # Format the name.
        tname = " " if name is None else f" \"{name}\" "
        not_integers = []

        # Get the index of the elements that are not integers.
        for i, element in enumerate(vobject):
            # No need to add this.
            if isinstance(element, int):
                continue

            # Add the index.
            not_integers.append(f"index = {i}, type = {type(element)}")

        raise TypeError(
            f"The variable{tname}must be a list or a tuple of integers. "
            f"Current type: {tuple(not_integers)}."
        )

    return flag


def validate_list_tuple_unique(
    vobject: Any, name: str = None, rexception: bool = True
) -> bool:
    """
        Validates that the given object is composed of unique values. For this,
        the list or tuple must have hashable elements. In this case, the
        elements are assumed to be hashable.

        :param vobject: The object to validate.

        :param name: The name of the variable. If None is provided, a blank
         space will be used. None by default.

        :param rexception: If an exception should be raised. True by default.

        :raise TypeError: If the object is not a list or a tuple.

        :raise ValueError: If there are repeated values of a given element.
    """
    # Validate it's a list or a tuple.
    if not (flag := validate_list_tuple(vobject, name=name)):
        return flag

    # Check that there are no repeated values.
    flag = len(set(vobject)) == len(vobject)

    # Evaluate.
    if not flag and rexception:
        # Format the name.
        tname = " " if name is None else f" \"{name}\" "

        # Add the objects to the dictionary.
        repeated = dict()
        for x in set(vobject):
            key = f"Value {x}"
            repeated[key] = vobject.count(x)

        raise ValueError(
            f"The variable{tname}must be a list or a tuple of unique values. "
            f"Repeated objects and count: {repeated}."
        )

    return flag
