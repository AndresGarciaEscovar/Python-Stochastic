from stochastic.Classes.RSA1D.nn_exclusion import NNExclusion 
from stochastic.Classes.RSA1D.dimers import Dimers
from stochastic.Utilities.RSA_analysis import RSA1DResultsAnalysis
from stochastic.Utilities.RSA_parameters import RSA1DParameters

if __name__ == "__main__":
    # Set the parameters.
    parameters = RSA1DParameters()
    parameters.length = 25
    parameters.maximum_time = 6.0
    parameters.repetitions = 1007
    parameters.periodic = True
    parameters.tolerance = 1.0*10**(-5)
    parameters.lattice_file = "Dimers_lattice.txt"
    parameters.results_file = "Dimers_results.txt"

    # Run the simulation.
    simulation = Dimers(parameters)
    simulation.run_simulation()

    # Plot the graphs.
    RSA1DResultsAnalysis.plot_results(parameters.results_file)
    RSA1DResultsAnalysis.plot_lattices(parameters.lattice_file)

    # Set the parameters.
    parameters = RSA1DParameters()
    parameters.length = 25
    parameters.maximum_time = 6.0
    parameters.repetitions = 1007
    parameters.periodic = True
    parameters.tolerance = 1.0*10**(-5)
    parameters.lattice_file = "NNExclusion_lattice.txt"
    parameters.results_file = "NNExclusion_results.txt"

    # Run the simulation.
    simulation = NNExclusion(parameters)
    simulation.run_simulation()

    # Plot the graphs.
    RSA1DResultsAnalysis.plot_results(parameters.results_file)
    RSA1DResultsAnalysis.plot_lattices(parameters.lattice_file)
