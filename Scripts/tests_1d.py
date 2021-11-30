""" Contains the examples for the 1D systems."""

# ------------------------------------------------------------------------------
# Imports.
# ------------------------------------------------------------------------------

# Imports: User-defined.
from stochastic.Classes.RSA1D.dimers import Dimers
from stochastic.Classes.RSA1D.nn_exclusion import NNExclusion

from stochastic.Utilities.RSA_analysis import RSA1DResultsAnalysis
from stochastic.Utilities.RSA_parameters import RSA1DParameters

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
    parameters = RSA1DParameters()

    # Lattice parameters.
    parameters.length = 25
    parameters.periodic = True

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

    RSA1DResultsAnalysis.plot_results(parameters.results_file)
    RSA1DResultsAnalysis.plot_lattices(parameters.lattice_file)

    # //////////////////////////////////////////////////////////////////////////
    # Nearest Neighbor Exclusion.
    # //////////////////////////////////////////////////////////////////////////

    # --------------------------------------------------------------------------
    # Parameters of the system.
    # --------------------------------------------------------------------------

    # Create the parameters.
    parameters = RSA1DParameters()

    # Lattice parameters.
    parameters.length = 25
    parameters.periodic = True

    # Statistics parameters.
    parameters.maximum_time = 6.0
    parameters.repetitions = 1007
    parameters.tolerance = 1.0*10**(-5)

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

    RSA1DResultsAnalysis.plot_results(parameters.results_file)
    RSA1DResultsAnalysis.plot_lattices(parameters.lattice_file)
