"""Collision detection utilities."""

import numpy as np


def collision_pairs(positions, threshold=1e-2):
    displacement = positions[:, None, :] - positions[None, :, :]
    distances = np.sqrt(np.sum(displacement**2, axis=2))
    i, j = np.triu_indices(len(positions), k=1)
    mask = distances[i, j] < threshold
    return list(zip(i[mask].tolist(), j[mask].tolist()))


def minimum_pair_distance(positions):
    displacement = positions[:, None, :] - positions[None, :, :]
    distances = np.sqrt(np.sum(displacement**2, axis=2))
    distances += np.eye(len(positions)) * np.inf
    return np.min(distances)
