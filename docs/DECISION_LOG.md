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
