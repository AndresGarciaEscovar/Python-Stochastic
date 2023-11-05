"""
    File that contains general functions for the project.
"""


# ##############################################################################
# Imports
# ##############################################################################


# General.
from typing import Any, Union

# ##############################################################################
# Functions
# ##############################################################################


def set_font_size(text: str, font: str = None) -> str:
    """
        Function that sets the font size of the text. Valid font sizes are:
          - tiny
          - scriptsize
          - footnotesize
          - small
          - large
          - Large
          - LARGE
          - huge
          - Huge

        :param text: Text whose font size will be set.

        :param font: Font size to set; it must be a string. The default value
         is "normalsize", which means that the font size will not be changed.

        :return: Text with the font size set.
    """
    # Check the font size.
    if font is None or font == "normalsize":
        return text

    # Validate the font sizes.
    fonts = (
        "tiny", "scriptsize", "footnotesize", "small", "large", "Large",
        "LARGE", "huge", "Huge"
    )

    # Check if the font size is valid.
    if font not in fonts:
        raise ValueError(
            f"Invalid font size, it must be one of the following: "
            f"{fonts}"
        )

    # Set the font size.
    return "".join([f"\\", font, "{", text, "}"])
