"""
    Generates the code for the splin exchange box in the grid.
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


def get_spin_boxes(
    coordinates: Union[list, tuple], boxes: Union[list, tuple],
    height: float, separation: float, offset: tuple
) -> str:
    """
        Gets the spin images for the image.

        :param coordinates: The coordinates of the spin ticks, such that they
         are in the middle of the arrow.

        :param boxes: The list of 

        :param height: The height of the spin arrows.

        :param separation: The separation between the ticks.

        :param offset: The offset of the elipses.

        :return: The text for the elipses.
    """
    # Auxiliary variables.
    fboxes = ["% Ellipses"]

    # No need to draw if there are no ellipses.
    if len(boxes) == 0:
        return ""

    # Auxiliary variables.
    xaxis = separation / 2
    yaxis = height * 1.15 / 2

    # Get all the bounding images.
    for index_0, index_1 in boxes:
        # Sort the indexes.
        index_0, index_1 = [func(index_0, index_1) for func in (min, max)]

        # Coordinates.
        coordinate_0 = coordinates[index_0]
        coordinate_1 = coordinates[index_1]

        # Top and bottom coordinates.
        top_left = coordinate_0[0] - xaxis, coordinate_0[1] + yaxis
        bottom_right = coordinate_1[0] + xaxis, coordinate_1[1] - yaxis

        # Get the bounding box.
        fboxes.append(lshapes.get_rectangle(top_left, bottom_right, offset))

    return "\n".join(fboxes)


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
    separation = cboxes.SEPARATION_HORIZONTAL * 3

    # Top coordinates.
    coords_str_top_lr = x_str, y_top
    coords_end_top_lr = x_str, y_top + aheight

    coords_str_top_ll = x_str - separation, y_top
    coords_end_top_ll = x_str - separation, y_top + aheight

    coords_str_top_rl = x_end, y_top
    coords_end_top_rl = x_end, y_top + aheight

    coords_str_top_rr = x_end + separation, y_top
    coords_end_top_rr = x_end + separation, y_top + aheight

    x_position_top = (coords_str_top_lr[0] + coords_str_top_rl[0]) / 2
    y_position_top = (coords_str_top_rl[1] + coords_end_top_rl[1]) / 2
    position_top = x_position_top, y_position_top

    # Bottom coordinates.
    coords_str_bot_lr = x_str, y_bot
    coords_end_bot_lr = x_str, y_bot + aheight

    coords_str_bot_ll = x_str - separation, y_bot
    coords_end_bot_ll = x_str - separation, y_bot + aheight

    coords_str_bot_rl = x_end, y_bot
    coords_end_bot_rl = x_end, y_bot + aheight

    coords_str_bot_rr = x_end + separation, y_bot
    coords_end_bot_rr = x_end + separation, y_bot + aheight

    x_position_bot = (coords_str_bot_lr[0] + coords_str_bot_rl[0]) / 2
    y_position_bot = (coords_str_bot_rl[1] + coords_end_bot_rl[1]) / 2
    position_bot = x_position_bot, y_position_bot

    # ------------------------------------------------------------------------ #
    #                                Upper Image                               #
    # ------------------------------------------------------------------------ #

    # Right arrow.
    elements.append(
        lshapes.get_line(coords_str_top_ll, coords_end_top_ll, offset, True)
    )
    elements.append(
        lshapes.get_line(coords_end_top_lr, coords_str_top_lr, offset, True)
    )

    # Left arrow.
    elements.append(
        lshapes.get_line(coords_end_top_rl, coords_str_top_rl, offset, True)
    )
    elements.append(
        lshapes.get_line(coords_str_top_rr, coords_end_top_rr, offset, True)
    )

    # Label.
    label = "to"
    elements.append(lshapes.get_text(label, position_top, offset))

    # ------------------------------------------------------------------------ #
    #                                Lower Image                               #
    # ------------------------------------------------------------------------ #

    # Right arrow.
    elements.append(
        lshapes.get_line(coords_end_bot_ll, coords_str_bot_ll, offset, True)
    )
    elements.append(
        lshapes.get_line(coords_str_bot_lr, coords_end_bot_lr, offset, True)
    )

    # Left arrow.
    elements.append(
        lshapes.get_line(coords_str_bot_rl, coords_end_bot_rl, offset, True)
    )
    elements.append(
        lshapes.get_line(coords_end_bot_rr, coords_str_bot_rr, offset, True)
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

    # The ellipses over the ticks.
    sboxes = settings["particle"]["images"]
    strings.append(get_spin_boxes(coordinates, sboxes, height, separat, offset))

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
    boxes = parameters["particle"]["images"]
    spins_down = parameters["particle"]["spins_down"]

    # Validate the different parameters.
    validate_spins(nspins)
    validate_boxes(boxes, nspins)
    validate_spins_down(spins_down, nspins)


def validate_boxes(boxes: Any, spins_number: Any) -> None:
    """
        Validates images are properly set. That is, the images is a list of lists
        of length 2. The lists must contain the sites around which the box will
        be drawn, such that the ticks must be adjacent to each general.

        :param boxes: The list of lists that contains the images.

        :param spins_number: The number of spin particles that the grid will
         have.

        :raise TypeError: If the are non-integer values in of spins.

        :raise ValueError: If there are numbers outside the valid range.
    """
    # Validate its a list or tuple.
    if not isinstance(boxes, (list, tuple)):
        raise TypeError(
            f"The images object must be a list or a tuple, not {type(boxes)}."
        )

    # Validate the sublists.
    for i, box in enumerate(boxes):
        # Check the box is a list or a tuple.
        if not isinstance(box, (list, tuple)):
            raise TypeError(
                f"The {i}th element of the list of images must be a list or a "
                f"tuple, not a {type(box)}."
            )

        # Check the numbers are integers valid integers.
        if len(box) != 2:
            raise TypeError(
                f"The box must have, exactly two elements. Current number of "
                f"elements: {len(box)}."
            )

        # Check the numbers are integers valid integers.
        if not all(isinstance(x, int) for x in box):
            raise TypeError(
                f"The elements in the list of sites are not integers. Types: "
                f"{tuple(type(x) for x in box)}."
            )

        # Check the box contains sites within the range.
        if not all(x in range(spins_number) for x in box):
            raise ValueError(
                f"One number, or more, in the {i} box are out of range. They "
                f"must be in the range [0, {spins_number}). Numbers: {box}."
            )

        # Check the box contains adjacent numbers.
        if not any(box[0] == box[1] + j for j in (1, -1)):
            raise ValueError(
                f"The sites in the box {i} must be adjacent to each general. "
                f"Sites: {box}."
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
