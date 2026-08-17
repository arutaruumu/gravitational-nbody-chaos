"""Direct Newtonian gravitational acceleration."""

import numpy as np


def compute_accelerations(
    positions: np.ndarray,
    masses: np.ndarray,
    G: float = 1.0,
    softening: float = 1e-3,
) -> np.ndarray:
    """Compute all accelerations using vectorized direct summation."""
    positions = np.asarray(positions, dtype=float)
    masses = np.asarray(masses, dtype=float)

    displacement = positions[None, :, :] - positions[:, None, :]
    distance_sq = np.sum(displacement**2, axis=2)
    softened = distance_sq + softening**2

    inv_distance_cubed = np.zeros_like(softened)
    off_diagonal = ~np.eye(len(positions), dtype=bool)
    inv_distance_cubed[off_diagonal] = softened[off_diagonal] ** (-1.5)

    acceleration = G * np.sum(
        displacement * inv_distance_cubed[:, :, None] * masses[None, :, None],
        axis=1,
    )
    return acceleration


def pairwise_acceleration(
    position_i,
    position_j,
    mass_j,
    G=1.0,
    softening=1e-3,
):
    """Acceleration on i due to one source body j."""
    displacement = np.asarray(position_j) - np.asarray(position_i)
    r2 = np.dot(displacement, displacement) + softening**2
    return G * mass_j * displacement / (r2 ** 1.5)
