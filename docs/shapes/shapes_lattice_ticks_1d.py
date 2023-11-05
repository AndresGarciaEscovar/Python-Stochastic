"""
    File that contains the functions to construct special grid shapes.
"""

# ##############################################################################
# Imports
# ##############################################################################


# General.
from typing import Union

# User defined.
import docs.validate.validate_lattice_ticks_1d as lvalidator

import docs.shapes.shapes_latex as lshapes


# ##############################################################################
# Private Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_get' Functions
# ------------------------------------------------------------------------------


def _get_adsorbing(
    configuration: dict, coordinates: Union[list, tuple], offset: tuple
) -> str:
    """
        Given the configuration, gets the circles or characters for the lattice.
        If the alphabetical characters are requested, it just returns a blank
        string.

        :param configuration: The configuration dictionary.

        :param coordinates: The coordinates of where the particles must be
         placed.

        :param offset: The offset of the ticks.

        :return: The string with the adsorbing particles.
    """
    # No need for further processing.
    if configuration["alphabetic"] or len(configuration["adsorbing"]) == 0:
        return ""

    # Auxiliary variables.
    strings = ["% Adsorbing particles"]

    # Extract the settings.
    arrow_length = configuration["arrow_length"]
    circle_radius = configuration["circle_radius"]
    separation_vertical = configuration["separation_vertical"]

    # Set the circles.
    for index in configuration["adsorbing"]:
        # Get the tick position.
        ncoord_x = coordinates[index][0]
        ncoord_y = coordinates[index][1]

        # Get the coordinates.
        pos_arrow_str_x = ncoord_x
        pos_arrow_str_y = ncoord_y
        pos_arrow_str = pos_arrow_str_x, pos_arrow_str_y

        pos_arrow_end_x = ncoord_x
        pos_arrow_end_y = ncoord_y + arrow_length
        pos_arrow_end = pos_arrow_end_x, pos_arrow_end_y

        # Get the arrow.
        fig = lshapes.get_line(pos_arrow_end, pos_arrow_str, offset, True)
        strings.append(fig)

        pos_circle_x = pos_arrow_end_x
        pos_circle_y = pos_arrow_end_y + separation_vertical + circle_radius
        pos_circle = pos_circle_x, pos_circle_y

        # Get the circle.
        fig = lshapes.get_circle(pos_circle, circle_radius, offset, True)
        strings.append(fig)

        # Add the dimers if needed.
        if not configuration["dimers"]:
            continue

        # Get the tick position.
        ncoord_x = coordinates[index + 1][0]
        ncoord_y = coordinates[index + 1][1]

        # Get the coordinates.
        pos_arrow_str_x_0 = ncoord_x
        pos_arrow_str_y_0 = ncoord_y
        pos_arrow_str_0 = pos_arrow_str_x_0, pos_arrow_str_y_0

        pos_arrow_end_x_0 = ncoord_x
        pos_arrow_end_y_0 = ncoord_y + arrow_length
        pos_arrow_end_0 = pos_arrow_end_x_0, pos_arrow_end_y_0

        # Get the arrow.
        fig = lshapes.get_line(pos_arrow_end_0, pos_arrow_str_0, offset, True)
        strings.append(fig)

        pos_circle_x_0 = pos_arrow_end_x_0
        pos_circle_y_0 = pos_arrow_end_y_0 + separation_vertical + circle_radius
        pos_circle_0 = pos_circle_x_0, pos_circle_y_0

        # Get the circle.
        fig = lshapes.get_circle(pos_circle_0, circle_radius, offset, True)
        strings.append(fig)

        # Join the circles.
        fig = lshapes.get_line(pos_circle, pos_circle_0, offset)
        strings.append(fig)

    return "\n".join(strings)


def _get_desorbing(
    configuration: dict, coordinates: Union[list, tuple], offset: tuple
) -> str:
    """
        Given the configuration, gets the circles or characters for the lattice.
        If the alphabetical characters are requested, it just returns a blank
        string.

        :param configuration: The configuration dictionary.

        :param coordinates: The coordinates of where the particles must be
         placed.

        :param offset: The offset of the ticks.

        :return: The string with the adsorbing particles.
    """
    # No need for further processing.
    if configuration["alphabetic"] or len(configuration["desorbing"]) == 0:
        return ""

    # Auxiliary variables.
    ncoordinates = []
    strings = ["% Adsorbing particles"]

    # Extract the settings.
    arrow_length = configuration["arrow_length"]

    # Get the adsorbing particles.
    for index in configuration["desorbing"]:
        # For dimers.

        # Get the tick position.
        ncoord_x = coordinates[index][0]
        ncoord_y = coordinates[index][1]

        # Get the coordinates.
        pos_arrow_str_x = ncoord_x
        pos_arrow_str_y = ncoord_y
        pos_arrow_str = [pos_arrow_str_x, pos_arrow_str_y]

        pos_arrow_end_x = ncoord_x
        pos_arrow_end_y = ncoord_y + arrow_length
        pos_arrow_end = [pos_arrow_end_x, pos_arrow_end_y]

        if configuration["dimers"]:
            ncoord_x_0 = coordinates[index + 1][0]
            pos_arrow_str[0] = (pos_arrow_str[0] + ncoord_x_0) / 2
            pos_arrow_end[0] = pos_arrow_str[0]

        # Convert into tuples.
        pos_arrow_str = tuple(pos_arrow_str)
        pos_arrow_end = tuple(pos_arrow_end)

        # Get the arrow.
        fig = lshapes.get_line(pos_arrow_str, pos_arrow_end, offset, True)
        strings.append(fig)

    return "\n".join(strings)


def _get_fixed(
    configuration: dict, coordinates: Union[list, tuple], offset: tuple
) -> tuple:
    """
        Given the configuration, gets the circles or characters for the lattice.
        If the alphabetical characters are used, fixed particles are replaced
        by B characters and the rest by A characters.

        :param configuration: The configuration dictionary.

        :param coordinates: The coordinates of the ticks.

        :param offset: The offset of the ticks.

        :return: The ticks and the baseline, along with the top coordinates of
         the ticks.
    """
    # Auxiliary variables.
    checked = set()
    ncoordinates = []
    radius = configuration["circle_radius"]
    strings = []

    # Get the flags.
    flag_dims = configuration["dimers"]
    flag_alph = configuration["alphabetic"]

    # For all the ticks.
    for i, coordinate in enumerate(coordinates):
        # Get the tick position.
        ncoord_x = coordinate[0]
        ncoord_y = coordinate[1]

        # Get the coordinates.
        if flag_alph:
            # Get the character and the position.
            letter = "B" if i in configuration["fixed"] else "A"
            pos_char = ncoord_x, ncoord_y + radius

            # Append the text.
            strings.append(lshapes.get_text(letter, pos_char, offset))

            # Character position.
            pos_char = list(pos_char)
            pos_char[1] += radius + configuration["separation_vertical"]
            pos_char = tuple(pos_char)
            ncoordinates.append(pos_char)

            continue

        # Circle model.
        if i not in configuration["fixed"]:
            # Add to the coordinates.
            if i not in checked:
                ncoordinates.append(coordinate)

            checked.add(i)
            continue

        # Add to the checked set.
        checked.add(i)

        # Get the circle position.
        pos_circle = ncoord_x, ncoord_y + radius
        strings.append(lshapes.get_circle(pos_circle, radius,  offset, True))

        # Character position.
        pos_circle = list(pos_circle)
        pos_circle[1] += radius + configuration["separation_vertical"]
        pos_circle = tuple(pos_circle)
        ncoordinates.append(pos_circle)

        # No need to add the dimer.
        if not flag_dims:
            continue

        # Add to the checked set.
        checked.add(i + 1)

        # Get the base position, once again.
        ncoord_x = coordinate[0]
        ncoord_y = coordinate[1]
        pos_circle = ncoord_x, ncoord_y + radius

        # Get the next tick position.
        ncoord_x_0 = coordinates[i + 1][0]
        ncoord_y_0 = coordinates[i + 1][1]

        # Get the circle position.
        pos_circle_0 = ncoord_x_0, ncoord_y_0 + radius
        strings.append(lshapes.get_circle(pos_circle_0, radius, offset, True))

        # Join the two circles.
        strings.append(lshapes.get_line(pos_circle, pos_circle_0, offset))

        # Character position.
        pos_circle_0 = list(pos_circle_0)
        pos_circle_0[1] += radius + configuration["separation_vertical"]
        pos_circle_0 = tuple(pos_circle_0)
        ncoordinates.append(pos_circle_0)

    return "\n".join(strings), tuple(ncoordinates)


def _get_ticks(configuration: dict, offset: tuple) -> tuple:
    """
        Given the configuration, gets the ticks and the base libe for the
        lattice.

        :param configuration: The configuration dictionary.

        :param offset: The offset of the ticks.

        :return: The ticks and the baseline, along with the coordinates of the
         ticks.
    """
    # Auxiliary variables.
    strings = []
    coordinates = []

    # Number of ticks.
    nticks = configuration["nticks"]

    # Extract the settings.
    position_str = configuration["position_start"]
    position_end = configuration["position_end"]

    # Get the base line.
    strings.append(lshapes.get_line(position_str, position_end, offset))

    # Set the only tick.
    if nticks == 1:
        # Get the tick height.
        height = configuration["ticks_height"]

        # Get the tick offsets
        pos_str_x = position_str[0] + configuration["offsets_x"][0]
        pos_end_x = position_end[0] + configuration["offsets_x"][1]
        pos = (pos_str_x + pos_end_x) / 2

        pos_str_y = position_str[1] + configuration["offsets_y"][0]
        pos_end_y = position_end[1] + configuration["offsets_y"][1] + height

        pos_str = pos, pos_str_y
        pos_end = pos, pos_end_y

        # Get the tick.
        strings.append(lshapes.get_line(pos_str, pos_end, offset))

        pos_end = list(pos_end)
        pos_end[1] += configuration["separation_vertical"]
        pos_end = tuple(pos_end)

        return "\n".join(strings), (pos_end,)

    # Interval at which the ticks will be drawn.
    position_str_x = position_str[0] + configuration["offsets_x"][0]
    position_end_x = position_end[0] + configuration["offsets_x"][1]

    # Interval at which to draw the ticks.
    interval = (position_end_x - position_str_x) / (nticks - 1)

    # Fixed variables.
    height = configuration["ticks_height"]

    # For all the ticks.
    for i in range(nticks):
        # Get the tick position.
        pos_str_x = position_str_x + i * interval
        pos_end_x = pos_str_x

        pos_str_y = position_str[1] + configuration["offsets_y"][0]
        pos_end_y = position_end[1] + configuration["offsets_y"][1] + height

        pos_str = pos_str_x, pos_str_y
        pos_end = pos_end_x, pos_end_y

        # Get the tick.
        strings.append(lshapes.get_line(pos_str, pos_end, offset))

        pos_end = list(pos_end)
        pos_end[1] += configuration["separation_vertical"]
        pos_end = tuple(pos_end)

        # Append the new coordinate.
        coordinates.append(pos_end)

    return "\n".join(strings), tuple(coordinates)


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
    return lvalidator.get_default_settings()


def get_grid(configuration: dict, offset: tuple = None) -> str:
    """
        Gets the 1 dimensional tick grid, with the specified configuration.

        :param configuration: A dictionary with the configuration of the grid.

        :param offset: The offset of all the tick items.

        :return: The requested LaTeX code for the grid.
    """
    # Auxiliary variables.
    strings = []

    # Validate and get ALL the settings.
    settings = lvalidator.validate(configuration)

    # Get the ticks.
    string, coordinates = _get_ticks(settings, offset)
    strings.append(string)

    # Get the fixed particles.
    string, coordinates = _get_fixed(settings, coordinates, offset)
    strings.append(string)

    # Get the adsorbing particles.
    string = _get_adsorbing(settings, coordinates, offset)
    strings.append(string)

    # Get the desorbing particles.
    string = _get_desorbing(settings, coordinates, offset)
    strings.append(string)

    return "\n".join(strings)
