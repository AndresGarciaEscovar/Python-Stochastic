"""
    Runs the linting algorithm.
"""


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#  Imports
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Standard library.
from pathlib import Path
from shutil import rmtree
from subprocess import run as rproc
from typing import Any


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#  Global Variables
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Current directory path.
DIR_CURRENT: Path = Path(__file__).parent
DIR_LINTING: str = DIR_CURRENT / ".." / ".." / "src"


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#  Main Function
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def lint(name: str) -> None:
    """
        Performs the linting operation.

        :param name: The name of the linter.
    """
    # Auxiliary variables.
    file: str = f"{DIR_CURRENT / f'linting_{name}.txt'}"

    # Run the command.
    command: tuple = name, f"{DIR_LINTING}"
    result: Any = rproc(
        command, capture_output=True, check=False, shell=False, text=True
    )

    # Write the output
    with open(file, encoding="utf-8", mode="w") as stream:
        stream.write(result.stdout)
        stream.write(result.stderr)


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
#  Main Function
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


def run_main() -> None:
    """
        Runs the main algorithm.
    """
    # Run the linters.
    lint("pylint")
    lint("flake8")

    # Remove the cache.
    remove_cache()


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#  Main Program
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


if __name__ == "__main__":
    run_main()
