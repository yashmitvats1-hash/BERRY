"""Tests for the neutral dynamical descriptors and the new benchmark fixtures.

These tests assert properties of transition kernels and influence graphs. None
of them asserts anything about consciousness, integrated information, or
phenomenal structure.
"""

import pytest

from icsig.diagnostics import (
    cycle_decomposition,
    fixed_points,
    influence_graph_is_acyclic,
    is_deterministic,
    provides_alternative_states,
    stochastic_boolean_influence_edges,
    strongly_connected_state_components,
    successor_support_sizes,
    unit_next_state_marginals,
)
from icsig.examples import (
    disconnected_union_with_isolated_unit,
    feedforward_chain,
    noisy_swap,
    stochastic_same_graph_different_kernel,
    two_unit_same_graph_different_dynamics,
)
from icsig.influence import unweighted_boolean_influence_edges


# --- Benchmark 01 systems are fully deterministic ---------------------------


def test_benchmark01_systems_are_fully_deterministic():
    swap, invert_b = two_unit_same_graph_different_dynamics()

    for system in (swap, invert_b):
        assert is_deterministic(system) is True
        assert successor_support_sizes(system) == (1, 1, 1, 1)
        assert provides_alternative_states(system) is False


def test_benchmark01_cycle_structures_differ():
    swap, invert_b = two_unit_same_graph_different_dynamics()

    assert cycle_decomposition(swap) == ((0,), (1, 2), (3,))
    assert cycle_decomposition(invert_b) == ((0, 2, 3, 1),)
    assert fixed_points(swap) == (0, 3)
    assert fixed_points(invert_b) == ()


def test_benchmark01_state_components_differ():
    swap, invert_b = two_unit_same_graph_different_dynamics()

    assert strongly_connected_state_components(swap) == (
        frozenset({0}),
        frozenset({1, 2}),
        frozenset({3}),
    )
    assert strongly_connected_state_components(invert_b) == (
        frozenset({0, 1, 2, 3}),
    )


# --- Stochastic fixtures for Benchmark 02 -----------------------------------


def test_noisy_swap_pair_shares_influence_graph_but_not_kernel():
    low_noise, high_noise = stochastic_same_graph_different_kernel()

    expected = frozenset({("A", "B"), ("B", "A")})
    assert stochastic_boolean_influence_edges(low_noise) == expected
    assert stochastic_boolean_influence_edges(high_noise) == expected
    assert low_noise.kernel != high_noise.kernel


def test_noisy_swap_pair_both_provide_alternative_states():
    low_noise, high_noise = stochastic_same_graph_different_kernel()

    for system in (low_noise, high_noise):
        assert is_deterministic(system) is False
        assert provides_alternative_states(system) is True
        assert successor_support_sizes(system) == (4, 4, 4, 4)


def test_noisy_swap_at_zero_noise_is_benchmark01_swap():
    swap, _ = two_unit_same_graph_different_dynamics()

    assert noisy_swap(0.0).kernel == swap.kernel


def test_noisy_swap_rejects_out_of_range_noise():
    with pytest.raises(ValueError, match="noise"):
        noisy_swap(1.5)


def test_stochastic_influence_rejects_negative_threshold():
    system = noisy_swap(0.1)
    with pytest.raises(ValueError, match="threshold"):
        stochastic_boolean_influence_edges(system, threshold=-1.0)


def test_strong_threshold_can_erase_weak_influence_edges():
    # At 0.1 noise the single-bit flip changes a marginal by 1.6 in L1 distance;
    # a threshold above that removes every edge. The threshold is a declared
    # modelling choice, so a benchmark must state it.
    system = noisy_swap(0.1)

    assert stochastic_boolean_influence_edges(system, threshold=1.0) == frozenset(
        {("A", "B"), ("B", "A")}
    )
    assert stochastic_boolean_influence_edges(system, threshold=1.7) == frozenset()


# --- Isolated-component and feedforward fixtures ----------------------------


def test_isolated_unit_leaves_the_influence_graph_unchanged():
    union = disconnected_union_with_isolated_unit()

    assert is_deterministic(union) is True
    assert unweighted_boolean_influence_edges(union) == frozenset(
        {("A", "B"), ("B", "A")}
    )
    assert union.number_of_units == 3
    assert union.number_of_states == 8


def test_isolated_unit_multiplies_recurrent_and_transient_states():
    union = disconnected_union_with_isolated_unit()

    assert cycle_decomposition(union) == ((0,), (2, 4), (6,))
    components = strongly_connected_state_components(union)
    assert len(components) == 7
    assert frozenset({2, 4}) in components


def test_isolated_unit_has_a_constant_next_state_marginal():
    union = disconnected_union_with_isolated_unit()

    for state_index in range(union.number_of_states):
        marginals = unit_next_state_marginals(union, state_index)
        # Third unit C is held at 0 regardless of the current state.
        assert marginals[2] == (1.0, 0.0)


def test_feedforward_chain_has_an_acyclic_influence_graph():
    chain = feedforward_chain()

    assert unweighted_boolean_influence_edges(chain) == frozenset(
        {("B", "A"), ("C", "B")}
    )
    assert influence_graph_is_acyclic(
        unweighted_boolean_influence_edges(chain)
    ) is True


def test_reciprocal_pair_has_a_cyclic_influence_graph():
    swap, _ = two_unit_same_graph_different_dynamics()
    edges = unweighted_boolean_influence_edges(swap)

    assert influence_graph_is_acyclic(edges) is False


def test_acyclicity_predicate_handles_self_loops_and_isolated_edges():
    assert influence_graph_is_acyclic(frozenset({("A", "A")})) is False
    assert influence_graph_is_acyclic(frozenset({("A", "B")})) is True
    assert influence_graph_is_acyclic(
        frozenset({("A", "B"), ("B", "C"), ("C", "A")})
    ) is False
    assert influence_graph_is_acyclic(frozenset()) is True


def test_unit_marginals_follow_the_swap_rules():
    swap, _ = two_unit_same_graph_different_dynamics()

    # State 01 means A=0, B=1; swap gives A_next=1 and B_next=0.
    assert unit_next_state_marginals(swap, 1) == ((0.0, 1.0), (1.0, 0.0))
