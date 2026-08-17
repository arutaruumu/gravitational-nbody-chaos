# Experiments

## Experiment 1 — Body-count scaling

Run $(N=3,10,50,100,500,1000\)$ where computational resources allow.

Measure runtime and compare with the expected

$$
T(N)\propto N^2.
$$


## Experiment 2 — Integrator comparison

Compare Euler, Leapfrog, and RK4 at matched initial conditions and time step.

Measure:

- maximum relative energy error;
- maximum angular-momentum error;
- runtime;
- final trajectory difference.

## Experiment 3 — Initial-condition perturbation

Run a reference system and a perturbed copy.

Use perturbations such as

$$
10^{-4},10^{-6},10^{-8}.
$$

Plot $(D(t)\)$ and $(\log D(t)\)$.

## Experiment 4 — Initial velocity sweep

Vary the velocity scale and record:

- bound/escaping behavior;
- collision events;
- radial spread;
- final energy.

## Experiment 5 — Time-step convergence

Repeat one configuration with progressively smaller $(\Delta t\)$.

The numerical error should generally decrease as the time step is refined, subject to the method and chaotic amplification.

## Reporting

Each experiment should report parameters, random seeds, runtime environment, measured values, and generated figures.
