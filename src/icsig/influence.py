"""Functional influence graphs for deterministic binary transition systems.

This utility extracts an unweighted Boolean dependency graph from a fully
specified deterministic state-transition table. It is a mathematical
abstraction, not by itself an interventional causal model or a consciousness
measure.
"""

from __future__ import annotations

from .models import FiniteBinaryTransitionSystem


def deterministic_successor_indices(
    system: FiniteBinaryTransitionSystem,
) -> tuple[int, ...]:
    """Return the unique next-state index for every state, or raise ValueError.

    A row is treated as deterministic when exactly one outcome is 1 (within
    system.tolerance) and all other outcomes are 0 (within that tolerance).
    """
    successors: list[int] = []
    tol = system.tolerance

    for row_index, row in enumerate(system.kernel):
        high = [index for index, probability in enumerate(row) if probability >= 1 - tol]
        if len(high) != 1:
            raise ValueError(f"kernel row {row_index} is not deterministic")
        winner = high[0]
        if any(probability > tol for index, probability in enumerate(row) if index != winner):
            raise ValueError(f"kernel row {row_index} is not deterministic")
        successors.append(winner)

    return tuple(successors)


def unweighted_boolean_influence_edges(
    system: FiniteBinaryTransitionSystem,
) -> frozenset[tuple[str, str]]:
    """Return edges (source_unit, next_time_target_unit) for Boolean dependence.

    State indices use lexicographic binary-tuple order, with the first listed
    unit as the most significant bit. There is an edge from unit i to target
    unit j when toggling only i can change j's next-state value for at least
    one assignment of the other current-state units.

    This deliberately loses sign, the specific transition truth table, and
    current state. It is suitable for showing what an unweighted influence
    graph discards; it should not be called a full causal repertoire.
    """
    successors = deterministic_successor_indices(system)
    n = system.number_of_units
    outputs = tuple(
        tuple((successor >> (n - position - 1)) & 1 for position in range(n))
        for successor in successors
    )

    edges: set[tuple[str, str]] = set()
    for source_index, source_unit in enumerate(system.units):
        bit = 1 << (n - source_index - 1)
        for state_index in range(system.number_of_states):
            # Inspect each pair once: current source bit 0 versus the same state
            # with only that bit toggled to 1.
            if state_index & bit:
                continue
            flipped_index = state_index | bit
            for target_index, target_unit in enumerate(system.units):
                if outputs[state_index][target_index] != outputs[flipped_index][target_index]:
                    edges.add((source_unit, target_unit))

    return frozenset(edges)
