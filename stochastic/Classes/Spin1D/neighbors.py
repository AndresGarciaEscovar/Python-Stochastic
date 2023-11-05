""" File that contains the random sequential adsorption (RSA) base classes, for
    RSA in one dimension.
"""

# ------------------------------------------------------------------------------
# Imports.
# ------------------------------------------------------------------------------

from stochastic.Interfaces.Spin1D_interface import Spin1D

# ------------------------------------------------------------------------------
# Classes.
# ------------------------------------------------------------------------------


class Neighbors(Spin1D):
    """ Class to simulate spin flip from the 1D Glauber Model, where only
        nearest neighbor interactions are considered.

        Constants:

        - UP: Represents the up state of a single spin.

        - DOWN: Represents the down state of a single spin.

        Parameters:

        - self.attemps: An integer that represents the number of attempts at
          making a spin flip.

        - self.dimensions: A 2-tuple that indicates the dimensions of the
          lattice.

        - self.lattice: A list that represents the lattice where the particles
          live.

        - self.lattice_file: The name of the file where the lattice must be
          printed.

        - self.maximum_time: The maximum time for which the simulation must be
          run.

        - self.periodic: A 2-tuple with boolean flags that indicate the
          periodicity of each dimension.

        - self.random_generator: The random number generator.

        - self.repetitions: The number of times the simulation must be run to
          get statistically significant data.

        - self.save_lattice_file_name: The name of the file where to save the
          lattice configuration.

        - self.save_results_file_name: The name of the file where to save the
          simulation results.

        - self.seed: The seed to seed the random number generator.

        - self.statistics_table: The list where the statistics are kept.

        - self.tolerance: The tolerance to compare the floating point numbers.
    """

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Constants
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    UP = 1  # type: int
    DOWN = -1  # type: int

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Getters/Setters/Deleters
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    @property
    def attempts(self) -> int:
        """ Returns the number of attempts to place a particle in the lattice.

            :return: The number of attempts to place a particle in the lattice.
        """
        return self.__attempts

    @attempts.setter
    def attempts(self, attempts: int) -> None:
        """ Sets the number of attempts.

            :param attempts: The number of attempts.
        """
        self.__attempts = attempts

    @attempts.deleter
    def attempts(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The attempts variable must not be deleted.")

    # --------------------------------------------------------------------------

    @property
    def lattice(self) -> list:
        """ Returns the list that represents the lattice.

            :return: The list that represents the lattice.
        """
        return self.__lattice

    @lattice.setter
    def lattice(self, _) -> None:
        """ Creates the lattice."""
        self.__lattice = [Spin1D.DOWN for _ in range(self.length)]

    @lattice.deleter
    def lattice(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The lattice variable must not be deleted.")

    # --------------------------------------------------------------------------