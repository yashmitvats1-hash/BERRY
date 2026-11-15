# ICSI-G Follow-up Packet — 2026-11-15 — Bridge Shape, Determinism, and the Unfolding Argument

You are DeepSeek, the independent formal/adversarial reviewer. This packet supplements `agent_packets/DEEPSEEK_BRIEF.md` and `agent_packets/DEEPSEEK_FOLLOWUP_2026-10-19.md`. Do not assume the claims below are correct; they are a proposal from the Claude workstream and your job is to break them. You cannot read the repository directly, so everything you need is reproduced here.

## Context in one paragraph

A deep-research pass on "what is phenomenal consciousness, and what does it mean for a system to genuinely experience something?" produced three findings that constrain ICSI-G. First, the literature supplies exactly three shapes of bridge principle from a mathematical object to phenomenal structure, and ICSI-G has never declared which it uses. Second, the 2026 IIT formalism assigns zero system integrated information to every fully deterministic system, and both Benchmark 01 systems are fully deterministic. Third, the unfolding argument against causal-structure theories applies to ICSI-G directly, and it does not appear anywhere in prior project memory. Eight hypotheses (H1–H8) were proposed. You are asked to audit four of them.

---

## Item 1 — Is the bridge-shape trichotomy exhaustive? (audits H2)

The claim: every admissible bridge from an ICSI-G object to phenomenal structure is one of

- **(i) Identity.** The object *is* the experience. IIT 4.0's explicit position: "an experience is identical to the cause–effect structure unfolded from a maximal substrate … with no additional ingredients," framed as an explanatory identity between intrinsic (subjective) and extrinsic (objective) existence. Cost: inherits the unfolding argument; must reject degeneracy at the structure level; must solve the scope problem.
- **(ii) Nomological law.** A basic psychophysical law correlates object and experience. Chalmers' positive proposal, including the double-aspect theory of information: the same abstract information space is embedded in physical processing and in conscious experience. Cost: the scope question is unresolved — "to just *which* physically realized information spaces does the basic principle apply?" — and without a principled constraint the view collapses into panpsychism, while a constraint appealing only to physical structure collapses it back into physicalism.
- **(iii) Structural coherence.** Phenomenal structure *mirrors* the structure of access/awareness without identity. Chalmers' principle: if two representations are functionally similar the corresponding experiences are phenomenally similar; if orthogonal, orthogonal. Methodological descendant: Fink et al.'s structural similarity constraint — "neural substrates of phenomenal types must share the structure governing the phenomenal types they are associated with." Cost: explicitly limited — "not all properties of experience are structural properties" — so it can never deliver a claim about whether a system is conscious, or about level.

Derived consequence table:

| Declared shape | May claim | Must answer | Cannot claim |
|---|---|---|---|
| (i) Identity | existence, subjecthood, content | unfolding argument; degeneracy; scope | — |
| (ii) Nomological law | existence, subjecthood, content | scope of the law; panpsychist overgeneration | — |
| (iii) Structural coherence | content only | dissociation between access structure and phenomenal structure | existence, level, any consciousness attribution |

**Your tasks.**
1. Is the trichotomy exhaustive? If not, state a fourth shape formally, with its own scope rule and falsifier, and show that it is not reducible to a disjunction of (i)–(iii). Candidates worth testing: supervenience-without-identity; realization/constitution relations; deflationary or quietist bridges that deny the need for one; two-dimensionalist bridges that locate the connection in the structure of phenomenal concepts rather than in the world.
2. Is the consequence table correct? In particular: does shape (iii) really forfeit existence claims, or can a coherence bridge plus an independent existence criterion recover them without becoming shape (ii)?
3. Under shape (iii), the agenda's "tie-free, complex-level discriminator" must be re-specified as a *structural* discriminator: a case where both theories grant that the system is conscious but assign different phenomenal structures. Is that specification coherent? Can you exhibit a candidate pair?
4. Does declaring a shape actually change what mathematics is required, or is it cosmetic? Give the sharpest case that it is cosmetic, and the sharpest case that it is not.

---

## Item 2 — Audit the determinism derivation (audits H3)

**The claim.** Under IIT_4_0_2026, every fully deterministic system has `φ_s = 0` at every state, hence is not a complex, hence is not a substrate of consciousness, regardless of causal structure.

**The derivation as given.** From Mayner, Marshall & Tononi, arXiv:2510.03881v1 (published as *Entropy* 28(4):410, 2026):

- `ii_{c/e}(s) = min{i_diff^{c/e}(s), i_spec^{c/e}(s)}` — intrinsic information is the minimum of intrinsic differentiation and intrinsic specification, by the principle of minimal existence.
- `ii(s) = min{ii_c(s), ii_e(s)}` (Eq. 13).
- `φ_s(s) = min{φ_c(s), φ_e(s), ii(s)}` (Eq. 23).
- `i_diff` is the intrinsic difference between the system's conditional distribution and a **maximally specific** distribution. For a fully deterministic system the conditional distribution *is* the maximally specific distribution, so the difference is zero.
- The source states this directly in the Figure 1 caption: "The fully deterministic system has `i_diff(s) = 0`, and thus `ii(s) = 0`." Symmetrically: "The uniformly random system has `i_spec(s) = 0` and so also has `ii(s) = 0`."
- The source's §2.3 diagnosis of the earlier formalism: "Perfectly deterministic systems could therefore achieve high intrinsic information despite having no intrinsically defined alternatives."
- The source's monad example (§3.1) maximises `φ_s` at intermediate determinism, `p = 0.744` giving `φ_s = 0.427`, not at `p = 1`.
- Therefore: deterministic ⇒ `i_diff = 0` ⇒ `ii = 0` ⇒ `φ_s = min{φ_c, φ_e, 0} = 0`.

**Verified in-repo (COMPUTATIONAL RESULT).** Both Benchmark 01 systems are fully deterministic. Benchmark 01 recap: units `(A, B)`, state order 00, 01, 10, 11.
- Swap: `A_next = B`, `B_next = A`. Successor map `(0, 2, 1, 3)`. Cycles `(0,), (1,2), (3,)`. Fixed points 00 and 11.
- Invert-plus-copy: `A_next = NOT B`, `B_next = A`. Successor map `(2, 0, 3, 1)`. One 4-cycle `00 → 10 → 11 → 01 → 00`.
- Both have unweighted influence graph exactly `{A→B, B→A}`; kernels and cycle structures differ.

**Your tasks.**
1. Check the derivation line by line. Is "maximally specific distribution" the right comparator for a deterministic conditional, or could `i_diff` be defined against a different reference such that a deterministic system scores positive?
2. Is the claim state-wise or system-wise? Could a system be deterministic overall yet have `i_diff > 0` at some state, or non-deterministic overall yet `i_diff = 0` at the state IIT selects?
3. **Grain.** The source's Discussion identifies macro-level sources of intrinsic differentiation: micro-level stochasticity, micro-to-macro grain mappings, and background fluctuations. Construct the strongest case that a *coarse-grained* description of a deterministic micro-system has `i_diff > 0`, and say what that does to the corollary "deterministic fixtures are dead comparators."
4. Verify that this is specific to IIT_4_0_2026 and does **not** hold of IIT_4_0_2023, which quantifies intrinsic information by specification alone. If it holds of both, the divergence claim collapses.
5. The corollary is that structural discriminators require stochastic substrates. Is that right, or could a deterministic system still support a structural comparison if the comparison is about `φ`-structure rather than `φ_s`? Distinguish carefully: `φ_s` governs substrate selection, and the Φ-structure governs content.
6. Note for your report: equation numbering above was checked against the **arXiv preprint**, not the published *Entropy* version. Flag any place where that matters.

---

## Item 3 — Does the plasticity repair actually work? (audits H4)

**The problem.** The unfolding argument (Doerig, Schurger, Hess & Herzog 2019, *Consciousness and Cognition* 72:49–59): for any recurrent network there is a purely feedforward network with an identical input–output function — replicate the recurrent layer once per timestep and wire the copies in sequence. Under IIT the recurrent original has `Φ > 0` and the unfolded twin has `Φ = 0`. So either the theory is false (unfolded twins can be conscious) or it is empirically untouchable (they cannot, and no i/o experiment distinguishes them). Doerig et al. add that systems with identical i/o functions can have arbitrary conscious content under IIT. ICSI-G is a causal-structure theory, so this applies to it.

**The proposed repair (H4).** Define ICSI-G's object over *history-dependent* dynamics — a kernel that changes as a function of the system's own trajectory — rather than over a static kernel. Basis: O'Reilly-Shah, Selvitella & Schurger (2026, *Neuroscience of Consciousness* 2026(1):niag027) prove that rapid synaptic plasticity negates functional equivalence between a recurrent network and a static feedforward network: the unfolded twin matches only at the instant of unfolding `t_0` and diverges for all `t > t_0`. Their arguments run through history-dependent plasticity, dynamical systems analysis, information theory, perturbation stability, complexity growth, and resource limits. If so, the construction has no fixed target, and the theory becomes empirically touchable: a behavioural experiment over a horizon longer than the divergence time `t*` can distinguish the two systems.

**Stated cost.** The object is no longer a static structure over a fixed base. Candidate B (unweighted graph over a fixed kernel) cannot represent a changing kernel at all. Candidate D's base space would have to become explicitly temporal — a sheaf over a trajectory or a time-indexed poset rather than over a static state space. Candidate C (state-conditioned topology) is the best fit.

**Your tasks.**
1. Does the repair escape the dilemma or relocate it? Construct the strongest counter: perhaps plasticity only pushes functional equivalence out to a longer horizon, so for any bounded experiment an unfolded twin exists, and the theory remains untouchable in practice for every experiment anyone could run.
2. Is "rapid" plasticity load-bearing? What happens with slow plasticity, or plasticity that is itself deterministic and computable from the initial state? If the update rule `K_{t+1} = f(K_t, s_t, s_{t+1})` is deterministic and known, can't an unfolded twin simply simulate `f`?
3. Does the repair preserve ICSI-G's own motivations? If the object is a trajectory of kernels, in what sense is it still *intrinsic causal structure* rather than a functional/dynamical description — and if it has become functional, has ICSI-G quietly converted itself into a functionalist theory, which would destroy its intended contrast with IIT?
4. Give a minimal finite example: the smallest system with a kernel-update rule for which no static feedforward system tracks its i/o map beyond `t = 0`. State the state space, the update rule, and the divergence time.
5. Independent of H4: is there a *different* route by which a causal-structure theory answers the unfolding argument? Consider restricting the domain to systems whose i/o function is not computable by a feedforward architecture at all, or denying premise P1 of Doerig et al. (that scientific investigation must rely on i/o-accessible measurement).

---

## Item 4 — Twin reporting policy (audits H8)

**The proposal.** No ICSI-G structural criterion should be reported without two twins:
- **unfolded twin** — same input–output function, different ICSI-G object;
- **inert twin** — same ICSI-G object, no functional integration of some part.

Together they force the criterion to say what separates it from pure functionalism (defeated by the unfolded twin) and from structuralism-about-anything (defeated by the inert twin).

**Available fixtures.**

*Inert twin (built and tested).* Units `(A, B, C)`; swap dynamics on `(A, B)`; `C_next = 0` always, so C is causally isolated. Successor map `(0, 0, 4, 4, 2, 2, 6, 6)` over states 000…111 with A most significant.

| Property | Benchmark 01 swap | Inert twin |
|---|---|---|
| Units / states | 2 / 4 | 3 / 8 |
| Unweighted influence graph | A↔B | **A↔B, unchanged** |
| Recurrent state cycles | `(0,), (1,2), (3,)` | `(0,), (2,4), (6,)` |
| Strongly connected state components | 3 | **7** |

*Acyclic-influence fixture (built and tested).* Units `(A, B, C)`; `A_next = B`, `B_next = C`, `C_next = 0`. Successor map `(0, 2, 4, 6, 0, 2, 4, 6)`. Influence graph `{C→B, B→A}` — acyclic. Nevertheless has one recurrent *state*: a fixed point at 000 that every state flows into.

*Stochastic pair (built and tested).* Units `(A, B)`; `A_next = B`, `B_next = A`, each next-state bit independently flipped with probability `p`. At `p = 0.1` and `p = 0.3`: same influence graph `{A→B, B→A}` under a distributional-dependence extractor, different kernels, successor support `(4,4,4,4)` at every state. At `p = 0.0` the kernel is **identical to Benchmark 01's swap system**, so the family interpolates between a deterministic and a stochastic comparator. The extractor marks an edge when toggling the source changes the target's next-state marginal by more than a declared L1 threshold for at least one background assignment; at `p = 0.1` that distance is 1.6, so threshold 1.0 keeps both edges and threshold 1.7 erases them.

**Your tasks.**
1. Is the twin policy sufficient, or is a third twin needed? Consider an *isomorphic twin* — same ICSI-G object, different substrate or grain — and a *degenerate twin*, in Michel's sense: different causal structure, same function, where biology suggests both could realise the same experience.
2. Usher objected to the unfolding argument on the ground that after ablation the recurrent and feedforward systems no longer implement the same function, and Doerig et al. replied that the argument concerns cases where they *do*. Audit the fixtures above against that standard: are the proposed twins genuinely functionally equivalent, or only structurally similar? Be specific about what "functionally equivalent" means for a closed autonomous system with no input ports.
3. **Model-class limitation.** The committed model class is a closed autonomous system: a square transition kernel over all joint states, with no input ports and no time-varying kernel. A true unfolded twin requires an input–output function to preserve. State precisely what must be added to the model class — and whether the addition changes what "system" means in a way that undermines the benchmark.
4. Does the inert twin actually defeat structuralism-about-anything, or does it only defeat *graph-level* structuralism? The inert twin leaves the influence graph invariant while changing state-space structure substantially, so a criterion sensitive to state-level recurrence already distinguishes it.

---

## Standards for your report

- Prefer explicit finite counterexamples and derivations over verbal summaries.
- Label every claim: MATHEMATICAL RESULT, COMPUTATIONAL RESULT, THEORETICAL CLAIM, EMPIRICAL EVIDENCE, ASSUMPTION / OPEN QUESTION, or REJECTED / CORRECTED.
- Do not infer phenomenal differences from mathematical differences. Do not treat topology or cohomology as a bridge by definition. Do not assert a divergence from any IIT version without naming the formalism (`IIT_4_0_2023` or `IIT_4_0_2026`), the version, the state, the boundary, the candidate complex, and the tie handling.
- Give the strongest case for each hypothesis and the strongest case against it, then a verdict per item: established, supported but incomplete, exploratory, refuted, or not testable as stated.
- State one concrete result that would change your overall verdict.
- Return the report in a portable format so it can be integrated into BERRY.

## Sources cited in this packet

- Albantakis, L. et al. (2023). "Integrated information theory (IIT) 4.0." *PLOS Computational Biology* 19(10):e1011465. DOI 10.1371/journal.pcbi.1011465.
- Mayner, W. G. P., Marshall, W. & Tononi, G. "Intrinsic Cause–Effect Power: The Tradeoff Between Differentiation and Specification." arXiv:2510.03881v1; *Entropy* 28(4):410 (2026). DOI 10.3390/e28040410.
- Marshall, W., Findlay, G., Albantakis, L. & Tononi, G. (2026). "Intrinsic units: identifying a system's causal grain." *Neuroscience of Consciousness* 2026(1):niag013. DOI 10.1093/nc/niag013.
- Doerig, A., Schurger, A., Hess, K. & Herzog, M. H. (2019). "The unfolding argument." *Consciousness and Cognition* 72:49–59. DOI 10.1016/j.concog.2019.04.002.
- O'Reilly-Shah, Selvitella & Schurger (2026). "A caveat regarding the unfolding argument: implications of plasticity." *Neuroscience of Consciousness* 2026(1):niag027. DOI 10.1093/nc/niag027.
- Michel, M. "On the dangers of conflating strong and weak versions of a theory of consciousness." (degeneracy; NCC vs neural constituents.)
- Mørch, H. H. "Why Consciousness Can't Overlap." (subjects; exclusion.)
- Chalmers, D. J. (1995/1996). "Facing Up to the Problem of Consciousness." (structural coherence; double-aspect information; psychophysical laws.)
- Fink, B. et al. (2021) and the quality-space literature (Clark 1993, 2000; Rosenthal 2010, 2015). (structural similarity constraint.)
- Butlin, P., Long, R., Bayne, T., Bengio, Y., Birch, J., Chalmers, D. et al. (2025/2026). "Identifying indicators of consciousness in AI systems." *Trends in Cognitive Sciences* 30(6). DOI 10.1016/j.tics.2025.10.011. (Indicator list excludes IIT as incompatible with computational functionalism.)
- Cogitate Consortium (2025). *Nature* 642(8066):133–142. DOI 10.1038/s41586-025-08888-1.

Annotated copies, with the specific claim each source supports, are in `docs/REFERENCES.md` and §7 of `docs/PHENOMENAL_CONSCIOUSNESS_2026-11-15.md`.
