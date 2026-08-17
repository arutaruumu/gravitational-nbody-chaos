"""Data model for N-body systems."""

from dataclasses import dataclass
import numpy as np


@dataclass
class NBodySystem:
    """Container for masses, positions, and velocities."""

    masses: np.ndarray
    positions: np.ndarray
    velocities: np.ndarray

    def __post_init__(self):
        self.masses = np.asarray(self.masses, dtype=float)
        self.positions = np.asarray(self.positions, dtype=float)
        self.velocities = np.asarray(self.velocities, dtype=float)

        if self.positions.ndim != 2 or self.positions.shape[1] != 2:
            raise ValueError("positions must have shape (N, 2)")
        if self.velocities.shape != self.positions.shape:
            raise ValueError("velocities must have the same shape as positions")
        if self.masses.ndim != 1 or len(self.masses) != len(self.positions):
            raise ValueError("masses must have shape (N,)")
        if np.any(self.masses <= 0):
            raise ValueError("all masses must be positive")

    @property
    def n_bodies(self) -> int:
        return len(self.masses)

    def copy(self) -> "NBodySystem":
        return NBodySystem(
            self.masses.copy(),
            self.positions.copy(),
            self.velocities.copy(),
        )