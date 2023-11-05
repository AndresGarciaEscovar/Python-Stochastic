"""
    Generates the code for different shapes in the figures.
"""


# ##############################################################################
# Global variables
# ##############################################################################


# Measurement units.
UNITS = "cm"


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'get' Functions
# ------------------------------------------------------------------------------


def get_circle(
    center: tuple, radius: float, offset: tuple = (0, 0), filled: bool = False,
    color: str = "black"
) -> str:
    """
        Gets the code for the rectangle.

        :param center: The center coordinates of the circle.

        :param radius: The radius of the circle.
        
        :param offset: The offset of the rectangle.

        :param filled: Whether the rectangle should be filled.

        :param color: The color of the circle.
        
        :return: The code for the rectangle.
    """
    # Get the coordinates.
    ccenter = transform_offset(center, offset)

    # Transform into strings.
    corigin = transform_coordinates(ccenter)
    
    # Get the arrow.
    ccircle = f"\\draw {corigin} circle ({radius:.4f});"
    if filled:
        ccircle = f"\\fill [{color}] {corigin} circle ({radius:.4f});"

    return ccircle


def get_coordinate(coordinate: tuple, idc: str, offset: tuple = (0, 0)) -> str:
    """
        Gets the coordinate tag with the given id.

        :param coordinate: The coordinate to be tagged.

        :param idc: The id of the coordinate.

        :param offset: The offset of the coordinate.
        
        :return: The code for defining the coordinate.
    """
    # Get the coordinates.
    ccoordinate = transform_offset(coordinate, offset)

    # Transform into strings.
    ccoordinate = transform_coordinates(ccoordinate)
    
    return f"\\coordinate ({idc}) at {ccoordinate};"


def get_ellipse(
    center: tuple, xaxis: float, yaxis: float, offset: tuple = (0, 0),
    filled: bool = False, color: str = "black"
) -> str:
    """
        Gets the code for the rectangle.

        :param center: The center coordinates of the circle.

        :param xaxis: The eccentricity of the x axis of the elipse.

        :param yaxis: The eccentricity of the y axis of the elipse.

        :param offset: The offset of the rectangle.

        :param filled: Whether the rectangle should be filled.

        :param color: The color of the circle.

        :return: The code for the rectangle.
    """
    # Get the coordinates.
    ccenter = transform_offset(center, offset)

    # Transform into strings.
    corigin = transform_coordinates(ccenter)

    # Get the arrow.
    pre = f"\\draw" if not filled else f"\\fill [{color}]"
    ccircle = f"{pre} {corigin} ellipse ({xaxis:.4f} and {yaxis:.4f});"
    if filled:
        ccircle = f"{pre} {corigin} circle ({xaxis:.4f} and {yaxis:.4f});"

    return ccircle


def get_line(
    start: tuple, end: tuple, offset: tuple = (0, 0), arrow: bool = False,
    double: bool = False
) -> str:
    """
        Gets the code for a line.

        :param start: The starting coordinates of the line.

        :param end: The ending coordinates of the line.

        :param offset: The offset of the line.

        :param arrow: Whether the line should have an arrow.

        :param double: Whether the arrow should be a double arrow.
        
        :return: The code for the line.
    """
    # Get the coordinates.
    cstart = transform_offset(start, offset)
    cend = transform_offset(end, offset)

    # Transform into strings.
    cstart = transform_coordinates(cstart)
    cend = transform_coordinates(cend)
    
    # Get the arrow.
    rarrow = " [->] " if arrow else " "

    # Get the line.
    line = f"\\draw{rarrow}{cstart} -- {cend};"
    if double:
        line += f"\n\\draw{rarrow}{cend} -- {cstart};"

    return line


def get_line_curved(
    node_name_0: str, node_name_1: str, outa: float, ina: float
) -> str:
    """
        Gets the code for a curved line.
        
        :param node_name_0: The name of the first node.

        :param node_name_1: The name of the second node.

        :param outa: The angle of the outgoing line.

        :param ina: The angle of the incoming line.
        
        :return: The code for the line.
    """
    # Get the line.
    line = f"\\draw [->] ({node_name_0}) to[out={outa}, in={ina}] ({node_name_1});"

    return line


def get_rectangle(
    tleft: tuple, lright: tuple, offset: tuple = (0, 0), filled: bool = False,
    color: str = "black"
) -> str:
    """
        Gets the code for the rectangle.

        :param tleft: The top left coordinates of the rectangle.

        :param lright: The lower right coordinates of the rectangle.

        :param offset: The offset of the rectangle.

        :param filled: Whether the rectangle should be filled.

        :param color: The color of the rectangle.
        
        :return: The code for the rectangle.
    """
    # Get the coordinates.
    ctleft = transform_offset(tleft, offset)
    clright = transform_offset(lright, offset)

    # Transform into strings.
    cstart = transform_coordinates(ctleft)
    cend = transform_coordinates(clright)
    
    # Get the arrow.
    rectangle = f"\\draw {cstart} rectangle {cend};"
    if filled:
        rectangle = f"\\fill [{color}] {cstart} rectangle {cend};"

    return rectangle


def get_text(text: str, position: tuple, offset: tuple = (0, 0)) -> str:
    """
        Gets the code for the text in the given position.

        :param text: The text to be written.

        :param position: The position of the text.

        :param offset: The offset of the text.
        
        :return: The code for the text.
    """
    # Get the position.
    aposition = transform_offset(position, offset)
    aposition = transform_coordinates(aposition)

    return f"\\node at {aposition} " + "{" + f"{text}" + "};"


def get_tick(
    center: tuple, length: float = 1, height: float = 1, offset: tuple = (0, 0)
) -> str:
    """
        Gets the code for the rectangle.

        :param center: The center coordinates of the tick.

        :param length: The length of the tick.

        :param height: The height of the tick.

        :param offset: The offset of the rectangle.
        
        :return: The code for the single tick.
    """
    # Get the coordinates.
    ccenter = transform_offset(center, offset)

    # The vertical line.
    vcstart = (ccenter[0], ccenter[1])
    vcend = (ccenter[0], ccenter[1] + height)

    vcstart = transform_coordinates(vcstart)
    vcend = transform_coordinates(vcend)

    # Get the tick.
    tick = f"\\draw {vcstart} -- {vcend};"
    if length > 0:
        # Get the coordinates.
        hcstart = (ccenter[0] - 0.5 * length, ccenter[1])
        hcend = (ccenter[0] + 0.5 * length, ccenter[1])

        # Turn into strings.
        hcstart = transform_coordinates(hcstart)
        hcend = transform_coordinates(hcend)

        # Add the horizontal line.
        tick += f"\n\\draw {hcstart} -- {hcend};"

    return tick


# ------------------------------------------------------------------------------
# 'transform' Functions
# ------------------------------------------------------------------------------


def transform_coordinates(coordinates: tuple) -> str:
    """
        Transforms the coordinates into a string.

        :param coordinates: The coordinates to transform.

        :return: The string with the coordinates.
    """
    # Global variables.
    global UNITS

    # Transform into strings.
    coords = [f"{int(x):d}" if x == 0 else f"{x:+.4f}{UNITS}" for x in coordinates]

    return "".join(["(", ",".join(coords), ")"])


def transform_offset(coordinates: tuple, offset: tuple) -> tuple:
    """
        Transforms the coordinates such that the offset is added.

        :param coordinates: The coordinates to transform.

        :param offset: The offset to add.

        :return: The transformed coordinates.
    """
    # Validate the coordinates and the offset are the same length.
    if len(coordinates) != len(offset):
        raise ValueError(
            f"The coordinates and the offset must have the same length. "
            f"Coordinates length: {len(coordinates)}, offset length: "
            f"{len(offset)}."
        )
    
    return tuple(x + y for x, y in zip(coordinates, offset))
