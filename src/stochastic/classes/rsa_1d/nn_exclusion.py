""" File that contains the random sequential adsorption with nearest neighbors
    exclusion.
"""

# ------------------------------------------------------------------------------
# Imports.
# ------------------------------------------------------------------------------

# Imports: User-defined.
from stochastic.interfaces.rsa_1d_interface import RSA1D
from stochastic.utilities.rsa_parameters import RSA1DParameters

# ------------------------------------------------------------------------------
# Classes.
# ------------------------------------------------------------------------------


class NNExclusion(RSA1D):
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
            f"RSA Nearest Neighbor Exclusion", f"seed={self.seed}", f"repetitions(n)={self.repetitions}",
            f"maximum time={self.maximum_time}", f"length={self.length}", f"periodic={self.periodic}"
        ])

        return preheader

    # --------------------------------------------------------------------------
    # Process Methods.
    # --------------------------------------------------------------------------

    def process_adsorb(self) -> None:
        """ Tries to perform an adsorption operation; i.e., select a random site
            in the lattice onto which to adsorb.
        """

        site = self.random_generator.integers(0, self.length)
        self.attempts += 1
        if self.validate_adsorb(site):
            self.lattice[site] = RSA1D.OCCUPIED
            self.attempts_successful += 1

    # --------------------------------------------------------------------------
    # Validate Methods.
    # --------------------------------------------------------------------------

    def validate_adsorb(self, site: int) -> bool:
        """ Determines if the given site can adsorb a particle.

            :param site: The site to be examined. Must be an integer number.

            :return: If the site is empty and its inmediate neighbors are empty.
        """

        site_ = self.normalize_site(site)
        if not self.lattice[site_] == RSA1D.EMPTY:
            return False

        examined = {site_}
        if ((site - 1) < 0 and self.periodic) or site > 0:
            site_ = self.normalize_site(site - 1)
            if (site_ not in examined) and not self.lattice[site_] == RSA1D.EMPTY:
                return False

        examined.add(site_)
        if ((site + 1) >= self.length and self.periodic) or (site + 1) < self.length:
            site_ = self.normalize_site(site + 1)
            if (site_ not in examined) and not self.lattice[site_] == RSA1D.EMPTY:
                return False

        return True

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # Constructor and Dunder Methods.
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

    # --------------------------------------------------------------------------
    # Constructor.
    # --------------------------------------------------------------------------

    def __init__(self, parameters: RSA1DParameters):
        """ Initializes the simulation parameters.

            :param parameters: A dataclass that contains the adjustable
             parameters of the simulation.
        """
        super(NNExclusion, self).__init__(parameters)
