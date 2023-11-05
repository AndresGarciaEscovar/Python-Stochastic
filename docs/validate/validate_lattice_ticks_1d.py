"""
    File that contains the validate functions of the parameters to construct
    special grid shapes.
"""

# ##############################################################################
# Imports
# ##############################################################################


# General.
from typing import Any

# User defined.
import docs.validate.validate_general as vgeneral

from docs.configurations import configuration_boxes as cboxes


# ##############################################################################
# Private Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_validate' Functions
# ------------------------------------------------------------------------------


def _validate_flag(vobject: Any, name: str) -> None:
    """
        Checks that the flags are boolean variables.

        :param vobject: The object to validate.

        :param name: The name of the object to validate.
    """
    # Validate the value is a positive, non-zero floating point number.
    vgeneral.validate_boolean(vobject, name=name)


def _validate_jumps(vobject: Any, nticks: int, name: str) -> None:
    """
        Checks that the jumps array is valid.

        :param vobject: The object to validate.

        :parma nticks: The number of ticks of the lattice.

        :param name: The name of the object to validate.
    """
    # List of possible sites.
    sites = tuple(x for x in range(nticks))
    vjumps = (0, 1)

    # Must be a list tuple.
    vgeneral.validate_list_tuple(vobject, name=name)

    # Validate the sub-entries.
    for i, element in enumerate(vobject):
        # String to use in the error message.
        string = f"{i} element of {name}"

        # Validate the elements.
        vgeneral.validate_list_tuple_integers(element, length=3, name=string)
        vgeneral.validate_list_tuple_existence(element[0], sites, name=string)
        vgeneral.validate_list_tuple_existence(element[1], vjumps, name=string)
        vgeneral.validate_list_tuple_existence(element[2], vjumps, name=string)

        # Extremes can't jump out of the lattice.
        if element[0] == 0 and element[1] == 1:
            raise ValueError(
                f"Invalid jump in {string}, the particle can't jump out of the "
                f"lattice. Values: {element}."
            )

        if element[0] == sites[-1] and element[2] == 1:
            raise ValueError(
                f"Invalid jump in {string}, the particle can't jump out of the "
                f"lattice. Values: {element}."
            )

    # Validate that the jumps are not repeated.
    sites = tuple(x[0] for x in vobject)
    vgeneral.validate_list_tuple_unique(sites, name="jumps")


def _validate_length(vobject: Any, name: str) -> None:
    """
        Checks that the lengths are positve, non-zero floating point numbers.

        :param vobject: The object to validate.

        :param name: The name of the object to validate.
    """
    # Validate the value is a positive, non-zero floating point number.
    vgeneral.validate_float_positive(vobject, zero=False, name=name)


def _validate_nticks(vobject: Any) -> None:
    """
        Checks that the number of ticks is a positive integer greater than 0.

        :param vobject: The object to validate.
    """
    # Validate it's a list or tuple of integers.
    vgeneral.validate_integer_positive(vobject, zero=False, name="nticks")


def _validate_particles(vobject: Any, nticks: int, name: str) -> None:
    """
        Checks that the particle arrays are valid.

        :param vobject: The object to validate.

        :parma nticks: The number of ticks of the lattice.

        :param name: The name of the object to validate.
    """
    # No need check if the list/tuple is empty.
    if isinstance(vobject, (list, tuple)) and len(vobject) == 0:
        return

    # Validate using a unique function.
    if name == "jumps":
        _validate_jumps(vobject, nticks, name)
        return

    # Validate it's a list or tuple of integers.
    vgeneral.validate_list_tuple_integers(vobject, name=name)

    # The integers must be in the range of the number of ticks.
    ticks = tuple(x for x in range(nticks))
    for value in vobject:
        try:
            vgeneral.validate_list_tuple_existence(value, ticks, name=name)

        except (TypeError, ValueError) as e:
            raise ValueError(
                f" {e} Remember that if the dimer option is set to True, the "
                f"number of sites is, effectively, reduced by one."
            )

    # The values must be unique.
    vgeneral.validate_list_tuple_unique(vobject, name=name)


def _validate_position(vobject: Any, name: str) -> None:
    """
        Checks that the object is a list or a tuple with two entries and are
        floating point numbers.

        :param vobject: The object to validate.

        :param name: The name of the object to validate.
    """
    # Validate the value is a postion.
    vgeneral.validate_list_tuple_floats(vobject, length=2, name=name)


def _validate_settings(configuration: Any) -> dict:
    """
        Validates that the setting keys are in the list of valid keys.

        :param configuration: The dictionary with the configuration settings.

        :return: The settings dictionary with the complete set of key-value
         pairs.

        :raise: ValueError if there are keys in the settings that are not in the
         list of valid keys.
    """
    # Default settings.
    settings = get_default_settings()
    dkeys = tuple(settings.keys())

    # Check that the settings is a dictionary.
    vgeneral.validate_dictionary(configuration, dkeys, "configuration")

    # Update the keys.
    for key, value in configuration.items():
        settings[key] = value

    return settings


# ##############################################################################
# Public Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'get' Functions
# ------------------------------------------------------------------------------


def get_default_settings() -> dict:
    """
        Gets the default settings for the lattice ticks.

        :return: The default settings for the lattice ticks.
    """
    return {
        # Number of ticks.
        "nticks": 1,

        # Length parameters.
        "arrow_length": cboxes.ARROW_LENGTH,
        "circle_radius": cboxes.CIRCLE_RADIUS,
        "separation_vertical": cboxes.SEPARATION_VERTICAL,
        "ticks_height": cboxes.TICK_HEIGHT,

        # Flags.
        "alphabetic": False,
        "dimers": False,

        # Particle arrays.
        "adsorbing": tuple(),
        "desorbing": tuple(),
        "fixed": tuple(),
        "jumps": tuple(),

        # Position parameters.
        "offsets_x": (0, 0),
        "offsets_y": (0, 0),
        "position_start": (cboxes.BOX_WIDTH * 0.25, -cboxes.BOX_HEIGHT * 0.5),
        "position_end": (cboxes.BOX_WIDTH * 0.75, -cboxes.BOX_HEIGHT * 0.5),
    }


# ------------------------------------------------------------------------------
# 'validate' Functions
# ------------------------------------------------------------------------------


def validate(configuration: dict) -> dict:
    """
        Validates that the configuration settings are consistent with the
        requested lattice.

        :param configuration: The dictionary with the lattice configuration
         settings.

        :return: The validated settings.
    """
    # Validate the configuration settings.
    settings = _validate_settings(configuration)

    # Extract the number of ticks.
    nticks = settings["nticks"]

    # Validate the number of ticks.
    _validate_nticks(nticks)

    # Validate the different flags.
    for flag in ("alphabetic", "dimers"):
        _validate_flag(settings[flag], flag)

    # Validate the different lengths.
    lengths = (
        "arrow_length", "circle_radius", "separation_vertical", "ticks_height"
    )
    for length in lengths:
        _validate_length(settings[length], length)

    # Validate the particle arrays.
    for particles in ("fixed", "adsorbing", "desorbing", "jumps"):
        # Prioritize the alphabetic flag.
        flag = settings["dimers"] and not settings["alphabetic"]

        # Extract the array.
        array = settings[particles]

        # For dimers, the number of sites is effectively one less.
        tnticks = nticks - 1 if flag else nticks

        # Validate the extra positions for the dimers.
        if particles == "fixed" and flag:
            # Get the neighbor sites.
            tarray = [i + 1 for i in array]
            array.extend(tarray)
            del tarray

        # Validate the array.
        _validate_particles(array, tnticks, particles)

    # Validate the positions arrays.
    positions = ("offsets_x", "offsets_y", "position_start", "position_end")
    for position in positions:
        _validate_position(settings[position], position)

    return settings
