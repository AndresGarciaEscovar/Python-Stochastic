"""
  Constains the functions to get the different box specifications.
"""


# ##############################################################################
# Imports
# ##############################################################################

# General.
import yaml

from pathlib import Path

# User defined.
from docs.images import ads_des_1d
# from docs.images import clu_par_1d as clu
# from docs.images import dif_all_1d as alo
# from docs.images import dif_vac_1d as vac
# from docs.images import rsa_dim_1d as rdi
# from docs.images import rsa_nne_1d as rnn
# from docs.images import spi_exc_1d as sex
# from docs.images import spi_fli_1d as slf

from docs.configurations import configuration_boxes as cboxes


# ##############################################################################
# Functions
# ##############################################################################


# ------------------------------------------------------------------------------
# 'get' Functions
# ------------------------------------------------------------------------------


def get_config(file: str) -> dict:
    """
        Returns the configuration settings of the requested system.

        :param file: The file where the configuration is stored.

        :return: The dictionary with the configuration settings of the box.
    """
    # Get the configuration file.
    with open(Path(file), "r") as file:
        config = yaml.safe_load(file)

    # Get the configuration settings.
    return config


def get_box(file: str, box: str, position: tuple) -> str:
    """
        Returns the configuration settings of the requested system.

        :param file: The file where the configuration is stored.

        :param box: The name of the box for which to get the text.

        :param position: The position of the box in the grid.

        :return: The text generated from the box.
    """
    # Get the configuration settings.
    functions = {
        "1d_ads_des": ads_des_1d.image,
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

    # No need to return when function is not defined.
    if functions[box] is None:
        return ""

    # Extract the position indexes.
    i, j = position

    # Get the configuration settings.
    dictionary = get_config(file)
    offset = cboxes.OFFSETS[i][j]
    offset = offset[0], -offset[1]

    # Get the box.
    return functions[box](dictionary, offset)
