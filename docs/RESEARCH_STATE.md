# Shared Research Memory: ICSI-G

Last consolidated: 2026-10-18. This file is the working memory for future sessions and agents. Update it when a finding is reproduced, overturned, or superseded; retain the history in DECISION_LOG.md.

## Mission

Determine whether Intrinsic Causal-Structural Information (ICSI), particularly the ICSI-G candidate, can be made into a mathematically coherent, independently motivated, and empirically discriminable account of phenomenal structure. Compare it with specifically identified versions of Integrated Information Theory (IIT), with IIT 4.0 as the immediate comparison target.

This is an open research program, not a settled theory. Do not infer that an artificial system is conscious from a graph, a simulation, or a mathematical distinction alone. Do not start AGI construction until the user explicitly changes the research goal.

## Working description

ICSI-G provisionally proposes that global intrinsic causal topology may determine phenomenal structure. Earlier notes have identified three candidate commitments:

1. **Global topology:** the system's intrinsic causal organization contributes to phenomenal structure.
2. **Nested coexistence:** appropriately specified causal structures at different scales might correspond to nested or overlapping phenomenal identities.
3. **Structural identity:** systems that preserve the theory's relevant intrinsic causal structure might share qualitative phenomenal character.

These are hypotheses to define and test, not accepted premises. The phrase “intrinsic causal structure” is still ambiguous until variables, interventions, grain, state dependence, and the object used to represent causal power are specified.

## Prior checkpoint: 2026-10-12 to 2026-10-13

### DeepSeek's critical review (as summarized in the project notes)

It identified unresolved choices involving system boundaries, interventions, spatial and temporal grain, state dependence, topology invariants, phenomenal identity, consciousness level, and the bridge from physical organization to experience. Its conclusion was that ICSI-G was under-specified and would need independent motivation even if made coherent.

### Gemini's mathematical proposal (as summarized in the project notes)

Gemini proposed a dynamic state-space transition sheaf over an Alexandrov causal topology, and suggested a nonzero first Betti number / cohomology criterion (written in earlier notes as b1 >= 1 or H^1 nonzero) as part of a rule for inclusion. It also suggested an empirical comparison under graded interhemispheric decoupling.

**Status: unvalidated proposal.** The sheaf, base space, topology, restriction maps, cohomology, and inclusion criterion were not sufficiently specified or independently justified in the material reviewed. A nonzero topological invariant does not, by itself, demonstrate phenomenal experience or avoid overgeneration. The proposed IIT comparison and experimental predictions must be checked against primary sources and explicit calculations before being repeated as theory-level consequences.

### Arena's computational audit (as summarized in the project notes)

Arena reported examining 700 reachable two-unit deterministic systems and described several important cautions:

- Full transition kernels can differ even when reported IIT structures are identical in some examined cases.
- Some earlier examples compared a complex against a non-complex, so they did not establish a complex-level disagreement.
- Conclusions can change depending on whether the analyzed subject is the full network or a selected complex.
- Coarse ICSI variants may merge systems distinguished by the IIT 2023 formalism.
- IIT 2023 / IIT 4.0 and any later formalism must be treated separately.
- No tested tie-free, complex-level case was reported to establish a new phenomenal prediction from ICSI-G.

Limitations recorded: not all source artifacts or exact software commit identities were available, and two-unit deterministic enumeration does not cover stochastic, multiscale, or larger systems. Treat these as reported findings pending reproduction, not yet as verified project results.

### Prior conceptual and adversarial notes

A static graph is not enough to recover dynamics: systems can share an unweighted graph while having different transition rules. If ICSI-G relies only on graph topology, it risks predicting identical phenomenal structure for systems whose causal dynamics differ. Conversely, using a full transition kernel may distinguish almost every non-isomorphic system without explaining which distinctions matter phenomenally.

Other unresolved cases include:
- adding an isolated or causally irrelevant component;
- distinct microscopic dynamics hidden by the same coarse graph;
- different current states under identical dynamics;
- nested or overlapping candidate subjects;
- trivial feedback systems and panpsychist overgeneration;
- consciousness changes during sleep, anesthesia, or perturbation;
- whether qualitative structure and “amount” or level of consciousness are separate questions.

Some older agent prose presented the sheaf-repaired theory and callosal-decoupling predictions with high confidence. Later review found the specification and derivation insufficient. The more cautious later verdict governs until the claims are reconstructed.

## Current verdict

**ICSI-G remains under-specified.** We have not shown that it is false in every possible formulation, but neither have we established an independently motivated theory or a validated discriminator from IIT 4.0. Three broad approaches have different costs:

- **Full intrinsic causal repertoire / transition kernel:** potentially rich, but the exact object, equivalence relation, and reason it maps to experience are unsettled; raw difference may be too permissive.
- **Coarse qualitative graph or topology:** more compact and invariant to some details, but may erase state- and dynamics-relevant distinctions.
- **Dynamic-sheaf/topological candidate:** potentially expressive, but currently a mathematical research proposal with key definitions and bridge claims missing.

Mathematical non-equivalence is not yet consciousness-theoretic non-equivalence. Even a verified theorem that two formalisms return different objects would not establish different experiences without bridge principles connecting those objects to phenomenal facts.

## Immediate research agenda

1. Write explicit, separate specifications for the four candidates in ICSI_G_CANDIDATES.md.
2. Audit the definitions and primary sources for IIT 4.0 and any later version separately.
3. Build minimal finite counterexamples, verify state-label invariance, and reproduce the claimed exhaustive two-unit baseline (including exact enumeration scope).
4. Search for a **tie-free, complex-level discriminator** in which both candidates' definitions and subject-selection rules are fully applied.
5. Define and stress-test subject selection: whole network, selected complex, nested, overlapping, and disconnected candidates.
6. State an explicit bridge principle from causal object to phenomenal structure, then identify observations that would support or falsify it.
7. Only after these steps, consider empirical paradigms and predictions.

## Evidence labels

Use one of these labels in every substantive report:

- **MATHEMATICAL RESULT** — follows from stated definitions or a reproducible proof/calculation.
- **COMPUTATIONAL RESULT** — generated by specified code, inputs, versions, and tests.
- **THEORETICAL CLAIM** — an interpretation or prediction requiring additional premises.
- **EMPIRICAL EVIDENCE** — observation from a real study or dataset, cited precisely.
- **ASSUMPTION / OPEN QUESTION** — not yet justified or settled.
- **REJECTED / CORRECTED** — a prior claim that fails a check; link the correction.

## Quality bar for a real advance

A result is a candidate advance only if it has: (a) fully specified inputs and theory objects; (b) an explicit equivalence relation and boundaries; (c) a proof or reproducible computation; (d) an actual comparison against a named version of IIT; (e) a non-arbitrary bridge principle; and (f) a risky discriminating prediction or a meaningful empirical constraint. Confidence language cannot substitute for any of these.


## Comparator update: IIT 4.0 (2023) versus the 2026 formulation

Checked against current primary / project sources on 2026-10-18:

- Albantakis et al., *IIT 4.0: Formulating the properties of phenomenal existence in physical terms* (PLOS Computational Biology, published 2023-10-17), is the reference for the first published IIT 4.0 formalism. It identifies experience with the cause-effect structure unfolded from a maximal substrate, and defines overlapping-substrate selection using system integrated information (φ_s). The paper's example code is associated with the PyPhi feature/iit-4.0 branch.
- PyPhi's current project documentation and 2.0 changelog distinguish IIT_4_0_2023 from IIT_4_0_2026, as well as IIT 3.0. The 2026 update, associated with Mayner, Marshall & Tononi (2026), adds an intrinsic-information requirement to system φ: φ_s = min{φ_c, φ_e, ii(s)}. PyPhi documents that the 2026 value can differ from the 2023 value and that deterministic systems can have φ_s = 0 under the 2026 formalism. The separate version-selection presets are explicit in PyPhi.
- Marshall et al., *Intrinsic units: identifying a system's causal grain* (Neuroscience of Consciousness, 2026-04-15), expands IIT's framework for identifying causal grain across micro/macro units.

**Research consequence:** “compare against IIT 4.0” is not a reproducible instruction by itself. Every benchmark must pin IIT_4_0_2023 or IIT_4_0_2026 (and the exact PyPhi commit/version), and report both when claims purport to be robust across the 2023 and 2026 formulations. Prior notes about PyPhi 1.2 / IIT 3.0 cannot establish an IIT 4.0 divergence. We must not infer that any IIT formalism predicts a particular step-function outcome in a callosal-decoupling experiment without deriving that prediction from the pinned formalism and an explicit bridge to measurement.

Sources and access dates are recorded in docs/REFERENCES.md.


## First project-owned benchmark (2026-10-18)

The repository now contains Benchmark 01 and an executable finite-state example. Two deterministic two-unit systems were defined in state order 00, 01, 10, 11:

- Swap: A_next = B and B_next = A.
- Invert-plus-copy: A_next = NOT B and B_next = A.

The extraction rule marks an unweighted edge from current unit i to next-time unit j when toggling i changes j's next value for at least one assignment of the other current units. Under this explicit rule, both systems have exactly the reciprocal edge set {A → B, B → A}, while their complete transition kernels and state cycles differ.

**Conclusion:** an unweighted influence graph does not determine the full transition dynamics. This is a mathematical counterexample to unweighted graph sufficiency only. It does not establish that either system is conscious, that their phenomenal character differs, or that IIT treats them as equivalent.

The neutral model validation tests and influence-graph tests total 12. A local test run on a mirrored copy of the committed source passed all 12. A GitHub Actions workflow was added for Python 3.11–3.13; its remote status has not been independently verified in this session.
