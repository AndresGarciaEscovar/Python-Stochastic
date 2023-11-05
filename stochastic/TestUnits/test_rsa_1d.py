""" File that contains the tests for the RSA1D class."""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Imports: General.
import random
import unittest

# Imports: User-defined classes.
from stochastic.Classes.RSA1D.dimers import Dimers
from stochastic.Classes.RSA1D.nn_exclusion import NNExclusion

from stochastic.Utilities.RSA_parameters import RSA1DParameters

# ------------------------------------------------------------------------------
# Classes.
# ------------------------------------------------------------------------------


class TestRSANNExclusion(unittest.TestCase):

    def test_count_doublets(self):
        """ Tests that counting empty triplets is valid.
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

        # Count the doublets when all the sites are empty.
        self.assertEqual(parameters.length, simulation.get_empty_nts(2))

        # Count the doublets when there is a single particle.
        simulation.lattice[5] = NNExclusion.OCCUPIED
        self.assertEqual(parameters.length - 2, simulation.get_empty_nts(2))

        # Count the doublets when there are two separated particles.
        simulation.lattice[5] = NNExclusion.OCCUPIED
        simulation.lattice[0] = NNExclusion.OCCUPIED
        self.assertEqual(parameters.length - 4, simulation.get_empty_nts(2))

        # Count the doublets when there are two adjacent particles.
        simulation.lattice[0] = NNExclusion.EMPTY
        simulation.lattice[5] = NNExclusion.OCCUPIED
        simulation.lattice[4] = NNExclusion.OCCUPIED
        self.assertEqual(parameters.length - 3, simulation.get_empty_nts(2))

        # Count the doublets with two particles separated by an empty site.
        simulation.lattice[4] = NNExclusion.EMPTY
        simulation.lattice[5] = NNExclusion.OCCUPIED
        simulation.lattice[7] = NNExclusion.OCCUPIED
        self.assertEqual(parameters.length - 4, simulation.get_empty_nts(2))

    def test_count_singlets(self):
        """ Tests that counting empty singlets is valid.
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

        # Count the singlets when all the sites are empty.
        self.assertEqual(parameters.length, simulation.get_empty_nts(1))

        # Count the singlets when there is a single particle.
        simulation.lattice[5] = NNExclusion.OCCUPIED
        self.assertEqual(parameters.length - 1, simulation.get_empty_nts(1))

        # Count the singlets when there are two separated particles.
        simulation.lattice[5] = NNExclusion.OCCUPIED
        simulation.lattice[0] = NNExclusion.OCCUPIED
        self.assertEqual(parameters.length - 2, simulation.get_empty_nts(1))

        # Count the singlets when there are two adjacent particles.
        simulation.lattice[0] = NNExclusion.EMPTY
        simulation.lattice[5] = NNExclusion.OCCUPIED
        simulation.lattice[4] = NNExclusion.OCCUPIED
        self.assertEqual(parameters.length - 2, simulation.get_empty_nts(1))

        # Count the singlets with two particles separated by an empty site.
        simulation.lattice[4] = NNExclusion.EMPTY
        simulation.lattice[5] = NNExclusion.OCCUPIED
        simulation.lattice[7] = NNExclusion.OCCUPIED
        self.assertEqual(parameters.length - 2, simulation.get_empty_nts(1))

    def test_count_triplets(self):
        """ Tests that counting empty triplets is valid.
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

        # Count the triplets when there are no particles.
        self.assertEqual(parameters.length, simulation.get_empty_nts(3))

        # Count the triplets when there is a single particle.
        simulation.lattice[5] = NNExclusion.OCCUPIED
        self.assertEqual(parameters.length - 3, simulation.get_empty_nts(3))

        # Count the triplets when there are two separated particles.
        simulation.lattice[5] = NNExclusion.OCCUPIED
        simulation.lattice[0] = NNExclusion.OCCUPIED
        self.assertEqual(parameters.length - 6, simulation.get_empty_nts(3))

        # Count the triplets when there are two adjacent particles.
        simulation.lattice[0] = NNExclusion.EMPTY
        simulation.lattice[5] = NNExclusion.OCCUPIED
        simulation.lattice[4] = NNExclusion.OCCUPIED
        self.assertEqual(parameters.length - 4, simulation.get_empty_nts(3))

        # Count the triplets with two particles separated by an empty site.
        simulation.lattice[4] = NNExclusion.EMPTY
        simulation.lattice[5] = NNExclusion.OCCUPIED
        simulation.lattice[7] = NNExclusion.OCCUPIED
        self.assertEqual(parameters.length - 5, simulation.get_empty_nts(3))

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


class TestRSADimers(unittest.TestCase):

    def test_count_doublets(self):
        """ Tests that counting empty triplets is valid.
        """

        # //////////////////////////////////////////////////////////////////////
        # System setup.
        # //////////////////////////////////////////////////////////////////////

        # Define the length.
        parameters = RSA1DParameters()
        parameters.length = 50
        parameters.maximum_time = 0.15
        parameters.periodic = True
        parameters.repetitions = 10_000

        # Create the simulation.
        simulation = Dimers(parameters)

        # //////////////////////////////////////////////////////////////////////
        # Tests
        # //////////////////////////////////////////////////////////////////////

        # Count the doublets when all the sites are empty.
        self.assertEqual(parameters.length, simulation.get_empty_nts(2))

        # Count the doublets when there is a single particle.
        simulation.lattice[5] = Dimers.OCCUPIED
        self.assertEqual(parameters.length - 2, simulation.get_empty_nts(2))

        # Count the doublets when there are two separated particles.
        simulation.lattice[5] = Dimers.OCCUPIED
        simulation.lattice[0] = Dimers.OCCUPIED
        self.assertEqual(parameters.length - 4, simulation.get_empty_nts(2))

        # Count the doublets when there are two adjacent particles.
        simulation.lattice[0] = Dimers.EMPTY
        simulation.lattice[5] = Dimers.OCCUPIED
        simulation.lattice[4] = Dimers.OCCUPIED
        self.assertEqual(parameters.length - 3, simulation.get_empty_nts(2))

        # Count the doublets with two particles separated by an empty site.
        simulation.lattice[4] = Dimers.EMPTY
        simulation.lattice[5] = Dimers.OCCUPIED
        simulation.lattice[7] = Dimers.OCCUPIED
        self.assertEqual(parameters.length - 4, simulation.get_empty_nts(2))

    def test_count_singlets(self):
        """ Tests that counting empty singlets is valid.
        """

        # //////////////////////////////////////////////////////////////////////
        # System setup.
        # //////////////////////////////////////////////////////////////////////

        # Define the length.
        parameters = RSA1DParameters()
        parameters.length = 50
        parameters.maximum_time = 0.15
        parameters.periodic = True
        parameters.repetitions = 10_000

        # Create the simulation.
        simulation = Dimers(parameters)

        # //////////////////////////////////////////////////////////////////////
        # Tests
        # //////////////////////////////////////////////////////////////////////

        # Count the singlets when all the sites are empty.
        self.assertEqual(parameters.length, simulation.get_empty_nts(1))

        # Count the singlets when there is a single particle.
        simulation.lattice[5] = Dimers.OCCUPIED
        self.assertEqual(parameters.length - 1, simulation.get_empty_nts(1))

        # Count the singlets when there are two separated particles.
        simulation.lattice[5] = Dimers.OCCUPIED
        simulation.lattice[0] = Dimers.OCCUPIED
        self.assertEqual(parameters.length - 2, simulation.get_empty_nts(1))

        # Count the singlets when there are two adjacent particles.
        simulation.lattice[0] = Dimers.EMPTY
        simulation.lattice[5] = Dimers.OCCUPIED
        simulation.lattice[4] = Dimers.OCCUPIED
        self.assertEqual(parameters.length - 2, simulation.get_empty_nts(1))

        # Count the singlets with two particles separated by an empty site.
        simulation.lattice[4] = Dimers.EMPTY
        simulation.lattice[5] = Dimers.OCCUPIED
        simulation.lattice[7] = Dimers.OCCUPIED
        self.assertEqual(parameters.length - 2, simulation.get_empty_nts(1))

    def test_count_triplets(self):
        """ Tests that counting empty triplets is valid.
        """

        # //////////////////////////////////////////////////////////////////////
        # System setup.
        # //////////////////////////////////////////////////////////////////////

        # Define the length.
        parameters = RSA1DParameters()
        parameters.length = 50
        parameters.maximum_time = 0.15
        parameters.periodic = True
        parameters.repetitions = 10_000

        # Create the simulation.
        simulation = Dimers(parameters)

        # //////////////////////////////////////////////////////////////////////
        # Tests
        # //////////////////////////////////////////////////////////////////////

        # Count the triplets when all the sites are empty.
        self.assertEqual(parameters.length, simulation.get_empty_nts(3))

        # Count the triplets when there is a single particle.
        simulation.lattice[5] = Dimers.OCCUPIED
        self.assertEqual(parameters.length - 3, simulation.get_empty_nts(3))

        # Count the triplets when there are two separated particles.
        simulation.lattice[5] = Dimers.OCCUPIED
        simulation.lattice[0] = Dimers.OCCUPIED
        self.assertEqual(parameters.length - 6, simulation.get_empty_nts(3))

        # Count the triplets when there are two adjacent particles.
        simulation.lattice[0] = Dimers.EMPTY
        simulation.lattice[5] = Dimers.OCCUPIED
        simulation.lattice[4] = Dimers.OCCUPIED
        self.assertEqual(parameters.length - 4, simulation.get_empty_nts(3))

        # Count the triplets with two particles separated by an empty site.
        simulation.lattice[4] = Dimers.EMPTY
        simulation.lattice[5] = Dimers.OCCUPIED
        simulation.lattice[7] = Dimers.OCCUPIED
        self.assertEqual(parameters.length - 5, simulation.get_empty_nts(3))

    def test_normalize_index(self):
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
        parameters.periodic = True
        parameters.repetitions = 10_000

        # Create the simulation.
        simulation = Dimers(parameters)

        # //////////////////////////////////////////////////////////////////////
        # Tests
        # //////////////////////////////////////////////////////////////////////

        # Test a site.
        site = -1
        self.assertEqual(parameters.length - 1, simulation.normalize_site(site))

        # Test another site.
        site = -1 - parameters.length
        self.assertEqual(parameters.length - 1, simulation.normalize_site(site))

        # Test another site.
        site = parameters.length
        self.assertEqual(0, simulation.normalize_site(site))

        # Test another site.
        site = parameters.length + 1
        self.assertEqual(1, simulation.normalize_site(site))

        # General test.
        for i in range(100_000):
            self.assertTrue(0 <= simulation.normalize_site(random.randint(-9000, 9000)) < parameters.length)

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
        parameters.periodic = True
        parameters.repetitions = 10_000

        # Create the simulation.
        simulation = Dimers(parameters)

        # //////////////////////////////////////////////////////////////////////
        # Tests
        # //////////////////////////////////////////////////////////////////////

        # With an empty lattice, it must be possible to adsorb anywhere.
        for i in range(simulation.length):
            self.assertTrue(simulation.validate_adsorb(i))

        # Set a particle in a site.
        site = 34
        simulation.lattice[site] = Dimers.OCCUPIED
        for i in range(simulation.length):
            if i == site - 1 or i == site:
                self.assertFalse(simulation.validate_adsorb(i))
                continue

            self.assertTrue(simulation.validate_adsorb(i))

        simulation.lattice[site] = Dimers.EMPTY

        # Set a particle at the origin a site.
        site = 0
        simulation.lattice[site] = Dimers.OCCUPIED
        for i in range(simulation.length):
            if i == simulation.normalize_site(site - 1) or i == simulation.normalize_site(site):
                self.assertFalse(simulation.validate_adsorb(i))

                continue

            self.assertTrue(simulation.validate_adsorb(i))

        simulation.lattice[site] = Dimers.EMPTY

        # Set a particle at the last site.
        site = -1
        simulation.lattice[site] = Dimers.OCCUPIED
        for i in range(simulation.length):
            if i == simulation.normalize_site(site - 1) or i == simulation.normalize_site(site):
                self.assertFalse(simulation.validate_adsorb(i))
                continue

            self.assertTrue(simulation.validate_adsorb(i))


# Executes the tests.
if __name__ == '__main__':
    unittest.main()
