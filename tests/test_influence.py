import pytest

from icsig.examples import two_unit_same_graph_different_dynamics
from icsig.influence import (
    deterministic_successor_indices,
    unweighted_boolean_influence_edges,
)
from icsig.models import FiniteBinaryTransitionSystem


def test_same_unweighted_influence_graph_can_hide_different_dynamics():
    swap, invert_b = two_unit_same_graph_different_dynamics()

    assert unweighted_boolean_influence_edges(swap) == frozenset(
        {("A", "B"), ("B", "A")}
    )
    assert unweighted_boolean_influence_edges(invert_b) == frozenset(
        {("A", "B"), ("B", "A")}
    )
    assert swap.kernel != invert_b.kernel


def test_demo_systems_have_different_transition_cycles():
    swap, invert_b = two_unit_same_graph_different_dynamics()

    assert deterministic_successor_indices(swap) == (0, 2, 1, 3)
    assert deterministic_successor_indices(invert_b) == (2, 0, 3, 1)


def test_influence_graph_rejects_stochastic_kernel():
    stochastic = FiniteBinaryTransitionSystem(
        units=("A",),
        kernel=((0.5, 0.5), (0.0, 1.0)),
    )
    with pytest.raises(ValueError, match="not deterministic"):
        unweighted_boolean_influence_edges(stochastic)


def test_one_unit_identity_map_has_a_self_influence_edge():
    # The helper uses an explicit state-index convention; a 2x2 one-unit
    # deterministic kernel remains straightforward under that convention.
    system = FiniteBinaryTransitionSystem(
        units=("A",),
        kernel=((1.0, 0.0), (0.0, 1.0)),
    )
    assert unweighted_boolean_influence_edges(system) == frozenset({("A", "A")})
