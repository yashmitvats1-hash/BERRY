"""Tests for the exhaustive two-unit enumeration.

These tests pin the counting conventions behind the reported
"700 reachable two-unit deterministic systems" figure.
"""

from icsig.enumeration import (
    boolean_functions,
    enumerate_two_unit_systems,
    fully_reachable_systems,
    image_size_histogram,
    reachable_state_pairs,
)
from icsig.influence import unweighted_boolean_influence_edges


def test_all_sixteen_boolean_functions_per_unit():
    functions = boolean_functions()
    assert len(functions) == 16
    assert len(set(functions)) == 16


def test_labeled_system_count_is_256():
    systems = enumerate_two_unit_systems()
    assert len(systems) == 256
    assert len({system.code for system in systems}) == 256
    # Each labeled pair of truth tables appears exactly once.
    pairs = {(system.f_a_code, system.f_b_code) for system in systems}
    assert len(pairs) == 256


def test_successor_map_is_consistent_with_truth_tables():
    for system in enumerate_two_unit_systems():
        for state_index, successor in enumerate(system.successors):
            a = (state_index >> 1) & 1
            b = state_index & 1
            assert system.successors[state_index] == (
                (system.f_a[state_index] << 1) | system.f_b[state_index]
            )
            assert system.f_a[state_index] == (successor >> 1) & 1
            assert system.f_b[state_index] == successor & 1
        assert system.kernel() is not None


def test_image_is_exactly_the_set_of_successors():
    for system in enumerate_two_unit_systems():
        assert system.image == frozenset(system.successors)
        assert system.image_size == len(set(system.successors))
        assert system.garden_of_eden_states == frozenset(
            range(4)
        ) - system.image


def test_image_size_histogram():
    histogram = image_size_histogram(enumerate_two_unit_systems())
    assert histogram == {1: 4, 2: 84, 3: 144, 4: 24}


def test_reachable_state_pairs_total_exactly_700():
    """The reported figure, under the one-step-reachability definition.

    700 = 1*4 + 2*84 + 3*144 + 4*24, the total number of
    (system, state) pairs whose state lies in the system's image.
    """
    systems = enumerate_two_unit_systems()
    assert reachable_state_pairs(systems) == 700
    assert sum(len(system.image) for system in systems) == 700
    # Complement: Garden-of-Eden pairs.
    assert 256 * 4 - 700 == 324


def test_fully_reachable_from_initial_state():
    systems = enumerate_two_unit_systems()
    full = fully_reachable_systems(systems, initial_state=0)
    # Every state lies in the forward orbit of 00: either a single
    # 4-cycle, or a shorter cycle with a tail rooted at 00.
    assert len(full) == 24
    for system in full:
        orbit = set()
        current = 0
        while current not in orbit:
            orbit.add(current)
            current = system.successors[current]
        assert orbit == {0, 1, 2, 3}


def test_strongly_connected_systems_are_the_single_four_cycles():
    from icsig.enumeration import strongly_connected_systems

    systems = enumerate_two_unit_systems()
    connected = strongly_connected_systems(systems)
    assert len(connected) == 6
    for system in connected:
        assert system.cycle_structure_signature() == ((4, 1),)


def test_cycle_signatures_of_benchmark_systems():
    systems = enumerate_two_unit_systems()
    swap = next(s for s in systems if s.f_a == (0, 1, 0, 1) and s.f_b == (0, 0, 1, 1))
    invert = next(
        s for s in systems if s.f_a == (1, 0, 1, 0) and s.f_b == (0, 0, 1, 1)
    )
    assert swap.code == 172
    assert swap.successors == (0, 2, 1, 3)
    assert swap.cycle_structure_signature() == ((1, 2), (2, 1))
    assert invert.code == 92
    assert invert.successors == (2, 0, 3, 1)
    assert invert.cycle_structure_signature() == ((4, 1),)


def test_benchmark_systems_share_the_same_unweighted_graph():
    systems = enumerate_two_unit_systems()
    swap = next(s for s in systems if s.f_a == (0, 1, 0, 1) and s.f_b == (0, 0, 1, 1))
    invert = next(
        s for s in systems if s.f_a == (1, 0, 1, 0) and s.f_b == (0, 0, 1, 1)
    )
    assert unweighted_boolean_influence_edges(
        swap.to_transition_system()
    ) == unweighted_boolean_influence_edges(
        invert.to_transition_system()
    )
    assert swap.kernel() != invert.kernel()


def test_transition_system_conversion_round_trips():
    from icsig.models import FiniteBinaryTransitionSystem

    for system in enumerate_two_unit_systems():
        converted = system.to_transition_system()
        assert isinstance(converted, FiniteBinaryTransitionSystem)
        assert converted.kernel == system.kernel()
        assert converted.number_of_units == 2
