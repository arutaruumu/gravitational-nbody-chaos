"""Visualization utilities."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot_orbits(positions, ax=None, title="N-Body Trajectories", alpha=0.8):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    for i in range(positions.shape[1]):
        ax.plot(positions[:, i, 0], positions[:, i, 1], alpha=alpha, linewidth=0.8)
        ax.scatter(positions[0, i, 0], positions[0, i, 1], s=15)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(title)
    return ax


def plot_conservation(time, history, ylabel, title):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(time, history)
    ax.set_xlabel("Time")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    return fig, ax


def plot_divergence(time, divergence):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.semilogy(time, np.maximum(divergence, 1e-300))
    ax.set_xlabel("Time")
    ax.set_ylabel("Trajectory divergence")
    ax.set_title("Sensitivity to Initial Conditions")
    return fig, ax


def phase_space(positions, velocities, body_index=0):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(
        positions[:, body_index, 0],
        velocities[:, body_index, 0],
        linewidth=0.8,
    )
    ax.set_xlabel("x")
    ax.set_ylabel("vx")
    ax.set_title(f"Phase Space — Body {body_index}")
    return fig, ax


def animate_system(positions, interval=30, frame_step=10, figsize=(7, 7)):
    fig, ax = plt.subplots(figsize=figsize)
    scatter = ax.scatter(
        positions[0, :, 0],
        positions[0, :, 1],
        s=20,
    )

    extent = np.max(np.abs(positions))
    extent = max(extent, 1.0) * 1.05
    ax.set_xlim(-extent, extent)
    ax.set_ylim(-extent, extent)
    ax.set_aspect("equal", adjustable="box")

    frames = range(0, len(positions), frame_step)

    def update(frame):
        scatter.set_offsets(positions[frame])
        return (scatter,)

    animation = FuncAnimation(
        fig,
        update,
        frames=frames,
        interval=interval,
        blit=True,
    )
    plt.close(fig)
    return animation
