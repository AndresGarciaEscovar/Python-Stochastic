import copy as cp
from stochastic.Classes.RSA_parameters import RSAParameters
from stochastic.Interfaces.RSA_interface import RSA

from stochastic.Classes.RSA_analysis import RSAResultsAnalysis

parameters = RSAParameters()

# Set the length.
parameters.length = 25

# Set the maximum time.
parameters.maximum_time = 6.0

# Set the number of repetitions.
parameters.repetitions = 1007
parameters.periodic = True
parameters.tolerance = 1.0*10**(-5)

simulation = RSA(parameters)
simulation.run_simulation()
RSAResultsAnalysis.plot_lattices("lattice.txt")

print(simulation.validate_adsorb(0))
