"""N-body simulation driver."""

import numpy as np
from tqdm.auto import tqdm

from .system import NBodySystem
from .integrators import euler_step, leapfrog_step, rk4_step

INTEGRATORS = {
    "euler": euler_step,
    "leapfrog": leapfrog_step,
    "rk4": rk4_step,
}


def simulate(
    system: NBodySystem,
    steps: int = 5000,
    dt: float = 0.01,
    G: float = 1.0,
    softening: float = 1e-3,
    integrator: str = "leapfrog",
    progress: bool = True,
):
    """Integrate an N-body system and return time/state histories."""
    if integrator not in INTEGRATORS:
        raise ValueError(f"Unknown integrator: {integrator}")

    if steps < 1 or dt <= 0:
        raise ValueError("steps must be positive and dt must be positive")

    stepper = INTEGRATORS[integrator]
    n = system.n_bodies

    positions_history = np.empty((steps + 1, n, 2), dtype=float)
    velocities_history = np.empty((steps + 1, n, 2), dtype=float)

    positions = system.positions.copy()
    velocities = system.velocities.copy()

    positions_history[0] = positions
    velocities_history[0] = velocities

    iterator = tqdm(range(steps), desc="Simulating") if progress else range(steps)

    for step in iterator:
        positions, velocities = stepper(
            positions,
            velocities,
            system.masses,
            dt,
            G,
            softening,
        )
        positions_history[step + 1] = positions
        velocities_history[step + 1] = velocities

    time = np.arange(steps + 1) * dt
    return time, positions_history, velocities_history
