"""Neutral computational tools for the BERRY ICSI-G research project.

The package is infrastructure only; it does not implement a theory of
phenomenal consciousness, IIT, or ICSI-G.
"""

from .models import FiniteBinaryTransitionSystem
from .influence import deterministic_successor_indices, unweighted_boolean_influence_edges
from .diagnostics import (
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

__all__ = [
    "FiniteBinaryTransitionSystem",
    "deterministic_successor_indices",
    "unweighted_boolean_influence_edges",
    "cycle_decomposition",
    "fixed_points",
    "influence_graph_is_acyclic",
    "is_deterministic",
    "provides_alternative_states",
    "stochastic_boolean_influence_edges",
    "strongly_connected_state_components",
    "successor_support_sizes",
    "unit_next_state_marginals",
]
