# Methodology

## 1. Research design

The project follows a computational-experiment workflow:

1. Define a reproducible initial state.
2. Compute Newtonian accelerations.
3. Integrate the equations of motion.
4. Store the trajectory.
5. Evaluate physical conservation laws.
6. Compare nearby trajectories.
7. Detect collisions and escape.
8. Visualize and quantify the results.
9. Repeat under controlled parameter changes.

## 2. Independent variables

The main independent variables are:

- body count \(N\)
- initial velocity scale
- initial spatial distribution
- perturbation amplitude
- time step
- integration method

## 3. Dependent variables

The main measured quantities are:

- runtime
- total-energy relative error
- angular-momentum relative error
- trajectory divergence
- Lyapunov-like rate
- collision count
- escape count
- radial stability measures

## 4. Controls

For comparative experiments, hold constant:

- random seed when appropriate
- mass distribution
- \(G\)
- softening
- simulation duration
- output cadence

Only the intended experimental parameter should change.

## 5. Validation

Validation includes:

- pairwise force symmetry;
- center-of-mass initialization;
- approximate conservation of energy and angular momentum;
- time-step convergence;
- comparison between integrators.

## 6. Reproducibility

Every reported experiment should expose its numerical configuration in the notebook or saved data file.
