"""
    Generates the code for the clustering box in the grid.
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
    radius = cboxes.CIRCLE_RADIUS * 0.7
    separation = cboxes.SEPARATION_VERTICAL

    # y-positions.
    y_str_line = separation
    y_end_line = y_str_line + cboxes.ARROW_LENGTH
    y_pos_circle = y_end_line + separation + radius

    # Function aliases.
    func_circle = lshapes.get_circle
    func_line = lshapes.get_line

    # Get the circles of the fixed particles.
    for i in adsorbing:
        # Get the corresponding coordinate.
        coordinate = coordinates[i]

        # Set the circle position.
        position_arrow_str = coordinate[0], coordinate[1] + y_end_line
        position_arrow_end = coordinate[0], coordinate[1] + y_str_line
        position_circle = coordinate[0], coordinate[1] + y_pos_circle

        # Get the arrow.
        fig = func_line(position_arrow_str, position_arrow_end, offset, True)
        boxes.append(fig)

        # Get the circle.
        fig = func_circle(position_circle, radius, offset, True)
        boxes.append(fig)

    return "\n".join(boxes)


def get_arrows(coordinates: tuple, jumps: tuple, offset: tuple) -> str:
    """
        Get the jump arrows for the system.

        :param coordinates: The coordinates of the ticks.

        :param jumps: The jumps of the particles.

        :param offset: The offset of the box.

        :return: The bounding box text of the image.
    """
    # Auxiliary variables.
    jnodes = set(x[0] for x in jumps)
    length = len(coordinates) - 1
    nodes = ["% Arrows"]
    nodes_prefix = "clu_par_"

    # Get the nodes.
    for jump in jumps:
        # Add the previous node to the list.
        if jump[0] > 0 and jump[1] != 0:
            jnodes.add(jump[0] - 1)

        # Add the next node to the list.
        if jump[0] < length and jump[2] != 0:
            jnodes.add(jump[0] + 1)

    # Function alias.
    func = lshapes.get_coordinate

    # Sorted nodes and separator.
    jnodes = tuple(sorted(list(jnodes)))
    separator = 2 * (cboxes.SEPARATION_VERTICAL + cboxes.CIRCLE_RADIUS)

    # Get the node strings.
    for node in jnodes:
        # Label of the node.
        nid = f"{nodes_prefix}{node}"

        # Coordinates of the node.
        crd = coordinates[node]
        crd = crd[0], crd[1] + separator

        # Add the node.
        nodes.append(func(crd, nid, offset))

    # Function alias.
    func = lshapes.get_line_curved

    # Get the curved arrows.
    for index, lj, rj in jumps:
        # Index where to start.
        nid_str = f"{nodes_prefix}{index}"

        # If jumping left.
        if lj != 0:
            nid_end = f"{nodes_prefix}{index - 1}"
            nodes.append(func(nid_str, nid_end, outa=90, ina=90))

        # If jumping right.
        if rj != 0:
            nid_end = f"{nodes_prefix}{index + 1}"
            nodes.append(func(nid_str, nid_end, outa=90, ina=90))

    return "\n".join(nodes)


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


def get_desorbing(
    coordinates: tuple, desorbing: Union[list, tuple], offset: tuple
) -> str:
    """
        Gets the arrows for the desorbing circles for the image.

        :param coordinates: The coordinates of ALL the ticks.

        :param desorbing: The indexes of the desorbing particles.

        :param offset: The offset of the circles.

        :return: The text for the arrows.
    """
    # No need to do anything if there are no particles that are desorbing.
    if len(desorbing) == 0:
        return ""

    # Auxiliary variables.
    boxes = ["% Fixed Particles"]

    # Parameters.
    radius = cboxes.CIRCLE_RADIUS
    separation = cboxes.SEPARATION_VERTICAL
    y_init = 2 * (radius + separation)
    y_fina = y_init + cboxes.ARROW_LENGTH

    # Get the circles of the fixed particles.
    for i in desorbing:
        # Get the corresponding coordinate.
        coordinate = coordinates[i]

        # Set the circle position.
        position_str = coordinate[0], coordinate[1] + y_init
        position_end = coordinate[0], coordinate[1] + y_fina
        boxes.append(lshapes.get_line(position_str, position_end, offset, True))

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
    radius = cboxes.CIRCLE_RADIUS * 0.7
    separation = cboxes.SEPARATION_VERTICAL
    spacing = radius + separation

    # Get the circles of the fixed particles.
    for i in fixed:
        # Get the corresponding coordinate.
        coordinate = coordinates[i]

        # Set the circle position.
        position = coordinate[0], coordinate[1] + spacing
        boxes.append(lshapes.get_circle(position, radius, offset, True))

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
    tpos = cboxes.LATTICE_POSITION_TICKS
    position_str = tpos[0], tpos[1] * 1.8
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

    # --------------------------------------------------------------------------
    # Other labels
    # --------------------------------------------------------------------------

    # Diagram labels.
    new_line = "\\" + "\\"
    text_size = "\\tiny{\\shortstack{"
    text_size_1 = "\\tiny{"

    # Desorption difficulty.
    label = text_size + f"Irreversible{new_line}nucleation" + "}}"
    position = cboxes.BOX_WIDTH * 0.30, -cboxes.BOX_HEIGHT * 0.5
    boxes.append(lshapes.get_text(label, position, offset))

    label = text_size + f"Irreversible{new_line}aggregation" + "}}"
    position = cboxes.BOX_WIDTH * 0.80, -cboxes.BOX_HEIGHT * 0.5
    boxes.append(lshapes.get_text(label, position, offset))

    label = text_size_1 + f"$h$" + "}"
    position = cboxes.BOX_WIDTH * 0.625, -cboxes.BOX_HEIGHT * 0.58
    boxes.append(lshapes.get_text(label, position, offset))

    label = text_size_1 + f"$P$" + "}"
    position = cboxes.BOX_WIDTH * 0.56, -cboxes.BOX_HEIGHT * 0.70
    boxes.append(lshapes.get_text(label, position, offset))

    label = text_size_1 + f"$h$" + "}"
    position = cboxes.BOX_WIDTH * 0.28, -cboxes.BOX_HEIGHT * 0.58
    boxes.append(lshapes.get_text(label, position, offset))

    label = text_size_1 + f"$P$" + "}"
    position = cboxes.BOX_WIDTH * 0.125, -cboxes.BOX_HEIGHT * 0.70
    boxes.append(lshapes.get_text(label, position, offset))

    return "\n".join(boxes)


def get_other(coordinates: tuple, offset: tuple) -> str:
    """
        Gets general elements for the image.

        :param coordinates: The coordinates of ALL the ticks.

        :param offset: The offset of the labels.

        :return: The text for the general elements.
    """
    # Auxliary variables.
    boxes = ["% Other elements"]

    # --------------------------------------------------------------------------
    # Lines joinining.
    # --------------------------------------------------------------------------

    # Extra offsets.
    t_offset = 0, cboxes.SEPARATION_VERTICAL + cboxes.CIRCLE_RADIUS * 0.7

    start_coord = tuple(x + y for x, y in zip(coordinates[-4], t_offset))
    end_coord = tuple(x + y for x, y in zip(coordinates[-1], t_offset))

    # Parameters.
    boxes.append(lshapes.get_line(start_coord, end_coord, offset))

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
    # Auxiliary varaibles.
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

    # Get the jumping arrows.
    jumps = settings["particle"]["jumps"]
    strings.append(get_arrows(coordinates, jumps, offset))

    # The general elements.
    strings.append(get_other(coordinates, offset))

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
    jumps = parameters["particle"]["jumps"]

    # Validate the different parameters.
    validate_ticks(nticks)
    validate_particles_adsorbing(adsorbing, nticks)
    validate_particles_jumps(jumps, fixed, nticks)
    validate_particles_fixed(fixed, nticks)


def validate_particles_jumps(
    particles: Any, fixed: Any, tick_number: Any
) -> None:
    """
        Validates the particles is a list whose values are list of integers and
        are in a valid range.

        :param particles: The list of particles and their jumps.

        :param fixed: The list of fixed particles.

        :param tick_number: The number of ticks that the grid will have.

        :raise TypeError: If the are non-integer values in lists of the list
         of particles.

        :raise ValueError: If there are numbers outside the valid range. If the
          jump lists do not have a valid length. If the values of the jumps are
          not valid. If the particles are jumping to a site that is already
          occupied.
    """
    # Auxiliary variables.
    unique = set()

    # Validate it's a list or a tuple.
    if not isinstance(particles, (list, tuple)):
        raise TypeError(
            f"The particles must be a list or a tuple, not {type(particles)}."
        )

    # No need to check if there are particles.
    if len(particles) == 0:
        return

    # Validate the type.
    if not all(isinstance(x, list) for x in particles):
        tlist = tuple(type(x) for x in particles)

        raise TypeError(
            f"There are non-list values in the particle list, {tlist}."
        )

    # Last site.
    ls = tick_number - 1

    # Validate the types in the list.
    for i, slist in enumerate(particles):
        # Length of the list must be three.
        if len(slist) != 3:
            raise ValueError(
                f"The particle list at index {i} does not have three elements."
            )

        # All elements must be integers greater than or equal to zero.
        if not all(isinstance(x, int) for x in slist):
            raise TypeError(
                f"The particle list at index {i} has a non-integer value: "
                f" {slist}."
            )

        # Check for uniquenes.
        if slist[0] in unique:
            plist = tuple(x[0] for x in particles)
            raise ValueError(
                f"There are repeated particles: {plist}."
            )
        unique.add(slist[0])

        # All elements must be greater than or equal to zero.
        if not all(x >= 0 for x in slist):
            raise ValueError(
                f"The particle list at index {i} has a negative value: "
                f" {slist}."
            )

        # The first element of each list must be in the valid range.
        if slist[0] not in range(tick_number):
            raise ValueError(
                f"The particle list at index {i} has a value outside the valid "
                f"range: {slist}."
            )

        # If all the jumps are zero, they should NOT be in the list.
        if all(x == 0 for x in slist[1:]):
            raise ValueError(
                f"The particle list at index {i} has both jumps as zero. This "
                f"cannot happen: {slist}."
            )

        # Particles in extremes cannot diffuse out.
        if slist[0] == 0 and slist[1] > 0 or slist[0] == ls and slist[2] > 0:
            raise ValueError(
                f"The particle at the extreme cannot jump out. Site: "
                f"{slist[0]}, jumps: {slist}."
            )

        # Particles cannot diffuse to non-empty sites.
        if slist[0] > 0 and slist[1] > 0 and (slist[0] - 1) in fixed:
            raise ValueError(
                f"The particle cannot jump left to a non-empty site. Site: "
                f"{slist[0]}, jumps: {slist}, fixed sites: {fixed}."
            )

        # Particles cannot diffuse to non-empty sites.
        if slist[0] < ls and slist[2] > 0 and (slist[0] + 1) in fixed:
            raise ValueError(
                f"The particle cannot jump right to a non-empty site. Site: "
                f"{slist[0]}, jumps: {slist}, fixed sites: {fixed}."
            )


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
