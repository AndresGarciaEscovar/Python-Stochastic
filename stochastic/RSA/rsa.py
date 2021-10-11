""" Contains the class to simulate random sequential adsorption with nearest
    neighbor exclusion for a periodic lattice.
"""

# ------------------------------------------------------------------------------
# Imports.
# ------------------------------------------------------------------------------

# Module to get random numbers.
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
        del self.__attempts_successful

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

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Public Interface.
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    def run_simulation(self, simulation_number: int):
        """ Runs a single simulation.
            :param simulation_number: The identification of the simulation; must
             be zero or a positive number.
        """

        # ----------------------------------------------------------------------
        # Auxiliary functions.
        # ----------------------------------------------------------------------

        def validate_parameters(simulation_number0: int):
            """ Validates that the simulation number is a positive integer.
                :param simulation_number0: The identification of the simulation;
                 must be zero or a positive number.
            """

            # Check it is an integer.
            if not isinstance(simulation_number0, (int,)):
                raise TypeError("The simulation number must be an integer.")

            # Check it is an integer.
            elif not simulation_number0 >= 0:
                raise ValueError("The simulation number must be a zero or"
                                 "positive number.")

        # ----------------------------------------------------------------------
        # Implementation.
        # ----------------------------------------------------------------------

        # Validate the parameters.
        validate_parameters(simulation_number)

        # ----------------------------------------------------------------------
        # Set the initial values.
        # ----------------------------------------------------------------------

        # Reset the number of attempts.
        self.attempts = 0

        # Reset the number of successful attempts.
        self.attempts_successful = 0

        # Reset the lattice particles.
        for i in range(self.length):
            self.lattice[i] = RSA.EMPTY

        # Initialize the elapsed time.
        elapsed_time = 0

        # ----------------------------------------------------------------------
        # Run the simulation.
        # ----------------------------------------------------------------------

        while elapsed_time < self.maximum_time:
            # Try to adsorb a particle.
            self._adsorb()

            # Get the elapsed time.
            elapsed_time = self.attempts / self.length

            print(f"{elapsed_time:1.5f}")

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

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Constructor and Dunder Methods.
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # --------------------------------------------------------------------------
    # Constructor.
    # --------------------------------------------------------------------------

    def __init__(self, length: int, maximum_time: float, seed: int = None):
        """ Initializes the simulation parameters.

            :param length: The number of cells the lattice must have.

            :param maximum_time: The maximum time the simulation will run for.

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

        self.maximum_time = maximum_time

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

    # --------------------------------------------------------------------------
    # Dunder Methods.
    # --------------------------------------------------------------------------


# Code executes here.
if __name__ == '__main__':

    a = RSA(50, 0.15)

    a.run_simulation(0)

    print(a.attempts/a.length)

    print(a.attempts_successful/a.length)