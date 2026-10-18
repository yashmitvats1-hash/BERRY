"""Small reproducible examples used by the BERRY benchmarks."""

from .models import FiniteBinaryTransitionSystem


def two_unit_same_graph_different_dynamics() -> tuple[
    FiniteBinaryTransitionSystem, FiniteBinaryTransitionSystem
]:
    """Return a swap system and an inversion-plus-copy system.

    State order is 00, 01, 10, 11 for units (A, B).

    System 1: A_next = B, B_next = A.
    System 2: A_next = NOT B, B_next = A.

    Both have the same unweighted reciprocal influence graph, but distinct
    transition kernels and different state-transition cycles.
    """
    swap = FiniteBinaryTransitionSystem(
        units=("A", "B"),
        kernel=(
            (1.0, 0.0, 0.0, 0.0),  # 00 -> 00
            (0.0, 0.0, 1.0, 0.0),  # 01 -> 10
            (0.0, 1.0, 0.0, 0.0),  # 10 -> 01
            (0.0, 0.0, 0.0, 1.0),  # 11 -> 11
        ),
    )
    invert_b = FiniteBinaryTransitionSystem(
        units=("A", "B"),
        kernel=(
            (0.0, 0.0, 1.0, 0.0),  # 00 -> 10
            (1.0, 0.0, 0.0, 0.0),  # 01 -> 00
            (0.0, 0.0, 0.0, 1.0),  # 10 -> 11
            (0.0, 1.0, 0.0, 0.0),  # 11 -> 01
        ),
    )
    return swap, invert_b
