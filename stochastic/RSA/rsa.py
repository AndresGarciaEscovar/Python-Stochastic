""" Contains the class to simulate random sequential adsorption with nearest
    neighbor exclusion for a periodic lattice.
"""

# ------------------------------------------------------------------------------
# Imports.
# ------------------------------------------------------------------------------

# Imports: General.
import numpy as np
import random

# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------


class RSA:
    """ Class to simulate random sequential adsorption with nearest neighbor
        exclusion for a periodic one-dimensional lattice.

        - self.attemps: An integer that represents the number of attempts at
          adsorbing a particle.

        - self.attempts_successful: An integer that represents the number of
          successful attempts at adsorbing a particle.

        - self.lattice: A list that represents the lattice where the particles
          live.

        - self.length: A positive integer that represents the length of the
          lattice.
    """

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Constants
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # Represents the empty value.
    EMPTY = 0

    # Represents the occupied value.
    OCCUPIED = 1

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
    def attempts(self, attempts: int):
        """ Sets the number of attempts.

            :param attempts: The number of attempts.
        """

        # Must be a number greater than or equal to zero.
        if attempts < 0:
            raise ValueError("The number of attempts must be zero or a positive number.")

        self.__attempts = attempts

    @attempts.deleter
    def attempts(self):
        """ Deletes the parameter.
        """
        del self.__attempts

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
    def attempts_successful(self, attempts_successful: int):
        """ Sets the number of successful attempts.

            :param attempts_successful: The number of successful attempts.
        """

        # Must be a number greater than or equal to zero.
        if attempts_successful < 0:
            raise ValueError("The number of successful attempts must be zero or a positive number.")

        self.__attempts_successful = attempts_successful

    @attempts_successful.deleter
    def attempts_successful(self):
        """ Deletes the parameter.
        """
        del self.__attempts_successful

    # --------------------------------------------------------------------------

    @property
    def generator(self) -> type(random.randint):
        """ Returns the seeded random number generator.

            :return: The seeded random number generator.
        """
        return self.__generator

    @generator.setter
    def generator(self, seed: int):
        """ Sets the random number generator.

            :param seed: To be used to get the generator.
        """

        try:
            self.__generator

        except AttributeError:
            # Seed the generator.
            if seed is not None:
                # Seed the generator.
                random.seed(abs(seed))

            self.__generator = random.randint

    @generator.deleter
    def generator(self):
        """ Deletes the parameter.
        """
        del self.__generator

    # --------------------------------------------------------------------------

    @property
    def lattice(self) -> list:
        """ Returns the list that represents the lattice.

            :return: The list that represents the lattice.
        """
        return self.__lattice

    @lattice.setter
    def lattice(self, length: int):
        """ Creates the lattice. Only sets the lattice once.

            :param length: The length of the lattice. A positive integer number.
        """
        try:
            # Can only be set once.
            self.__lattice

        except AttributeError:
            # Check the length is an integer number.
            if not isinstance(length, (int,)):
                raise TypeError("The length must be an integer number.")

            # Also a number greater than zero.
            elif length <= 0:
                raise ValueError("The length must be an integer number greater than zero.")

            self.__lattice = [RSA.EMPTY for _ in range(length)]

    @lattice.deleter
    def lattice(self):
        """ Deletes the parameter.
        """
        del self.__lattice

    # --------------------------------------------------------------------------

    @property
    def length(self) -> int:
        """ Returns the length of the lattice.

            :return: The length of the lattice.
        """
        return self.__length

    @length.setter
    def length(self, length: int):
        """ Sets the length of the lattice. Only sets the length once.

            :param length: The length of the lattice. A positive integer number.
        """
        try:
            # Can only be set once.
            self.__length

        except AttributeError:
            # Check the length is an integer number.
            if not isinstance(length, (int,)):
                raise TypeError("The length must be an integer number.")

            # Also a number greater than zero.
            elif length <= 0:
                raise ValueError("The length must be an integer number greater than zero.")

            self.__length = length

    @length.deleter
    def length(self):
        """ Deletes the parameter.
        """
        del self.__length

    # --------------------------------------------------------------------------

    @property
    def maximum_time(self) -> float:
        """ Returns the maximum simulation time.

            :return: The maximum simulation time.
        """
        return self.__maximum_time

    @maximum_time.setter
    def maximum_time(self, maximum_time: float):
        """ Sets the maximum simulation time. If the provided time is negative
            it will be turned into a positive number. Only set once.

            :param maximum_time: The maximum simulation time; a positive number.
        """
        try:
            # Can only be set once.
            self.__maximum_time

        except AttributeError:
            # Set the maximum time.
            self.__maximum_time = float(abs(maximum_time))

    @maximum_time.deleter
    def maximum_time(self):
        """ Deletes the parameter.
        """
        del self.__maximum_time

        # --------------------------------------------------------------------------

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
    def repetitions(self, repetitions: int):
        """ Sets the number of times that the simulation must be averaged to get
            statistically significant results.

            :param repetitions: The number of times that the simulation must be
             averaged to get statistically significant results. If the number is
             negative, the absolute value will be taken.
        """

        # Set the number of repetitions.
        self.__repetitions = int(abs(repetitions))

    @repetitions.deleter
    def repetitions(self):
        """ Deletes the parameter.
        """
        del self.__repetitions

    # --------------------------------------------------------------------------

    @property
    def seed(self) -> int:
        """ Returns the seed used in the random number generator.

            :return: The seed used in the random number generator.
        """
        return self.__seed

    @seed.setter
    def seed(self, seed: int):
        """ Sets the seed used in the random number generator.

            :param seed: The seed to be used in the random number generator.
        """
        try:
            # Can only be set once.
            self.__seed

        except AttributeError:
            # Can only be set once.
            self.__seed = seed

    @seed.deleter
    def seed(self):
        """ Deletes the parameter.
        """
        del self.__seed

    # --------------------------------------------------------------------------

    @property
    def statistics_table(self) -> list:
        """ Returns the statistics table.

            :return: The statistics table.
        """
        return self.__statistics_table

    @statistics_table.setter
    def statistics_table(self, _):
        """ Initializes the statistics table to an empty list. Can only be
            manipulated, not changed.
        """
        # Initialize to an empty array.
        self.__statistics_table = []

    @statistics_table.deleter
    def statistics_table(self):
        """ Deletes the parameter.
        """
        del self.__statistics_table

    # --------------------------------------------------------------------------

    @property
    def tolerance(self) -> float:
        """ Returns the tolerance to compare floating point numbers.

            :return: The tolerance to compare floating point numbers.
        """
        return self.__tolerance

    @tolerance.setter
    def tolerance(self, tolerance: float):
        """ Sets the tolerance to compare floating point numbers.
        """
        # Set the tolerance to a positive number.
        self.__tolerance = abs(float(tolerance))

    @tolerance.deleter
    def tolerance(self):
        """ Deletes the parameter.
        """
        del self.__tolerance

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Public Interface.
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # --------------------------------------------------------------------------
    # Plot Results.
    # --------------------------------------------------------------------------

    def print_results(self, file_path: str):
        """ Saves the results, with the information, to the given file.

            :param file_path: The string with the full path of where the file
             with the information must be stored.
        """

        # ----------------------------------------------------------------------
        # Auxiliary variables.
        # ----------------------------------------------------------------------

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
                # Get the maximum column width with the proper formatting.
                for i0, entry in enumerate(statistic0):
                    # The first entry if formatted differently.
                    if i0 > 0:
                        # At most 10 significant figures.
                        columns_width0[i0] = max(columns_width0[i0], len(f"{statistic0[i0]:0.10f}"))\

                        continue

                    # At most three significant figures.
                    columns_width0[i0] = max(columns_width0[i0], len(f"{statistic0[i0]:0.3f}"))

            return columns_width0

        # ----------------------------------------------------------------------
        # Implementation.
        # ----------------------------------------------------------------------

        # Auxiliary variables.
        h_string = []

        # Set the table preheader.
        preheader = ",".join([f"seed={self.seed}", f"repetitions(n)={self.repetitions}",
                              f"maximum time={self.maximum_time}", f"length={self.length}"
                              ])

        # Set the table header.
        header = ["attemps/n", "successes/n", "singlets/n", "doublets/n", "triplets/n"]

        # Get the column widths.
        colum_widths = get_colum_widths(header, self.statistics_table)

        # Open the file and write it.
        with open(file_path, "w") as fl:
            # Write the pre-header string.
            fl.write(preheader + "\n")

            # Format the header string.
            for i, value in enumerate(colum_widths):
                # Get each formatted entry
                h_string.append(f"{header[i]:<{value + 2}}")

            # Write the header string.
            fl.write(",".join(h_string) + "\n")

            # Write the statistics.
            for statistic in self.statistics_table:
                # Declare an empty array.
                h_string = []
                # Format the header string.
                for i, value in enumerate(colum_widths):
                    # Get each formatted entry
                    h_string.append(f"{statistic[i]:<0.{value}f}")

                # Write the statistic string.
                fl.write(",".join(h_string) + "\n")



    # --------------------------------------------------------------------------
    # Run Simulation Methods.
    # --------------------------------------------------------------------------

    def run_simulation(self):
        """ Runs the simulation the number of specified times by the repetition
            parameter.
        """

        # ----------------------------------------------------------------------
        # Auxiliary variables.
        # ----------------------------------------------------------------------

        def run_single_simulation():
            """ Runs a single simulation.
            """

            # ----------------------------------------------------------------------
            # Set the initial values.
            # ----------------------------------------------------------------------

            # Reset the simulation variables.
            self._reset_simulation_variables()

            # Initialize the elapsed time.
            elapsed_time = 0

            # ----------------------------------------------------------------------
            # Run the simulation.
            # ----------------------------------------------------------------------

            while elapsed_time < self.maximum_time:
                # Try to adsorb a particle.
                self._adsorb()

                # Always try to record the statistics.
                self._record_statistics()

                # Get the elapsed time.
                elapsed_time = self.attempts / self.length

        # ----------------------------------------------------------------------
        # Implementation.
        # ----------------------------------------------------------------------

        # Always empty the statistics array.
        self.statistics_table = None

        # For the requested number of times.
        for _ in range(self.repetitions):
            # Run a single simulation.
            run_single_simulation()

        # Normalize the statistics.
        self._record_statistics(self.repetitions)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Private Interface.
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # --------------------------------------------------------------------------
    # Fix Methods.
    # --------------------------------------------------------------------------

    def _fix_index(self, index: int) -> int:
        """ Given an index, either positive or negative, fixes it to be an index
            within the lattice.

            :param index: An integer that represents a periodic index within the
             lattice.

            :return: An index such that is in the range [0, self.length).
        """

        # If the index is negative.
        while index < 0:
            # Add the length.
            index += self.length

        return index % self.length

    # --------------------------------------------------------------------------
    # Get Methods.
    # --------------------------------------------------------------------------

    def _get_almost_equal(self, number0: float, number1: float):
        """ Determines if two numbers are equal within the tolerance limit.

            :param number0: The base number for comparison.

            :param number1: The other number for comparison.

            :return: True if the numbers are equal within the given tolerance.
             False, otherwise.
        """

        # If the first number is zero.
        if number0 == 0.0:
            return abs(number1) <= self.tolerance

        # Otherwise.
        return abs((number0 - number1)/ number1) <= self.tolerance

    def _get_can_adsorb(self, site: int) -> bool:
        """ Determines if the given site can adsorb a particle.

            :param site: The site to be examined. Must be an integer number.

            :return: If the site is empty and its inmediate neighbors are empty.
        """

        # Get the current site.
        if not self.lattice[self._fix_index(site)] == RSA.EMPTY:
            return False

        # Get the previous site.
        if not self.lattice[self._fix_index(site - 1)] == RSA.EMPTY:
            return False

        # Get the next site.
        if not self.lattice[self._fix_index(site + 1)] == RSA.EMPTY:
            return False

        return True

    def _get_empty_doublets(self):
        """ Gets the number of sites that are empty and whose right neighbor is
            empty.

            :return: The number of sites that are empty and whose right neighbor
             is empty.
        """

        # Counter to store the number of triplets.
        counter = 0

        # For every site.
        for i, site in enumerate(self.lattice):

            # Get the current site.
            if not self.lattice[self._fix_index(i)] == RSA.EMPTY:
                continue

            # Get the next site.
            if not self.lattice[self._fix_index(i + 1)] == RSA.EMPTY:
                continue

            # Add to the counter if needed.
            counter += 1

        return counter

    def _get_empty_singlets(self):
        """ Gets the number of sites that are empty.

            :return: The number of sites that are empty.
        """

        # Counter to store the number of triplets.
        counter = 0

        # For every site.
        for i, site in enumerate(self.lattice):

            # Get the current site.
            if not self.lattice[self._fix_index(i)] == RSA.EMPTY:
                continue

            # Add to the counter if needed.
            counter += 1

        return counter

    def _get_empty_triplets(self):
        """ Gets the number of sites that are empty and whose neighbors are
            empty.

            :return: The number of sites that are empty and whose neighbors are
             empty.
        """

        # Counter to store the number of triplets.
        counter = 0

        # For every site.
        for i, site in enumerate(self.lattice):

            # Get the previous site.
            if not self.lattice[self._fix_index(i - 1)] == RSA.EMPTY:
                continue

            # Get the current site.
            if not self.lattice[self._fix_index(i)] == RSA.EMPTY:
                continue

            # Get the next site.
            if not self.lattice[self._fix_index(i + 1)] == RSA.EMPTY:
                continue

            # Add to the counter if needed.
            counter += 1

        return counter

    # --------------------------------------------------------------------------
    # Process Methods.
    # --------------------------------------------------------------------------

    def _adsorb(self):
        """ Tries to perform an adsorption operation; i.e., select a random site
            in the lattice onto which to adsorb.
        """

        # Choose a site where to adsorb.
        site = self.generator(0, self.length - 1)

        # Add one to the counter.
        self.attempts += 1

        # Attempt to adsorb a particle.
        if self._get_can_adsorb(site):
            # Adsorb a particle.
            self.lattice[site] = RSA.OCCUPIED

            # Add to the successful adsorption counter.
            self.attempts_successful += 1

    def _record_statistics(self, number_simulations: int = None):
        """ Records the statistics.

            :param number_simulations: The number of simulationms with
             which to take the average.
        """

        # ----------------------------------------------------------------------
        # Auxiliary functions.
        # ----------------------------------------------------------------------

        def normalize_results(number_simulations0: int):
            """ Averages the final results with the number of simulations.

                :param number_simulations0: The number of simulationms with
                 which to take the average.
            """

            # For all the entries.
            for i, _ in enumerate(self.statistics_table):
                # Divide the number of successful attempts by the number of simulations.
                self.statistics_table[i][1] /= number_simulations0

                # Divide the number of remaining singlets by the number of simulations.
                self.statistics_table[i][2] /= number_simulations0

                # Divide the number of remaining doublets by the number of simulations.
                self.statistics_table[i][3] /= number_simulations0

                # Divide the number of remaining triplets by the number of simulations.
                self.statistics_table[i][4] /= number_simulations0

        # ----------------------------------------------------------------------
        # Implementation.
        # ----------------------------------------------------------------------

        # If the normalization is requested.
        if number_simulations is not None:
            # Normalize the results.
            normalize_results(number_simulations)

            return

        # Only take statistics so often.
        if not (10 * self.attempts) % self.length == 0:
            return

        # ----------------------------------------------------------------------
        # Set the proper variables.
        # ----------------------------------------------------------------------

        # Get the elapsed time.
        elapsed_time = self.attempts / self.length

        # Successful Attempts.
        successful = self.attempts_successful / self.length

        # Get the number of empty singlets.
        singlets = self._get_empty_singlets() / self.length

        # Get the number of doublets.
        doublets = self._get_empty_doublets() / self.length

        # Get the number of triplets.
        triplets = self._get_empty_triplets() / self.length

        # Go through all the entries.
        for i, statistic in enumerate(self.statistics_table):
            # If the time already exists, add it to the simulation.
            if self._get_almost_equal(elapsed_time, statistic[0]):
                # Add to the successful attempts.
                self.statistics_table[i][1] += successful

                # Add to the singlets.
                self.statistics_table[i][2] += singlets

                # Add to the doublets.
                self.statistics_table[i][3] += doublets

                # Add to the triplets.
                self.statistics_table[i][4] += triplets

                return

        # Add an entry.
        self.statistics_table.append([elapsed_time, successful, singlets, doublets, triplets])

    # --------------------------------------------------------------------------
    # Reset Methods.
    # --------------------------------------------------------------------------

    def _reset_simulation_variables(self):
        """ Resets the variables for a single simulation to their initial state.
        """

        # Reset the lattice.
        for i in range(self.length):
            # Set all the particles to empty.
            self.lattice[i] = RSA.EMPTY

        # ----------------------------------------------------------------------
        # Reset the counters.
        # ----------------------------------------------------------------------

        # The attempts counter.
        self.attempts = 0

        # The successful attempts counter.
        self.attempts_successful = 0

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Constructor and Dunder Methods.
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # --------------------------------------------------------------------------
    # Constructor.
    # --------------------------------------------------------------------------

    def __init__(self, length: int, maximum_time: float, repetitions: int = 1000, seed: int = None):
        """ Initializes the simulation parameters.

            :param length: The number of cells the lattice must have.

            :param maximum_time: The maximum time the simulation will run for.

            :param repetitions: The number of times over which to average the
             simulations.

            :param seed: The seed to be used in the random number generator;
             None, by default.
        """

        # ----------------------------------------------------------------------
        # Counters.
        # ----------------------------------------------------------------------

        # Set the number of attempts counter.
        self.attempts = 0

        # Set the number of successful attempts counter.
        self.attempts_successful = 0

        # Set the maximum simulation time.
        self.maximum_time = maximum_time

        # Set the number of times the simulation must be performed.
        self.repetitions = repetitions

        # ----------------------------------------------------------------------
        # Lattice parameters.
        # ----------------------------------------------------------------------

        # Set the length of the lattice.
        self.length = length

        # Set the lattice.
        self.lattice = self.length

        # ----------------------------------------------------------------------
        # Random number generator parameters.
        # ----------------------------------------------------------------------

        # Set the seed for the system to None.
        self.seed = seed

        # Initialize the random number generator.
        self.generator = seed

        # ----------------------------------------------------------------------
        # Other simulation parameters.
        # ----------------------------------------------------------------------

        # Empty the statictics list.
        self.statistics_table = None

        # Set the tolerance.
        self.tolerance = 1.0 * 10**(-5)

    # --------------------------------------------------------------------------
    # Dunder Methods.
    # --------------------------------------------------------------------------


# Code executes here.
if __name__ == '__main__':

    a = RSA(50, 0.15)

    a.run_simulation(0)

    print(a.attempts/a.length)

    print(a.attempts_successful/a.length)