""" Script to install as a conda package.
      1. Install conda and create and environment; activate the environment.
      2. Install the package by running the command: python setup.py develop
      3. Start developing elsewhere with the activated environment.
"""

# Imports.
from setuptools import setup, find_packages

# To setup the package.
setup(name='stochastic',
      version='0.1',
      description='Suite that contains several stochastic simulations for different processes.',
      url='https://github.com/AndresGarciaEscovar/Stochastic',
      author='Andres Garcia Escovar group',
      author_email='andrumen@hotmail.com',
      license='Personal',
      packages=find_packages(),
      zip_safe=False
      )
