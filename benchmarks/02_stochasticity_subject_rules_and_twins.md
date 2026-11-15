# Benchmark 02 — Stochasticity, subject rules, and mandatory twins

Status: **SPECIFICATION, not a result.** The fixtures below exist, are tested, and their neutral dynamical properties are reported as COMPUTATIONAL RESULTs. No consciousness, integrated-information, IIT, or ICSI-G quantity has been computed for any of them, and none is claimed.

**Why this benchmark exists.** Two findings in `docs/PHENOMENAL_CONSCIOUSNESS_2026-11-15.md` constrain what a discriminator can look like:

1. **Deterministic fixtures are dead comparators against IIT_4_0_2026.** That formalism defines `φ_s(s) = min{φ_c(s), φ_e(s), ii(s)}` with `ii_{c/e}(s) = min{i_diff, i_spec}`, and for a fully deterministic system `i_diff = 0`, hence `φ_s = 0` at every state, irrespective of causal structure (Mayner, Marshall & Tononi, arXiv:2510.03881v1, Eq. 13 and Eq. 23; Figure 1 caption). Both Benchmark 01 systems are fully deterministic. Any *structural* comparison must therefore move to stochastic substrates. See hypothesis H3.
2. **Subject rules must be forced to declare their quantifier.** Unit-level and state-level recurrence come apart, and adjoining an irrelevant component changes one and not the other. See hypothesis H5.

Benchmark 01 remains valid for what it established — that an unweighted influence graph does not determine a transition kernel. This benchmark adds the fixtures needed for the next questions.

---

## Fixtures

All fixtures are implemented in `src/icsig/examples.py`, described by `src/icsig/diagnostics.py`, and tested by `tests/test_diagnostics.py`. Print all of them with:

```bash
python examples/diagnostics_report.py
```

State ordering is lexicographic over binary tuples with the first listed unit as the most significant bit, matching the rest of the package.

### F1 — Noisy swap family (stochastic)

Units `(A, B)`. Intended dynamics `A_next = B`, `B_next = A`, with each next-state bit independently flipped with probability `p`. The two bits are drawn independently, so the joint next-state distribution factorises.

Constructor: `noisy_swap(p)`. Benchmark pair: `stochastic_same_graph_different_kernel()` returns `noisy_swap(0.1)` and `noisy_swap(0.3)`.

| p | Deterministic | Successor support | Influence graph | Kernel |
|---|---|---|---|---|
| 0.0 | yes | (1,1,1,1) | A↔B | **identical to Benchmark 01's swap system** |
| 0.1 | no | (4,4,4,4) | A↔B | distinct |
| 0.3 | no | (4,4,4,4) | A↔B | distinct |

**COMPUTATIONAL RESULT.** `noisy_swap(0.1)` and `noisy_swap(0.3)` share the influence graph `{A→B, B→A}` under the stochastic extractor and have different kernels. `noisy_swap(0.0)` reproduces Benchmark 01's swap kernel exactly, so the family interpolates continuously between a dead deterministic comparator and a live stochastic one.

**Threshold declaration (required).** The stochastic extractor marks an edge when toggling the source changes the target's next-state marginal by more than `threshold` in L1 distance, for at least one background assignment. At `p = 0.1` that distance is 1.6, so `threshold = 1.0` retains both edges and `threshold = 1.7` erases them. Any benchmark using this extractor must state its threshold; it is a modelling choice, not a fact about the system.

### F2 — Disconnected union (inert twin)

Units `(A, B, C)`. Swap dynamics on `(A, B)`; `C_next = 0` always, so C is neither influenced by nor influences the others.

Constructor: `disconnected_union_with_isolated_unit()`. Successor map `(0, 0, 4, 4, 2, 2, 6, 6)`.

| Property | Benchmark 01 swap | Disconnected union |
|---|---|---|
| Units | 2 | 3 |
| States | 4 | 8 |
| Unweighted influence graph | A↔B | **A↔B (unchanged)** |
| Recurrent state cycles | `(0,), (1,2), (3,)` | `(0,), (2,4), (6,)` |
| Strongly connected state components | 3 | **7** |
| C's next-state marginal | — | `(1.0, 0.0)` at every state |

**COMPUTATIONAL RESULT.** Adding one causally isolated unit leaves the influence graph invariant while taking the number of strongly connected state components from 3 to 7. This is the project's minimal "add an irrelevant component" fixture and the concrete mechanism behind the overgeneration worry in H5. It also serves as the **inert twin** required by H8: same structural invariant at the graph level, no functional integration of the added component.

### F3 — Feedforward chain (acyclic-influence fixture)

Units `(A, B, C)`. Update rules `A_next = B`, `B_next = C`, `C_next = 0`.

Constructor: `feedforward_chain()`. Successor map `(0, 2, 4, 6, 0, 2, 4, 6)`.

**COMPUTATIONAL RESULT.** Influence graph is `{C→B, B→A}` — acyclic. The fixture nevertheless has one recurrent *state*: a fixed point at 000 that every other state flows into, giving one cycle and 8 strongly connected state components.

**This is the ambiguity the benchmark exists to expose.** "Strongly connected support" as phrased in `docs/AGENT_REPORT_SYNTHESIS_2026-10-18.md` does not specify whether it quantifies over strongly connected *units* in the influence graph or strongly connected *states* in the transition digraph. On F3 the two readings disagree: no unit-level cycle, one state-level cycle. Any subject rule must pick one and say so. F3 is also the project's first candidate "unconscious twin" under any IIT-style criterion that requires recurrent influence at the unit level.

---

## Summary table (all fixtures)

```text
fixture                    units  det   alts  acyclic  cycles
B01 swap                   2      True  False False    ((0,), (1, 2), (3,))
B01 invert-plus-copy       2      True  False False    ((0, 2, 3, 1),)
B02 noisy swap p=0.1       2      False True  False    n/a
B02 noisy swap p=0.3       2      False True  False    n/a
B02 swap plus isolated C   3      True  False False    ((0,), (2, 4), (6,))
B02 feedforward chain      3      True  False True     ((0,),)
```

`det` = fully deterministic; `alts` = at least one state has two or more possible successors; `acyclic` = the unit-level influence graph contains no directed cycle.

---

## What must be computed next, and by whom

Nothing below has been done. Each item states the artifact, the owner under `docs/AGENT_PROTOCOL.md`, and what would count as a result rather than a claim.

### Step 1 — Pinned IIT runs on F1 only (Arena)

Run F1 (`p = 0.1` and `p = 0.3`) and both Benchmark 01 systems under a **pinned PyPhi commit**, reporting separately for `IIT_4_0_2023` and `IIT_4_0_2026`:

- `φ_s` per state;
- `i_diff`, `i_spec`, and `ii` per state (2026 preset only);
- the selected complex, and tie handling;
- system, state, background/marginalisation settings, and formalism preset, all recorded verbatim.

**Expected under H3, to be confirmed not assumed:** `φ_s = 0` at every state for both deterministic Benchmark 01 systems under `IIT_4_0_2026`; `φ_s > 0` for at least one of them under `IIT_4_0_2023`; `φ_s > 0` for both F1 members under both presets.

**This is a version-sensitivity finding until it is paired with a bridge principle.** A difference in formal output between 2023 and 2026 on the same system is exactly what `docs/RESEARCH_STATE.md` warns must not be reported as an ICSI-G result.

**Outstanding obligation.** `docs/REFERENCES.md` requires that equation numbering be verified against the published *Entropy* 28(4):410 version rather than the arXiv preprint. That check has not been performed and must precede any implementation.

### Step 2 — Grain sensitivity (Arena, with ChatGPT)

The 2026 paper's Discussion identifies macro-level sources of intrinsic differentiation: micro-level stochasticity, micro-to-macro grain mappings, and background fluctuations. A system deterministic at a coarse grain need not be deterministic at the grain IIT selects. Repeat Step 1 with at least one coarse-graining of F1 into macro units, and report whether the determinism conclusion survives. See Marshall, Findlay, Albantakis & Tononi (2026), "Intrinsic units: identifying a system's causal grain."

### Step 3 — Sheaf instantiation on F1–F3 (Gemini)

Instantiate the proposed sheaf on all six fixtures with explicit cells, stalks, restrictions, coboundary matrices, and state convention, and report the invariant for each. Specific questions:

- Does the invariant distinguish F1 at `p = 0.1` from F1 at `p = 0.3`, given identical influence graphs?
- Does it change when an isolated unit is adjoined (F2)? If yes, the invariant is not graph-level and Candidate B is excluded; if no, the invariant cannot see the overgeneration mechanism and H5's rule (a) is unavailable to it.
- Does it vanish or degenerate on F3, whose unit-level graph is acyclic but which has a recurrent state?
- Is the invariant stable under unit relabeling and under bit-flip gauge transformations, proved separately for each?

Do not treat a non-zero Betti number or non-zero cohomology group as evidence of anything. Per `docs/REFERENCES.md`, a non-zero topological invariant does not by itself demonstrate phenomenal experience or avoid overgeneration.

### Step 4 — Subject-rule decision (ChatGPT, with Claude)

Resolve, in writing and before Step 3's results are interpreted:

1. Unit-level or state-level quantification for "strongly connected support" (forced by F3).
2. Maximality rule (H5 rule a) or deflationary subjects (H5 rule b).
3. Tie-breaking policy, including the case of a tie with no next-highest value.
4. Whether F2's isolated component is inside or outside the subject boundary, and on what grounds.

### Step 5 — Model-class extension (Arena, with ChatGPT)

The current `FiniteBinaryTransitionSystem` has no input ports and no time-varying kernel, so **neither the unfolding construction nor the plasticity repair can be expressed in it**. Required additions, each behind its own tests:

1. Input-conditioned kernel `K(s' | s, u)`.
2. Kernel-update rule `K_{t+1} = f(K_t, s_t, s_{t+1})` for the plasticity hypothesis H4.
3. An input–output equivalence checker over a bounded horizon.
4. `unfold(K, T)`, producing a feedforward system equivalent over horizon `T`, for the unfolded twin required by H8.

Until Step 5 exists, H4 and the unfolded-twin half of H8 are **not testable as stated** and should be labelled accordingly in any report.

### Step 6 — Only then, bridge and prediction

With Steps 1–5 complete and a bridge shape declared under H2, the project can ask whether any candidate yields a tie-free discriminator, and of which kind — existence-level (H3) or structural (H2 corollary). H6's quality-space test presupposes a named invariant from Step 3 and a declared bridge shape from H2, so it comes after both.

---

## Reproduction

From the project root:

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python examples/diagnostics_report.py
```

A local run on 2026-11-15 with Python 3.11.2 reported **28 tests passed** (12 pre-existing from Benchmark 01, 16 new for the fixtures and descriptors in this benchmark). The `diagnostics_report.py` output above is verbatim from that run. Remote CI status has not been verified.

Executable definitions: `src/icsig/examples.py`. Neutral descriptors: `src/icsig/diagnostics.py`. Tests: `tests/test_diagnostics.py`.

---

## What this benchmark does not show

- That any fixture is or is not conscious, or is or is not a subject.
- That ICSI-G and IIT_4_0_2026 disagree about phenomenal structure. They have not been compared, and under H3 the deterministic fixtures cannot support such a comparison at all.
- That `φ_s = 0` for the Benchmark 01 systems. That is a derivation from published equations plus a verified property of the fixtures; the PyPhi confirmation in Step 1 has not been run.
- That the unfolding argument refutes ICSI-G. It identifies a dilemma that ICSI-G has not yet answered, and H4 proposes a repair that has not been tested.
- That a non-zero Betti number, a non-trivial cohomology group, an acyclic influence graph, or a recurrent state has any phenomenal significance.
