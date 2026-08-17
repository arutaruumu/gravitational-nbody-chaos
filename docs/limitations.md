# Limitations

## Newtonian gravity

The model ignores general-relativistic effects, radiation, and relativistic velocities.

## Point masses

Bodies are treated as point particles. Physical radius, internal structure, tides, and material properties are not modeled.

## Softening

Softening removes the singularity at zero separation but modifies the short-range gravitational potential.

## Two dimensions

The default implementation is planar. Three-dimensional dynamics are a future extension.

## Direct summation

The force calculation scales as $(O(N^2)\)$. This limits very large simulations.

## Chaos estimation

The default divergence calculation is a Lyapunov-like diagnostic, not a rigorous maximal Lyapunov exponent.

## Finite precision

Floating-point arithmetic introduces numerical error.

## Finite time

A system may appear stable during a finite simulation window while undergoing instability on longer timescales.

## Interpretation

Numerical evidence of divergence should not automatically be interpreted as proof of global chaos. Conclusions should be restricted to the tested parameter regime and simulation duration.
