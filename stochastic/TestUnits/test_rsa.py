""" File that contains the tests for the RSA1D class."""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Imports: General.
import random
import unittest

# Imports: User-defined classes.
from stochastic.RSA1D.rsa import RSA, RSADimer, RSAParameters

# ------------------------------------------------------------------------------
# Classes.
# ------------------------------------------------------------------------------


class TestRSA(unittest.TestCase):

    def test_can_adsorb(self):
        """ Checks the function that determines whether a particle can be
            adsorbed is valid.
        """

        # ----------------------------------------------------------------------
        # Get the simulation.
        # ----------------------------------------------------------------------

        # Define the length.
        length = 50

        # Define the maximum time.
        maximum_time = 0.15

        # Setup the simulation parameters.
        parameters = RSAParameters()

        # The length of the lattice.
        parameters.length = length

        # The maximum time of the simulation.
        parameters.maximum_time = maximum_time

        # Set the number of repetitions to 10_000
        parameters.repetitions = 10_000

        # ----------------------------------------------------------------------
        # Create the simulation.
        # ----------------------------------------------------------------------

        # Create a simulation; the seed doesn't matter.
        simulation = RSA(parameters)

        # ----------------------------------------------------------------------
        # With an empty lattice, it must be possible to adsorb anywhere.
        # ----------------------------------------------------------------------

        # Test every site.
        for i in range(simulation.length):
            self.assertTrue(simulation._get_can_adsorb(i))

        # ----------------------------------------------------------------------
        # Set a particle in a site.
        # ----------------------------------------------------------------------

        # Set the site.
        site = 34

        # Set a particle in the site.
        simulation.lattice[site] = RSA.OCCUPIED

        # Test every site.
        for i in range(simulation.length):
            # Particles cannot be adsorbed in these sites.
            if i == site - 1 or i == site or i == site + 1:
                self.assertFalse(simulation._get_can_adsorb(i))
                continue

            # Otherwise they can be adsorbed.
            self.assertTrue(simulation._get_can_adsorb(i))

        # Remember to empty the site.
        simulation.lattice[site] = RSA.EMPTY

        # ----------------------------------------------------------------------
        # Set a particle at the origin a site.
        # ----------------------------------------------------------------------

        # Set the site.
        site = 0

        # Set a particle in the site.
        simulation.lattice[site] = RSA.OCCUPIED

        # Test every site.
        for i in range(simulation.length):
            # Particles cannot be adsorbed in these sites.
            if i == simulation._fix_index(site - 1) or i == simulation._fix_index(site) or i == simulation._fix_index(site + 1):
                self.assertFalse(simulation._get_can_adsorb(i))

                continue

            # Otherwise they can be adsorbed.
            self.assertTrue(simulation._get_can_adsorb(i))

        # Set a particle in the site.
        simulation.lattice[site] = RSA.EMPTY

        # ----------------------------------------------------------------------
        # Set a particle at the last site.
        # ----------------------------------------------------------------------

        # Set the site.
        site = -1

        # Set a particle in the site.
        simulation.lattice[site] = RSA.OCCUPIED

        # Test every site.
        for i in range(simulation.length):
            # Particles cannot be adsorbed in these sites.
            if i == simulation._fix_index(site - 1) or i == simulation._fix_index(site) or i == simulation._fix_index(site + 1):
                self.assertFalse(simulation._get_can_adsorb(i))

                continue

            # Otherwise they can be adsorbed.
            self.assertTrue(simulation._get_can_adsorb(i))

    def test_count_doublets(self):
        """ Tests that counting empty triplets is valid.
        """

        # ----------------------------------------------------------------------
        # Get the simulation.
        # ----------------------------------------------------------------------

        # Define the length.
        length = 50

        # Define the maximum time.
        maximum_time = 0.15

        # Setup the simulation parameters.
        parameters = RSAParameters()

        # The length of the lattice.
        parameters.length = length

        # The maximum time of the simulation.
        parameters.maximum_time = maximum_time

        # Set the number of repetitions to 10_000
        parameters.repetitions = 10_000

        # ----------------------------------------------------------------------
        # Create the simulation.
        # ----------------------------------------------------------------------

        # Create a simulation; the seed doesn't matter.
        simulation = RSA(parameters)

        # ----------------------------------------------------------------------
        # Count the doublets when all the sites are empty.
        # ----------------------------------------------------------------------

        # There must be as much doublets as sites.
        self.assertEqual(length, simulation._get_empty_doublets())

        # ----------------------------------------------------------------------
        # Count the doublets when there is a single particle.
        # ----------------------------------------------------------------------

        # Set a site with a particle.
        simulation.lattice[5] = RSA.OCCUPIED

        # There must now be 2 less doublets.
        self.assertEqual(length - 2, simulation._get_empty_doublets())

        # ----------------------------------------------------------------------
        # Count the doublets when there are two separated particles.
        # ----------------------------------------------------------------------

        # Set a site with a particle.
        simulation.lattice[5] = RSA.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[0] = RSA.OCCUPIED

        # There must now be 4 less doublets.
        self.assertEqual(length - 4, simulation._get_empty_doublets())

        # ----------------------------------------------------------------------
        # Count the doublets when there are two adjacent particles.
        # ----------------------------------------------------------------------

        # Empty the zeroth site.
        simulation.lattice[0] = RSA.EMPTY

        # Set a site with a particle.
        simulation.lattice[5] = RSA.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[4] = RSA.OCCUPIED

        # There must now be 3 less doublets.
        self.assertEqual(length - 3, simulation._get_empty_doublets())

        # ----------------------------------------------------------------------
        # Count the doublets when there are two particles separated by a empty
        # site.
        # ----------------------------------------------------------------------

        # Set another site with a particle.
        simulation.lattice[4] = RSA.EMPTY

        # Set a site with a particle.
        simulation.lattice[5] = RSA.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[7] = RSA.OCCUPIED

        # There must now be 4 less doublets.
        self.assertEqual(length - 4, simulation._get_empty_doublets())

    def test_count_singlets(self):
        """ Tests that counting empty singlets is valid.
        """

        # ----------------------------------------------------------------------
        # Get the simulation.
        # ----------------------------------------------------------------------

        # Define the length.
        length = 50

        # Define the maximum time.
        maximum_time = 0.15

        # Setup the simulation parameters.
        parameters = RSAParameters()

        # The length of the lattice.
        parameters.length = length

        # The maximum time of the simulation.
        parameters.maximum_time = maximum_time

        # Set the number of repetitions to 10_000
        parameters.repetitions = 10_000

        # ----------------------------------------------------------------------
        # Create the simulation.
        # ----------------------------------------------------------------------

        # Create a simulation; the seed doesn't matter.
        simulation = RSA(parameters)

        # ----------------------------------------------------------------------
        # Count the singlets when all the sites are empty.
        # ----------------------------------------------------------------------

        # There must be as much singlets as sites.
        self.assertEqual(length, simulation._get_empty_singlets())

        # ----------------------------------------------------------------------
        # Count the singlets when there is a single particle.
        # ----------------------------------------------------------------------

        # Set a site with a particle.
        simulation.lattice[5] = RSA.OCCUPIED

        # There must now be 1 less singlet.
        self.assertEqual(length - 1, simulation._get_empty_singlets())

        # ----------------------------------------------------------------------
        # Count the singlets when there are two separated particles.
        # ----------------------------------------------------------------------

        # Set a site with a particle.
        simulation.lattice[5] = RSA.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[0] = RSA.OCCUPIED

        # There must now be 2 less singlets.
        self.assertEqual(length - 2, simulation._get_empty_singlets())

        # ----------------------------------------------------------------------
        # Count the singlets when there are two adjacent particles.
        # ----------------------------------------------------------------------

        # Empty the zeroth site.
        simulation.lattice[0] = RSA.EMPTY

        # Set a site with a particle.
        simulation.lattice[5] = RSA.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[4] = RSA.OCCUPIED

        # There must now be 2 less singlets
        self.assertEqual(length - 2, simulation._get_empty_singlets())

        # ----------------------------------------------------------------------
        # Count the singlets when there are two particles separated by a empty
        # site.
        # ----------------------------------------------------------------------

        # Set another site with a particle.
        simulation.lattice[4] = RSA.EMPTY

        # Set a site with a particle.
        simulation.lattice[5] = RSA.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[7] = RSA.OCCUPIED

        # There must now be 2 less singlets.
        self.assertEqual(length - 2, simulation._get_empty_singlets())

    def test_count_triplets(self):
        """ Tests that counting empty triplets is valid.
        """

        # ----------------------------------------------------------------------
        # Get the simulation.
        # ----------------------------------------------------------------------

        # Define the length.
        length = 50

        # Define the maximum time.
        maximum_time = 0.15

        # Setup the simulation parameters.
        parameters = RSAParameters()

        # The length of the lattice.
        parameters.length = length

        # The maximum time of the simulation.
        parameters.maximum_time = maximum_time

        # Set the number of repetitions to 10_000
        parameters.repetitions = 10_000

        # ----------------------------------------------------------------------
        # Create the simulation.
        # ----------------------------------------------------------------------

        # Create a simulation; the seed doesn't matter.
        simulation = RSA(parameters)

        # ----------------------------------------------------------------------
        # Count the triplets when all the sites are empty.
        # ----------------------------------------------------------------------

        # There must be as much triplets as sites.
        self.assertEqual(length, simulation._get_empty_triplets())

        # ----------------------------------------------------------------------
        # Count the triplets when there is a single particle.
        # ----------------------------------------------------------------------

        # Set a site with a particle.
        simulation.lattice[5] = RSA.OCCUPIED

        # There must now be 3 less triplets.
        self.assertEqual(length - 3, simulation._get_empty_triplets())

        # ----------------------------------------------------------------------
        # Count the triplets when there are two separated particles.
        # ----------------------------------------------------------------------

        # Set a site with a particle.
        simulation.lattice[5] = RSA.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[0] = RSA.OCCUPIED

        # There must now be 6 less triplets.
        self.assertEqual(length - 6, simulation._get_empty_triplets())

        # ----------------------------------------------------------------------
        # Count the triplets when there are two adjacent particles.
        # ----------------------------------------------------------------------

        # Empty the zeroth site.
        simulation.lattice[0] = RSA.EMPTY

        # Set a site with a particle.
        simulation.lattice[5] = RSA.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[4] = RSA.OCCUPIED

        # There must now be 4 less triplets.
        self.assertEqual(length - 4, simulation._get_empty_triplets())

        # ----------------------------------------------------------------------
        # Count the triplets when there are two particles separated by a empty
        # site.
        # ----------------------------------------------------------------------

        # Set another site with a particle.
        simulation.lattice[4] = RSA.EMPTY

        # Set a site with a particle.
        simulation.lattice[5] = RSA.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[7] = RSA.OCCUPIED

        # There must now be 5 less triplets.
        self.assertEqual(length - 5, simulation._get_empty_triplets())

    def test_fix_index(self):
        """ Tests that indexes are correctly fixed to indexes between the
            lattice.
        """

        # ----------------------------------------------------------------------
        # Get the simulation.
        # ----------------------------------------------------------------------

        # Define the length.
        length = 50

        # Define the maximum time.
        maximum_time = 0.15

        # Setup the simulation parameters.
        parameters = RSAParameters()

        # The length of the lattice.
        parameters.length = length

        # The maximum time of the simulation.
        parameters.maximum_time = maximum_time

        # Set the number of repetitions to 10_000
        parameters.repetitions = 10_000

        # ----------------------------------------------------------------------
        # Create the simulation.
        # ----------------------------------------------------------------------

        # Create a simulation; the seed doesn't matter.
        simulation = RSA(parameters)

        # ----------------------------------------------------------------------
        # Test a site.
        # ----------------------------------------------------------------------

        # Set a site.
        site = -1

        # Fix the site.
        self.assertEqual(length - 1,simulation._fix_index(site))

        # ----------------------------------------------------------------------
        # Test another site.
        # ----------------------------------------------------------------------

        # This must also yield the length.
        site = -1 - length

        # Fix the site.
        self.assertEqual(length - 1, simulation._fix_index(site))

        # ----------------------------------------------------------------------
        # Test another site.
        # ----------------------------------------------------------------------

        # This must also yield zero.
        site = length

        # Fix the site.
        self.assertEqual(0, simulation._fix_index(site))

        # ----------------------------------------------------------------------
        # Test another site.
        # ----------------------------------------------------------------------

        # This must also yield 1.
        site = length + 1

        # Fix the site.
        self.assertEqual(1, simulation._fix_index(site))

        # ----------------------------------------------------------------------
        # General test.
        # ----------------------------------------------------------------------

        # Test for several random numbers.
        for i in range(100_000):
            self.assertTrue(0 <= simulation._fix_index(random.randint(-9000, 9000)) < length)


class TestRSADimer(unittest.TestCase):

    def test_can_adsorb(self):
        """ Checks the function that determines whether a particle can be
            adsorbed is valid.
        """

        # ----------------------------------------------------------------------
        # Get the simulation.
        # ----------------------------------------------------------------------

        # Define the length.
        length = 50

        # Define the maximum time.
        maximum_time = 0.15

        # Setup the simulation parameters.
        parameters = RSAParameters()

        # The length of the lattice.
        parameters.length = length

        # The maximum time of the simulation.
        parameters.maximum_time = maximum_time

        # Set the number of repetitions to 10_000
        parameters.repetitions = 10_000

        # ----------------------------------------------------------------------
        # Create the simulation.
        # ----------------------------------------------------------------------

        # Create a simulation; the seed doesn't matter.
        simulation = RSADimer(parameters)

        # ----------------------------------------------------------------------
        # With an empty lattice, it must be possible to adsorb anywhere.
        # ----------------------------------------------------------------------

        # Test every site.
        for i in range(simulation.length):
            self.assertTrue(simulation._get_can_adsorb(i))

        # ----------------------------------------------------------------------
        # Set a particle in a site.
        # ----------------------------------------------------------------------

        # Set the site.
        site = 34

        # Set a particle in the site.
        simulation.lattice[site] = RSADimer.OCCUPIED

        # Test every site.
        for i in range(simulation.length):
            # Particles cannot be adsorbed in these sites.
            if i == site - 1 or i == site:
                self.assertFalse(simulation._get_can_adsorb(i))
                continue

            # Otherwise they can be adsorbed.
            self.assertTrue(simulation._get_can_adsorb(i))

        # Remember to empty the site.
        simulation.lattice[site] = RSADimer.EMPTY

        # ----------------------------------------------------------------------
        # Set a particle at the origin a site.
        # ----------------------------------------------------------------------

        # Set the site.
        site = 0

        # Set a particle in the site.
        simulation.lattice[site] = RSADimer.OCCUPIED

        # Test every site.
        for i in range(simulation.length):
            # Particles cannot be adsorbed in these sites.
            if i == simulation._fix_index(site - 1) or i == simulation._fix_index(site):
                self.assertFalse(simulation._get_can_adsorb(i))

                continue

            # Otherwise they can be adsorbed.
            self.assertTrue(simulation._get_can_adsorb(i))

        # Set a particle in the site.
        simulation.lattice[site] = RSADimer.EMPTY

        # ----------------------------------------------------------------------
        # Set a particle at the last site.
        # ----------------------------------------------------------------------

        # Set the site.
        site = -1

        # Set a particle in the site.
        simulation.lattice[site] = RSADimer.OCCUPIED

        # Test every site.
        for i in range(simulation.length):
            # Particles cannot be adsorbed in these sites.
            if i == simulation._fix_index(site - 1) or i == simulation._fix_index(site):
                self.assertFalse(simulation._get_can_adsorb(i))

                continue

            # Otherwise they can be adsorbed.
            self.assertTrue(simulation._get_can_adsorb(i))

    def test_count_doublets(self):
        """ Tests that counting empty triplets is valid.
        """

        # ----------------------------------------------------------------------
        # Get the simulation.
        # ----------------------------------------------------------------------

        # Define the length.
        length = 50

        # Define the maximum time.
        maximum_time = 0.15

        # Setup the simulation parameters.
        parameters = RSAParameters()

        # The length of the lattice.
        parameters.length = length

        # The maximum time of the simulation.
        parameters.maximum_time = maximum_time

        # Set the number of repetitions to 10_000
        parameters.repetitions = 10_000

        # ----------------------------------------------------------------------
        # Create the simulation.
        # ----------------------------------------------------------------------

        # Create a simulation; the seed doesn't matter.
        simulation = RSADimer(parameters)

        # ----------------------------------------------------------------------
        # Count the doublets when all the sites are empty.
        # ----------------------------------------------------------------------

        # There must be as much doublets as sites.
        self.assertEqual(length, simulation._get_empty_doublets())

        # ----------------------------------------------------------------------
        # Count the doublets when there is a single particle.
        # ----------------------------------------------------------------------

        # Set a site with a particle.
        simulation.lattice[5] = RSADimer.OCCUPIED

        # There must now be 2 less doublets.
        self.assertEqual(length - 2, simulation._get_empty_doublets())

        # ----------------------------------------------------------------------
        # Count the doublets when there are two separated particles.
        # ----------------------------------------------------------------------

        # Set a site with a particle.
        simulation.lattice[5] = RSADimer.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[0] = RSADimer.OCCUPIED

        # There must now be 4 less doublets.
        self.assertEqual(length - 4, simulation._get_empty_doublets())

        # ----------------------------------------------------------------------
        # Count the doublets when there are two adjacent particles.
        # ----------------------------------------------------------------------

        # Empty the zeroth site.
        simulation.lattice[0] = RSADimer.EMPTY

        # Set a site with a particle.
        simulation.lattice[5] = RSADimer.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[4] = RSADimer.OCCUPIED

        # There must now be 3 less doublets.
        self.assertEqual(length - 3, simulation._get_empty_doublets())

        # ----------------------------------------------------------------------
        # Count the doublets when there are two particles separated by a empty
        # site.
        # ----------------------------------------------------------------------

        # Set another site with a particle.
        simulation.lattice[4] = RSADimer.EMPTY

        # Set a site with a particle.
        simulation.lattice[5] = RSADimer.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[7] = RSADimer.OCCUPIED

        # There must now be 4 less doublets.
        self.assertEqual(length - 4, simulation._get_empty_doublets())

    def test_count_singlets(self):
        """ Tests that counting empty singlets is valid.
        """

        # ----------------------------------------------------------------------
        # Get the simulation.
        # ----------------------------------------------------------------------

        # Define the length.
        length = 50

        # Define the maximum time.
        maximum_time = 0.15

        # Setup the simulation parameters.
        parameters = RSAParameters()

        # The length of the lattice.
        parameters.length = length

        # The maximum time of the simulation.
        parameters.maximum_time = maximum_time

        # Set the number of repetitions to 10_000
        parameters.repetitions = 10_000

        # ----------------------------------------------------------------------
        # Create the simulation.
        # ----------------------------------------------------------------------

        # Create a simulation; the seed doesn't matter.
        simulation = RSADimer(parameters)

        # ----------------------------------------------------------------------
        # Count the singlets when all the sites are empty.
        # ----------------------------------------------------------------------

        # There must be as much singlets as sites.
        self.assertEqual(length, simulation._get_empty_singlets())

        # ----------------------------------------------------------------------
        # Count the singlets when there is a single particle.
        # ----------------------------------------------------------------------

        # Set a site with a particle.
        simulation.lattice[5] = RSADimer.OCCUPIED

        # There must now be 1 less singlet.
        self.assertEqual(length - 1, simulation._get_empty_singlets())

        # ----------------------------------------------------------------------
        # Count the singlets when there are two separated particles.
        # ----------------------------------------------------------------------

        # Set a site with a particle.
        simulation.lattice[5] = RSADimer.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[0] = RSADimer.OCCUPIED

        # There must now be 2 less singlets.
        self.assertEqual(length - 2, simulation._get_empty_singlets())

        # ----------------------------------------------------------------------
        # Count the singlets when there are two adjacent particles.
        # ----------------------------------------------------------------------

        # Empty the zeroth site.
        simulation.lattice[0] = RSADimer.EMPTY

        # Set a site with a particle.
        simulation.lattice[5] = RSADimer.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[4] = RSADimer.OCCUPIED

        # There must now be 2 less singlets
        self.assertEqual(length - 2, simulation._get_empty_singlets())

        # ----------------------------------------------------------------------
        # Count the singlets when there are two particles separated by a empty
        # site.
        # ----------------------------------------------------------------------

        # Set another site with a particle.
        simulation.lattice[4] = RSADimer.EMPTY

        # Set a site with a particle.
        simulation.lattice[5] = RSADimer.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[7] = RSADimer.OCCUPIED

        # There must now be 2 less singlets.
        self.assertEqual(length - 2, simulation._get_empty_singlets())

    def test_count_triplets(self):
        """ Tests that counting empty triplets is valid.
        """

        # ----------------------------------------------------------------------
        # Get the simulation.
        # ----------------------------------------------------------------------

        # Define the length.
        length = 50

        # Define the maximum time.
        maximum_time = 0.15

        # Setup the simulation parameters.
        parameters = RSAParameters()

        # The length of the lattice.
        parameters.length = length

        # The maximum time of the simulation.
        parameters.maximum_time = maximum_time

        # Set the number of repetitions to 10_000
        parameters.repetitions = 10_000

        # ----------------------------------------------------------------------
        # Create the simulation.
        # ----------------------------------------------------------------------

        # Create a simulation; the seed doesn't matter.
        simulation = RSA(parameters)

        # ----------------------------------------------------------------------
        # Count the triplets when all the sites are empty.
        # ----------------------------------------------------------------------

        # There must be as much triplets as sites.
        self.assertEqual(length, simulation._get_empty_triplets())

        # ----------------------------------------------------------------------
        # Count the triplets when there is a single particle.
        # ----------------------------------------------------------------------

        # Set a site with a particle.
        simulation.lattice[5] = RSADimer.OCCUPIED

        # There must now be 3 less triplets.
        self.assertEqual(length - 3, simulation._get_empty_triplets())

        # ----------------------------------------------------------------------
        # Count the triplets when there are two separated particles.
        # ----------------------------------------------------------------------

        # Set a site with a particle.
        simulation.lattice[5] = RSADimer.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[0] = RSADimer.OCCUPIED

        # There must now be 6 less triplets.
        self.assertEqual(length - 6, simulation._get_empty_triplets())

        # ----------------------------------------------------------------------
        # Count the triplets when there are two adjacent particles.
        # ----------------------------------------------------------------------

        # Empty the zeroth site.
        simulation.lattice[0] = RSADimer.EMPTY

        # Set a site with a particle.
        simulation.lattice[5] = RSADimer.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[4] = RSADimer.OCCUPIED

        # There must now be 4 less triplets.
        self.assertEqual(length - 4, simulation._get_empty_triplets())

        # ----------------------------------------------------------------------
        # Count the triplets when there are two particles separated by a empty
        # site.
        # ----------------------------------------------------------------------

        # Set another site with a particle.
        simulation.lattice[4] = RSADimer.EMPTY

        # Set a site with a particle.
        simulation.lattice[5] = RSADimer.OCCUPIED

        # Set another site with a particle.
        simulation.lattice[7] = RSADimer.OCCUPIED

        # There must now be 5 less triplets.
        self.assertEqual(length - 5, simulation._get_empty_triplets())

    def test_fix_index(self):
        """ Tests that indexes are correctly fixed to indexes between the
            lattice.
        """

        # ----------------------------------------------------------------------
        # Get the simulation.
        # ----------------------------------------------------------------------

        # Define the length.
        length = 50

        # Define the maximum time.
        maximum_time = 0.15

        # Setup the simulation parameters.
        parameters = RSAParameters()

        # The length of the lattice.
        parameters.length = length

        # The maximum time of the simulation.
        parameters.maximum_time = maximum_time

        # Set the number of repetitions to 10_000
        parameters.repetitions = 10_000

        # ----------------------------------------------------------------------
        # Create the simulation.
        # ----------------------------------------------------------------------

        # Create a simulation; the seed doesn't matter.
        simulation = RSADimer(parameters)

        # ----------------------------------------------------------------------
        # Test a site.
        # ----------------------------------------------------------------------

        # Set a site.
        site = -1

        # Fix the site.
        self.assertEqual(length - 1,simulation._fix_index(site))

        # ----------------------------------------------------------------------
        # Test another site.
        # ----------------------------------------------------------------------

        # This must also yield the length.
        site = -1 - length

        # Fix the site.
        self.assertEqual(length - 1, simulation._fix_index(site))

        # ----------------------------------------------------------------------
        # Test another site.
        # ----------------------------------------------------------------------

        # This must also yield zero.
        site = length

        # Fix the site.
        self.assertEqual(0, simulation._fix_index(site))

        # ----------------------------------------------------------------------
        # Test another site.
        # ----------------------------------------------------------------------

        # This must also yield 1.
        site = length + 1

        # Fix the site.
        self.assertEqual(1, simulation._fix_index(site))

        # ----------------------------------------------------------------------
        # General test.
        # ----------------------------------------------------------------------

        # Test for several random numbers.
        for i in range(100_000):
            self.assertTrue(0 <= simulation._fix_index(random.randint(-9000, 9000)) < length)


# Executes the tests.
if __name__ == '__main__':
    unittest.main()
