# Benchmark 01 — Same unweighted influence graph, different dynamics

Status: **MATHEMATICAL RESULT** under the explicit finite-state definitions below. This is a counterexample to the sufficiency of an unweighted Boolean influence graph for reconstructing a transition kernel. It is **not** a consciousness result.

## State-space convention

There are two binary units, (A, B), with joint states ordered lexicographically as 00, 01, 10, 11. A row in the transition probability matrix (TPM) gives the next-state distribution conditional on the current joint state. Both systems are deterministic.

## System S: swap

The update equations are:

- A_next = B
- B_next = A

| Current state | Next state |
|---|---|
| 00 | 00 |
| 01 | 10 |
| 10 | 01 |
| 11 | 11 |

TPM rows in the state order above:

```text
[[1, 0, 0, 0],
 [0, 0, 1, 0],
 [0, 1, 0, 0],
 [0, 0, 0, 1]]
```

Its unweighted influence edges are B → A and A → B.

## System N: invert B, then copy A

The update equations are:

- A_next = NOT B
- B_next = A

| Current state | Next state |
|---|---|
| 00 | 10 |
| 01 | 00 |
| 10 | 11 |
| 11 | 01 |

TPM rows:

```text
[[0, 0, 1, 0],
 [1, 0, 0, 0],
 [0, 0, 0, 1],
 [0, 1, 0, 0]]
```

Its unweighted influence edges are again B → A and A → B.

## Result and interpretation

**MATHEMATICAL RESULT:** the unweighted influence graph is the same in both cases, but the full transition kernels differ. System S has fixed states 00 and 11 and a 2-cycle 01 ↔ 10. System N has a 4-cycle 00 → 10 → 11 → 01 → 00.

Therefore, if a candidate ICSI-G formulation takes only this unweighted graph as its identity object, it identifies these two dynamics despite their different transition tables. To distinguish them, the formulation must retain additional information (for example, polarity / state mappings / full intervention-defined repertoires) or justify why the discarded difference is irrelevant to phenomenal structure.

This example does **not** show:
- that the systems have different experiences;
- that IIT_4_0_2023 or IIT_4_0_2026 assigns the same or different structures;
- that either system is a conscious subject;
- that a full causal-repertoire formulation of ICSI-G is a correct theory.

Those claims require separate definitions and computations.

## Reproduction

From the project root:

```bash
python examples/same_graph_different_dynamics.py
python -m pytest -q
```

Executable system definitions are in src/icsig/examples.py. The graph extraction rule is in src/icsig/influence.py. Tests assert the equal unweighted edges and unequal kernels.
