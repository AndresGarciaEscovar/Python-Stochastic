"""
    Script for testing the program.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from pathlib import Path
from shutil import rmtree

# User.
from stochastic.programs.rsa_1d_dimers.main import run


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Simulation parameters.
PARAMETERS: dict = {
    "simulation": {
        "attempts": 100,
        "length": 100,
        "periodic": False,
        "repetitions": 10,
        "seed": -1
    },
    "history": {
        "file": "history.txt",
        "interval": 0,
        "save": False
    },
    "output": {
        "output": "output.txt",
        "working": ""
    }
}


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Functions - Auxiliary
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def remove_cache() -> None:
    """
        Removes the cache.
    """
    # Auxiliary variables.
    path: Path = Path(__file__).parent.parent.parent
    dires: list = [
        x for x in path.rglob("*") if x.is_dir() and x.name == "__pycache__"
    ]

    # Remove each directory.
    for dire in dires:
        if dire.exists():
            rmtree(f"{dire}")


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Functions
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def run_main() -> None:
    """
        Runs the main function.
    """
    # Run the simulation.
    results = run(PARAMETERS)

    # Remove the cache.
    remove_cache()


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    run_main()
