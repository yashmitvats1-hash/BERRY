# Hypothesis Ledger — Phenomenal Bridge and Discriminators

**Date:** 2026-11-15
**Author role:** applier and hypothesis purposer (Claude workstream)
**Parent document:** `docs/PHENOMENAL_CONSCIOUSNESS_2026-11-15.md`
**Status:** every entry below is a *proposal*. None is an established result. Nothing here asserts that any system — biological or artificial — is or is not conscious.

## How to read this ledger

Each hypothesis states what must be true, which bridge shape it presupposes (see parent §4.2), which explanandum slots it targets (G1 existence, G2 subjecthood, G3 content, G4 level, G5 non-mimicry), what would falsify it, the smallest artifact that would settle it, and who is best placed to produce that artifact under `docs/AGENT_PROTOCOL.md`.

**Risk** is stated deliberately: a hypothesis that would cost ICSI-G nothing to be wrong about is not worth running. Per research rule 7, counterexamples are the goal.

---

## H1 — Explanandum scoping

**Statement.** ICSI-G, in all four current candidate formulations, is a theory of *phenomenal structure* (composition, and at best integration). It is silent on phenomenal existence, silent on intrinsicality, and silent on level. Therefore any comparison with IIT that trades on whether a system is conscious at all, or on how much consciousness it has, exceeds ICSI-G's declared explanandum and is inadmissible unless a candidate adds an explicit existence or level postulate with independent justification.

**Bridge shape.** None required — this is a scoping claim about the candidates as written.
**Targets.** G3 (positively); G1, G4 (by exclusion).
**Basis.** Parent §4.1. IIT 4.0 derives intrinsicality first, from the "for itself" character of experience; a graph, kernel, or sheaf is an object computable by an external observer about a system, and nothing in Candidates A–D captures internality.

**Prediction.** If H1 is right, then searching the existing candidate text for an existence criterion or a level scalar will turn up nothing, and the phrase "consciousness level" will appear only in the list of *open* questions. If H1 is wrong, at least one candidate already entails a scalar ranking of systems by degree of experience.

**Falsifier.** A derivation, from a fully specified candidate, of (a) a criterion distinguishing conscious from non-conscious substrates, or (b) an ordinal or scalar level ranking, that does not smuggle in a premise outside the candidate's stated object.

**Smallest artifact.** A one-page audit table, one row per candidate, one column per explanandum slot, each cell marked *addresses / silent / contradicts*, with a pointer to the line of specification that licenses the mark.
**Owner.** Claude (draft) → ChatGPT (adjudicate and, if accepted, add an **Explanandum** row to the mandatory comparison table in `docs/ICSI_G_CANDIDATES.md`).
**Label.** THEORETICAL CLAIM.
**Risk.** High. If H1 holds, it forbids an entire class of comparisons the project has been attempting, including the callosal-decoupling step-function inference that `docs/RESEARCH_STATE.md` already flags as underived.

---

## H2 — Bridge-shape declaration

**Statement.** Every admissible ICSI-G bridge principle is exactly one of three shapes: **(i) identity** (the object *is* the experience), **(ii) nomological law** (a basic psychophysical law correlates object and experience), **(iii) structural coherence** (phenomenal structure mirrors the structure of access/awareness, without identity). The three have different overgeneration profiles, different falsifiers, and different admissible discriminators. A candidate that does not declare its shape cannot be evaluated, and a candidate that declares one shape while making claims that require another is internally inconsistent.

**Bridge shape.** Meta-hypothesis: it constrains which shapes are available.
**Targets.** All of G1–G5, by routing.
**Basis.** Parent §4.2. Shape (i) is IIT 4.0's explicit "explanatory identity"; shape (ii) is Chalmers' psychophysical laws and double-aspect theory of information; shape (iii) is Chalmers' principle of structural coherence and, methodologically, Fink et al.'s structural similarity constraint on NCCs.

**Derived consequences (these are the content of the hypothesis).**

| Declared shape | May claim | Must answer | Cannot claim |
|---|---|---|---|
| (i) Identity | G1, G2, G3 | unfolding argument; degeneracy; scope | — |
| (ii) Nomological law | G1, G2, G3 | scope of the law (which information spaces?); panpsychist overgeneration | — |
| (iii) Structural coherence | G3 only | dissociation cases between access structure and phenomenal structure | G1, G4, and any statement about whether a system is conscious |

**Prediction.** Under shape (iii), the "tie-free, complex-level discriminator" the agenda seeks must be re-specified as a *structural* discriminator: a case where both theories grant that the system is conscious but assign different phenomenal structures. Under shape (i) or (ii), an existence-level discriminator is admissible — and H3 supplies one immediately.

**Falsifier.** A fourth bridge shape that is not reducible to (i)–(iii), stated formally with its own scope rule and falsifier. Or a candidate that generates an existence-level prediction while declaring shape (iii).

**Smallest artifact.** A revision to research rule 4 and to the "Phenomenal bridge" row of the mandatory comparison table, requiring the declared shape plus a one-paragraph scope statement.
**Owner.** Claude (draft) → ChatGPT (integrate) → DeepSeek (adversarial audit via packet).
**Label.** THEORETICAL CLAIM.
**Risk.** High, and cheap to test. This is specification work, not mathematics, and it unblocks agenda items 4 and 6 simultaneously.

---

## H3 — Determinism divergence (H-DET)

**Statement.** ICSI-G imposes no indeterminism requirement: nothing in Candidates A–D makes intrinsic differentiation, stochasticity, or a repertoire of alternative next states a condition for phenomenal structure. IIT_4_0_2026 does impose one: `ii_{c/e}(s) = min{i_diff, i_spec}` and `φ_s(s) = min{φ_c, φ_e, ii(s)}`, and for a fully deterministic system `i_diff = 0`, hence `φ_s = 0`, hence no complex. Therefore **every fully deterministic system with non-trivial intrinsic causal structure is a commitment-level discriminator between ICSI-G and IIT_4_0_2026 about phenomenal existence (G1)**.

**Corollary (design constraint).** Because both sides must be evaluated on systems where IIT_4_0_2026 can return a non-zero answer, **any benchmark intended to discriminate phenomenal *structure* must use stochastic substrates.** Deterministic fixtures — including both Benchmark 01 systems — are dead comparators for structural questions under IIT_4_0_2026.

**Bridge shape.** (i) or (ii). Under (iii) the divergence is inadmissible, because shape (iii) makes no existence claim.
**Targets.** G1 (the divergence); the corollary constrains G3 benchmarks.
**Basis.** Parent §4.3. Derivation: deterministic ⇒ conditional distribution equals the maximally specific distribution ⇒ `i_diff = 0` ⇒ `ii = 0` ⇒ `φ_s = 0`. Confirmed by the source's own Figure 1 caption ("The fully deterministic system has `i_diff(s) = 0`, and thus `ii(s) = 0`") and by the monad example, whose `φ_s` peaks at intermediate determinism (`p = 0.744`) rather than at `p = 1`.

**Supporting COMPUTATIONAL RESULT (in-repo, verified).** Both Benchmark 01 fixtures are fully deterministic: `is_deterministic == True`, `successor_support_sizes == (1,1,1,1)`, `provides_alternative_states == False`. The stochastic fixtures `noisy_swap(0.1)` and `noisy_swap(0.3)` both have support `(4,4,4,4)` and share the influence graph `A↔B` while differing in kernel; `noisy_swap(0.0)` is exactly Benchmark 01's swap system.

**Prediction.** A pinned PyPhi run under the `IIT_4_0_2026` preset on either Benchmark 01 system returns `φ_s = 0` at every state, while the same run under `IIT_4_0_2023` returns `φ_s > 0` for at least one of them. On the stochastic fixtures, both presets should return `φ_s > 0`.

**Falsifier.** Any of:
- `i_diff > 0` for a fully deterministic system under the published *Entropy* definition (would collapse the derivation);
- a pinned PyPhi `IIT_4_0_2026` run returning `φ_s > 0` on a fully deterministic system at the declared grain;
- an ICSI-G candidate that turns out to require stochasticity after all (in which case the divergence disappears and the corollary becomes trivially satisfied rather than a constraint).

**Smallest artifact.** Two runs of a pinned PyPhi commit on the six fixtures in `benchmarks/02_stochasticity_subject_rules_and_twins.md`, under both presets, reporting `φ_s` per state, the selected complex, and tie handling — plus a written confirmation of the equation numbering in the published *Entropy* version.
**Owner.** Arena (computation, version pinning) with Claude (specification of what would count as confirmation).
**Label.** MATHEMATICAL RESULT for the derivation from the stated equations; THEORETICAL CLAIM for the divergence, pending the PyPhi confirmation and the grain caveat; COMPUTATIONAL RESULT for the determinism of the fixtures.
**Risk.** High. If H3 holds, the project's existing benchmark cannot be used for the purpose it was being held in reserve for, and agenda item 4 needs stochastic systems from the start.

**Grain caveat (must travel with the hypothesis).** The 2026 paper's Discussion lists macro-level sources of intrinsic differentiation — micro-level stochasticity, micro-to-macro grain mappings, and background fluctuations. A system deterministic at one grain need not be deterministic at the grain IIT selects. Any use of H3 must pin the grain and the coarse-graining policy; see Marshall, Findlay, Albantakis & Tononi (2026), "Intrinsic units: identifying a system's causal grain."

---

## H4 — Plasticity-restricted causal object (H-PLAST)

**Statement.** If ICSI-G's identity object is defined over *history-dependent* dynamics — a system whose transition kernel changes as a function of its own trajectory (rapid plasticity) — rather than over a static kernel, then the unfolding argument does not apply to it, because the functional-equivalence construction it depends on fails. Concretely: for a plastic recurrent system R, an unfolded static feedforward twin F matches R's input–output map only at the instant of unfolding, and diverges for all later times; so there is no static twin that preserves function while destroying the ICSI-G object.

**Bridge shape.** (i) or (ii). This is the repair that lets ICSI-G keep an identity bridge.
**Targets.** G5 (non-mimicry) primarily, and it protects G3.
**Basis.** Parent §3.4a and §4.5. O'Reilly-Shah, Selvitella & Schurger (2026) prove the plasticity caveat with arguments from history-dependent plasticity, dynamical systems analysis, information theory, perturbation stability, complexity growth, and resource limits.

**Cost (stated honestly).** The object is no longer a static structure over a fixed base. This threatens Candidate B outright (an unweighted graph over a fixed kernel cannot represent a changing kernel) and requires Candidate D's base space to be explicitly temporal — the sheaf would need to live over a trajectory or a time-indexed poset, not over a static state space. Candidate C is the best fit, since a state-conditioned topology is already part-way there.

**Prediction.** Two systems with identical i/o functions at `t = 0`, one plastic-recurrent and one static-feedforward, will (a) diverge in i/o behaviour at some `t* > 0`, (b) diverge in the ICSI-G object at `t*`, and (c) be distinguishable by a *behavioural* experiment run over a horizon longer than `t*`. Claim (c) is what makes the theory empirically touchable, which is exactly what the unfolding argument denies of static causal-structure theories.

**Falsifier.** A construction of a static feedforward system that tracks a plastic recurrent system's input–output map over an arbitrary interval. Or: demonstration that the ICSI-G object is invariant under the plasticity dynamics for a system whose behaviour demonstrably changes, which would mean the object is not tracking what the theory needs it to track.

**Smallest artifact.** A finite-state model class extension. The current `FiniteBinaryTransitionSystem` has no input ports and no time-varying kernel, so neither the unfolding construction nor the plasticity repair can be expressed in it. Required: (1) an input-conditioned kernel `K(s' | s, u)`; (2) a kernel-update rule `K_{t+1} = f(K_t, s_t, s_{t+1})`; (3) an i/o-equivalence checker over a bounded horizon; (4) the unfold construction `unfold(K, T)` producing a feedforward system equivalent over horizon `T`.
**Owner.** ChatGPT (formalisation of the object) + Arena (model class extension and equivalence checker) + DeepSeek (adversarial audit of whether the repair actually escapes the dilemma or just relocates it).
**Label.** THEORETICAL CLAIM.
**Risk.** High and structurally consequential. This is the only identified route by which ICSI-G keeps an identity bridge and remains empirically touchable. It is also the hypothesis most likely to fail, because it may turn out that plasticity merely pushes the equivalence construction out to a longer horizon rather than removing it.

---

## H5 — ICSI-G needs an exclusion analogue (H-EXCL)

**Statement.** Without a maximality rule, ICSI-G's "nested coexistence" commitment overgenerates subjects: for any candidate substrate satisfying the invariant, structure-preserving supersets, subsets, and parasets also satisfy it, so the number of candidate subjects is unbounded. ICSI-G must adopt either **(a)** a maximality rule over its own invariant — the subject is the maximal connected support attaining the invariant, with ties broken in favour of the next-highest value relative to the tied systems, mirroring IIT's exclusion — or **(b)** a deflationary account of subjects on which nested candidates are not distinct subjects, which preserves nested coexistence at the cost of denying that it yields distinct phenomenal identities.

**Bridge shape.** Independent of shape; this is a subject-selection requirement that any shape inherits.
**Targets.** G2.
**Basis.** Parent §4.4. Mørch argues consciousness cannot overlap and proposes a replacement formulation of exclusion; IIT's own postulate selects the maximal `φ_s` and resolves ties by the next-highest value. The problem of the many applies to any structure-based criterion that lacks a maximality clause.

**Supporting COMPUTATIONAL RESULT (in-repo).** Adding a causally isolated third unit to the swap dynamics leaves the unweighted influence graph exactly `{A→B, B→A}` while taking the state space from 4 to 8, recurrent cycles from `(0,), (1,2), (3,)` to `(0,), (2,4), (6,)`, and strongly connected state components from 3 to 7. A graph-level rule cannot see the change; a state-level rule sees seven candidate supports where it saw three.

**Specification ambiguity that must be closed first.** The feedforward-chain fixture has an acyclic *unit-level* influence graph but a recurrent *state* (a fixed point at 000 that every state flows into). A rule phrased as "strongly connected support" — as in the Gemini proposal recorded in `docs/AGENT_REPORT_SYNTHESIS_2026-10-18.md` — must declare whether it quantifies over strongly connected units in the influence graph or strongly connected states in the transition digraph. On the fixture the two readings give different answers (the chain has no unit-level cycle but one state-level cycle).

**Prediction.** Under rule (a), a disconnected union yields exactly as many subjects as it has maximal components attaining the invariant. Under no rule, it yields unboundedly many — one per structure-preserving superset. Rule (a) and rule (b) agree on the disconnected-union fixture and disagree on genuinely nested cases, so a nested fixture is required to separate them.

**Falsifier.** A case where the maximality rule is ill-defined — a tie with no next-highest value, or a maximum attained by incomparable supports — and no tie-breaking policy rescues it. Or a nested case that ICSI-G's own coexistence commitment requires counting as distinct subjects while rule (a) excludes one of them.

**Smallest artifact.** (1) A nested-subject fixture: a substrate containing two overlapping supports, each attaining the invariant, neither containing the other. (2) A tie fixture: two disjoint supports with equal invariant values. (3) A written decision between rule (a) and rule (b), with the unit-level/state-level ambiguity resolved.
**Owner.** ChatGPT (subject-selection policy) + Gemini (whether a sheaf-theoretic maximality rule is definable at all, since global sections may not restrict cleanly to a maximal support) + Claude (nested and tie fixtures, and the philosophical choice between (a) and (b)).
**Label.** THEORETICAL CLAIM + COMPUTATIONAL RESULT (fixture behaviour).
**Risk.** Moderate. Failing to adopt either rule is not fatal to the mathematics but is fatal to any claim about subjects, and G2 is where the ethical stakes live.

---

## H6 — The quality-space isomorphism test (H-HUE)

**Statement.** If ICSI-G's bridge is shape (i) or (ii), and if phenomenal quality is organised as a similarity space, then the ICSI-G object computed over colour-selective cortical populations must share the topological structure of the psychophysically derived hue similarity space. Human trichromat hue space is circular — parameterised by an angle ω ∈ S¹ — while dichromat hue space collapses to a line (or, on some descriptions, to two endpoint hues with a neutral midpoint) between blue near 475 nm and yellow near 575 nm, with grey in between. A circle has non-trivial first homology; an interval does not. Therefore:

> **Prediction.** A topological analysis of the neural representational-similarity structure for equiluminant chromatic stimuli in colour-selective cortex should recover a circular (1-cycle-bearing) structure in trichromats and a contractible, 1-cycle-free structure in dichromats. Any ICSI-G invariant that does **not** track this difference is refuted *as a bridge to phenomenal quality*, whatever its mathematical properties.

This is the flagship hypothesis of the ledger because it is the only one that tests the *bridge* rather than the mathematics, it is risky, and it is comparatively cheap: colour-vision-deficiency neuroimaging datasets exist, and the contrast is a within-species, cross-phenotype manipulation rather than a cross-species inference.

**Bridge shape.** (i) or (ii). Under (iii) the test becomes weaker but still meaningful: shape (iii) predicts that the structure of *access* (discrimination performance) tracks the structure of experience, and the dichromat/trichromat contrast in discrimination behaviour is independently well established.
**Targets.** G3.
**Basis.** Parent §2.3 and §5. Fink et al.'s structural similarity constraint: "neural substrates of phenomenal types must share the structure governing the phenomenal types they are associated with." Quality-space methodology: Clark (1993, 2000), Rosenthal (2010, 2015), with the JND/topology construction. Colour-vision topology: Meyer & Greenberg (1988); Lee (tetrachromacy theory), which states the trichromatic hue circle as ω ∈ S¹ and the dichromatic hue space as zero-dimensional.

**Why this is a real test and not a restatement.** The ICSI-G object is defined over *causal* structure; the quality space is defined over *phenomenal similarity* judgements. They are constructed from disjoint data. An isomorphism between them would be a substantive finding; a failure to match would be a substantive refutation of the bridge. Neither outcome is available by definition.

**Prerequisite checks that must pass before this is run.**
1. **Pin the phenomenal topology.** Sources disagree on whether dichromat hue is 0-dimensional (two hues) or 1-dimensional (a line). Both agree there is no 1-cycle, but the hypothesis must state the exact psychophysical construction used — which JND criterion, which stimulus set, which topology — because different topologies give different variation classes, and this is a known defect of quality-space methodology.
2. **Control for signal strength.** Michel's confound applies: fMRI representational-similarity structure can reflect signal quality rather than phenomenal structure. The design must use matched-performance or dissociation paradigms, not raw decoding accuracy.
3. **Declare the invariant.** Which invariant of the ICSI-G object is supposed to correspond to the 1-cycle? A first Betti number of what complex, over what base, at what resolution? This must be fixed before looking at any neural data.
4. **State the negative control.** A structure that should *not* differ between trichromats and dichromats — e.g. luminance-channel organisation — so that a global difference in data quality does not masquerade as confirmation.

**Falsifier.** Any of: neural representational topology identical in trichromats and dichromats while their phenomenal hue spaces demonstrably differ; a circular phenomenal hue space that no causal-structure invariant of the colour pathway tracks; or an ICSI-G invariant that is circular in both phenotypes.

**Smallest artifact.** A specification document — no data analysis yet — containing (1) the psychophysical construction and its topology, (2) the named ICSI-G invariant and how it is computed from a neural substrate, (3) the mapping claim between the two, (4) the confound controls, and (5) the pre-registered interpretation table for all four outcomes (match / mismatch / both-circular / neither-circular).
**Owner.** Claude (specification and confound controls) + Gemini (whether the named invariant is well-defined and stable) + ChatGPT (whether the mapping claim is consistent with the declared bridge shape).
**Label.** THEORETICAL CLAIM (a proposed empirical test). **This is not empirical evidence.** No result is reported here and none should be inferred from this document.
**Risk.** Very high. This is the only hypothesis in the ledger that could be falsified by data obtainable within the current state of the field, and it targets the exact gap the project has identified as blocking — the bridge.

---

## H7 — Structural silence on level (H-LEVEL)

**Statement.** ICSI-G should make *no* level prediction, and its silence is a prediction. Any scalar or ordinal level output from an ICSI-G candidate is a claim outside its declared explanandum (H1) and must be withdrawn unless independently justified. Specifically: ICSI-G should be silent on anesthesia, sleep, and perturbation — states where level varies while structure may not.

**Bridge shape.** Any.
**Targets.** G4, by refusal.
**Basis.** Parent §2.3, §4.1. Level is tracked clinically by behaviour-independent measures such as the perturbational complexity index (TMS–EEG response compressed with Lempel–Ziv complexity; threshold near 0.31; validated across wakefulness, dreaming, NREM sleep, sedation, and disorders of consciousness). ICSI-G has no counterpart, and inventing one would require saying what phenomenological fact it tracks.

**Prediction.** Across the anesthesia states used in the perturbational-complexity literature — propofol and xenon (unreported) versus ketamine (vivid dream-like reports on recovery) — an ICSI-G structure object computed from a fixed model of the relevant circuitry should be approximately *invariant*, while PCI is not. Invariance is the correct behaviour if H7 holds, because ICSI-G is not a level theory.

**Falsifier.** An ICSI-G candidate that predicts a level ordering which happens to match PCI, derived from its own object rather than fitted to it. That would be a genuine advance — and would refute H7 — but it would have to be derived before being compared.

**Why propose a hypothesis whose content is a refusal.** Because `docs/RESEARCH_STATE.md` already records the failure mode it prevents: "We must not infer that any IIT formalism predicts a particular step-function outcome in a callosal-decoupling experiment without deriving that prediction from the pinned formalism and an explicit bridge to measurement." H7 generalises that discipline from one experiment to the whole level dimension, and it protects the project from the most common way structural theories overreach.

**Smallest artifact.** A standing clause in the candidate specifications: "This candidate makes no claim about level of consciousness. Any level-like scalar it emits is a diagnostic, not a prediction."
**Owner.** ChatGPT (integrate into the specification template).
**Label.** THEORETICAL CLAIM.
**Risk.** Low as a hypothesis, high as a discipline. Adopting it costs nothing and forecloses an entire category of overclaim.

---

## H8 — Mandatory twin reporting (H-MIMIC)

**Statement.** No ICSI-G structural criterion should be reported without its two twins:
- **the unfolded twin** — a system with the same input–output function and a different ICSI-G object;
- **the inert twin** — a system with the same ICSI-G object and no functional integration (e.g. by adjoining a causally isolated component, or by holding the structure fixed while disconnecting it from any input–output role).

Together the twins force the criterion to state what distinguishes it from both pure functionalism (which the unfolded twin defeats) and pure structuralism-about-anything (which the inert twin defeats).

**Bridge shape.** Shape-dependent: under shape (i) the twins generate Doerig's dilemma and the criterion must answer it; under shape (iii) the unfolded twin is expected to differ in access structure as well, which is a checkable prediction rather than a dilemma.
**Targets.** G5.
**Basis.** Parent §3.4, §4.5. The unfolding argument is constructive, so the unfolded twin is not hypothetical — it can be built. Butlin et al.'s exclusion of IIT from their indicator list follows from the same incompatibility with computational functionalism, and ICSI-G inherits it.

**Prediction.** For every candidate, at least one unfolded twin and at least one inert twin exist and can be exhibited as finite fixtures. For Candidate B the unfolded twin is trivially available: the feedforward-chain fixture is acyclic at the unit level while the reciprocal pair is not.

**Falsifier.** A criterion for which no unfolded twin can be constructed — which would be a significant positive result, because it would mean the criterion is *not* a pure causal-structure criterion, and would immediately raise the question of what else it depends on.

**Model-class limitation (must be recorded).** The current `FiniteBinaryTransitionSystem` has no input ports, so a true unfolded twin — which requires an input–output function to preserve — cannot be expressed in the committed model class. The inert twin *can* be expressed, and the disconnected-union fixture is exactly that. Building unfolded twins requires the input-conditioned extension specified under H4.
**Owner.** Arena (model extension and twin construction) + Claude (which pairs of twins would be decisive) + DeepSeek (whether the twins are genuinely functionally equivalent, since Usher's objection turned on cases where they were not).
**Label.** THEORETICAL CLAIM + COMPUTATIONAL RESULT (the inert twin fixture exists and is tested).
**Risk.** Moderate. This is a reporting policy rather than a theory claim, but it is the policy that prevents the project from re-deriving mathematical differences and calling them phenomenal ones.

---

## 7. Proposed amendments to shared memory

These are **proposals for the project lead**, not edits to `docs/RESEARCH_STATE.md` or `docs/ICSI_G_CANDIDATES.md`, which per `docs/AGENT_PROTOCOL.md` are owned by ChatGPT. Nothing in shared memory has been rewritten.

1. **Research rule 4, strengthened.** "A structural difference is not automatically a phenomenal difference. An explicit bridge principle is required, **and it must declare which of the three shapes in `docs/HYPOTHESIS_LEDGER_2026-11-15.md` §H2 it instantiates, with a scope statement.**"
2. **New research rule 9.** "Deterministic fixtures cannot discriminate phenomenal structure against IIT_4_0_2026, because that formalism assigns `φ_s = 0` to fully deterministic systems at every state. Structural benchmarks must use stochastic substrates. (H3.)"
3. **Mandatory comparison table, two new rows.** **Explanandum** — which of {existence, intrinsicality, specificity, integration, exclusion, composition, level} the candidate addresses, and which it is silent on (H1). **Twins** — the unfolded twin and the inert twin, or a statement that neither can be constructed in the current model class (H8).
4. **Candidate D minimum definitions, item 6, strengthened.** The invariant must be named together with the phenomenal feature it is claimed to correspond to, and must be checkable against a psychophysically derived quality space (H6). A bare "b₁ ≥ 1 / H¹ non-zero" condition does not satisfy this and remains, as currently recorded, an unverified hypothesis.
5. **Agenda item 4, re-scoped.** The search for a tie-free complex-level discriminator should be split into (4a) an *existence-level* discriminator, of which H3 is a candidate pending PyPhi confirmation, and (4b) a *structural* discriminator, which requires stochastic fixtures and a declared bridge shape.
6. **New agenda item 8.** Extend the model class with input ports and a kernel-update rule so that the unfolding construction and the plasticity repair can be expressed at all (H4, H8). Until this exists, neither can be tested in-repo.
7. **`docs/REFERENCES.md`.** Add the sources numbered 10, 13, 15, 17, 19, 21, 26, 30, 37, 38 in the parent document, with access date 2026-11-15, and record the outstanding obligation to verify *Entropy* 28(4):410 equation numbering against arXiv:2510.03881v1.

## 8. Sequencing

Dependencies run in one direction, and running them out of order wastes effort:

```
H2 (declare bridge shape)
 ├── H1 (declare explanandum) ──┐
 ├── H3 (determinism divergence)│── H7 (level silence)
 └── H4 (plasticity repair) ────┘
              │
              └── H8 (twin reporting) ── requires the H4 model extension
H5 (exclusion analogue) ── requires the unit-level/state-level decision
H6 (quality-space test) ── requires H2, and the named invariant from Gemini
```

Recommended order: **H2 → H1 → H3 → H5 → H8/H4 → H6**. H2 and H1 are pure specification and can be closed in a single review pass. H3 is the first item with a computational confirmation path. H6 is last because it is the most expensive and presupposes everything else — but it is the only one that could be settled by data.

## 9. What would change the author's verdict

Per the deliverable format's requirement for an update condition: I would revise the assessment in the parent document if any of the following were produced.

- A PyPhi run under a pinned commit showing `φ_s > 0` for a fully deterministic system under `IIT_4_0_2026`. (Would falsify H3's corollary.)
- A fourth bridge shape, formally stated with its own scope rule. (Would falsify H2.)
- A derivation of a level scalar from any fully specified candidate. (Would falsify H1 and H7.)
- A static feedforward construction tracking a plastic recurrent system over an arbitrary interval. (Would falsify H4.)
- Evidence of a circular neural representational topology in dichromats alongside a contractible one in trichromats, or of identical topology across phenotypes with demonstrably different phenomenal hue spaces. (Would falsify H6.)
