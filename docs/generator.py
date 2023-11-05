"""
    Generates the code for the requested grid type.


"""


# ##############################################################################
# Imports
# ##############################################################################


# General.
from itertools import product
from pathlib import Path

# User defined.
import docs.configurations.configuration_manager as cmanager


# ##############################################################################
# Global Variables
# ##############################################################################


# Path of file where the configurations are stored.
PARENT = Path(__file__).parent

# Paths of configuration files.
FPATHS = {
    "1d_ads_des": f"{PARENT / 'other' / 'configuration_ads_des_1d.yml'}",
    "1d_par_clu": None,
    "1d_dif_vac": None,
    "1d_exc_all": None,
    "1d_rsa_dim": None,
    "1d_rsa_nne": None,
    "1d_spi_exc": None,
    "1d_spi_fli": None,
    "1d_sur_rea": None,
    "2d_cry_gro": None,
    "2d_par_dom": None,
    "2d_per_epi": None,
    "2d_rsa_dim": None,
}


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'format' Functions
# ------------------------------------------------------------------------------


def format_text(text: str) -> str:
    """
        Formats the text to be used in the file.

        :param text: The text to be formatted.

        :return: The formatted text.
    """
    # Auxiliary variables.
    indent = " " * 8
    replacement = f"\n{indent}"

    return f"{indent}" + text.strip().replace("\n", replacement)


# ------------------------------------------------------------------------------
# 'get' Functions
# ------------------------------------------------------------------------------


def get_string(gtype: str) -> str:
    """
        From the grid and the configuration settings, generates the code for the
        requested grid images.

        :param gtype: The type of grid to be used.

        :return: The string with the code for the requested grid images.
    """
    validate_grid(gtype)

    # Auxiliary variables.
    grid = get_grid_1d() if gtype == "1D" else get_grid_2d()

    # Get the strings for the images.
    grid_cols = tuple(x for x in range(len(grid[0])))
    grid_rows = tuple(x for x in range(len(grid)))
    strings = []

    # Iterate over the grid.
    for (i, j) in product(grid_rows, grid_cols):
        # Name of the grid to be used.
        name = grid[i][j]

        # Append the string located at the given grid.
        if (string := cmanager.get_box(FPATHS[name], name, (i, j))) == "":
            continue
        strings.append(f"% {name.replace('_', ' ').title()}")
        strings.append(string.strip())

    return "\n".join(strings)


def get_grid_1d() -> tuple:
    """
        Returns the grid with the tuples that contain the different offsets
        and required information for each box of the 1D grid.

        :return: The grid with the offset for each box.
    """
    return (
        ("1d_ads_des", "1d_dif_vac", "1d_par_clu"),
        ("1d_rsa_dim", "1d_rsa_nne", "1d_sur_rea"),
        ("1d_exc_all", "1d_spi_fli", "1d_spi_exc"),
    )


def get_grid_2d() -> tuple:
    """
        Returns the grid with the tuples that contain the different offsets
        and required information for each box of the 2D grid.

        :return: The grid with the offset for each box.
    """
    return (
        ("2d_rsa_dim", "2d_par_dom"),
        ("2d_cry_gro", "2d_per_epi")
    )


# ------------------------------------------------------------------------------
# 'save' Functions
# ------------------------------------------------------------------------------


def save_file(texts: dict) -> str:
    """
        Saves the text to the file.

        :param texts: The dictionary with the text entries to be saved.

        :return: The path where the file was saved.
    """
    # Get the current path.
    path_parent = Path(__file__)

    # Extract the template.text and main.tex file path.
    template_path = path_parent.parent / "templates" / "template.tex"
    main_path = (path_parent.parent / "main.tex").resolve()

    # Get the text from the template.
    with open(f"{template_path}", mode="r", newline="\n") as file:
        template = file.read()
    
    # Replace the text in the template.
    ttext = template.replace("<images-1d>", texts["1D"])
    ttext = ttext.replace("<images-2d>", texts["2D"])

    # Save the text to the file.
    with open(f"{main_path}", mode="w", newline="\n") as file:
        file.write(ttext)
    
    return f"{main_path}"


# ------------------------------------------------------------------------------
# 'validate' Functions
# ------------------------------------------------------------------------------


def validate_grid(gtype: str) -> None:
    """
        Validates the grid type.

        :param gtype: The type of grid to be used.
    """
    # Auxiliary variables.
    valid = {"1D", "2D"}

    # Check if the grid type is valid.
    if gtype not in valid:
        raise ValueError(f"Invalid grid type: {gtype}. Valid types: {valid}")


# ##############################################################################
# Main Function
# ##############################################################################


def run_main() -> None:
    """
        Main function of the file.
    """
    # Get strings for the images.
    text = dict()
    for gtype in ("1D", "2D"):
        text[gtype] = format_text(get_string(gtype))

    # Save the file.
    save_file(text)


# ##############################################################################
# Main Program
# ##############################################################################


if __name__ == "__main__":
    """
        Runs the main program by running the main function.
    """
    run_main()
