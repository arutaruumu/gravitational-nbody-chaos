"""Physical diagnostics."""

import numpy as np


def kinetic_energy(velocities, masses):
    return 0.5 * np.sum(masses * np.sum(velocities**2, axis=1))


def potential_energy(positions, masses, G=1.0, softening=1e-3):
    displacement = positions[:, None, :] - positions[None, :, :]
    distances = np.sqrt(np.sum(displacement**2, axis=2) + softening**2)
    i, j = np.triu_indices(len(masses), k=1)
    return -G * np.sum(masses[i] * masses[j] / distances[i, j])


def total_energy(positions, velocities, masses, G=1.0, softening=1e-3):
    return kinetic_energy(velocities, masses) + potential_energy(
        positions, masses, G, softening
    )


def angular_momentum(positions, velocities, masses):
    return np.sum(
        masses * (positions[:, 0] * velocities[:, 1] - positions[:, 1] * velocities[:, 0])
    )


def energy_history(positions_history, velocities_history, masses, G=1.0, softening=1e-3):
    return np.array([
        total_energy(p, v, masses, G, softening)
        for p, v in zip(positions_history, velocities_history)
    ])


def angular_momentum_history(positions_history, velocities_history, masses):
    return np.array([
        angular_momentum(p, v, masses)
        for p, v in zip(positions_history, velocities_history)
    ])


def relative_error(history):
    initial = history[0]
    scale = max(abs(initial), np.finfo(float).eps)
    return np.abs(history - initial) / scale


def center_of_mass(positions, masses):
    return np.sum(positions * masses[:, None], axis=0) / np.sum(masses)
