"""Print the first BERRY graph-vs-dynamics counterexample."""

from icsig.examples import two_unit_same_graph_different_dynamics
from icsig.influence import unweighted_boolean_influence_edges

swap, invert_b = two_unit_same_graph_different_dynamics()
print("State order: 00, 01, 10, 11")
print("Swap kernel:", swap.kernel)
print("Invert-plus-copy kernel:", invert_b.kernel)
print("Swap graph:", sorted(unweighted_boolean_influence_edges(swap)))
print("Invert-plus-copy graph:", sorted(unweighted_boolean_influence_edges(invert_b)))
print("Kernels equal:", swap.kernel == invert_b.kernel)
