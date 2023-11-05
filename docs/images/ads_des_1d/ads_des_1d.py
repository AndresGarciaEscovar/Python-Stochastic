"""
    Generates the code for the adsorption - desorption box in the grid.
"""


# ##############################################################################
# Importsf
# ##############################################################################


# General
from typing import Any, Union

# User defined.
import docs.configurations.configuration_boxes as cboxes
import docs.general.other_general as ogen
import docs.shapes.shapes_latex as lshapes
import docs.shapes.shapes_lattice_ticks_1d as gshapes


# ##############################################################################
# Private Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# '_get' Functions
# ------------------------------------------------------------------------------


def _get_box(offset: tuple) -> str:
    """
        Get the main bounding box.

        :param offset: The offset of the box.

        :return: The bounding box text.
    """
    # Auxiliary variables
    strings = ["% Boxes"]

    # Main box.
    rect_pos_bot_r = cboxes.BOX_POSITION_BOTTOM
    rect_pos_top_l = cboxes.BOX_POSITION_TOP

    # Get the rectangles.
    fig = lshapes.get_rectangle(rect_pos_top_l, rect_pos_bot_r, offset)
    strings.append(fig)

    return "\n".join(strings)


def _get_grid(settings: dict, offset: tuple) -> str:
    """
        Gets the grid ticks for the image.

        :param settings: The settings dictionary with the grid information.

        :param offset: The offset of the grid. Must be a tuple of two elements.

        :return: The grid for the image.
    """
    # Auxiliary variables.
    strings = []

    # --------------------------------------------------------------------------
    # Other quantities.
    # --------------------------------------------------------------------------

    # Base values.
    box_height = cboxes.BOX_POSITION_BOTTOM[1]
    box_width = cboxes.BOX_POSITION_BOTTOM[0]

    # Start position.
    x_pos_str = cboxes.SEPARATION_HORIZONTAL
    y_pos_str = box_height * 0.4
    pos_str = x_pos_str, y_pos_str

    # End position.
    x_pos_end = box_width - cboxes.SEPARATION_HORIZONTAL
    y_pos_end = y_pos_str
    pos_end = x_pos_end, y_pos_end

    # Offsets.
    x_offsets = cboxes.SEPARATION_HORIZONTAL, -cboxes.SEPARATION_HORIZONTAL

    # --------------------------------------------------------------------------
    # Setup the dictionaries.
    # --------------------------------------------------------------------------

    # Specific grid settings.
    tsettings = {
        "nticks": settings["nticks"],
        "adsorbing": settings["particles"]["adsorbing"],
        "desorbing": settings["particles"]["desorbing"],
        "fixed": settings["particles"]["fixed"],
        "position_end": pos_end,
        "position_start": pos_str,
        "offsets_x": x_offsets,
    }

    # Get the grid.
    strings.append(gshapes.get_grid(tsettings, offset))

    return "\n".join(strings)


def _get_labels(label: str, offset: tuple) -> str:
    """
        Gets the labels for the image.

        :param label: The label of the box.

        :param offset: The offset of the labels.

        :return: The text for the labels.
    """
    # Auxiliary variables.
    strings = ["% Labels"]

    # --------------------------------------------------------------------------
    # Main label.
    # --------------------------------------------------------------------------

    pos_label_x = cboxes.BOX_POSITION_BOTTOM[0] * 0.5
    pos_label_y = cboxes.BOX_POSITION_BOTTOM[1] * 0.9
    pos_label = pos_label_x, pos_label_y

    fig = lshapes.get_text(label, pos_label, offset)
    strings.append(fig)

    # --------------------------------------------------------------------------
    # Other labels.
    # --------------------------------------------------------------------------

    # Easy label.
    tlabel = ogen.set_font_size("Easy", "footnotesize")
    pos_label_x = cboxes.BOX_POSITION_BOTTOM[0] * 0.1
    pos_label_y = cboxes.BOX_POSITION_BOTTOM[1] * 0.1
    pos_label = pos_label_x, pos_label_y

    fig = lshapes.get_text(tlabel, pos_label, offset)
    strings.append(fig)

    # Moderate label.
    tlabel = ogen.set_font_size("Moderate", "footnotesize")
    pos_label_x = cboxes.BOX_POSITION_BOTTOM[0] * 0.50
    pos_label_y = cboxes.BOX_POSITION_BOTTOM[1] * 0.1
    pos_label = pos_label_x, pos_label_y

    fig = lshapes.get_text(tlabel, pos_label, offset)
    strings.append(fig)

    # Hard label.
    tlabel = ogen.set_font_size("Hard", "footnotesize")
    pos_label_x = cboxes.BOX_POSITION_BOTTOM[0] * 0.765
    pos_label_y = cboxes.BOX_POSITION_BOTTOM[1] * 0.1
    pos_label = pos_label_x, pos_label_y

    fig = lshapes.get_text(tlabel, pos_label, offset)
    strings.append(fig)

    # P probability.
    tlabel = ogen.set_font_size("P", "footnotesize")
    pos_label_x = cboxes.BOX_POSITION_BOTTOM[0] * 0.365
    pos_label_y = cboxes.BOX_POSITION_BOTTOM[1] * 0.30
    pos_label = pos_label_x, pos_label_y

    fig = lshapes.get_text(tlabel, pos_label, offset)
    strings.append(fig)


    return "\n".join(strings)


def _get_other(settings: dict, offset: tuple) -> str:
    """
        Gets general elements for the image.

        :param settings: The settings dictionary with the grid information.

        :param offset: The offset of the labels.

        :return: The text for the general elements.
    """
    # Auxiliary variables.
    strings = ["% Other elements"]

    # Base values.
    box_height = cboxes.BOX_POSITION_BOTTOM[1]
    box_width = cboxes.BOX_POSITION_BOTTOM[0]

    # --------------------------------------------------------------------------
    # Adsorption Tick
    # --------------------------------------------------------------------------

    # Start position.
    pos_str_a_x = box_width * 0.25
    pos_str_a_y = box_height * 0.8
    pos_str_a = pos_str_a_x, pos_str_a_y

    # End position.
    pos_end_a_x = pos_str_a_x + cboxes.TICK_LENGTH
    pos_end_a_y = pos_str_a_y
    pos_end_a = pos_end_a_x, pos_end_a_y

    # Setup the dictionaries.
    tsettings = {
        "nticks": 1,
        "adsorbing": [0],
        "position_end": pos_end_a,
        "position_start": pos_str_a,
    }

    # Get the grid.
    strings.append(gshapes.get_grid(tsettings, offset))

    # --------------------------------------------------------------------------
    # Desorption Tick
    # --------------------------------------------------------------------------

    # Start position.
    pos_str_d_x = box_width * 0.75
    pos_str_d_y = box_height * 0.8
    pos_str_d = pos_str_d_x, pos_str_d_y

    # End position.
    pos_end_d_x = pos_str_d_x - cboxes.TICK_LENGTH
    pos_end_d_y = pos_str_d_y
    pos_end_d = pos_end_d_x, pos_end_d_y

    # Setup the dictionaries.
    tsettings = {
        "nticks": 1,
        "desorbing": [0],
        "fixed": [0],
        "position_end": pos_end_d,
        "position_start": pos_str_d,
    }

    # Get the grid.
    strings.append(gshapes.get_grid(tsettings, offset))

    # --------------------------------------------------------------------------
    # 'or' label
    # --------------------------------------------------------------------------

    label = ogen.set_font_size("or", "footnotesize")
    const = 2 * (cboxes.SEPARATION_VERTICAL + cboxes.CIRCLE_RADIUS)
    const += cboxes.ARROW_HEIGHT

    pos_label_x = (pos_str_d[0] + pos_str_a[0]) / 2
    pos_label_y = (pos_str_d[1] + pos_str_d[1] + const) / 2
    pos_label = pos_label_x, pos_label_y

    fig = lshapes.get_text(label, pos_label, offset)
    strings.append(fig)

    return "\n".join(strings)


# ------------------------------------------------------------------------------
# '_validate' Functions
# ------------------------------------------------------------------------------


def _validate(configuration: dict) -> None:
    """
        Validates the configuration dictionary for the system specific settings.

        :param configuration: The configuration dictionary.
    """
    # Check that the particles are valid.
    _validate_particles(configuration)


def _validate_particles(configuration: dict) -> None:
    """
        Validates that the particle configurations are valid.

        :param configuration: The configuration dictionary.

        :raise ValueError: If the particle configurations are not consistent
         with the system.
    """
    # Lattice particles.
    adsorbing = configuration["particles"]["adsorbing"]
    desorbing = configuration["particles"]["desorbing"]
    fixed = configuration["particles"]["fixed"]

    # Check no intersections with the adsorption and desorption sites.
    intersection = set(adsorbing) & set(desorbing)

    # Evaluate.
    if len(intersection) > 0:
        raise ValueError(
            f"The adsorption and desorption sites must not intersect "
            f"different. Common particles: {intersection}."
        )

    # Desorbing particles must be a subset of the fixed particles.
    if not set(desorbing).issubset(set(fixed)):
        raise ValueError(
            f"The adsorbing particles must be a subset of the fixed "
            f"particles. Fixed: {set(fixed)}, desorbing: {set(desorbing)}."
        )


# ##############################################################################
# Public Functions
# ##############################################################################


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
    # Validate the settings.
    _validate(settings)

    # Auxiliary varaibles.
    strings = [
        _get_box(offset),
        _get_grid(settings, offset),
        _get_labels(settings["label"], offset),
        _get_other(settings, offset),
    ]

    return "\n".join(strings)
