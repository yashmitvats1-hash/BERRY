"""Print neutral dynamical diagnostics for the BERRY benchmark fixtures.

Run with:

    python examples/diagnostics_report.py

The output describes transition kernels and influence graphs only. Nothing here
computes integrated information or asserts anything about experience.
"""

from icsig.diagnostics import (
    cycle_decomposition,
    influence_graph_is_acyclic,
    is_deterministic,
    provides_alternative_states,
    stochastic_boolean_influence_edges,
    strongly_connected_state_components,
    successor_support_sizes,
)
from icsig.examples import (
    disconnected_union_with_isolated_unit,
    feedforward_chain,
    stochastic_same_graph_different_kernel,
    two_unit_same_graph_different_dynamics,
)
from icsig.influence import unweighted_boolean_influence_edges

swap, invert_b = two_unit_same_graph_different_dynamics()
low_noise, high_noise = stochastic_same_graph_different_kernel()
union = disconnected_union_with_isolated_unit()
chain = feedforward_chain()

fixtures = [
    ("B01 swap", swap, True),
    ("B01 invert-plus-copy", invert_b, True),
    ("B02 noisy swap p=0.1", low_noise, False),
    ("B02 noisy swap p=0.3", high_noise, False),
    ("B02 swap plus isolated C", union, True),
    ("B02 feedforward chain", chain, True),
]

print(f"{'fixture':26} {'units':6} {'det':4} {'alts':5} {'acyclic':8} cycles")
for name, system, deterministic_only in fixtures:
    if deterministic_only:
        edges = unweighted_boolean_influence_edges(system)
    else:
        edges = stochastic_boolean_influence_edges(system)
    acyclic = influence_graph_is_acyclic(edges)
    cycles = cycle_decomposition(system) if deterministic_only else "n/a"
    print(
        f"{name:26} {system.number_of_units:<6} "
        f"{str(is_deterministic(system)):4} "
        f"{str(provides_alternative_states(system)):5} "
        f"{str(acyclic):8} {cycles}"
    )

print()
print("Successor support sizes")
for name, system, _ in fixtures:
    print(f"  {name:26} {successor_support_sizes(system)}")

print()
print("Influence graphs")
for name, system, deterministic_only in fixtures:
    if deterministic_only:
        edges = unweighted_boolean_influence_edges(system)
        kind = "deterministic extractor"
    else:
        edges = stochastic_boolean_influence_edges(system)
        kind = "stochastic extractor (threshold 1e-9)"
    print(f"  {name:26} {sorted(edges)}  [{kind}]")

print()
print("Strongly connected state components (deterministic fixtures)")
for name, system, deterministic_only in fixtures:
    if deterministic_only:
        components = strongly_connected_state_components(system)
        print(f"  {name:26} {len(components)} components: "
              f"{[sorted(c) for c in components]}")
