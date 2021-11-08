""" File that contains the tests for the RSA2D class."""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Imports: General.
import random
import unittest

# Imports: User-defined classes.
from stochastic.Classes.RSA2D.dimers import Dimers

from stochastic.Utilities.RSA_parameters import RSA2DParameters

# ------------------------------------------------------------------------------
# Classes.
# ------------------------------------------------------------------------------


class TestRSADimers(unittest.TestCase):

    def test_coverage(self):
        """ Tests that counting empty triplets is valid.
        """

        # //////////////////////////////////////////////////////////////////////
        # System setup.
        # //////////////////////////////////////////////////////////////////////

        # Define the length.
        parameters = RSA2DParameters()
        parameters.dimensions = (10, 10)
        parameters.periodic = (False, False)
        parameters.maximum_time = 0.15
        parameters.repetitions = 10_000

        # Create the simulation.
        simulation = Dimers(parameters)

        # //////////////////////////////////////////////////////////////////////
        # Tests
        # //////////////////////////////////////////////////////////////////////

        simulation.process_adsorb()

    @unittest.skip("Skip while refactoring.")
    def test_normalize_site(self):
        """ Tests that indexes are correctly fixed to indexes between the
            lattice.
        """

        # //////////////////////////////////////////////////////////////////////
        # System setup.
        # //////////////////////////////////////////////////////////////////////

        # Define the length.
        parameters = RSA1DParameters()
        parameters.length = 50
        parameters.maximum_time = 0.15
        parameters.repetitions = 10_000

        # Create the simulation.
        simulation = NNExclusion(parameters)

        # //////////////////////////////////////////////////////////////////////
        # Tests
        # //////////////////////////////////////////////////////////////////////

        # Set a site.
        site = -1
        self.assertEqual(parameters.length - 1, simulation.normalize_site(site))

        # This must yield the length.
        site = -1 - parameters.length
        self.assertEqual(parameters.length - 1,  simulation.normalize_site(site))

        # This must yield zero.
        site = parameters.length
        self.assertEqual(0,  simulation.normalize_site(site))

        # This must yield 1.
        site = parameters.length + 1
        self.assertEqual(1,  simulation.normalize_site(site))
        for i in range(100_000):
            self.assertTrue(0 <= simulation.normalize_site(random.randint(-9000, 9000)) < parameters.length)

    @unittest.skip("Skip while refactoring.")
    def test_validate_adsorb(self):
        """ Checks the function that determines whether a particle can be
            adsorbed is valid.
        """

        # //////////////////////////////////////////////////////////////////////
        # System setup.
        # //////////////////////////////////////////////////////////////////////

        # Define the length.
        parameters = RSA1DParameters()
        parameters.length = 50
        parameters.maximum_time = 0.15
        parameters.repetitions = 10_000

        # Create the simulation.
        simulation = NNExclusion(parameters)

        # //////////////////////////////////////////////////////////////////////
        # Tests
        # //////////////////////////////////////////////////////////////////////

        # With an empty lattice, it must be possible to adsorb anywhere.
        for i in range(simulation.length):
            self.assertTrue(simulation.validate_adsorb(i))

        # Set a particle in a site.
        site = 34
        simulation.lattice[site] = NNExclusion.OCCUPIED
        for i in range(simulation.length):
            if i == site - 1 or i == site or i == site + 1:
                self.assertFalse(simulation.validate_adsorb(i))
                continue

            self.assertTrue(simulation.validate_adsorb(i))

        simulation.lattice[site] = NNExclusion.EMPTY

        # Set a particle at the origin a site.
        site = 0
        simulation.lattice[site] = NNExclusion.OCCUPIED
        for i in range(simulation.length):
            valid = i == simulation.normalize_site(site - 1) or i == simulation.normalize_site(site)
            valid = valid or i == simulation.normalize_site(site + 1)
            if valid:
                self.assertFalse(simulation.validate_adsorb(i))
                continue

            self.assertTrue(simulation.validate_adsorb(i))

        simulation.lattice[site] = NNExclusion.EMPTY

        # Set a particle at the last site.
        site = -1
        simulation.lattice[site] = NNExclusion.OCCUPIED
        for i in range(simulation.length):
            valid = i == simulation.normalize_site(site - 1) or i == simulation.normalize_site(site)
            valid = valid or i == simulation.normalize_site(site + 1)
            if valid:
                self.assertFalse(simulation.validate_adsorb(i))
                continue

            self.assertTrue(simulation.validate_adsorb(i))

# Executes the tests.
if __name__ == '__main__':
    unittest.main()
