from stochastic.Classes.RSA1D.nn_exclusion import NNExclusion 
from stochastic.Classes.RSA1D.dimers import Dimers
from stochastic.Utilities.RSA_analysis import RSA1DResultsAnalysis
from stochastic.Utilities.RSA_parameters import RSAParameters

if __name__ == "__main__":
    # Set the parameters.
    parameters = RSAParameters()
    parameters.length = 25
    parameters.maximum_time = 6.0
    parameters.repetitions = 1007
    parameters.periodic = True
    parameters.tolerance = 1.0*10**(-5)

    # Run the simulation.
    # simulation = Dimers(parameters)
    # simulation.run_simulation()

    # Run the simulation.
    simulation = NNExclusion(parameters)
    simulation.run_simulation()

    # Plot the graphs.
    RSA1DResultsAnalysis.plot_results("results.txt")
    RSA1DResultsAnalysis.plot_lattices("lattice.txt")
