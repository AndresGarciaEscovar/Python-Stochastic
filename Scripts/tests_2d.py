from stochastic.Classes.RSA2D.dimers import Dimers
from stochastic.Classes.RSA2D.nn_exclusion import NNExclusion

from stochastic.Utilities.RSA_analysis import RSA2DResultsAnalysis
from stochastic.Utilities.RSA_parameters import RSA2DParameters

if __name__ == "__main__":
    # Set the parameters.
    parameters = RSA2DParameters()
    parameters.dimensions = (25, 25)
    parameters.periodic = (False, False)
    parameters.maximum_time = 6.0
    parameters.repetitions = 1007
    parameters.tolerance = 1.0*10**(-5)
    parameters.lattice_file = "Dimers_lattice.txt"
    parameters.results_file = "Dimers_results.txt"

    # Run the simulation.
    simulation = Dimers(parameters)
    simulation.run_simulation()

    # Plot the graphs.
    RSA2DResultsAnalysis.plot_results(parameters.results_file)
    RSA2DResultsAnalysis.plot_lattices(parameters.lattice_file)

    # Set the parameters.
    parameters = RSA2DParameters()
    parameters.dimensions = (25, 25)
    parameters.periodic = (False, False)
    parameters.maximum_time = 6.0
    parameters.repetitions = 1007
    parameters.tolerance = 1.0 * 10 ** (-5)
    parameters.lattice_file = "NNExclusion_lattice.txt"
    parameters.results_file = "NNExclusion_results.txt"

    # Run the simulation.
    simulation = NNExclusion(parameters)
    simulation.run_simulation()

    # Plot the graphs.
    RSA2DResultsAnalysis.plot_results(parameters.results_file)
    RSA2DResultsAnalysis.plot_lattices(parameters.lattice_file)
