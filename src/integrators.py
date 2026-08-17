"""Numerical integration methods."""

import numpy as np
from .gravity import compute_accelerations


def euler_step(positions, velocities, masses, dt, G=1.0, softening=1e-3):
    acceleration = compute_accelerations(positions, masses, G, softening)
    new_positions = positions + dt * velocities
    new_velocities = velocities + dt * acceleration
    return new_positions, new_velocities


def leapfrog_step(positions, velocities, masses, dt, G=1.0, softening=1e-3):
    acceleration = compute_accelerations(positions, masses, G, softening)
    half_velocity = velocities + 0.5 * dt * acceleration
    new_positions = positions + dt * half_velocity
    new_acceleration = compute_accelerations(
        new_positions, masses, G, softening
    )
    new_velocities = half_velocity + 0.5 * dt * new_acceleration
    return new_positions, new_velocities


def rk4_step(positions, velocities, masses, dt, G=1.0, softening=1e-3):
    """Classical RK4 for the first-order state y=(r,v)."""
    def acceleration(pos):
        return compute_accelerations(pos, masses, G, softening)

    def deriv(pos, vel):
        return vel, acceleration(pos)

    k1_r, k1_v = deriv(positions, velocities)
    k2_r, k2_v = deriv(
        positions + 0.5 * dt * k1_r,
        velocities + 0.5 * dt * k1_v,
    )
    k3_r, k3_v = deriv(
        positions + 0.5 * dt * k2_r,
        velocities + 0.5 * dt * k2_v,
    )
    k4_r, k4_v = deriv(
        positions + dt * k3_r,
        velocities + dt * k3_v,
    )

    new_positions = positions + (dt / 6.0) * (
        k1_r + 2*k2_r + 2*k3_r + k4_r
    )
    new_velocities = velocities + (dt / 6.0) * (
        k1_v + 2*k2_v + 2*k3_v + k4_v
    )
    return new_positions, new_velocities
