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
    coordinates: tuple, adsorbing: Union[list, tuple], offset: tuple,
    top: bool = False
) -> str:
    """
        Gets the arrows for the desorbing circles for the image.

        :param coordinates: The coordinates of ALL the ticks.

        :param adsorbing: The indexes of the adsorbing particles.

        :param offset: The offset of the circles.

        :param top: If the request is for the top.

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

    # Function aliases.
    func_circle = lshapes.get_circle
    func_line = lshapes.get_line

    # Get the circles of the fixed particles.
    for i in adsorbing:
        # Get the corresponding coordinate.
        coordinate = coordinates[i]

        # y-positions.
        circle = coordinate[0], coordinate[1] + 3.5 * radius + separation
        arrow_str = circle[0], circle[1] - radius - separation
        arrow_end = circle[0], coordinate[1] + separation

        # Get the arrow.
        fig = func_line(arrow_str, arrow_end, offset, True)
        boxes.append(fig)

        # Get the circle.
        fig = func_circle(circle, radius, offset, True)
        boxes.append(fig)

        if top:
            continue

        y_avg = (arrow_str[1] + arrow_end[1])  / 2
        pos_str = arrow_str[0] - cboxes.SEPARATION_HORIZONTAL, y_avg + cboxes.SEPARATION_VERTICAL
        pos_end = arrow_str[0] + cboxes.SEPARATION_HORIZONTAL, y_avg - cboxes.SEPARATION_VERTICAL
        fig = func_line(pos_str, pos_end, offset)
        boxes.append(fig)

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
        coordinate = coordinates[i]

        # Set the circle position.
        position = coordinate[0], coordinate[1] + spacing

        boxes.append(lshapes.get_circle(position, radius, offset, True))
        boxes.append(lshapes.get_circle(position, radius, offset, True))

    return "\n".join(boxes)


def get_grid_main(nticks: int, offset: tuple) -> tuple:
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
    position = cboxes.LATTICE_POSITION_TICKS[0], -cboxes.BOX_HEIGHT * 0.5
    position_str = position[0], position[1]
    position_end = position_str[0] + cboxes.LENGTH_LATTICE * .425, position_str[1]

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


def get_grid_other(name: str, nticks: int, offset: tuple) -> tuple:
    """
        Gets the grid ticks for the image.

        :param name: The name of the grid.

        :param nticks: The number of ticks in the grid.

        :param offset: The offset of the grid. Must be a tuple of two elements.

        :return: The grid ticks for the image and the final coordinates of the
         ticks on the grid.
    """
    # Auxiliary variables.
    boxes = [f"% Ticks Grid - {name}"]
    pos_factor = {
        "top": 0.2,
        "top_bottom": 0.4,
        "bottom_top": 0.6,
        "bottom": 0.8,
    }

    # Position factor.
    factor = pos_factor[name]

    # Lattice Position.
    position = cboxes.LATTICE_POSITION_TICKS[0], -cboxes.BOX_HEIGHT * factor
    position_str = position[0] + cboxes.LENGTH_LATTICE * .6, position[1]
    position_end = position_str[0] + cboxes.LENGTH_LATTICE * .4, position_str[1]

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

    # Configuration strings.
    dimensionality = settings["dimensionality"]
    strings.append(get_boxes(dimensionality, offset))

    # The main labels.
    label = settings["label"]
    strings.append(get_labels(label, offset))
    #
    # The grid with the ticks.
    nticks = settings["grid"]["main"]["nticks"]
    string, coordinates = get_grid_main(nticks, offset)
    strings.append(string)
    #
    # Get the fixed particles.
    fixed = settings["grid"]["main"]["fixed"]
    string = get_fixed(coordinates, fixed, offset)
    strings.append(string)

    for grid_name, values in settings["grid"].items():
        # No need to checkout this grid.
        if grid_name == "main":
            continue

        nticks = values["nticks"]
        string, coordinates = get_grid_other(grid_name, nticks, offset)
        strings.append(string)

        fixed = values["fixed"]
        string = get_fixed(coordinates, fixed, offset)
        strings.append(string)

        adsorbing = values["adsorbing"]
        string = get_adsorbing(
            coordinates, adsorbing, offset, grid_name == "top"
        )
        strings.append(string)

    #
    # # Set the adsorbing circles and arrows.
    # adsorbing = settings["particle"]["adsorbing"]
    # string = get_adsorbing(coordinates, adsorbing, offset)
    # strings.append(string)

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
    for value in parameters["grid"].values():
        nticks = value["nticks"]
        adsorbing = value["adsorbing"]
        fixed = value["fixed"]

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
