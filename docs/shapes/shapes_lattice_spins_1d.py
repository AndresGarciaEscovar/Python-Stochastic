"""
    File that contains the functions to construct special grid shapes.
"""

# ##############################################################################
# Imports
# ##############################################################################


# User defined
import docs.shapes.shapes_latex as lshapes

# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'get' Functions
# ------------------------------------------------------------------------------


def get_spins_grid(configuration: dict, offset: tuple = None) -> tuple:
    """
        Gets the 1 dimensional tick grid, with the specified configuration.

        :param configuration: A dictionary with the configuration of the grid.

        :param offset: The offset of all the tick items.

        :return: The grid arrows for the image, the coordinates of the
         arrows (in the middle of the arrow) on the grid and the separation
         between the ticks.
    """
    # Auxiliary variables.
    tick_list = []
    crds = []

    # Set the default values.
    offset = (0, 0) if offset is None else offset

    # --------------------------------------------------------------------------
    # Parameters
    # --------------------------------------------------------------------------

    # Main parameters.
    nspins = configuration["nspins"]
    position_str, position_end = configuration["positions"]
    spins_down = configuration["spins_down"]
    tick_height = configuration["arrow_height"]

    # Interval.
    interval = (position_end[0] - position_str[0]) / (nspins - 1)
    start = position_str[0], position_str[1]

    # Get the coordinates.
    for i in range(nspins):
        # Start and end coordinates.
        tcrd_str = start[0] + i * interval, start[1]
        tcrd_end = start[0] + i * interval, start[1] + tick_height

        # Flip the coordinates if needed.
        if i in spins_down:
            tcrd_str, tcrd_end = tcrd_end, tcrd_str

        # Draw the arrow.
        tick_list.append(lshapes.get_line(tcrd_str, tcrd_end, offset, True))

        # Append the middle coordinate.
        crds.append((tcrd_str[0], (tcrd_str[1] + tcrd_end[1]) / 2))

    return "\n".join(tick_list), tuple(crds), interval


def get_tick_grid(configuration: dict, offset: tuple = None) -> tuple:
    """
        Gets the 1 dimensional tick grid, with the specified configuration.

        :param configuration: A dictionary with the configuration of the grid.

        :param offset: The offset of all the tick items.

        :return: The grid ticks for the image and the final coordinates of the
         ticks on the grid.
    """
    # --------------------------------------------------------------------------
    # Parameters
    # --------------------------------------------------------------------------

    # Main parameters.
    nticks = configuration["nticks"]
    position_str, position_end = configuration["positions"]
    height = configuration["ticks_height"]
    x_offsets = configuration["x_offsets"]
    y_offsets = configuration["y_offsets"]

    # --------------------------------------------------------------------------
    # Auxiliary variables
    # --------------------------------------------------------------------------

    # Lists.
    crds = []
    tick_list = []

    # Default values.
    offset = (0, 0) if offset is None else offset

    # --------------------------------------------------------------------------
    # Base line.
    # --------------------------------------------------------------------------

    # The base line.
    tick_list.append(lshapes.get_line(position_str, position_end, offset))

    # --------------------------------------------------------------------------
    # Coordinates
    # --------------------------------------------------------------------------

    # ---------------------------- Horizontal line --------------------------- #

    # Starting position.
    h_pos_str_x = position_str[0] + x_offsets[0]
    h_pos_str_y = position_str[1]
    h_pos_str = h_pos_str_x, h_pos_str_y

    h_pos_end_x = position_end[0] - x_offsets[1]
    h_pos_end_y = position_end[1]
    h_pos_end = h_pos_end_x, h_pos_end_y

    # ----------------------------- Vertical line ---------------------------- #

    v_pos_str_y = h_pos_str[1] + y_offsets[0]
    v_pos_end_y = v_pos_str_y + height - y_offsets[1]

    # --------------------------------------------------------------------------
    # Only 1 tick
    # --------------------------------------------------------------------------

    if nticks == 1:
        # Tick.
        v_pos_str_x = (h_pos_str[0] + h_pos_end[0]) / 2
        v_pos_end_x = (h_pos_str[0] + h_pos_end[0]) / 2

        v_pos_str = v_pos_str_x, v_pos_str_y
        v_pos_end = v_pos_end_x, v_pos_end_y
        tick_list.append(lshapes.get_line(v_pos_str, v_pos_end, offset))

        # Coordinates
        v_pos_end = v_pos_end[0], v_pos_end[1] + y_offsets[0]
        crds.append(v_pos_end)

        return "\n".join(tick_list), tuple(crds)

    # --------------------------------------------------------------------------
    # Ticks.
    # --------------------------------------------------------------------------

    # Tick coordinates.
    interval = (h_pos_end[0] - h_pos_str[0]) / (nticks - 1)

    # Place every tick.
    for i in range(nticks):
        # Tick.
        v_pos_str_x = h_pos_str[0] + i * interval
        v_pos_end_x = h_pos_str[0] + i * interval
        v_pos_str = v_pos_str_x, v_pos_str_y
        v_pos_end = v_pos_end_x, v_pos_end_y
        tick_list.append(lshapes.get_line(v_pos_str, v_pos_end, offset))

        # Coordinates
        v_pos_end = v_pos_end[0], v_pos_end[1] + y_offsets[0]
        crds.append(v_pos_end)

    return "\n".join(tick_list), tuple(crds)
