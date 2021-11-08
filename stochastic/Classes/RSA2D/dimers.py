""" File that contains the random sequential adsorption of dimers.
"""

# ------------------------------------------------------------------------------
# Imports.
# ------------------------------------------------------------------------------

# Imports: General.
# Imports: User-defined.
from stochastic.Interfaces.RSA_2D_interface import RSA2D
from stochastic.Utilities.RSA_parameters import RSA2DParameters

# ------------------------------------------------------------------------------
# Classes.
# ------------------------------------------------------------------------------


class Dimers(RSA2D):
    """ Class to simulate random sequential adsorption with nearest neighbor
        exclusion for a one-dimensional lattice.

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
            f"RSA Dimer", f"seed={self.seed}", f"repetitions(n)={self.repetitions}",
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
        generator = self.random_generator
        site = (self.random_generator.integers(self.dimensions[0]), self.random_generator.integers(self.dimensions[1]))

        self.attempts += 1
        if self.validate_adsorb(site):
            site_ = self.normalize_site(site + 1)
            self.lattice[site] = RSA2D.OCCUPIED
            self.lattice[site_] = RSA2D.OCCUPIED
            self.attempts_successful += 1

    # --------------------------------------------------------------------------
    # Validate Methods.
    # --------------------------------------------------------------------------

    def validate_adsorb(self, site_0: tuple, site_1: tuple) -> bool:
        """ Determines if the given site can adsorb a particle.

            :param site_0: Number of the zeroth site where the dimer is going to
             be adsorbed.

             :param site_1: Number of the first site where the dimer is going to
             be adsorbed.

            :return: If the site is empty and its inmediate neighbors are empty.
        """

        if not self.lattice[site_0[0]][site_0[1]] == RSA2D.EMPTY:
            return False

        examined = {site_0}
        site_1_ = tuple(
            self.normalize_site(site_1[i], self.dimensions[i]) if self.periodic[i] else site_1[i] for i in site_1
        )

        particle = self.lattice[site_1_[0]][site_1_[1]]
        if self.validate_in_lattice(site_1_) and site_1_ not in examined and particle == RSA2D.EMPTY:
            return True

        return False

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
        super(Dimers, self).__init__(parameters)
