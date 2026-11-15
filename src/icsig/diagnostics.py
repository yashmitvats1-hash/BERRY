"""Neutral dynamical descriptors for finite binary transition systems.

Every function here describes a transition kernel. None of them implements a
theory of consciousness, computes integrated information, or asserts anything
about phenomenal structure. In particular:

* ``successor_support_sizes`` reports how many next states a kernel assigns
  positive probability to. It is a description of a probability table. It is
  *not* a computation of IIT's intrinsic differentiation, and it does not
  license any claim about a repertoire of alternatives in the IIT sense.
* ``strongly_connected_state_components`` and ``influence_graph_is_acyclic``
  are ordinary graph-theoretic predicates. They are supplied because the
  project needs a shared, tested vocabulary for "recurrent support" and
  "feedforward", not because either predicate marks a conscious subject.

State-index convention (shared with the rest of the package): joint states are
ordered lexicographically over binary tuples, with the first listed unit as the
most significant bit.
"""

from __future__ import annotations

import math
from collections import defaultdict

from .influence import deterministic_successor_indices
from .models import FiniteBinaryTransitionSystem


def is_deterministic(system: FiniteBinaryTransitionSystem) -> bool:
    """Return True when every row of the kernel is a one-hot distribution.

    Uses the same tolerance semantics as ``deterministic_successor_indices``:
    a row is deterministic when exactly one entry is >= 1 - tolerance and every
    other entry is <= tolerance.
    """
    tol = system.tolerance
    for row in system.kernel:
        high = [p for p in row if p >= 1 - tol]
        if len(high) != 1:
            return False
        winner = row.index(max(row))
        if any(p > tol for index, p in enumerate(row) if index != winner):
            return False
    return True


def successor_support_sizes(system: FiniteBinaryTransitionSystem) -> tuple[int, ...]:
    """Return, per current state, the count of next states with positive probability.

    "Positive" means strictly greater than ``system.tolerance``. A value of 1
    everywhere is the signature of a fully deterministic kernel; a value of 2
    or more somewhere means the kernel itself carries stochastic branching.

    This is a property of the supplied table only. It says nothing about
    interventions, background distributions, or causal power.
    """
    tol = system.tolerance
    return tuple(
        sum(1 for probability in row if probability > tol) for row in system.kernel
    )


def provides_alternative_states(system: FiniteBinaryTransitionSystem) -> bool:
    """Return True when at least one current state has two or more possible successors.

    Provided as a neutral predicate so that benchmark families can be sorted by
    whether they are deterministic or stochastic. Sorting is a modelling choice;
    it is not a consciousness criterion.
    """
    return any(size >= 2 for size in successor_support_sizes(system))


def unit_next_state_marginals(
    system: FiniteBinaryTransitionSystem,
    state_index: int,
) -> tuple[tuple[float, float], ...]:
    """Return each unit's next-state marginal distribution for one current state.

    The result is a tuple with one ``(p_zero, p_one)`` pair per unit, in
    ``system.units`` order.
    """
    if isinstance(state_index, bool) or not isinstance(state_index, int):
        raise TypeError("state_index must be an integer")
    if not 0 <= state_index < system.number_of_states:
        raise IndexError(
            f"state_index must be in [0, {system.number_of_states - 1}]"
        )

    n = system.number_of_units
    row = system.kernel[state_index]
    marginals: list[tuple[float, float]] = []
    for unit_position in range(n):
        shift = n - unit_position - 1
        p_one = sum(
            probability
            for successor, probability in enumerate(row)
            if (successor >> shift) & 1
        )
        marginals.append((1.0 - p_one, p_one))
    return tuple(marginals)


def stochastic_boolean_influence_edges(
    system: FiniteBinaryTransitionSystem,
    threshold: float = 1e-9,
) -> frozenset[tuple[str, str]]:
    """Return edges (source_unit, next_time_target_unit) for distributional dependence.

    This generalises ``unweighted_boolean_influence_edges`` to stochastic
    kernels. There is an edge from unit i to unit j when, for at least one
    assignment of the other current units, toggling only i changes unit j's
    next-state marginal by more than ``threshold`` in L1 distance.

    The threshold must be declared whenever this is used in a benchmark, because
    it controls which weak dependencies survive. Like the deterministic
    extractor, this discards sign, exact probabilities, current state, and
    higher-order interactions; it is not a full causal repertoire.
    """
    if not math.isfinite(threshold) or threshold < 0:
        raise ValueError("threshold must be finite and non-negative")

    n = system.number_of_units
    number_of_states = system.number_of_states
    marginals = tuple(
        unit_next_state_marginals(system, state_index)
        for state_index in range(number_of_states)
    )

    edges: set[tuple[str, str]] = set()
    for source_index, source_unit in enumerate(system.units):
        bit = 1 << (n - source_index - 1)
        for state_index in range(number_of_states):
            if state_index & bit:
                continue
            flipped_index = state_index | bit
            for target_index, target_unit in enumerate(system.units):
                base = marginals[state_index][target_index]
                flipped = marginals[flipped_index][target_index]
                distance = abs(base[0] - flipped[0]) + abs(base[1] - flipped[1])
                if distance > threshold:
                    edges.add((source_unit, target_unit))
    return frozenset(edges)


def influence_graph_is_acyclic(
    edges: frozenset[tuple[str, str]] | set[tuple[str, str]],
) -> bool:
    """Return True when a directed edge set over unit labels contains no directed cycle.

    Self-loops count as cycles. This is a plain reachability test used to sort
    systems into "feedforward" and "recurrent" families; the labels are
    descriptive of the graph only.
    """
    adjacency: dict[str, list[str]] = defaultdict(list)
    nodes: set[str] = set()
    for source, target in edges:
        adjacency[source].append(target)
        nodes.add(source)
        nodes.add(target)

    WHITE, GREY, BLACK = 0, 1, 2
    colour = {node: WHITE for node in nodes}

    for root in sorted(nodes):
        if colour[root] != WHITE:
            continue
        colour[root] = GREY
        # Iterative depth-first search carrying the next neighbour index, so the
        # traversal needs no recursion limit and reports a cycle as soon as it
        # reaches a GREY node still on the current stack.
        stack: list[tuple[str, int]] = [(root, 0)]
        while stack:
            current, position = stack.pop()
            neighbours = adjacency.get(current, ())
            if position < len(neighbours):
                stack.append((current, position + 1))
                successor = neighbours[position]
                if colour[successor] == GREY:
                    return False
                if colour[successor] == WHITE:
                    colour[successor] = GREY
                    stack.append((successor, 0))
            else:
                colour[current] = BLACK

    return True


def fixed_points(system: FiniteBinaryTransitionSystem) -> tuple[int, ...]:
    """Return state indices that map to themselves. Requires a deterministic kernel."""
    successors = deterministic_successor_indices(system)
    return tuple(index for index, successor in enumerate(successors) if index == successor)


def strongly_connected_state_components(
    system: FiniteBinaryTransitionSystem,
) -> tuple[frozenset[int], ...]:
    """Return the strongly connected components of the state-transition digraph.

    Requires a deterministic kernel, so every state has exactly one successor.
    The digraph is therefore a functional graph: each recurrent cycle is one
    component, and every state that merely feeds into a cycle is a singleton
    component. A fixed point is a cycle of length one.

    Sorted by smallest member index for reproducible output.
    """
    deterministic_successor_indices(system)  # raises unless the kernel is deterministic

    on_cycle: set[int] = set()
    components: list[frozenset[int]] = []
    for cycle in cycle_decomposition(system):
        components.append(frozenset(cycle))
        on_cycle.update(cycle)

    for state_index in range(system.number_of_states):
        if state_index not in on_cycle:
            components.append(frozenset({state_index}))

    return tuple(sorted(components, key=lambda component: min(component)))


def cycle_decomposition(system: FiniteBinaryTransitionSystem) -> tuple[tuple[int, ...], ...]:
    """Return each recurrent cycle as an ordered tuple of state indices.

    Deterministic kernels only. Cycles are ordered by smallest member index, and
    each cycle is rotated so that its smallest member comes first. This makes
    the output invariant to which state the traversal happened to enter from.
    """
    successors = deterministic_successor_indices(system)
    seen: set[int] = set()
    cycles: list[tuple[int, ...]] = []

    for start in range(system.number_of_states):
        if start in seen:
            continue
        current = start
        trail: list[int] = []
        while current not in seen:
            if current in trail:
                cycle_nodes = trail[trail.index(current):]
                smallest = min(cycle_nodes)
                rotation = cycle_nodes.index(smallest)
                cycles.append(tuple(cycle_nodes[rotation:] + cycle_nodes[:rotation]))
                break
            trail.append(current)
            current = successors[current]
        seen.update(trail)

    return tuple(sorted(cycles))
