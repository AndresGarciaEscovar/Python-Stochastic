""" Contains the examples for the 2D systems."""

# ------------------------------------------------------------------------------
# Imports.
# ------------------------------------------------------------------------------

# Imports: User-defined.
from stochastic.Classes.RSA2D.dimers import Dimers
from stochastic.Classes.RSA2D.nn_exclusion import NNExclusion

from stochastic.Utilities.RSA_analysis import RSA2DResultsAnalysis
from stochastic.Utilities.RSA_parameters import RSA2DParameters

# ------------------------------------------------------------------------------
# Main Program.
# ------------------------------------------------------------------------------


if __name__ == "__main__":

    # //////////////////////////////////////////////////////////////////////////
    # Dimers.
    # //////////////////////////////////////////////////////////////////////////

    # --------------------------------------------------------------------------
    # Parameters of the system.
    # --------------------------------------------------------------------------

    # Create the parameters.
    parameters = RSA2DParameters()

    # Lattice parameters.
    parameters.dimensions = (25, 25)
    parameters.periodic = (False, False)

    # Statistics parameters.
    parameters.maximum_time = 6.0
    parameters.repetitions = 1007
    parameters.tolerance = 1.0*10**(-5)

    # Save parameters.
    parameters.lattice_file = "Dimers_lattice.txt"
    parameters.results_file = "Dimers_results.txt"

    # --------------------------------------------------------------------------
    # Run the simulation.
    # --------------------------------------------------------------------------

    simulation = Dimers(parameters)
    simulation.run_simulation()

    # --------------------------------------------------------------------------
    # Make the plots.
    # --------------------------------------------------------------------------

    RSA2DResultsAnalysis.plot_results(parameters.results_file)
    RSA2DResultsAnalysis.plot_lattices(parameters.lattice_file)

    # //////////////////////////////////////////////////////////////////////////
    # Nearest Neighbor Exclusion.
    # //////////////////////////////////////////////////////////////////////////

    # --------------------------------------------------------------------------
    # Parameters of the system.
    # --------------------------------------------------------------------------

    # Create the parameters.
    parameters = RSA2DParameters()

    # Lattice parameters.
    parameters.dimensions = (25, 25)
    parameters.periodic = (False, False)

    # Statistics parameters.
    parameters.maximum_time = 6.0
    parameters.repetitions = 1007
    parameters.tolerance = 1.0 * 10 ** (-5)

    # Save parameters.
    parameters.lattice_file = "NNExclusion_lattice.txt"
    parameters.results_file = "NNExclusion_results.txt"

    # --------------------------------------------------------------------------
    # Run the simulation.
    # --------------------------------------------------------------------------

    simulation = NNExclusion(parameters)
    simulation.run_simulation()

    # --------------------------------------------------------------------------
    # Make the plots.
    # --------------------------------------------------------------------------

    RSA2DResultsAnalysis.plot_results(parameters.results_file)
    RSA2DResultsAnalysis.plot_lattices(parameters.lattice_file)
