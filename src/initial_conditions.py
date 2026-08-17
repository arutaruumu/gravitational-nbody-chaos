"""Initial-condition generators and center-of-mass utilities."""

import numpy as np
from .system import NBodySystem


def random_system(
    n_bodies=10,
    mass_range=(0.5, 2.0),
    position_scale=1.0,
    velocity_scale=0.3,
    seed=42,
):
    rng = np.random.default_rng(seed)
    masses = rng.uniform(*mass_range, n_bodies)
    positions = rng.normal(0.0, position_scale, (n_bodies, 2))
    velocities = rng.normal(0.0, velocity_scale, (n_bodies, 2))
    return center_system(NBodySystem(masses, positions, velocities))


def binary_system(
    mass1=1.0,
    mass2=1.0,
    separation=2.0,
    G=1.0,
):
    """Circular two-body binary in the center-of-mass frame."""
    m_total = mass1 + mass2
    r1 = separation * mass2 / m_total
    r2 = separation * mass1 / m_total
    omega = np.sqrt(G * m_total / separation**3)

    positions = np.array([[-r1, 0.0], [r2, 0.0]])
    velocities = np.array([[0.0, -omega * r1], [0.0, omega * r2]])
    masses = np.array([mass1, mass2])
    return NBodySystem(masses, positions, velocities)


def disk_system(
    n_bodies=50,
    mass_range=(0.2, 1.0),
    radius=5.0,
    velocity_scale=0.5,
    seed=42,
):
    """Create a simple disk-like configuration around the origin."""
    rng = np.random.default_rng(seed)
    masses = rng.uniform(*mass_range, n_bodies)
    angles = rng.uniform(0, 2 * np.pi, n_bodies)
    radii = radius * np.sqrt(rng.uniform(0, 1, n_bodies))
    positions = np.column_stack((radii * np.cos(angles), radii * np.sin(angles)))

    tangential = np.column_stack((-np.sin(angles), np.cos(angles)))
    velocities = velocity_scale * tangential
    return center_system(NBodySystem(masses, positions, velocities))


def center_system(system: NBodySystem) -> NBodySystem:
    """Shift positions and velocities into the center-of-mass frame."""
    total_mass = np.sum(system.masses)
    r_cm = np.sum(system.positions * system.masses[:, None], axis=0) / total_mass
    v_cm = np.sum(system.velocities * system.masses[:, None], axis=0) / total_mass

    system.positions -= r_cm
    system.velocities -= v_cm
    return system


def perturb_system(system: NBodySystem, amplitude=1e-8, seed=123) -> NBodySystem:
    """Create a nearby initial state by perturbing positions."""
    rng = np.random.default_rng(seed)
    positions = system.positions + rng.normal(0.0, amplitude, system.positions.shape)
    return NBodySystem(system.masses.copy(), positions, system.velocities.copy())
