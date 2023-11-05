"""
    Script to install as a conda package.
        1. Install conda and create and environment; activate the environment.
        2. Install the package by running the command: python setup.py develop.
        3. Start developing elsewhere with the activated environment.
"""

# ##############################################################################
# Imports
# ##############################################################################


# General.
from setuptools import setup, find_packages


# ##############################################################################
# 'setup' Function
# ##############################################################################


setup(
    author="Andres Garcia Escovar group",
    author_email="andrumen@hotmail.com",
    description=(
        "Suite that contains several stochastic simulations for different "
        "processes."
    ),
    license="Personal",
    packages=find_packages(),
    name="stochastic",
    url="https://github.com/AndresGarciaEscovar/Stochastic",
    version='0.1',
)
