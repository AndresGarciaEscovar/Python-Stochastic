import copy as cp
from stochastic.Classes.dimers import Dimers
from stochastic.Utilities.RSA_analysis import RSAResultsAnalysis
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
    simulation = Dimers(parameters)
    simulation.run_simulation()

    # Plot the graphs.
    RSAResultsAnalysis.plot_results("results.txt")
    RSAResultsAnalysis.plot_lattices("lattice.txt")
