# 1D Random Sequential Adsorption (RSA) of Dimers

## Index

- [Introduction](#introduction)
   - [Model Description](#model-description)
   - [Simulation Algorithm - Pseudocode](#simulation-algorithm---pseudocode)
- [Program Implementation](#program-implementation)
   - [Quick Start](#quick-start)
   - [Setting Up the Environment](#setting-up-the-environment)
   - [Running the Simulation](#running-the-simulation)
   - [Saving and Loading a Simulation](#saving-and-loading-a-simulation)
   - [Analysis and Results](#analysis-and-results)

## Introduction

Random sequential adsorption (RSA) is a fundamental process in which particles
are irreversibly, and randomly, deposited onto a substrate. Once particles are
deposited, they cannot be removed or rearranged. As particles are added, the
subtrate becomes populated and eventually saturates, reaching a state where no
more particles can be added due to the constraints of the system.

RSA has been widely used to model various physical, chemical, and biological
processes, such as the adsorption of molecules on surfaces, the packing of
colloidal particles, and the formation of thin films. RSA is useful to
understand some litography techniques where the deposition process follows a
random sequential adsorption mechanism.

### Model Description

<img src="../images/model_1d_rsa_dimers.png" alt="1D RSA of Dimers" width="200"/>

Consider a one-dimensional discrete substrate of length \(`L`\) where particles
can adsorb, but cannot desorb or move once they are adsorbed. The lattice can be
finite or infinite, i.e., in the case of an infinite lattice, it is modeled as a
lattice with periodic boundary conditions, `x = x + L`, where `x` is the
position on the lattice and `L` is the length of the lattice, that is also the
period of the lattice.

Each site can have one of two states: occupied or empty, and each site can only
be occupied by one particle. In this model, two joined particles, i.e., dimers,
are deposited onto the lattice at a constant rate `k`. Since the rate is
constant, `k` can be set to 1 without loss of generality. For a dimer to be
adsorbed, two adjacent sites must be empty. If the deposition attempt is
successful, the two sites become occupied and no more particles can be adsorbed
on those sites. If any of the sites where the particle is trying to adsorb is
already occupied, the deposition attempt fails and the system remains unchanged.

The different quantities to be tracked are defined as follows:

- `L`: Length of the lattice.

- `t`: The physical time of the system, that is proportional to the number of
  of deposition attempts. The proportionality constant is the inverse length of
  the lattice, `1/(kL)`, over the total rate of the system; since the deposition
  rate is set to 1, `k = 1`, it can be simplied to `1/L`.  Thus, the elapsed
  time can be calculated as `t = Na / L`, where `Na` is the number of deposition
  attempts.

- `C(t)`: The coverage of the lattice at time `t`, defined as the fraction of
  occupied sites on the lattice. It is calculated as `C(t) = N(t) / L`, that is
  the percentage of occupied sites, where `N(t)` is the number of occupied sites
  at time `t`.

- `S(t)`: The percentage of single sites that are **NOT** occupied at time `t`.
   Can be calculated as `S(t) = 1 - C(t)`.

- `D(t)`: The percentage of pair sites that are **NOT** occupied at time `t`.
   This gives an idea of how many more dimers can be adsorbed on the lattice at
   time `t`.

- `T(t)`: The percentage of three consecutive sites that are **NOT** occupied at
   time `t`.

A single simulation is not enought to determine the behavior of the system,
since the process is stochastic and there might be multiple outcomes for the
same initial conditions, and number of deposition attempts. Therefore, it is
necessary to perform multiple simulations and average the different ensembles to
obtain a more accurate representation of the system's behavior.

### Simulation Algorithm - Pseudocode

The following pseudocode outlines the algorithm for simulating the 1D RSA of
dimers. Additional actions like saving the state of the system, or data
processing are not included in the pseudocode, but they are implemented in the
program:

1. Define a lattice of length `L` initialized with all sites empty.
1. Setup the variables:
   - The variables where to save the results of `C(t)`, `S(t)`, `D(t)`, and
     `T(t)`.
   - Define a variable where to track the accumulated statistics of the
     different repetitions of the simulation, call it `stats`, that must contain
     the variables to save the accumulated results of `C(t)`, `S(t)`, `D(t)`,
     and `T(t)`.
   - A variable that defines the number of repetitions of the simulation, call
     it `nsims`.
   - A variable that defines the number of deposition attempts, call it
     `nattempts`.
1. For each simulation from `1` to `nsims`:
   1. Empty the lattice and reset the time `t` to `0`.
   1. Empty the statistics variables `C(t)`, `S(t)`, `D(t)`, and `T(t)`.
   1. For each deposition attempt from `1` to `nattempts`:
      1. Increase the number of deposition attempts `Na` by 1, `Na = Na + 1`.
      1. Randomly select a site `i` on the lattice, i.e., a site from `0` to
        `L-1`; because the array indexing starts at `0`.
      1. Attempt to deposit a dimer on the selected site `i` and the adjacent
         site `i+1`. In the case of a periodic lattice, if the selected site is
         `L-1`, the adjacent site will be `0`.
      1. Increase the time `t` by 1, since integer numbers are more accurate to
         track than floating point numbers, and the time can be calculated as
         `t = Na / L`.
      1. Record the values of `C(t)`, `S(t)`, `D(t)`, and `T(t)` at the current
         time `t`.
      1. If the maximum number of deposition attempts is reached, exit the loop;
         otherwise, continue to the next deposition attempt.
   1. Update the `stats` by accumulating the values of `C(t)`, `S(t)`, `D(t)`,
      and `T(t)` at the given times.
   1. Increment the number of simulations performed.
   1. If the maximum number of simulations has been exceeded, exit the loop;
1. Process the accumulated statistics in `stats` to obtain the average values of
   `C(t)`, `S(t)`, `D(t)`, and `T(t)` at the different times.
1. Save the results to a file or display them as needed.
1. Finish the program successfully.

If at any point the simulation crashes, or an error occurs, the program will be
left to fail, and the error message will be printed to the console. Details on
how to run the program, and how to save and load simulations are provided in the
next section.

## Program Implementation

### Quick Start

### Setting Up the Environment

### Running the Simulation

### Saving and Loading a Simulation

### Analysis and Results
