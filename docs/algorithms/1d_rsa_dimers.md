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

### Simulation Algorithm - Pseudocode

The

## Program Implementation

### Quick Start

### Setting Up the Environment

### Running the Simulation

### Saving and Loading a Simulation

### Analysis and Results
