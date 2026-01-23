""" File that contains the random sequential adsorption (RSA) base classes, for
    RSA in one dimension.
"""

# ------------------------------------------------------------------------------
# Imports.
# ------------------------------------------------------------------------------

# Imports: General.
import itertools
import numpy

from abc import ABCMeta, abstractmethod
from typing import Any

# Imports: User-defined.
from stochastic.utilities.RSA_parameters import RSA2DParameters

# ------------------------------------------------------------------------------
# Classes.
# ------------------------------------------------------------------------------


class RSA2D(metaclass=ABCMeta):
    """ Class that is the interface to build random sequential adsorption
        simulations in 2 dimensions.

        Constants:

        - EMPTY: Represents the empty state of a cell in the system.

        - OCCUPIED: Represents the occupied state of a cell in the system.

        Parameters:

        - self.attemps: An integer that represents the number of attempts at
          adsorbing a particle.

        - self.attempts_successful: An integer that represents the number of
          successful attempts at adsorbing a particle.

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

    EMPTY = 0  # type: int
    OCCUPIED = 1  # type: int

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
    def attempts_successful(self) -> int:
        """ Returns the number of successful attempts to place a particle in the
            lattice.

            :return: The number of successful attempts to place a particle in
             the lattice.
        """
        return self.__attempts_successful

    @attempts_successful.setter
    def attempts_successful(self, attempts_successful: int) -> None:
        """ Sets the number of successful attempts.

            :param attempts_successful: The number of successful attempts to
             make a move.
        """
        self.__attempts_successful = attempts_successful

    @attempts_successful.deleter
    def attempts_successful(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The attempts_successful variable must not be deleted.")

    # --------------------------------------------------------------------------

    @property
    def dimensions(self) -> tuple:
        """ Returns the dimensions of the lattice.

            :return: The dimensions of the lattice.
        """
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: tuple) -> None:
        """ Sets the length of the lattice.

            :param dimensions: A tuple of positive integers tha represent the
             dimensions of the lattice.
        """
        self.__dimensions = (int(abs(dimensions[0])), int(abs(dimensions[1])))

    @dimensions.deleter
    def dimensions(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The length variable must not be deleted.")

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
        self.__lattice = [[RSA2D.EMPTY for _ in range(self.dimensions[1])] for _ in range(self.dimensions[0])]

    @lattice.deleter
    def lattice(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The lattice variable must not be deleted.")

    # --------------------------------------------------------------------------

    @property
    def lattice_file(self) -> str:
        """ Returns the string with the name of the file where the lattice
            configuration must be saved.

            :return: The string with the name of the file where the lattice
             configuration must be saved.
        """
        return self.__lattice_file

    @lattice_file.setter
    def lattice_file(self, lattice_file: str) -> None:
        """ Sets the string with the name of the file where the lattice
            configuration must be saved.

            :param lattice_file: The string with the name of the file where the
             lattice configuration must be saved.
        """
        self.__lattice_file = str(lattice_file)

    @lattice_file.deleter
    def lattice_file(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The lattice_file variable must not be deleted.")

    # --------------------------------------------------------------------------

    @property
    def maximum_time(self) -> float:
        """ Returns the maximum simulation time.

            :return: The maximum simulation time.
        """
        return self.__maximum_time

    @maximum_time.setter
    def maximum_time(self, maximum_time: float) -> None:
        """ Sets the maximum simulation time. If the provided time is negative
            it will be turned into a positive number.

            :param maximum_time: The maximum simulation time; a positive real
             number.
        """
        self.__maximum_time = float(abs(maximum_time))

    @maximum_time.deleter
    def maximum_time(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The maximum_time variable must not be deleted.")

    # --------------------------------------------------------------------------

    @property
    def periodic(self) -> tuple[bool, ...]:
        """ Indicates if the lattice is periodic.

            :return: True, if the lattice is periodic. False, otherwise.
        """
        return self.__periodic

    @periodic.setter
    def periodic(self, periodic: tuple[bool, ...]) -> None:
        """ Sets the flag to indicate if the lattice is periodic. One flag for
            each dimension.

            :param periodic: The flag to indicate if the lattice is periodic.
        """
        self.__periodic = (periodic[0], periodic[1])

    @periodic.deleter
    def periodic(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The periodic variable must not be deleted.")

    # --------------------------------------------------------------------------

    @property
    def random_generator(self) -> Any:
        """ Returns the seeded random number generator.

            :return: The seeded random number generator.
        """
        return self.__random_generator

    @random_generator.setter
    def random_generator(self, _) -> None:
        """ Sets the random number generator."""
        self.__random_generator = numpy.random.default_rng(self.seed)

    @random_generator.deleter
    def random_generator(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The random_generator variable must not be deleted.")

    # --------------------------------------------------------------------------

    @property
    def repetitions(self) -> int:
        """ Returns the number of times that the simulation must be averaged to
            get statistically significant results.

            :return: The number of times that the simulation must be averaged to
             get statistically significant results.
        """
        return self.__repetitions

    @repetitions.setter
    def repetitions(self, repetitions: int) -> None:
        """ Sets the number of times that the simulation must be averaged to get
            statistically significant results.

            :param repetitions: The number of times that the simulation must be
             averaged to get statistically significant results. If the number is
             negative, the absolute value will be taken.
        """
        self.__repetitions = int(abs(repetitions))

    @repetitions.deleter
    def repetitions(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The repetitions variable must not be deleted.")

    # --------------------------------------------------------------------------

    @property
    def results_file(self) -> str:
        """ Returns the name of the file where the simulation results are to be
            saved.

            :return: The name of the file where the simulation results are to be
            saved.
        """
        return self.__results_file

    @results_file.setter
    def results_file(self, results_file: str) -> None:
        """ Sets the name of the file where the simulation results are to be
            saved.

            :param results_file: The name of the file where the simulation
            results are to be saved.
        """
        self.__results_file = results_file

    @results_file.deleter
    def results_file(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The results_file variable must not be deleted.")

    # --------------------------------------------------------------------------

    @property
    def seed(self) -> int:
        """ Returns the seed used in the random number generator.

            :return: The seed used in the random number generator.
        """
        return self.__seed

    @seed.setter
    def seed(self, seed: int) -> None:
        """ Sets the seed used in the random number generator.

            :param seed: The seed to be used in the random number generator.
        """
        self.__seed = int(abs(seed))

    @seed.deleter
    def seed(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The seed variable must not be deleted.")

    # --------------------------------------------------------------------------

    @property
    def statistics_table(self) -> list:
        """ Returns the statistics table.

            :return: The statistics table.
        """
        return self.__statistics_table

    @statistics_table.setter
    def statistics_table(self, _) -> None:
        """ Initializes the statistics table to an empty list. Can only be
            manipulated, not changed.
        """
        self.__statistics_table = []

    @statistics_table.deleter
    def statistics_table(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The statistics_table variable must not be deleted.")

    # --------------------------------------------------------------------------

    @property
    def tolerance(self) -> float:
        """ Returns the tolerance to compare floating point numbers.

            :return: The tolerance to compare floating point numbers.
        """
        return self.__tolerance

    @tolerance.setter
    def tolerance(self, tolerance: float) -> None:
        """ Sets the tolerance to compare floating point numbers.
        """
        self.__tolerance = abs(float(tolerance))

    @tolerance.deleter
    def tolerance(self) -> None:
        """ Deletes the parameter."""
        raise PermissionError("The tolerance variable must not be deleted.")

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Methods.
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # --------------------------------------------------------------------------
    # Get Methods.
    # --------------------------------------------------------------------------

    def get_coverage(self):
        """ Gets the number non-empty sites in the lattice.

            :return: the number non-empty sites in the lattice.
        """
        iterator = itertools.product(*[range(i) for i in self.dimensions])
        return sum([1 for i, j in iterator if not self.lattice[i][j] == RSA2D.EMPTY])

    def get_number_of_cells(self):
        """ Returns the number of cells in the lattice.
        """
        return int(numpy.prod(self.dimensions))

    @abstractmethod
    def get_preheader(self) -> str:
        """ Returns the pre-header, i.e., the string that contains the
            simulation information.

            :return: The string that represents the pre-header.
        """
        ...

    # --------------------------------------------------------------------------
    # Normalize Methods.
    # --------------------------------------------------------------------------

    def normalize_site(self, site: tuple) -> tuple:
        """ Given an scalar integer site, returns the site in the lattice, as it
            would correspond to the periodicity.

            :param site: The site to be normalized.

            :return: The normalized site.
        """

        # //////////////////////////////////////////////////////////////////////
        # Auxiliary functions.
        # //////////////////////////////////////////////////////////////////////

        def get_periodic(index0: int, periodicity0: int) -> int:
            """ Given a scalar integer index, and its periodicity, returns the
                proper index in the range 0 <= index0 < periodicity.

                :param index0: The index to be normalized.

                :param periodicity0: The periodicty of the dimension.

                :return: The normalized site.
            """

            while index0 < 0:
                index0 += periodicity0

            return index0 % periodicity0

        # //////////////////////////////////////////////////////////////////////
        # Implementation.
        # //////////////////////////////////////////////////////////////////////

        site_ = tuple(
            get_periodic(site[i], self.dimensions[i]) if self.periodic[i] else site[i] for i in range(2)
        )

        return site_

    # --------------------------------------------------------------------------
    # Print Results.
    # --------------------------------------------------------------------------

    def print_results(self) -> None:
        """ Saves the results, with the information, to the given file."""

        # //////////////////////////////////////////////////////////////////////
        # Auxiliary functions.
        # //////////////////////////////////////////////////////////////////////

        def get_colum_widths(header0, statistics_table0):
            """ Gets the width of all the columns for it to be properly
                formatted.

                :param header0: The header titles.

                :param statistics_table0: The table of statistics.

                :return: The values with the widths of the columns in the proper
                 format.
            """

            # Get an array with the column widths of the header strings.
            columns_width0 = [max(len(column0), 10) for column0 in header0]

            # Get each statistic.
            for statistic0 in statistics_table0:
                for i0, entry in enumerate(statistic0):
                    if i0 > 0:
                        columns_width0[i0] = max(columns_width0[i0], len(f"{statistic0[i0]:0.10f}"))
                        continue

                    columns_width0[i0] = max(columns_width0[i0], len(f"{statistic0[i0]:0.3f}"))

            return columns_width0

        # //////////////////////////////////////////////////////////////////////
        # Implementation.
        # //////////////////////////////////////////////////////////////////////

        h_string = []
        preheader = self.get_preheader()
        header = ["attemps/n", "successes/n", "coverage"]
        colum_widths = get_colum_widths(header, self.statistics_table)

        with open(self.results_file, "w") as fl:
            fl.write(preheader + "\n")
            for i, value in enumerate(colum_widths):
                h_string.append(f"{header[i]:<{value + 2}}")

            fl.write(",".join(h_string) + "\n")
            for statistic in self.statistics_table:
                h_string = []
                for i, value in enumerate(colum_widths):
                    h_string.append(f"{statistic[i]:<0.{value}f}")

                fl.write(",".join(h_string) + "\n")

    # --------------------------------------------------------------------------
    # Process Methods.
    # --------------------------------------------------------------------------

    @abstractmethod
    def process_adsorb(self) -> None:
        """ Tries to perform an adsorption operation; i.e., select a random site
            in the lattice onto which to adsorb.
        """
        ...

    # --------------------------------------------------------------------------
    # Reset Methods.
    # --------------------------------------------------------------------------

    def reset_simulation_variables(self) -> None:
        """ Resets the variables for a single simulation to their initial state.
        """

        # Reset the lattice.
        for i, j in itertools.product(*[range(dimension) for dimension in self.dimensions]):
            self.lattice[i][j] = RSA2D.EMPTY

        # Reset the counters.
        self.attempts = 0
        self.attempts_successful = 0

    # --------------------------------------------------------------------------
    # Run Methods.
    # --------------------------------------------------------------------------

    def run_simulation(self) -> None:
        """ Runs the simulation the number of specified times by the repetition
            parameter.
        """

        # Initialize the variables.
        self.statistics_table = None
        self.random_generator = None

        # Run the simulation.
        for i in range(self.repetitions):
            self.run_simulation_single(i)

        # Normalize the results.
        self.statistics_record(self.repetitions)
        self.print_results()

    def run_simulation_single(self, number: int) -> None:

        self.reset_simulation_variables()
        elapsed_time = 0

        # Run the simulation.
        if number == 0:
            self.save_lattice(initial=True, last=False)

        while elapsed_time < self.maximum_time:
            self.statistics_record()
            self.process_adsorb()
            if number == 0 and (10 * self.attempts) % self.get_number_of_cells() == 0:
                self.save_lattice(initial=False, last=False)

            elapsed_time = self.attempts / self.get_number_of_cells()

        self.statistics_record()
        if number == 0:
            self.save_lattice(initial=False, last=True)

    # --------------------------------------------------------------------------
    # Save Methods.
    # --------------------------------------------------------------------------

    def save_lattice(self, initial=True, last=False) -> None:
        """ Prints the lattice to the given file.

            :param initial: True, if it is the first lattice to be printed.
             False, otherwise.

            :param last: True, if it is the last lattice to be printed.
             False, otherwise.
        """

        # Set the table preheader.
        preheader = self.get_preheader()

        # Set the table header.
        header = ["time\\index"]
        product = itertools.product
        header.extend([
            f"({indexes[0]}x{indexes[1]})" for indexes in product(*[range(dimension) for dimension in self.dimensions])
        ])
        header = ",".join(header)

        # Always open in append mode.
        with open(self.lattice_file, "a") as fl:
            if initial:
                fl.write("\n".join([preheader, header, ""]))

            tmp_stats = [self.attempts / self.get_number_of_cells()]
            for i, j in itertools.product(*[range(dimension) for dimension in self.dimensions]):
                tmp_stats.append(self.lattice[i][j])
            tmp_stats = ",".join([f"{stat:0.3f}" if i == 0 else f"{stat:1}" for i, stat in enumerate(tmp_stats)])
            fl.write("".join([tmp_stats, "\n"]))

            if last:
                fl.write("".join(["-" * self.get_number_of_cells(), "\n"]))

    # --------------------------------------------------------------------------
    # Statistics Methods.
    # --------------------------------------------------------------------------

    def statistics_record(self, number_simulations: int = None) -> None:
        """ Records the statistics.

            :param number_simulations: The number of simulationms with
             which to take the average.
        """

        # //////////////////////////////////////////////////////////////////////
        # Auxiliary functions.
        # //////////////////////////////////////////////////////////////////////

        def normalize_results(number_simulations0: int):
            """ Averages the final results with the number of simulations.

                :param number_simulations0: The number of simulationms with
                 which to take the average.
            """

            for i0, _ in enumerate(self.statistics_table):
                self.statistics_table[i0][1] /= number_simulations0
                self.statistics_table[i0][2] /= number_simulations0

        # //////////////////////////////////////////////////////////////////////
        # Implementation.
        # //////////////////////////////////////////////////////////////////////

        if number_simulations is not None:
            normalize_results(number_simulations)
            return

        if not (10 * self.attempts) % self.get_number_of_cells() == 0:
            return

        # Get statistics.
        elapsed_time = self.attempts / self.get_number_of_cells()
        successful = self.attempts_successful / self.get_number_of_cells()
        coverage = self.get_coverage() / self.get_number_of_cells()

        # Go through all the entries.
        for i, statistic in enumerate(self.statistics_table):
            if self.validate_almost_equal(elapsed_time, statistic[0]):
                self.statistics_table[i][1] += successful
                self.statistics_table[i][2] += coverage
                return

        self.statistics_table.append([elapsed_time, successful, coverage])

    # --------------------------------------------------------------------------
    # Validate Methods.
    # --------------------------------------------------------------------------

    def validate_almost_equal(self, number0: float, number1: float) -> bool:
        """ Determines if two numbers are equal within the tolerance limit.

            :param number0: The base number for comparison.

            :param number1: The general number for comparison.

            :return: True if the numbers are equal within the given tolerance.
             False, otherwise.
        """

        if number0 == 0.0:
            return abs(number1) <= self.tolerance

        return abs((number0 - number1) / number0) <= self.tolerance

    @abstractmethod
    def validate_adsorb(self, *args) -> bool:
        """ Determines if the given site can adsorb a particle.

            :param args: The needed arguments to validate the adsorption.

            :return: If the site is empty and its inmediate neighbors are empty.
        """
        ...

    def validate_in_lattice(self, indexes: tuple) -> bool:
        """ Validates if the given indexes are in the lattice."""
        return all(map(lambda x, y: 0 <= x < y, indexes, self.dimensions))

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Constructor and Dunder Methods.
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # --------------------------------------------------------------------------
    # Constructor.
    # --------------------------------------------------------------------------

    def __init__(self, parameters: RSA2DParameters):
        """ Initializes the simulation parameters.

            :param parameters: A dataclass that contains the adjustable
             parameters of the simulation.
        """

        # Counters.
        self.attempts = 0
        self.attempts_successful = 0
        self.maximum_time = parameters.maximum_time
        self.repetitions = parameters.repetitions

        # Lattice parameters.
        self.dimensions = parameters.dimensions
        self.lattice = None
        self.periodic = parameters.periodic
        self.lattice_file = parameters.lattice_file

        # Random number generator parameters.
        self.seed = parameters.seed
        self.random_generator = None

        # Other simulation parameters.
        self.results_file = parameters.results_file
        self.statistics_table = None
        self.tolerance = parameters.tolerance
