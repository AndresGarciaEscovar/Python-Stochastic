import copy as cp
from stochastic.Classes.dimers import Dimers
from stochastic.Utilities.RSA_analysis import RSAResultsAnalysis
from stochastic.Utilities.RSA_parameters import RSAParameters


parameters = RSAParameters()

# Set the length.
parameters.length = 25

# Set the maximum time.
parameters.maximum_time = 6.0

# Set the number of repetitions.
parameters.repetitions = 1007
parameters.periodic = True
parameters.tolerance = 1.0*10**(-5)

simulation = Dimers(parameters)
simulation.run_simulation()
RSAResultsAnalysis.plot_results("results.txt")
RSAResultsAnalysis.plot_lattices("lattice.txt")
