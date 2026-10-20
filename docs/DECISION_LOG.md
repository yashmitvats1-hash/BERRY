# Decision Log

## 2026-10-18 — Repository initialization

**Decision:** BERRY will be a research and reproducibility repository for evaluating ICSI-G, not an AGI build.

**Current verdict:** ICSI-G is under-specified. The current evidence does not establish that it is a distinct and empirically discriminable theory of phenomenal consciousness versus IIT 4.0. This verdict is provisional and can change only through formal definitions, reproducible results, and a justified phenomenal bridge.

**Candidate variants kept separate:** full causal repertoire / transition kernel; coarse qualitative causal graph; state-conditioned global topology; dynamic state-space transition sheaf.

**Agent assignments:** ChatGPT leads formalization, review, and integration; Gemini investigates sheaf/topology; Arena reproduces computational claims; Claude audits phenomenal bridge principles and conceptual falsifiers; DeepSeek conducts an independent adversarial review using the offline packet.

**Implementation choice:** Add only a neutral finite-binary transition-system validator as the first executable artifact. It validates matrix shape and probability constraints; it does not compute consciousness, IIT, or ICSI-G.

**Research rule:** No claim about consciousness follows from mathematical divergence alone. Any proposed discriminator must compare well-specified predictions and state its bridge assumptions.

## Pending decisions

- Final mathematical object for each candidate.
- Exact IIT 4.0 primary specification and chosen reproducible implementation.
- Boundary, grain, intervention, and subject-selection policies.
- Whether the sheaf proposal yields a nontrivial, well-defined invariant with motivated phenomenal significance.
- Whether any tie-free, complex-level discriminator survives independent reproduction.


## 2026-10-18 — First executable counterexample

**Result label:** MATHEMATICAL RESULT, under an explicit unweighted Boolean-influence-graph definition.

Two deterministic two-unit systems (swap; invert-plus-copy) have the same unweighted reciprocal influence graph but different transition kernels and cycle structure. The result demonstrates that this coarse graph object loses dynamics. It does not establish a phenomenal difference or an IIT result. See benchmarks/01_same_influence_graph_different_dynamics.md.

**Implementation status:** Added a validated finite binary transition-kernel model, deterministic-successor parsing, an unweighted functional-influence graph extractor, the two example systems, 12 unit tests, a runnable script, and a GitHub Actions test workflow. A local mirror of the package/test logic passed all 12 tests. Remote CI remains unverified.

**Comparator update:** Primary documentation located during the session distinguishes IIT_4_0_2023 from IIT_4_0_2026. All future comparisons must pin one version and the exact PyPhi revision; historical IIT 3.0 results cannot stand in for IIT 4.0.

## 2026-10-20 — Arena replication of the enumeration and IIT comparisons (Issue #2)

**Reproduction status:** The committed package and tests were run on the actual checkout: 12/12 original tests pass on CPython 3.11.2 (closing the earlier "local mirror only" caveat); the icsig suite now totals 29 tests on the PyPhi environment.

**Correction 1 (enumeration scope):** the reported "700 reachable two-unit deterministic systems" is reproduced only as a count of (system, state) pairs: there are exactly **256** labeled deterministic two-unit binary systems, and **700** of the 1024 (system, state) pairs have a one-step-reachable (non-Garden-of-Eden) state, with image-size histogram {1: 4, 2: 84, 3: 144, 4: 24}. Alternative readings of "reachable" give 24 (forward orbit of 00) or 6 (strongly connected) systems. The 700-pair scope coincides exactly with PyPhi 2.0's analyzability rule (Garden-of-Eden states raise StateUnreachableForwardsError). The research record's phrasing is corrected; the number itself is reproduced.

**Correction 2 (identical IIT structures):** the earlier caution that "full transition kernels can differ even when reported IIT structures are identical" holds only degenerately: the only kernel-distinct pairs with identical state-conditioned CES profiles are 16 systems in 4 classes whose reachable-state CES is **empty** (φ_s = 0, zero distinctions). No two systems share a non-empty CES profile. Kernel difference without IIT structure is phenomenally empty by IIT's own standard, not a merger of structured systems.

**New results (all COMPUTATIONAL, pinned to PyPhi 2.0.0rc5.dev10+g134a8f31b):** (a) under IIT_4_0_2023, the Benchmark-01 pair S and N are tie-free complex-level discriminations — same unweighted graph, same scalar φ_s = 2.0 at all states, both the unique complex, but different CES (Φ 4.0 with 2 relations vs Φ 2.0 with 0 relations, negated cause specifications); (b) under IIT_4_0_2026 every deterministic two-unit system has φ_s = 0 at every state — no complexes exist in the baseline, so the discrimination is formalism-version-dependent; (c) in 384 of 700 analyzable states IIT selects singleton complexes while the whole network has φ_s = 0 (the complex-vs-non-complex trap, quantified); (d) all 16 unweighted influence-graph classes contain CES-distinct systems (coarse-graph candidate B merges everywhere); (e) 236 of 256 systems have state-dependent non-empty CES and none has a constant non-empty CES.

**Environment decision:** PyPhi 2.0 requires Python >= 3.13 and is not on PyPI; a CPython 3.13.16 was built from source (with OpenSSL 3.5.9, zlib, and a manually compiled libffi) and PyPhi installed at pinned commit 134a8f31b49db512322465ed3ba5da7194d362fd. Full provenance in docs/REFERENCES.md. Re-verify against a final PyPhi 2.0.0 tag when published.

**Artifacts:** src/icsig/enumeration.py, src/icsig/iit_comparison.py, examples/enumerate_reachable_systems.py, examples/iit_version_pinned_sweep.py, tests/test_enumeration.py, tests/test_iit_comparison.py, results/iit_two_unit_sweep.json, benchmarks/02_two_unit_enumeration.md, benchmarks/03_iit_version_pinned_comparison.md, reports/arena_issue_2_replication.md.

**CI note:** a proposed workflow addition (an `iit-tests` job installing the pinned PyPhi on Python 3.13) is saved as patches/add_iit_tests_job.patch, not committed: the submitting agent's GitHub token lacks the `workflows` permission. Maintainer review required. The existing unit-tests job continues to run the dependency-free and enumeration tests on Python 3.11–3.13.
