import copy as cp
from stochastic.RSA.rsa import RSA, RSADimer, RSAParameters, RSAResultsAnalysis

parameters = RSAParameters()

# Set the length.
parameters.length = 25

# Set the maximum time.
parameters.maximum_time = 6.0

# Set the number of repetitions.
parameters.repetitions = 1007

a = RSA(parameters)

a.run_simulation()

a.print_results("final_results.txt")

RSAResultsAnalysis.plot_lattices("lattice.txt")