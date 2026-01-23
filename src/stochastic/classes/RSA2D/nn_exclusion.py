""" File that contains the random sequential adsorption of monomers with nearest
    neighbor exclusion.
"""

# ------------------------------------------------------------------------------
# Imports.
# ------------------------------------------------------------------------------

# Imports: General.
import copy as cp

# Imports: User-defined.
from stochastic.interfaces.RSA_2D_interface import RSA2D
from stochastic.utilities.RSA_parameters import RSA2DParameters

# ------------------------------------------------------------------------------
# Classes.
# ------------------------------------------------------------------------------


class NNExclusion(RSA2D):
    """ Class to simulate random sequential adsorption with nearest neighbor
        exclusion for a two-dimensional lattice.

        Inherited parameters:

        - self.attemps: An integer that represents the number of attempts at
          adsorbing a particle.

        - self.attempts_successful: An integer that represents the number of
          successful attempts at adsorbing a particle.

        - self.generator: The random number generator.

        - self.lattice: A list that represents the lattice where the particles
          live.

        - self.lattice_file: The name of the file where the lattice must be
          printed.

        - self.length: A positive integer that represents the length of the
          lattice.

        - self.maximum_time: The maximum time for which the simulation must be
          run.

        - self.repetitions: The number of times the simulation must be run to
          get statistically significant data.

        - self.seed: The seed to seed the random number generator.

        - self.statistics_table: The list where the statistics are kept.

        - self.tolerance: The tolerance to compare the floating point numbers.
    """

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Methods.
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # --------------------------------------------------------------------------
    # Get Methods.
    # --------------------------------------------------------------------------

    def get_preheader(self) -> str:
        """ Returns the pre-header, i.e., the string that contains the
            simulation information.

            :return: The string that represents the pre-header.
        """

        preheader = ",".join([
            f"RSA-2D NN Exclusion", f"seed={self.seed}", f"repetitions(n)={self.repetitions}",
            f"maximum time={self.maximum_time}", f"dimensions={self.dimensions}", f"periodic={self.periodic}"
        ])

        return preheader

    # --------------------------------------------------------------------------
    # Process Methods.
    # --------------------------------------------------------------------------

    def process_adsorb(self) -> None:
        """ Tries to perform an adsorption operation; i.e., select a random site
            in the lattice onto which to adsorb.
        """

        generator = self.random_generator.integers
        site = [generator(0, self.dimensions[i]) for i in range(2)]

        self.attempts += 1
        site = tuple(site)
        if self.validate_adsorb(site):
            self.lattice[site[0]][site[1]] = RSA2D.OCCUPIED
            self.attempts_successful += 1

    # --------------------------------------------------------------------------
    # Validate Methods.
    # --------------------------------------------------------------------------

    def validate_adsorb(self, site: tuple) -> bool:
        """ Determines if the given site can adsorb a particle.

            :param site: The tuple that represents the site where the particle
             is to be adsorbed.

            :return: If the site is empty and its inmediate neighbors are empty.
        """

        if not self.lattice[site[0]][site[1]] == RSA2D.EMPTY:
            return False

        examined = set()
        indexes = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for indexes_ in indexes:
            indexes_ = tuple(index + site[i] for i, index in enumerate(indexes_))
            indexes_ = self.normalize_site(indexes_)
            if self.validate_in_lattice(indexes_):
                examined.add(cp.deepcopy(indexes_))

        valid = True
        for indexes_ in examined:
            valid = valid and self.lattice[indexes_[0]][indexes_[1]] == RSA2D.EMPTY

        return valid

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
        super(NNExclusion, self).__init__(parameters)
