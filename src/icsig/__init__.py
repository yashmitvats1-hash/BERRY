"""Neutral computational tools for the BERRY ICSI-G research project.

The package is infrastructure only; it does not implement a theory of
phenomenal consciousness, IIT, or ICSI-G.
"""

from .models import FiniteBinaryTransitionSystem
from .influence import deterministic_successor_indices, unweighted_boolean_influence_edges

__all__ = ["FiniteBinaryTransitionSystem", "deterministic_successor_indices", "unweighted_boolean_influence_edges"]
