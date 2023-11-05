"""
    Generates the code for the splin flip box in the grid.
"""

# ##############################################################################
# Imports
# ##############################################################################


# General
from typing import Any, Union

# User defined.
import docs.configurations.configuration_boxes as cboxes

import docs.shapes.shapes_lattice_ticks_1d as gshapes
import docs.shapes.shapes_latex as lshapes


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'get' Functions
# ------------------------------------------------------------------------------


def get_boxes(label: str, offset: tuple) -> str:
    """
        Get the bounding box of the image.

        :param label: The label of the box.

        :param offset: The offset of the box.

        :return: The bounding box text of the image.
    """
    # Auxiliary variables.
    boxes = ["% Boxes"]

    # Main box.
    position_br = cboxes.BOX_POSITION_BOTTOM
    position_tl = cboxes.BOX_POSITION_TOP
    fig = lshapes.get_rectangle(position_tl, position_br, offset)
    boxes.append(fig)

    # Set the label box.
    position_br = cboxes.TITLE_BOX_POSITION_BOTTOM
    position_tl = cboxes.TITLE_BOX_POSITION_TOP
    fig = lshapes.get_rectangle(position_tl, position_br, offset)
    boxes.append(fig)

    # Set the label.
    position = tuple((x + y) / 2 for x, y in zip(position_tl, position_br))
    fig = lshapes.get_text(label, position, offset)
    boxes.append(fig)

    return "\n".join(boxes)


def get_ellipses(
    coordinates: Union[list, tuple], ellipses: Union[list, tuple],
    height: float, separation: float, offset: tuple
) -> str:
    """
        Gets the elipses for the image.

        :param coordinates: The coordinates of the spin ticks, such that they
         are in the middle of the arrow.

        :param ellipses: A list of sites around which the elipses will be drawn.

        :param height: The height of the spin arrows.

        :param separation: The separation between the ticks.

        :param offset: The offset of the elipses.

        :return: The text for the elipses.
    """
    # Auxiliary variables.
    fellipses = ["% Ellipses"]

    # No need to draw if there are no ellipses.
    if len(ellipses) == 0:
        return ""

    # Auxiliary variables.
    xaxis = separation / 2
    yaxis = height * 2 / 3

    # Get all the ellipses.
    for index in ellipses:
        # Extract the coordinates.
        position = coordinates[index]
        fellipses.append(lshapes.get_ellipse(position, xaxis, yaxis, offset))

    return "\n".join(fellipses)


def get_grid(
    nspins: int, spins_down: Union[list, tuple], offset: tuple
) -> tuple:
    """
        Gets the spin grid for the image.

        :param nspins: The number of spins in the grid.

        :param spins_down: The spins that are down.

        :param offset: The offset of the grid.

        :return: The text for the grid and the coordinates of the ticks.
    """
    # Auxiliary variables.
    boxes = ["% Grid"]

    # Lattice Position.
    position_str = cboxes.LATTICE_POSITION_TICKS
    position_end = position_str[0] + cboxes.LENGTH_LATTICE, position_str[1]

    # Basic grid configuration.
    configuration = {
        "positions": (position_str, position_end),
        "nspins": nspins,
        "spins_down": spins_down,
        "arrow_height": cboxes.ARROW_HEIGHT * 3,
    }

    # Other values.
    height = configuration["arrow_height"]

    # Set the grid components.
    string, coordinates, separat = gshapes.get_spins_grid(configuration, offset)
    boxes.append(string)

    return "\n".join(boxes), coordinates, height, separat


def get_labels(label: str, offset: tuple) -> str:
    """
        Gets the labels for the image.

        :param label: The label of the box.

        :param offset: The offset of the labels.

        :return: The text for the labels.
    """
    # Auxliary variables.
    boxes = []

    # --------------------------------------------------------------------------
    # Main label
    # --------------------------------------------------------------------------

    position = cboxes.LABEL_POSITION_MAIN
    fig = lshapes.get_text(label, position, offset)
    boxes.append(fig)

    # --------------------------------------------------------------------------
    # Other labels
    # --------------------------------------------------------------------------

    label = "\\tiny{Easy}"
    position = cboxes.BOX_WIDTH * 0.25, -cboxes.BOX_HEIGHT * 0.20
    fig = lshapes.get_text(label, position, offset)
    boxes.append(fig)

    label = "\\tiny{Moderate}"
    position = cboxes.BOX_WIDTH * 0.45, -cboxes.BOX_HEIGHT * 0.20
    fig = lshapes.get_text(label, position, offset)
    boxes.append(fig)

    label = "\\tiny{Hard}"
    position = cboxes.BOX_WIDTH * 0.70, -cboxes.BOX_HEIGHT * 0.20
    fig = lshapes.get_text(label, position, offset)
    boxes.append(fig)

    return "\n".join(boxes)


def get_other(height: float, offset: tuple) -> str:
    """
        Gets general elements for the image.

        :param height: The height of the spin arrows.

        :param offset: The offset of the labels.

        :return: The text for the general elements.
    """
    # Arrows and elements.
    elements = []

    # ------------------------------------------------------------------------ #
    #                                Coordinates                               #
    # ------------------------------------------------------------------------ #

    # y coordinates.
    y_top = -cboxes.BOX_HEIGHT * 0.65
    y_bot = -cboxes.BOX_HEIGHT * 0.85

    # x coordinates.
    x_str = cboxes.BOX_WIDTH * 0.40
    x_end = cboxes.BOX_WIDTH * 0.60

    aheight = height * 0.7

    # Top coordinates.
    coords_str_top_l = x_str, y_top
    coords_end_top_l = x_str, y_top + aheight

    coords_str_top_r = x_end, y_top
    coords_end_top_r = x_end, y_top + aheight

    x_position_top = (coords_str_top_l[0] + coords_str_top_r[0]) / 2
    y_position_top = (coords_str_top_r[1] + coords_end_top_r[1]) / 2
    position_top = x_position_top, y_position_top

    # Bottom coordinates.
    coords_str_bot_l = x_str, y_bot
    coords_end_bot_l = x_str, y_bot + aheight

    coords_str_bot_r = x_end, y_bot
    coords_end_bot_r = x_end, y_bot + aheight

    x_position_bot = (coords_str_bot_l[0] + coords_str_bot_r[0]) / 2
    y_position_bot = (coords_str_bot_r[1] + coords_end_bot_r[1]) / 2
    position_bot = x_position_bot, y_position_bot

    # ------------------------------------------------------------------------ #
    #                                Upper Image                               #
    # ------------------------------------------------------------------------ #

    # Right arrow.
    elements.append(
        lshapes.get_line(coords_str_top_l, coords_end_top_l, offset, True)
    )

    # Left arrow.
    elements.append(
        lshapes.get_line(coords_end_top_r, coords_str_top_r, offset, True)
    )

    # Label.
    label = "to"
    elements.append(lshapes.get_text(label, position_top, offset))

    # ------------------------------------------------------------------------ #
    #                                Lower Image                               #
    # ------------------------------------------------------------------------ #

    # Right arrow.
    elements.append(
        lshapes.get_line(coords_end_bot_l, coords_str_bot_l, offset, True)
    )

    # Left arrow.
    elements.append(
        lshapes.get_line(coords_str_bot_r, coords_end_bot_r, offset, True)
    )

    # Label.
    label = "to"
    elements.append(lshapes.get_text(label, position_bot, offset))

    return "\n".join(elements)


# ------------------------------------------------------------------------------
# 'image' Functions
# ------------------------------------------------------------------------------


def image(settings: dict, offset: tuple) -> str:
    """
        Gets the image for the spin flip, with the given settings.

        :param settings: The settings dictionary for the image.

        :param offset: The offset of the box.

        :return: The text for the spin flip model.
    """
    # Auxiliary variables.
    strings = []

    # Validate the configuration settings.
    validate(settings)

    # Configuration strings.
    dimensionality = settings["dimensionality"]
    strings.append(get_boxes(dimensionality, offset))

    # The labels.
    label = settings["label"]
    strings.append(get_labels(label, offset))

    # The grid with the spins.
    nspins = settings["nspins"]
    spins_down = settings["particle"]["spins_down"]
    string, coordinates, height, separat = get_grid(nspins, spins_down, offset)
    strings.append(string)

    # # The ellipses over the ticks.
    ellipses = settings["particle"]["ellipses"]
    strings.append(get_ellipses(coordinates, ellipses, height, separat, offset))

    # The general elements.
    strings.append(get_other(height, offset))

    return "\n".join(strings)


# ------------------------------------------------------------------------------
# 'validate' Functions
# ------------------------------------------------------------------------------


def validate(parameters: dict) -> None:
    """
        Validates that the different parameters in the configuration file are
        correct, or represent a valid state of the system.

        :param parameters: The dictionary with the parameters.
    """
    # Auxiliary variables.
    nspins = parameters["nspins"]
    ellipses = parameters["particle"]["ellipses"]
    spins_down = parameters["particle"]["spins_down"]

    # Validate the different parameters.
    validate_spins(nspins)
    validate_ellipses(ellipses, nspins)
    validate_spins_down(spins_down, nspins)


def validate_ellipses(ellipses: Any, spins_number: Any) -> None:
    """
        Validates the spins that are down are integers and are in a valid range.

        :param ellipses: The list of the sites around which the elipses will be
         drawn.

        :param spins_number: The number of spin particles that the grid will
         have.

        :raise TypeError: If the are non-integer values in of spins.

        :raise ValueError: If there are numbers outside the valid range.
    """
    # Validate its a list or tuple.
    if not isinstance(ellipses, (list, tuple)):
        raise TypeError(
            f"The spins down must be a list or tuple, not {type(ellipses)}."
        )

    # No need to check if there are no spin downs.
    if len(ellipses) == 0:
        return

    # Validate the type.
    if not all(isinstance(x, int) for x in ellipses):
        raise TypeError(
            f"The ellipses must be a list of integers, not "
            f"{type(ellipses)}."
        )

    # Spin down must be a list of unique values.
    if len(set(ellipses)) != len(ellipses):
        raise ValueError(
            f"The ellipses must be a list of unique values, not "
            f"{ellipses}."
        )

    # All numbers must be in the valid range.
    if not all(x in range(spins_number) for x in ellipses):
        raise ValueError(
            f"The ellipses must be in the range [0, {spins_number}), not "
            f"{ellipses}."
        )


def validate_spins(spins_number: Any) -> None:
    """
        Validates the number of spins is an integer number greater than zero.

        :param spins_number: The number of spins that the grid will have.

        :raise TypeError: If the number of spins is not an integer.

        :raise ValueError: If the number of spins is not greater than zero.
    """
    # Validate the type.
    if not isinstance(spins_number, int):
        raise TypeError(
            f"The number of ticks must be an integer, not {type(spins_number)}."
        )

    # Validate the value.
    if spins_number <= 0:
        raise ValueError(
            f"The number of ticks must be greater than zero, not "
            f"{spins_number}."
        )


def validate_spins_down(spins_down: Any, spins_number: Any) -> None:
    """
        Validates the spins that are down are integers and are in a valid range.

        :param spins_down: The list of spins that must be down.

        :param spins_number: The number of spin particles that the grid will
         have.

        :raise TypeError: If the are non-integer values in of spins.

        :raise ValueError: If there are numbers outside the valid range.
    """
    # Validate it is a list or tuple.
    if not isinstance(spins_down, (list, tuple)):
        raise TypeError(
            f"The spins down must be a list or tuple, not {type(spins_down)}."
        )

    # No need to check if there are no spin downs.
    if len(spins_down) == 0:
        return

    # Validate the type.
    if not all(isinstance(x, int) for x in spins_down):
        raise TypeError(
            f"The spins down must be a list of integers, not "
            f"{type(spins_down)}."
        )

    # All numbers must be in the valid range.
    if not all(x in range(spins_number) for x in spins_down):
        raise ValueError(
            f"The spins down must be in the range [0, {spins_number}), not "
            f"{spins_down}."
        )
