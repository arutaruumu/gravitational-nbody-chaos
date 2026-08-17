"""Trajectory divergence and Lyapunov-like diagnostics."""

import numpy as np


def trajectory_divergence(positions_a, positions_b):
    if positions_a.shape != positions_b.shape:
        raise ValueError("Trajectory arrays must have identical shapes.")
    return np.sqrt(np.sum((positions_a - positions_b) ** 2, axis=(1, 2)))


def lyapunov_like_exponent(time, divergence, d0=None):
    time = np.asarray(time, dtype=float)
    divergence = np.asarray(divergence, dtype=float)

    if d0 is None:
        positive = divergence[divergence > 0]
        if len(positive) == 0:
            return np.full_like(time, np.nan)
        d0 = positive[0]

    result = np.full_like(time, np.nan)
    valid = (time > 0) & (divergence > 0)
    result[valid] = np.log(divergence[valid] / d0) / time[valid]
    return result


def log_divergence(divergence, floor=1e-300):
    return np.log(np.maximum(divergence, floor))
