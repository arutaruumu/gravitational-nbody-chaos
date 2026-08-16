# Gravitational N-Body Chaos Simulator

An open-source computational physics project for studying Newtonian gravitational N-body dynamics, numerical integration, conservation laws, chaotic divergence, orbital stability, collisions, escape trajectories, and computational scaling.

> **Research question:** How do the number of gravitationally interacting bodies and their initial conditions influence dynamical stability, chaotic behavior, and computational cost in Newtonian N-body systems?

## Features

- Direct Newtonian N-body gravity
- Configurable systems from 3 to ~1000 bodies
- Random, binary, and disk-like initial conditions
- Center-of-mass correction
- Leapfrog / Velocity Verlet integration
- Euler and RK4 baselines
- Energy and angular-momentum diagnostics
- Nearby-trajectory divergence
- Lyapunov-like finite-time divergence estimate
- Collision detection
- Distance- and energy-based escape diagnostics
- Orbit, phase-space, conservation, divergence, and animation visualizations
- Reproducible experiments
- Automated unit tests

## Scientific workflow

```text
Initial Conditions
        ↓
Newtonian Gravity
        ↓
Numerical Integrator
        ↓
N-Body Evolution
        ↓
Conservation Diagnostics
        ↓
Chaos / Stability Analysis
        ↓
Collision / Escape Analysis
        ↓
Visualization
        ↓
Reproducible Experiments
```

## Repository structure

- `src/` — reusable simulation and analysis library
- `notebooks/` — explanatory Google Colab/Jupyter research notebooks
- `experiments/` — reproducible experiment scripts
- `tests/` — validation and regression tests
- `docs/` — mathematical and methodological documentation
- `results/` — generated figures and numerical data
- `assets/` — animations and screenshots

## Mathematical model

For body \(i\),

\[
\frac{d^2\mathbf r_i}{dt^2}
=
G\sum_{j\ne i}
m_j
\frac{\mathbf r_j-\mathbf r_i}
{\left(|\mathbf r_j-\mathbf r_i|^2+\epsilon^2\right)^{3/2}}.
\]

The total energy is

\[
E=K+U,
\]

with

\[
K=\frac12\sum_i m_i|\mathbf v_i|^2
\]

and

\[
U=-G\sum_{i<j}
\frac{m_im_j}
{\sqrt{|\mathbf r_i-\mathbf r_j|^2+\epsilon^2}}.
\]

For 2-D motion, the total angular momentum is

\[
L_z=\sum_i m_i(x_iv_{y,i}-y_iv_{x,i}).
\]

For chaos analysis, two initially nearby trajectories are compared through

\[
D(t)=
\sqrt{\sum_i
|\mathbf r_i^{(A)}-\mathbf r_i^{(B)}|^2}.
\]

A simple finite-time Lyapunov-like estimate is

\[
\lambda(t)=\frac{1}{t}
\ln\left(\frac{D(t)}{D_0}\right).
\]

This is intentionally called **Lyapunov-like**; it is not a rigorous maximal Lyapunov exponent calculation.

## Numerical method

The recommended production integrator is Leapfrog / Velocity Verlet:

\[
\mathbf v_{n+1/2}
=
\mathbf v_n+\frac{\Delta t}{2}\mathbf a_n
\]

\[
\mathbf r_{n+1}
=
\mathbf r_n+\Delta t\mathbf v_{n+1/2}
\]

\[
\mathbf v_{n+1}
=
\mathbf v_{n+1/2}
+\frac{\Delta t}{2}\mathbf a_{n+1}.
\]

Euler and RK4 are included for comparison.

## Quick start

### Local installation

```bash
git clone https://github.com/YOUR_USERNAME/gravitational-nbody-chaos.git
cd gravitational-nbody-chaos
pip install -r requirements.txt
```

### Run a simulation

```bash
python -m experiments.body_count
```

### Google Colab

Upload or open the notebooks under `notebooks/` in Google Colab. The notebooks are designed to import the `src/` package from the repository root.

## Reproducibility

Experiments should report:

- number of bodies \(N\)
- masses
- initial-condition seed
- gravitational constant \(G\)
- softening parameter \(\epsilon\)
- time step \(\Delta t\)
- total simulation time
- integrator
- collision threshold
- escape threshold

## Scope and limitations

This project uses classical Newtonian gravity, point-mass bodies, a 2-D default model, finite simulation time, and direct \(O(N^2)\) force evaluation. These assumptions are documented in `docs/limitations.md`.

## Research status

This repository is intended as an open-source computational research and educational framework. Results should be interpreted as numerical experiments under the stated assumptions rather than as exact analytical solutions of arbitrary N-body systems.

## License

MIT License. See `LICENSE`.

## Citation

If you use this software, please cite it using `CITATION.cff`.
