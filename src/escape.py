"""Escape and boundness diagnostics."""

import numpy as np


def escaped_by_radius(positions, center, threshold=100.0):
    distances = np.linalg.norm(positions - center, axis=1)
    return np.where(distances > threshold)[0]


def radial_distance(positions, center=None):
    if center is None:
        center = np.zeros(positions.shape[-1])
    return np.linalg.norm(positions - center, axis=-1)


def specific_energy_against_central_mass(
    positions,
    velocities,
    central_mass,
    G=1.0,
    center=None,
):
    if center is None:
        center = np.zeros(2)
    r_vec = positions - center
    r = np.linalg.norm(r_vec, axis=1)
    v2 = np.sum(velocities**2, axis=1)
    return 0.5 * v2 - G * central_mass / np.maximum(r, 1e-15)
