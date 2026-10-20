# Arena replication report — Issue #2

Workstream: computational replication and adversarial model
checking (per docs/AGENT_PROTOCOL.md). Date: 2026-10-20.
Agent: Arena. All findings below carry the evidence labels
defined in docs/RESEARCH_STATE.md.

## 1. Claim summary

1. **[COMPUTATIONAL RESULT — reproduced]** The reported
   "700 reachable two-unit deterministic systems" is exactly
   reproduced as the count of (system, state) pairs whose
   state is one-step reachable (in the image of the
   successor map) across the 256 labeled deterministic
   two-unit binary systems: `1·4 + 2·84 + 3·144 + 4·24 =
   700` reachable pairs, 324 Garden-of-Eden pairs. The
   figure is **not** a count of systems; there are exactly
   256 labeled systems. The original report's phrasing was
   ambiguous; the reconstructed definition is the only one
   found that yields 700, and it coincides with PyPhi 2.0's
   own analyzability rule (Garden-of-Eden states are
   rejected with `StateUnreachableForwardsError`).
   **[CORRECTION of the research record's phrasing; logged
   in DECISION_LOG.md.]**

2. **[COMPUTATIONAL RESULT — reproduced]** Benchmark 01's
   pair is confirmed and extended: under the pinned PyPhi
   build, the swap system `S` and the invert-and-copy
   system `N` have the same unweighted influence graph,
   different kernels, and — under `IIT_4_0_2023` — the
   same whole-network `φ_s = 2.0` at all four states but
   **different cause-effect structures** (`Φ = 4.0` with 2
   relations vs `Φ = 2.0` with 0 relations; negated cause
   specifications in `N`).

3. **[COMPUTATIONAL RESULT — new]** Version sensitivity is
   decisive: under `IIT_4_0_2026`, every deterministic
   two-unit system has `φ_s = 0` at every state, hence
   **no complexes at all** in the entire baseline. Every
   complex-level statement about these systems must pin
   `IIT_4_0_2023`; under the default 2026 formalism the
   complex-level comparison is void.

4. **[COMPUTATIONAL RESULT — new]** Subject-selection
   trap quantified: in 384 of the 700 analyzable states,
   IIT selects singleton complexes while the whole network
   has `φ_s = 0`. A whole-network comparison there is a
   non-complex comparison.

5. **[COMPUTATIONAL RESULT — correction]** The earlier
   claim that "full transition kernels can differ even when
   reported IIT structures are identical" is confirmed only
   degenerately: the sole kernel-distinct pairs with
   identical state-conditioned CES profiles are 16 systems
   in 4 classes whose reachable-state CES is **empty**
   (zero distinctions, `Φ = 0`). No two systems share a
   non-empty CES profile.

6. **[COMPUTATIONAL RESULT — new]** Coarse-graph merging:
   all 16 influence-graph classes contain systems with
   distinct IIT 4.0 (2023) CES profiles; the Benchmark-01
   graph class itself contains 4 systems with 4 distinct
   profiles.

7. **[COMPUTATIONAL RESULT — new]** State dependence: 236
   of 256 systems have state-dependent non-empty CES; none
   has a constant non-empty CES; 20 have empty CES
   everywhere.

8. **[COMPUTATIONAL RESULT — new]** Tie-free complex-level
   discriminator between ICSI-G candidate B and
   `IIT_4_0_2023`: `S` vs `N` (same graph, same scalar
   `φ_s`, both complexes, different CES). **[THEORETICAL
   CLAIM if and only if a bridge principle is supplied:
   none is supplied here; the difference is mathematical,
   not phenomenal.]**

## 2. Definitions and assumptions

* Two binary units `A`, `B`; states `00, 01, 10, 11`
  (big-endian in this package; PyPhi uses little-endian —
  the conversion is explicit in `src/icsig/iit_comparison.py`
  and round-trip tested).
* Deterministic synchronous system: pair of Boolean
  functions `f_A, f_B : {0,1}² → {0,1}`; 256 labeled
  systems.
* Reachable state: in the image of the one-step successor
  map (non-Garden-of-Eden).
* IIT quantities are **PyPhi's** computations of the named
  formalisms, not independent re-derivations: `φ_s`
  (system integrated information), complexes (exclusion
  postulate competition), CES distinctions and relations
  with `Φ` (structure integrated information).
* Assumption: PyPhi 2.0's presets faithfully implement
  Albantakis et al. (2023) and Mayner et al. (2026). The
  2026 equations were not re-derived from the paper here.

## 3. Computational procedure

1. Enumerated all 256 labeled systems; computed successor
   maps, images, cycle decompositions, influence graphs
   (`src/icsig/enumeration.py`).
2. Reproduced the 700 figure and its decomposition;
   cross-checked the alternative reachability notions (24
   forward-orbit systems; 6 strongly connected).
3. Installed PyPhi at pinned commit `134a8f31b…` (build
   provenance in REFERENCES.md) on a from-source CPython
   3.13.16.
4. Swept all 256 systems × 4 states × 2 formalisms with
   `pyphi.analyze` (SIA + CES) and `substrate.complexes`
   (`examples/iit_version_pinned_sweep.py`); recorded
   `φ_s`, complex sets, and label-independent CES
   fingerprints (mechanisms, purviews, specified states,
   directional `φ`, relations, `Φ`) to
   `results/iit_two_unit_sweep.json`.
5. Aggregated: version sensitivity, complex selection,
   profile collision classes, influence-graph classes,
   state dependence.

## 4. Minimal examples / counterexamples

* **Graph/dynamics (Benchmark 01):** `S` vs `N` — same
  unweighted graph, different kernels, different CES under
  2023 (`Φ` 4.0 vs 2.0; relations 2 vs 0).
* **Kernel-difference without IIT structure:** codes 3, 6,
  9, 12 (`f_A ≡ 0`; `f_B ∈ {A, A⊕B, ¬(A⊕B), ¬A}`) — four
  distinct kernels and three distinct influence graphs,
  empty CES at every reachable state, identical (empty)
  profiles.
* **Complex-vs-non-complex trap:** system 1 (`f_A ≡ 0`,
  `f_B = NOR(A,B)`), state `00`: whole network `φ_s = 0`;
  complex `{B}` with `φ_s ≈ 0.1578`.

## 5. Sources

* Albantakis et al. (2023), *IIT 4.0*, PLOS Comput. Biol.
  19(10):e1011465 — DOI 10.1371/journal.pcbi.1011465.
* Mayner, Marshall & Tononi (2026), *Intrinsic Cause–Effect
  Power*, Entropy 28(4):410 — DOI 10.3390/e28040410 (as
  recorded in REFERENCES.md; equation numbering still to
  be verified against the published text).
* PyPhi 2.0.0rc5.dev10+g134a8f31b, commit
  `134a8f31b49db512322465ed3ba5da7194d362fd`,
  github.com/wmayner/pyphi (`main`, 2026-10-16); changelog
  statements on formalism presets and deterministic
  `φ_s = 0` under the default.

## 6. Reproduction artifacts

* `src/icsig/enumeration.py`, `src/icsig/iit_comparison.py`
* `examples/enumerate_reachable_systems.py`,
  `examples/iit_version_pinned_sweep.py`
* `tests/test_enumeration.py`, `tests/test_iit_comparison.py`
  (the latter skips when PyPhi is absent)
* `results/iit_two_unit_sweep.json` (full sweep evidence)
* `benchmarks/02_two_unit_enumeration.md`,
  `benchmarks/03_iit_version_pinned_comparison.md`
* Test status: 23 passed / 6 skipped on CPython 3.11.2
  (core suite); 29 passed on CPython 3.13.16 with PyPhi.

## 7. Failure conditions and uncertainties

* PyPhi 2.0 was still on a release-candidate-line version;
  no final `v2.0.0` tag existed at computation time.
  Re-verify against the final tag when published.
* The CES fingerprint omits full repertoire probability
  vectors (compares maximizers and `φ` values only).
* The 700-figure reconstruction depends on the
  one-step-image reading of "reachable"; other readings
  give 24 or 6 (documented in Benchmark 02).
* Deterministic two-unit systems do not exercise
  stochasticity, larger substrates, or macro grains.

## 8. Recommended changes to the candidate specification

* **Candidate B (coarse graph):** now has a computed,
  pinned, tie-free complex-level counterexample class (all
  16 graph classes merge CES-distinct systems under
  `IIT_4_0_2023`). Any revival of candidate B must either
  justify phenomenal irrelevance of the merged distinctions
  or add retained structure (signs, weights, state
  conditioning).
* **Candidate A (full kernel):** the 16 empty-CES systems
  show kernel differences that IIT scores as zero
  structure; candidate A needs an explicit rule for which
  kernel differences are phenomenally relevant, or it
  remains "raw difference is too permissive".
* **Candidate C (state-conditioned topology):** IIT's
  object is state-dependent in 236 of 256 systems (and
  never constant when non-empty); a state-independent
  topology cannot match it. A state-conditioned variant
  must specify the state-dependence rule explicitly.
* **Version pinning is mandatory:** any future IIT
  comparison must name `IIT_4_0_2023` or `IIT_4_0_2026`
  and the PyPhi commit; the two formalisms give opposite
  complex-level verdicts on the entire deterministic
  baseline.

## 9. Verdict

**Established (computational):** the 700 figure is
reproduced under an explicit, PyPhi-consistent definition
with a corrected phrasing; the S/N pair is a tie-free,
complex-level, version-pinned discriminator of ICSI-G
candidate B against `IIT_4_0_2023` (mathematical
discrimination only); the version-sensitivity, subject
selection, and empty-structure corrections are
established. **Open:** whether any ICSI-G formulation
survives as a distinct theory still requires the
specification work owned by the project lead and Gemini;
no phenomenal prediction is made here.
