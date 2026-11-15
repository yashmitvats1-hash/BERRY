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

## 2026-11-15 — Phenomenal-bridge analysis, hypothesis ledger, and Benchmark 02 (proposed)

**Submitted by:** Claude workstream, in the role of applier and hypothesis purposer. Recorded as a proposal for the project lead; **no shared research memory (`docs/RESEARCH_STATE.md`, `docs/ICSI_G_CANDIDATES.md`) was rewritten**, per the coordination rules in `docs/AGENT_PROTOCOL.md`.

**Deliverables added**

- `docs/PHENOMENAL_CONSCIOUSNESS_2026-11-15.md` — deep-research report on what phenomenal consciousness is and what it means for a system to genuinely experience something, followed by an application to ICSI-G.
- `docs/HYPOTHESIS_LEDGER_2026-11-15.md` — eight falsifiable hypotheses (H1–H8) with bridge shape, explanandum target, prediction, falsifier, smallest artifact, owner, and evidence label; plus seven proposed amendments to shared memory and a dependency ordering.
- `benchmarks/02_stochasticity_subject_rules_and_twins.md` — specification for six fixtures and a six-step computation protocol. Marked SPECIFICATION, not a result.
- `agent_packets/FOLLOWUP_2026-11-15_BRIDGE_AND_HYPOTHESES.md` — offline packet for the DeepSeek review of H2, H3, H4, H8.
- `src/icsig/diagnostics.py`, new fixtures in `src/icsig/examples.py`, `tests/test_diagnostics.py`, `examples/diagnostics_report.py`.
- `docs/REFERENCES.md` — addendum of sources checked 2026-11-15, with per-source notes on exactly which claim each supports.

**Newly recorded findings**

1. **The unfolding argument applies to ICSI-G and was absent from project memory.** ICSI-G is a causal-structure theory in Doerig et al.'s (2019) sense, so the false-or-untouchable dilemma applies to it directly. Label: THEORETICAL CLAIM. Two repairs proposed: restrict the object to plastic/history-dependent dynamics (H4, following O'Reilly-Shah, Selvitella & Schurger 2026), or adopt a structural-coherence bridge rather than an identity bridge (H2).
2. **Deterministic fixtures are dead comparators against IIT_4_0_2026 for structural questions.** Verified against arXiv:2510.03881v1: `φ_s(s) = min{φ_c(s), φ_e(s), ii(s)}` with `ii_{c/e}(s) = min{i_diff, i_spec}`, and a fully deterministic system has `i_diff = 0`, hence `φ_s = 0` at every state regardless of causal structure. Both Benchmark 01 systems are fully deterministic (COMPUTATIONAL RESULT, verified in-repo). Consequence: structural discriminators require stochastic substrates. Labels: MATHEMATICAL RESULT for the derivation; THEORETICAL CLAIM for the divergence; COMPUTATIONAL RESULT for the fixtures. **Outstanding obligation:** equation numbering was checked against the arXiv preprint, not the published *Entropy* 28(4):410 version.
3. **ICSI-G's declared explanandum is narrower than IIT's.** None of candidates A–D addresses intrinsicality (the "for itself" feature IIT derives first) or level. Comparisons trading on existence or level exceed the candidates as written. Label: THEORETICAL CLAIM.
4. **The bridge-principle requirement (research rule 4) is incomplete as stated.** It does not say what would count as a bridge. Three shapes are available — identity, nomological law, structural coherence — with different costs, scopes, and admissible discriminators. A candidate must declare which it uses. Label: THEORETICAL CLAIM.
5. **"Strongly connected support" is ambiguous between unit-level and state-level recurrence.** The new feedforward-chain fixture has an acyclic unit-level influence graph and one recurrent state, so the two readings disagree. Must be resolved before any invariant is interpreted. Label: COMPUTATIONAL RESULT (fixture behaviour) + ASSUMPTION / OPEN QUESTION (which reading to adopt).

**Current verdict: unchanged.** ICSI-G remains under-specified. This submission does not establish that ICSI-G is a distinct theory of phenomenal consciousness, does not establish a validated discriminator from any IIT version, and does not assert anything about whether any system is conscious. It identifies two previously unrecorded threats (findings 1 and 2), narrows the search space for the tie-free discriminator, and proposes eight hypotheses with explicit falsifiers.

**Implementation status.** 28 tests pass locally (12 pre-existing, 16 new) with Python 3.11.2 under `.venv`. `examples/diagnostics_report.py` runs and its output is reproduced verbatim in Benchmark 02. The new descriptors are neutral: they describe transition kernels and influence graphs, and compute no consciousness, IIT, or ICSI-G quantity. Remote CI remains unverified.

**Known limitation recorded now rather than later.** The committed model class has no input ports and no time-varying kernel, so **neither the unfolding construction nor the plasticity repair is expressible in-repo**. H4 and the unfolded-twin half of H8 are therefore *not testable as stated* until the Step 5 model extension in Benchmark 02 exists.
