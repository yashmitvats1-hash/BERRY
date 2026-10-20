"""Exhaustive enumeration of deterministic two-unit binary systems.

This module reconstructs the project's reported "700 reachable two-unit
deterministic systems" figure under explicit definitions, so that the
count is reproducible rather than recalled.

Definitions used here
---------------------
*Unit and state space.* Two binary units, ``A`` and ``B``. Joint states
are ordered lexicographically as ``00, 01, 10, 11`` with ``A`` the most
significant bit (the convention of :mod:`icsig.models`). State indices
run 0..3.

*System.* A deterministic synchronous system is a pair of Boolean update
functions ``f_A, f_B : {0,1}^2 -> {0,1}``. Each function is identified
by its 4-bit truth table over the states ``00, 01, 10, 11``; there are
16 functions per unit and ``16 x 16 = 256`` labeled systems in total.
System ``code`` ``16*i + j`` pairs truth table ``i`` (for ``A``) with
truth table ``j`` (for ``B``).

*Reachable state.* A state ``s`` is *reachable* (more precisely:
*one-step reachable*, or *non-Garden-of-Eden*) when it lies in the image
of the successor map, i.e. when at least one state maps to it under the
system's one-step transition function. This is the standard notion for
deterministic finite systems and is what reproduces the reported figure:
across the 256 labeled systems, exactly 700 of the ``256 x 4 = 1024``
(system, state) pairs have the state in the system's image.

*Other reachability notions.* "Reachable from a designated initial
state" (e.g. ``00``) is a different notion: 24 systems have every
state in the forward orbit of ``00`` (the orbit is a 4-cycle, or a
shorter cycle with a tail rooted at ``00``). "Strongly connected"
(every state reaches every state) is stricter still: exactly the 6
single-4-cycle permutations qualify. All three counts are provided
so the enumeration scope is unambiguous.

The module is pure combinatorics: it computes no IIT quantities and
makes no consciousness claims.
"""

from __future__ import annotations

from dataclasses import dataclass

from .influence import unweighted_boolean_influence_edges
from .models import FiniteBinaryTransitionSystem

#: Joint states in the package's big-endian lexicographic convention.
STATE_ORDER: tuple[tuple[int, int], ...] = ((0, 0), (0, 1), (1, 0), (1, 1))


def boolean_functions() -> tuple[tuple[int, ...], ...]:
    """Return all 16 Boolean functions of two variables.

    Each function is a truth table over the states ``00, 01, 10, 11``
    (big-endian: ``A`` is the most significant bit), identified by its
    4-bit code.
    """
    return tuple(tuple((code >> k) & 1 for k in range(4)) for code in range(16))


@dataclass(frozen=True)
class TwoUnitDeterministicSystem:
    """One labeled deterministic two-unit binary system.

    Attributes:
        code: Canonical index ``16*i + j`` where ``i`` and ``j`` are
            the truth-table codes of ``f_A`` and ``f_B``.
        f_a: Truth table of ``A``'s update function over ``STATE_ORDER``.
        f_b: Truth table of ``B``'s update function over ``STATE_ORDER``.
        successors: One-step successor state index for each state index.
        image: Indices of states in the image of the successor map
            (the one-step reachable states).
    """

    code: int
    f_a: tuple[int, ...]
    f_b: tuple[int, ...]
    successors: tuple[int, ...]
    image: frozenset[int]

    @property
    def f_a_code(self) -> int:
        """Truth-table code of ``A``'s update function (0..15)."""
        return sum(bit << k for k, bit in enumerate(self.f_a))

    @property
    def f_b_code(self) -> int:
        """Truth-table code of ``B``'s update function (0..15)."""
        return sum(bit << k for k, bit in enumerate(self.f_b))

    @property
    def image_size(self) -> int:
        """Number of one-step reachable states (image size)."""
        return len(self.image)

    @property
    def garden_of_eden_states(self) -> frozenset[int]:
        """States with no preimage under the successor map."""
        return frozenset(range(4)) - self.image

    def kernel(self) -> tuple[tuple[float, ...], ...]:
        """Return the one-step transition kernel in big-endian order."""
        kernel = [[0.0] * 4 for _ in range(4)]
        for source, target in enumerate(self.successors):
            kernel[source][target] = 1.0
        return tuple(tuple(row) for row in kernel)

    def to_transition_system(self) -> FiniteBinaryTransitionSystem:
        """Return the same system as a validated finite transition system."""
        return FiniteBinaryTransitionSystem(
            units=("A", "B"), kernel=self.kernel()
        )

    def cycle_decomposition(self) -> tuple[frozenset[int], ...]:
        """Return the cycles of the functional graph as state-index sets.

        Every deterministic finite map decomposes into cycles with trees
        feeding into them; the cyclic states are the attractor states.
        """
        cyclic: set[int] = set()
        for start in range(4):
            seen: set[int] = set()
            current = start
            while current not in seen:
                seen.add(current)
                current = self.successors[current]
            cyclic.add(current)
        return tuple(frozenset(cycle) for cycle in _minimal_cycles(
            cyclic, self.successors
        ))

    def cycle_structure_signature(self) -> tuple[tuple[int, int], ...]:
        """Return sorted ``(cycle_length, number_of_such_cycles)`` pairs.

        This is the standard invariant of a functional graph: e.g. the
        swap system has signature ``((1, 2), (2, 1))`` (two fixed points
        and one 2-cycle) and the invert-and-copy system ``((4, 1),)``.
        """
        lengths = sorted(len(cycle) for cycle in self.cycle_decomposition())
        signature: dict[int, int] = {}
        for length in lengths:
            signature[length] = signature.get(length, 0) + 1
        return tuple(sorted(signature.items()))


def _minimal_cycles(
    cyclic_states: set[int], successors: tuple[int, ...]
) -> set[frozenset[int]]:
    """Partition the cyclic states into their disjoint cycles."""
    remaining = set(cyclic_states)
    cycles: set[frozenset[int]] = set()
    while remaining:
        start = min(remaining)
        cycle = {start}
        current = successors[start]
        while current != start:
            cycle.add(current)
            current = successors[current]
        cycles.add(frozenset(cycle))
        remaining -= cycle
    return cycles


def enumerate_two_unit_systems() -> tuple[TwoUnitDeterministicSystem, ...]:
    """Enumerate all 256 labeled deterministic two-unit binary systems."""
    systems: list[TwoUnitDeterministicSystem] = []
    functions = boolean_functions()
    for i, f_a in enumerate(functions):
        for j, f_b in enumerate(functions):
            successors = tuple(
                (f_a[state] << 1) | f_b[state] for state in range(4)
            )
            systems.append(
                TwoUnitDeterministicSystem(
                    code=16 * i + j,
                    f_a=f_a,
                    f_b=f_b,
                    successors=successors,
                    image=frozenset(successors),
                )
            )
    return tuple(systems)


def reachable_state_pairs(
    systems: tuple[TwoUnitDeterministicSystem, ...],
) -> int:
    """Count (system, state) pairs whose state is one-step reachable."""
    return sum(len(system.image) for system in systems)


def fully_reachable_systems(
    systems: tuple[TwoUnitDeterministicSystem, ...],
    initial_state: int = 0,
) -> tuple[TwoUnitDeterministicSystem, ...]:
    """Return systems whose every state is in the forward orbit of
    ``initial_state``.

    This is a stricter reachability notion than the one-step image:
    24 of the 256 systems qualify (their functional graph is a
    4-cycle, or a shorter cycle with a tail rooted at the initial
    state).
    """
    fully: list[TwoUnitDeterministicSystem] = []
    for system in systems:
        reachable: set[int] = set()
        current = initial_state
        while current not in reachable:
            reachable.add(current)
            current = system.successors[current]
        if len(reachable) == 4:
            fully.append(system)
    return tuple(fully)


def strongly_connected_systems(
    systems: tuple[TwoUnitDeterministicSystem, ...],
) -> tuple[TwoUnitDeterministicSystem, ...]:
    """Return systems whose every state reaches every state.

    For a deterministic map this means the functional graph is a
    single cycle covering all states: exactly the 6 four-cycle
    permutations qualify.
    """
    connected: list[TwoUnitDeterministicSystem] = []
    for system in systems:
        if all(
            len(_forward_orbit(system, start)) == 4
            for start in range(4)
        ):
            connected.append(system)
    return tuple(connected)


def _forward_orbit(
    system: TwoUnitDeterministicSystem, start: int
) -> set[int]:
    """Return the states reachable from ``start``."""
    orbit: set[int] = set()
    current = start
    while current not in orbit:
        orbit.add(current)
        current = system.successors[current]
    return orbit


def image_size_histogram(
    systems: tuple[TwoUnitDeterministicSystem, ...],
) -> dict[int, int]:
    """Return the number of systems with each image (reachable-set) size."""
    histogram: dict[int, int] = {}
    for system in systems:
        histogram[len(system.image)] = histogram.get(len(system.image), 0) + 1
    return dict(sorted(histogram.items()))


def systems_by_influence_graph(
    systems: tuple[TwoUnitDeterministicSystem, ...],
) -> dict[frozenset[tuple[str, str]], tuple[TwoUnitDeterministicSystem, ...]]:
    """Group systems by their unweighted Boolean influence graph."""
    groups: dict[frozenset[tuple[str, str]], list[TwoUnitDeterministicSystem]] = {}
    for system in systems:
        edges = unweighted_boolean_influence_edges(
            system.to_transition_system()
        )
        groups.setdefault(edges, []).append(system)
    return {edges: tuple(members) for edges, members in groups.items()}
