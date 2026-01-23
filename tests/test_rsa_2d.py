""" File that contains the tests for the RSA2D class."""

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------

# Imports: General.
import copy
import itertools
import numpy
import random
import unittest

# Imports: User-defined classes.
from stochastic.classes.rsa_2d.dimers import Dimers

from stochastic.utilities.rsa_parameters import RSA2DParameters

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
        parameters.dimensions = (20, 20)
        parameters.periodic = (True, True)
        parameters.maximum_time = 0.15
        parameters.repetitions = 10_000

        # Create the simulation.
        simulation = Dimers(parameters)

        # //////////////////////////////////////////////////////////////////////
        # Tests
        # //////////////////////////////////////////////////////////////////////

        # Choose 10 unique sites.
        indexes_list = set()
        while len(indexes_list) < 10:
            indexes_ = random.randint(0, simulation.dimensions[0] - 1), random.randint(0, simulation.dimensions[1] - 1)
            indexes_list.add(indexes_)

        for indexes in indexes_list:
            simulation.lattice[indexes[0]][indexes[1]] = simulation.OCCUPIED

        self.assertEqual(simulation.get_coverage(), len(indexes_list))

    def test_normalize_site(self):
        """ Tests that indexes are correctly fixed to indexes between the
            lattice.
        """

        # //////////////////////////////////////////////////////////////////////
        # System setup.
        # //////////////////////////////////////////////////////////////////////

        # Define the length.
        parameters = RSA2DParameters()
        parameters.dimensions = (20, 20)
        parameters.periodic = (False, False)
        parameters.maximum_time = 0.15
        parameters.repetitions = 10_000

        # Create the simulation.
        simulation = Dimers(parameters)

        # //////////////////////////////////////////////////////////////////////
        # Tests
        # //////////////////////////////////////////////////////////////////////

        # Change to both indexes periodic.
        simulation.periodic = (True, True)
        for indexes in itertools.product(*[range(i) for i in simulation.dimensions]):
            indexes_ = simulation.normalize_site(indexes)
            self.assertEqual(indexes, indexes_)

        indexes = (-1, -1)
        indexes_ = (simulation.dimensions[0] - 1, simulation.dimensions[1] - 1)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (20, -1)
        indexes_ = 0, simulation.dimensions[1] - 1
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (-1, 20)
        indexes_ = simulation.dimensions[0] - 1, 0
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (20, 20)
        indexes_ = 0, 0
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        # Change to only x periodic index.
        simulation.periodic = (True, False)

        indexes = (-1, 4)
        indexes_ = (simulation.dimensions[0] - 1, 4)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (20, 4)
        indexes_ = (0, 4)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (-1, -1)
        indexes_ = (simulation.dimensions[0] - 1, -1)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (20, -1)
        indexes_ = (0, -1)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (-1, -1)
        indexes_ = (simulation.dimensions[0] - 1, -1)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (20, 30)
        indexes_ = (0, 30)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        # Change to only y periodic index.
        simulation.periodic = (False, True)

        indexes = (4, -1)
        indexes_ = (4, simulation.dimensions[1] - 1)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (4, 20)
        indexes_ = (4, 0)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (-1, -1)
        indexes_ = (-1, simulation.dimensions[1] - 1)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (-1, 20)
        indexes_ = (-1, 0)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (-1, -1)
        indexes_ = (-1, simulation.dimensions[1] - 1)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        indexes = (30, 20)
        indexes_ = (30, 0)
        indexes = simulation.normalize_site(indexes)
        self.assertEqual(indexes, indexes_)

        # No periodic indexes.
        simulation.periodic = (False, False)
        indexes_list = set()
        dims = simulation.dimensions
        for i in range(50):
            indexes_ = -random.randint(-10, -1), random.randint(0, dims[1] - 1)
            indexes_list.add(copy.deepcopy(indexes_))

            indexes_ = random.randint(dims[0], 2 * dims[0]), random.randint(0, dims[1] - 1)
            indexes_list.add(copy.deepcopy(indexes_))

            indexes_ = random.randint(0, dims[0] - 1), -random.randint(-10, -1)
            indexes_list.add(copy.deepcopy(indexes_))

            indexes_ = random.randint(0, dims[0] - 1), random.randint(dims[1], 2 * dims[1])
            indexes_list.add(copy.deepcopy(indexes_))

            indexes_ = random.randint(-10, -1), random.randint(-10, -1)
            indexes_list.add(copy.deepcopy(indexes_))

            indexes_ = random.randint(dims[0], 2 * dims[0]), random.randint(dims[1], 2 * dims[1])
            indexes_list.add(copy.deepcopy(indexes_))

            indexes_ = random.randint(-10, -1), random.randint(dims[1], 2 * dims[1])
            indexes_list.add(copy.deepcopy(indexes_))

            indexes_ = random.randint(dims[0], 2 * dims[0]), random.randint(-10, -1),
            indexes_list.add(copy.deepcopy(indexes_))

        for indexes in indexes_list:
            indexes_1 = simulation.normalize_site(indexes)
            self.assertEqual(indexes, indexes_1)

        for indexes in itertools.product(*[range(i) for i in simulation.dimensions]):
            indexes_ = simulation.normalize_site(indexes)
            self.assertEqual(indexes, indexes_)

    def test_validate_adsorb(self):
        """ Checks the function that determines whether a particle can be
            adsorbed is valid.
        """

        # //////////////////////////////////////////////////////////////////////
        # System setup.
        # //////////////////////////////////////////////////////////////////////

        # Define the length.
        parameters = RSA2DParameters()
        parameters.dimensions = (20, 20)
        parameters.periodic = (False, False)
        parameters.maximum_time = 0.15
        parameters.repetitions = 10_000

        # Create the simulation.
        simulation = Dimers(parameters)

        # //////////////////////////////////////////////////////////////////////
        # Tests
        # //////////////////////////////////////////////////////////////////////

        # With an empty lattice, it must be possible to adsorb anywhere.
        simulation.periodic = (True, True)
        for site_0 in itertools.product(*[range(i) for i in simulation.dimensions]):
            for indexes in numpy.array([[1, 0], [-1, 0], [0, 1], [0, -1]], dtype=int):
                site_1 = tuple(map(int, indexes + site_0))
                site_1 = simulation.normalize_site(site_1)
                self.assertTrue(simulation.validate_adsorb(site_0, site_1))

        # With an empty lattice, it must be possible to adsorb anywhere.
        simulation.periodic = (False, True)
        for site_0 in itertools.product(*[range(i) for i in simulation.dimensions]):
            for indexes in numpy.array([[1, 0], [-1, 0], [0, 1], [0, -1]], dtype=int):
                site_1 = tuple(map(int, indexes + site_0))
                site_1 = simulation.normalize_site(site_1)
                if simulation.validate_in_lattice(site_1):
                    self.assertTrue(simulation.validate_adsorb(site_0, site_1))
                    continue

                self.assertFalse(simulation.validate_adsorb(site_0, site_1))

        # With an empty lattice, it must be possible to adsorb anywhere.
        simulation.periodic = (True, False)
        for site_0 in itertools.product(*[range(i) for i in simulation.dimensions]):
            for indexes in numpy.array([[1, 0], [-1, 0], [0, 1], [0, -1]], dtype=int):
                site_1 = tuple(map(int, indexes + site_0))
                site_1 = simulation.normalize_site(site_1)
                if simulation.validate_in_lattice(site_1):
                    self.assertTrue(simulation.validate_adsorb(site_0, site_1))
                    continue

                self.assertFalse(simulation.validate_adsorb(site_0, site_1))

        # With an empty lattice, it must be possible to adsorb anywhere.
        simulation.periodic = (False, False)
        for site_0 in itertools.product(*[range(i) for i in simulation.dimensions]):
            for indexes in numpy.array([[1, 0], [-1, 0], [0, 1], [0, -1]], dtype=int):
                site_1 = tuple(map(int, indexes + site_0))
                site_1 = simulation.normalize_site(site_1)
                if simulation.validate_in_lattice(site_1):
                    self.assertTrue(simulation.validate_adsorb(site_0, site_1))
                    continue

                self.assertFalse(simulation.validate_adsorb(site_0, site_1))


# Executes the tests.
if __name__ == '__main__':
    unittest.main()
