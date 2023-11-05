"""
    Generates the code for the RSA dimers box in the grid.
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


def get_adsorbing(
    coordinates: tuple, adsorbing: Union[list, tuple], offset: tuple
) -> str:
    """
        Gets the arrows for the desorbing circles for the image.

        :param coordinates: The coordinates of ALL the ticks.

        :param adsorbing: The indexes of the adsorbing particles.

        :param offset: The offset of the circles.

        :return: The text for the arrows.
    """
    # No need to do anything if there are no particles that are desorbing.
    if len(adsorbing) == 0:
        return ""

    # Auxiliary variables.
    boxes = ["% Adsorbing Particles"]

    # Parameters.
    radius = cboxes.CIRCLE_RADIUS * 0.8
    separation = cboxes.SEPARATION_VERTICAL

    # y-positions.
    y_str_line = 2 * (separation + radius)
    y_end_line = y_str_line + separation + cboxes.ARROW_LENGTH
    y_pos_circle = y_end_line + separation + radius

    # Function aliases.
    func_circle = lshapes.get_circle
    func_line = lshapes.get_line

    # Get the circles of the fixed particles.
    for i in adsorbing:
        # Get the corresponding coordinate.
        coordinate_0 = coordinates[i]
        coordinate_1 = coordinates[i + 1]

        # Set the circle position.
        pos_arrow_str = coordinate_0[0], coordinate_0[1] + y_end_line
        pos_arrow_end = coordinate_0[0], coordinate_0[1] + y_str_line
        circle_0 = coordinate_0[0], coordinate_0[1] + y_pos_circle

        # Get the arrow.
        if i not in {3, 10}:
            fig = func_line(pos_arrow_str, pos_arrow_end, offset, True)
            boxes.append(fig)

        # Get the circle.
        fig = func_circle(circle_0, radius, offset, True)
        boxes.append(fig)

        # Set the circle position.
        pos_arrow_str = coordinate_1[0], coordinate_1[1] + y_end_line
        pos_arrow_end = coordinate_1[0], coordinate_1[1] + y_str_line
        circle_1 = coordinate_1[0], coordinate_1[1] + y_pos_circle

        # Get the arrow.
        if i not in {3, 10}:
            fig = func_line(pos_arrow_str, pos_arrow_end, offset, True)
            boxes.append(fig)

        # Get the circle.
        fig = func_circle(circle_1, radius, offset, True)
        boxes.append(fig)

        # Line joining the dimer.
        fig = func_line(circle_0, circle_1, offset)
        boxes.append(fig)

        if i in {3, 10}:
            pos_avg = tuple((x + y) * .5 for x, y in zip(circle_0, circle_1))
            pos_1 = tuple(x - 0.7 * cboxes.ARROW_LENGTH for x in pos_avg)
            pos_2 = tuple(x + 0.7 * cboxes.ARROW_LENGTH for x in pos_avg)
            fig = func_line(pos_1, pos_2, offset)
            boxes.append(fig)
            continue

    return "\n".join(boxes)


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


def get_fixed(
    coordinates: tuple, fixed: Union[list, tuple], offset: tuple
) -> str:
    """
        Gets the circles for the image.

        :param coordinates: The coordinates of ALL the ticks.

        :param fixed: The indexes of the fixed particles.

        :param offset: The offset of the circles.

        :return: The text for the circles.
    """
    # No need to do anything if there are no fixed particles.
    if len(fixed) == 0:
        return ""

    # Auxiliary variables.
    boxes = ["% Fixed Particles"]

    # Parameters.
    radius = cboxes.CIRCLE_RADIUS * 0.8
    separation = cboxes.SEPARATION_VERTICAL
    spacing = radius + separation

    # Get the circles of the fixed particles.
    for i in fixed:
        # Get the corresponding coordinate.
        coordinate_0 = coordinates[i]
        coordinate_1 = coordinates[i + 1]

        # Set the circle position.
        position_0 = coordinate_0[0], coordinate_0[1] + spacing
        position_1 = coordinate_1[0], coordinate_1[1] + spacing

        boxes.append(lshapes.get_circle(position_0, radius, offset, True))
        boxes.append(lshapes.get_circle(position_1, radius, offset, True))

        # Set the line position.
        boxes.append(lshapes.get_line(position_0, position_1, offset))

    return "\n".join(boxes)


def get_grid(nticks: int, offset: tuple) -> tuple:
    """
        Gets the grid ticks for the image.

        :param nticks: The number of ticks in the grid.

        :param offset: The offset of the grid. Must be a tuple of two elements.

        :return: The grid ticks for the image and the final coordinates of the
         ticks on the grid.
    """
    # Auxiliary variables.
    boxes = ["% Ticks Grid"]

    # Lattice Position.
    position_str = cboxes.LATTICE_POSITION_TICKS
    position_end = position_str[0] + cboxes.LENGTH_LATTICE, position_str[1]

    # Basic grid configuration.
    configuration = {
        "positions": (position_str, position_end),
        "nticks": nticks,
        "ticks_height": cboxes.TICK_HEIGHT,
        "x_offsets": tuple(cboxes.BOX_MARGIN * 0.5 for _ in range(2)),
        "y_offsets": (0, 0),
    }

    # Set the grid components.
    grid = gshapes.get_tick_grid(configuration, offset)
    boxes.append(grid[0])

    return "\n".join(boxes), grid[1]


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


# ------------------------------------------------------------------------------
# 'image' Functions
# ------------------------------------------------------------------------------


def image(settings: dict, offset: tuple) -> str:
    """
        Gets the adsorption-desorption image, with the given offset.

        :param settings: The dictionary with the settings for the image.

        :param offset: The offset of the box.

        :return: The text for the adsorption-desorption system.
    """
    # Auxiliary variables.
    strings = []

    # Validate the configuration settings.
    validate(settings)

    # # Configuration strings.
    dimensionality = settings["dimensionality"]
    strings.append(get_boxes(dimensionality, offset))

    # The main labels.
    label = settings["label"]
    strings.append(get_labels(label, offset))

    # The grid with the ticks.
    nticks = settings["nticks"]
    string, coordinates = get_grid(nticks, offset)
    strings.append(string)

    # Get the fixed particles.
    fixed = settings["particle"]["fixed"]
    string = get_fixed(coordinates, fixed, offset)
    strings.append(string)

    # Set the adsorbing circles and arrows.
    adsorbing = settings["particle"]["adsorbing"]
    string = get_adsorbing(coordinates, adsorbing, offset)
    strings.append(string)

    return "\n".join(strings)


# ------------------------------------------------------------------------------
# 'validate' Functions
# ------------------------------------------------------------------------------


def validate(parameters: dict) -> None:
    """
        Validates that the different parameters in the configuration file are
        correct, or represent a valid state of the system.

        :param parameters: The dictionary with the system parameters.
    """
    # Auxiliary variables.
    nticks = parameters["nticks"]
    adsorbing = parameters["particle"]["adsorbing"]
    fixed = parameters["particle"]["fixed"]

    # Validate the different parameters.
    validate_ticks(nticks)
    validate_particles_adsorbing(adsorbing, nticks)
    validate_particles_fixed(fixed, nticks)


def validate_particles_adsorbing(particles: Any, tick_number: Any) -> None:
    """
        Validates the particles is a list whose values are integers and are in
        a valid range.

        :param particles: The list of particles.

        :param tick_number: The number of ticks that the grid will have.

        :raise TypeError: If there are non-integer values in the particle list.

        :raise ValueError: If there are numbers outside the valid range.
    """
    # Validate that the adsorbing variable is a list or a tuple.
    if not isinstance(particles, (list, tuple)):
        raise TypeError(
            f"The adsorbing variable must be a list or a tuple, not "
            f"{type(particles)}."
        )

    # No need to check if there are particles.
    if len(particles) == 0:
        return

    # Validate the type.
    if not all(isinstance(x, int) for x in particles):
        raise TypeError(
            f"There are non-integer values in the particle list, {particles}. "
            f"Makes sure all the values are integers."
        )

    # Validate the values.
    if not all(x in range(tick_number) for x in particles):
        raise ValueError(
            f"There are site numbers outside the valid range, {particles}. "
            f"Makes sure all the values are in the range [0, {tick_number})."
        )

    # Validate that the values are unique.
    if len(particles) != len(set(particles)):
        # Get the repeated values.
        repeated = set(x for x in particles if particles.count(x) > 1)

        raise ValueError(
            f"There are repeated values in the adsorbing particles. "
            f"Repeated values: {repeated}."
        )


def validate_particles_fixed(particles: Any, tick_number: Any) -> None:
    """
        Validates the particles is a list whose values are integers and are in
        a valid range.

        :param particles: The list of particles.

        :param tick_number: The number of ticks that the grid will have.

        :raise TypeError: If there are non-integer values in the particle list.

        :raise ValueError: If there are numbers outside the valid range.
    """
    # Validate that the fixed variable is a list or a tuple.
    if not isinstance(particles, (list, tuple)):
        raise TypeError(
            f"The particles variable must be a list or a tuple, not "
            f"{type(particles)}."
        )

    # No need to check if there are particles.
    if len(particles) == 0:
        return

    # Validate the type.
    if not all(isinstance(x, int) for x in particles):
        raise TypeError(
            f"There are non-integer values in the particle list, {particles}. "
            f"Makes sure all the values are integers."
        )

    # Validate the values.
    if not all(x in range(tick_number) for x in particles):
        raise ValueError(
            f"There are site numbers outside the valid range, {particles}. "
            f"Makes sure all the values are in the range [0, {tick_number})."
        )

    # Validate that the values are unique.
    if len(particles) != len(set(particles)):
        # Get the repeated values.
        repeated = set(x for x in particles if particles.count(x) > 1)

        # Raise the error.
        raise ValueError(
            f"There are repeated values in the fixed particles. "
            f"Repeated values: {repeated}."
        )


def validate_ticks(tick_number: Any) -> None:
    """
        Validates the number of ticks is an integer number greater than zero.

        :param tick_number: The number of ticks that the grid will have.

        :raise TypeError: If the number of ticks is not an integer.

        :raise ValueError: If the number of ticks is not greater than zero.
    """
    # Validate the type.
    if not isinstance(tick_number, int):
        raise TypeError(
            f"The number of ticks must be an integer, not {type(tick_number)}."
        )

    # Validate the value.
    if tick_number <= 0:
        raise ValueError(
            f"The number of ticks must be greater than zero, not {tick_number}."
        )
