# Benchmark 02 — Exhaustive enumeration of two-unit deterministic systems

Status: **COMPUTATIONAL RESULT** (reproduced; see reproduction block).
This benchmark reconstructs the project's previously reported
"700 reachable two-unit deterministic systems" under explicit
definitions, corrects the phrasing, and provides the classification
data that later benchmarks build on. It computes no IIT quantities
and makes no consciousness claims.

## Definitions

* **Unit and state space.** Two binary units `A`, `B`; joint states
  ordered `00, 01, 10, 11` (big-endian, `A` most significant),
  state indices 0–3.
* **System.** A deterministic synchronous system is a pair of Boolean
  update functions `f_A, f_B : {0,1}^2 -> {0,1}`, each identified by
  its 4-bit truth table. There are 16 functions per unit and
  `16 × 16 = 256` **labeled** systems. System `code = 16·i + j`
  pairs truth table `i` (for `A`) with truth table `j` (for `B`).
* **Reachable state (one-step / non-Garden-of-Eden).** A state `s`
  is *reachable* when it lies in the image of the successor map,
  i.e. when at least one state maps to it in one step. This is the
  definition that reproduces the reported figure, and it coincides
  with PyPhi 2.0's own analyzability requirement: PyPhi rejects
  Garden-of-Eden states with `StateUnreachableForwardsError`,
  because IIT requires the current state to be reachable through
  the system's own dynamics.
* **Other notions, for disambiguation.** "Every state in the forward
  orbit of `00`" holds for 24 systems; "strongly connected" (every
  state reaches every state, i.e. a single 4-cycle) holds for 6.

## Results

**COMPUTATIONAL RESULT:** the labeled enumeration contains exactly
**256** deterministic two-unit binary systems. Across the
`256 × 4 = 1024` (system, state) pairs:

| Quantity | Count |
|---|---|
| (system, state) pairs, total | 1024 |
| one-step reachable pairs (state in image) | **700** |
| Garden-of-Eden pairs (state not in image) | 324 |

**COMPUTATIONAL RESULT:** the image-size histogram is
`{1: 4, 2: 84, 3: 144, 4: 24}`, and
`1·4 + 2·84 + 3·144 + 4·24 = 700`.

**Correction to the research record.** The earlier report of
"700 reachable two-unit deterministic systems" is reproduced only
under the (system, state)-pair reading: there are 256 labeled
systems, not 700, and 700 counts the reachable *states across
systems* (equivalently, the (system, state) pairs IIT can analyze
at all). The figure is therefore correct as a count of analyzable
(system, state) pairs and incorrect as a count of systems. This
correction is logged in `docs/DECISION_LOG.md`.

**COMPUTATIONAL RESULT:** functional-graph classification of the
256 systems (cycle structure as `(length, count)` pairs):

| Cycle signature | Systems | | Cycle signature | Systems |
|---|---|---|---|---|
| one fixed point | 64 | | one 3-cycle | 24 |
| one 2-cycle | 48 | | three fixed points | 12 |
| two fixed points | 48 | | two fixed points + one 3-cycle | 8 |
| fixed point + 2-cycle | 36 | | one 4-cycle | 6 |
| two fixed points + 2-cycle | 6 | | four fixed points | 1 |
| two 2-cycles | 3 | | | |

Attractor counts: 142 systems have a single attractor, 95 have two,
18 have three, 1 has four (the identity system, four fixed points).
The 142 single-attractor systems are exactly the connected
functional graphs on four labeled states.

**COMPUTATIONAL RESULT:** the 256 systems fall into **16 distinct
unweighted Boolean influence graphs**. The full graph
`{A→A, A→B, B→A, B→B}` contains 100 systems; six graphs contain 20
each; nine graphs contain 4 each. Benchmark 03 shows that all 16
classes contain systems with distinct IIT cause-effect structures.

## Reproduction

```bash
python -m pip install -e ".[dev]"
python examples/enumerate_reachable_systems.py
python -m pytest -q tests/test_enumeration.py
```

Executable definitions: `src/icsig/enumeration.py`
(`enumerate_two_unit_systems`, `reachable_state_pairs`,
`image_size_histogram`, `fully_reachable_systems`,
`strongly_connected_systems`, `cycle_structure_signature`).
Tests: `tests/test_enumeration.py`.

Software for this benchmark: CPython 3.11.2 (Debian bookworm),
pytest 9.1.1; the package has no third-party dependencies.

## Failure conditions and uncertainties

* The count 700 depends on the one-step-image definition of
  "reachable"; the two alternative notions defined above give 24
  and 6. The original report did not define the term, so the
  definition reconstructed here is the one that reproduces the
  figure exactly and matches PyPhi's analyzability rule.
* The enumeration covers labeled systems only. Quotienting by
  unit relabeling and state negation would reduce 256 further;
  that reduction is deliberately not applied, because IIT's
  formalisms are defined on labeled substrates and PyPhi's
  unit-order invariance is separately tested by its own suite.
* Two-unit deterministic systems do not cover stochastic kernels,
  larger substrates, or multiscale structure; those extensions are
  out of scope for this baseline (per the agent protocol).
