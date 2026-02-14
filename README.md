# Stochastic

## Index

- [Information](#information)
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Manual](#manual)

## Information

- **Author**: Andres Garcia Escovar
- **Email**: <andrumen1@yahoo.com>
- **License**: MIT License
- **Repository**: https://github.com/AndresGarciaEscovar/Python-Stochastic

## Overview

A suite that provides a suite for running specific Kinetic Monte Carlo (KMC)
simulations for a limited set of models. This suite is not intended to be a
general-purpose KMC simulator, but rather a collection of specific
implementations for particular models. The suite includes implementations for:

- **Random Sequential Adsorption (RSA)**: A model for simulating the adsorption
  of particles onto a surface, where particles are added sequentially and
  randomly, without overlapping. The algorithm is implemented in 1 and 2
  dimensions, and can be used to study the kinetics of adsorption processes.

## Requirements

- Python 3.11.14 or higher (mandatory)

## Installation

The use of a virtual environment is recommended to avoid conflicts with other
packages. You can create a virtual environment using `venv` or `conda`.

There are two ways to install the Stochastic suite:

1. **Manual Installation**: You can clone the repository and install the package
   manually, with the virtual environment already activated, install the package
   using `pip`:

    1. Clone the repository:
       ```bash
       https://github.com/AndresGarciaEscovar/Python-Stochastic.git
       ```
       You can also download the ZIP file from the GitHub repository and extract
       it to your desired location.

    2. Navigate to the project directory; it is assumed that the directory is
       named `Python-Stochastic`, but it may vary based on how you downloaded
       the repository:
       ```bash
       cd Python-Stochastic
       ```
    3. Install the package using pip:
       ```bash
       pip install .
       ```

2. **Using pip**: If the package is published on PyPI, you can install it
   directly using pip:
    ```bash
    pip install stochastic_kmc
    ```
While the latter method is more convenient, the manual installation method
allows you to use the latest version of the code directly from the repository,
which may include features or bug fixes that are not yet available in the PyPI
version.

## Manual

For specific instructions and detailed information, please refer to the
[index markdown file](./docs/index.md) in the `docs` directory.
