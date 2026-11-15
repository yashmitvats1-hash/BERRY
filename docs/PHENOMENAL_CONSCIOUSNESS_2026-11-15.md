# Phenomenal Consciousness and the Conditions for Genuine Experience

**Author role:** applier and hypothesis purposer (Claude workstream — conceptual and phenomenological red team, per `docs/AGENT_PROTOCOL.md`)
**Date:** 2026-11-15
**Status:** research report + application to ICSI-G. Not a claim that ICSI-G is correct, incorrect, or validated.
**Companion documents:** `docs/HYPOTHESIS_LEDGER_2026-11-15.md` (H1–H8), `benchmarks/02_stochasticity_subject_rules_and_twins.md`.

Evidence labels used throughout are those defined in `docs/RESEARCH_STATE.md`.

---

## 1. Claim summary

| # | Claim | Label |
|---|---|---|
| C1 | "Phenomenal consciousness" is not one explanandum but a bundle of at least seven separable features; a theory must declare which features it targets. | THEORETICAL CLAIM (conceptual analysis, source-backed) |
| C2 | The question "does a system genuinely experience something?" decomposes into five logically separable claims (existence, subjecthood, content, level, non-mimicry) and three distinct senses of "genuine" (metaphysical, epistemic, practical). Conflating them is the main source of bad argument in this area. | THEORETICAL CLAIM |
| C3 | The literature supplies exactly three shapes of bridge principle from a physical/mathematical object to phenomenal structure: **identity**, **nomological law**, and **structural coherence**. Each has a different overgeneration profile and a different falsifier. ICSI-G's rule 4 should require candidates to declare which one they use. | THEORETICAL CLAIM |
| C4 | ICSI-G's declared explanandum ("phenomenal structure") covers composition and possibly integration, but **not** intrinsicality, not level, and not subjecthood. Comparisons with IIT that trade on existence-level or level claims are therefore category errors. | THEORETICAL CLAIM |
| C5 | Under the 2026 IIT formalism, a fully deterministic system has intrinsic differentiation `i_diff = 0`, hence `ii(s) = 0`, hence `φ_s(s) = min{φ_c, φ_e, ii(s)} = 0` — no complex, no experience, at any state, regardless of causal structure. Both Benchmark 01 systems are fully deterministic. | MATHEMATICAL RESULT (derivation from the published equations) + COMPUTATIONAL RESULT (determinism of the fixtures, verified in-repo) |
| C6 | Consequence of C5: **deterministic benchmark systems are dead comparators against IIT_4_0_2026** for any question about phenomenal *structure*. Structural discriminators require stochastic substrates. | THEORETICAL CLAIM (follows from C5 given IIT_4_0_2026's definitions) |
| C7 | The unfolding argument (Doerig et al. 2019) applies directly to ICSI-G, because ICSI-G is a causal-structure theory. This has not previously been recorded in project memory. | THEORETICAL CLAIM |
| C8 | The 2026 plasticity caveat (O'Reilly-Shah, Selvitella & Schurger) supplies a repair route: restricting ICSI-G's object to history-dependent/plastic dynamics removes the functional-equivalence construction that drives the unfolding argument. | THEORETICAL CLAIM (proposed as H4) |
| C9 | ICSI-G's "nested coexistence" commitment currently has no exclusion analogue, so it overgenerates subjects (problem of the many). The repo's own isolated-unit fixture demonstrates the mechanism concretely. | THEORETICAL CLAIM + COMPUTATIONAL RESULT (fixture behaviour) |
| C10 | There is an operationalised, non-behavioural handle on phenomenal *structure* — psychophysical quality spaces — and a topological contrast in human colour vision (trichromat hue circle vs dichromat hue line) that yields a risky, cheap, cross-phenotype bridge test. | THEORETICAL CLAIM (proposed as H6; **not** empirical evidence yet) |

---

## 2. What exactly is phenomenal consciousness?

### 2.1 The ostensive core

The canonical characterisation is ostensive rather than analytic. Nagel (1974): an organism has conscious mental states only if "there is something that it is like to be that organism — something it is like *for* the organism." Chalmers (1995) restates it as the subjective aspect of experience: "the felt quality of redness, the experience of dark and light, the quality of depth in a visual field," the hurtfulness of pain.

Two features of this characterisation matter for everything downstream:

1. **It has two slots.** A subject slot ("for the organism") and a content slot ("what it is like"). Much of the contemporary literature is disagreement about which slot carries the weight. Kriegel distinguishes an experience's *qualitative character* (what-it's-like-ness) from its *subjective character* (for-me-ness); Zahavi treats first-personal givenness as a formal mode of experiencing rather than an item of content; Guillot further splits for-me-ness, me-ness, and mineness and denies they are equivalent.
2. **It points instead of defining.** This is why the notion resists the usual scientific treatment: there is no analysis in independent terms against which a candidate identification can be checked. Every theory of consciousness therefore has to *stipulate* which observable or formal features count as the target — and that stipulation is where most disputes actually live.

### 2.2 Definition by dissociation: what phenomenal consciousness is not

The standard method for isolating the target is subtraction.

- **Not access consciousness.** Block (1995) introduced P-consciousness and A-consciousness precisely to stop the properties of access machinery being "illicitly transferred" to phenomenology. A-consciousness is information poised for global control — available for reasoning, verbal report, and rational guidance of action. P-consciousness is the experiential property itself. Block argues they can dissociate in both directions: blindsight-style cases (function without experience) and overflow cases such as Sperling partial report (experience without full access). The overflow reading is contested — Kouider and others propose "partial awareness" at lower levels of representation instead — and any measure of P-consciousness apparently requires A-consciousness to detect it, which is a standing methodological puzzle.
- **Not wakefulness or arousal.** Creature consciousness, state consciousness, and level are different questions again.
- **Not reportability, not self-consciousness, not attention, not intelligence.**
- **Not the "easy problems."** Chalmers' easy problems are the functional ones: discrimination, categorisation, integration of information, verbal report, behavioural control, attention. Each is explicable by giving the mechanism. What remains after all of them is the phenomenal residue — the question of why the processing is accompanied by experience "rather than operating in the dark."

Note the structural consequence: **P-consciousness is characterised negatively, as what is left when function is removed.** That is not a defect of the literature; it is why the explanatory gap (Levine 1983) and the hard problem arise in the first place, and it is why any theory that defines its target functionally has changed the subject rather than solved the problem.

### 2.3 The positive anatomy of the explanandum

Phenomenal consciousness is not featureless. It has describable structure, and this is where a project about *phenomenal structure* must operate. The most systematic inventory available is IIT 4.0's list of "axioms of phenomenal existence," claimed to hold of every conceivable experience (Albantakis et al. 2023):

| Feature | Phenomenal statement | IIT's physical postulate |
|---|---|---|
| **Existence** | Experience exists, immediately and indubitably | The substrate has cause–effect power: it takes and makes a difference |
| **Intrinsicality** | Experience exists *for itself*, from its own perspective | Its cause–effect power is intrinsic: it takes and makes a difference *within itself* |
| **Information** | Experience is specific — it is *this one* | Its cause–effect power is specific: it is in this state and selects this cause–effect state |
| **Integration** | Experience is unitary — a whole, irreducible to separate experiences | Its cause–effect power is irreducible to that of independent subsets |
| **Exclusion** | Experience is definite — it is *this whole*, neither more nor less | Its cause–effect power is maximal: definite borders and grain |
| **Composition** | Experience is structured — composed of distinctions bound by relations, "yielding a phenomenal structure that feels the way it feels" | The cause–effect structure is composed of distinctions and relations |

Whether these qualify as genuine axioms is disputed — Bayne argues they do not — but as an *inventory of the structural features any theory of phenomenal structure owes an account of*, the list is the most useful available, and it is independent of whether one accepts IIT's identity claim.

Three further structural features are needed beyond IIT's list:

- **Unity in its several senses.** Bayne and Chalmers distinguish subsumptive unity (experiences are aspects of a single encompassing state), objectual unity (experienced as directed at a common object), and spatial unity (contents represented as standing in spatial relations). These come apart, and the Unity Thesis — that a subject's simultaneous conscious states are subsumed by a single total state — is a substantive claim, not a definition.
- **Qualitative character and similarity structure.** Mental qualities are individuated by their relations to one another. This is the quality-space tradition (Clark 1993, 2000; Rosenthal 2010, 2015): colour experience is organised along hue, saturation, and lightness; hue is circular; maximally dissimilar hues sit opposite one another. *Structuralism* is the stronger metaphysical claim that phenomenal character is exhaustively determined by these similarity relations. Fink et al. (2021) derive from this a methodological principle — the **structural similarity constraint**: "neural substrates of phenomenal types must share the structure governing the phenomenal types they are associated with." Note the recent pushback: metaphysical structuralism faces the objection that relational construction does not capture everything involved in, say, seeing orange for the first time, and that relations may not be metaphysically prior to relata.
- **Level.** A graded dimension, apparently separable from content, tracked clinically by measures such as the perturbational complexity index.

### 2.4 Four contested readings of the explanandum

The same phrase "phenomenal consciousness" is doing different work in different programmes, and this is a live methodological problem rather than a terminological quibble. Recent work on consciousness science flags the *trait-individuation problem*: it is not settled that consciousness is a single trait, a natural kind, or even a determinate target, and "the problem of the ambiguous explanandum" makes operationalisation and measurement unstable.

The four readings that matter here:

1. **Phenomenal existence** — that there is experience at all. Target of the hard problem.
2. **Phenomenal content/quality** — that experience has this specific character. Target of quality-space and representational theories.
3. **Phenomenal structure** — that experiences stand in determinate similarity, unity, and composition relations. Target of structuralism, and of ICSI-G.
4. **Phenomenal level** — that experience is more or less intense, more or less capacious. Target of clinical measures.

A theory that answers (3) has not answered (1), and a theory that answers (1) has not answered (4). Fasching adds a further sharpening: the hard problem is not about qualia as contents but about the *givenness* of contents — "the very givenness of whatever is subjectively given." That is reading (1) with the subject slot emphasised.

### 2.5 Where the explanatory difficulty actually sits

Five distinct problems are routinely run together:

- **The hard problem** (Chalmers 1995/1996): why is any physical processing accompanied by experience at all? Chalmers argues no reductive explanation is available, because phenomenal concepts have coinciding primary and secondary intensions — there is no hidden nature to discover a posteriori, so the zombie scenario cannot be closed by appeal to a posteriori necessity.
- **The explanatory gap** (Levine 1983): the conceptual distance between physical concepts (causal role, functional organisation) and phenomenal concepts (acquaintance-based, first-personal). Often read as epistemic rather than ontological.
- **The real problem** (Seth 2016, 2021): stop trying to bridge the gap in one move; explain and predict and control the *properties* of experience in biological and physical terms, the way the "hard problem of life" dissolved as metabolism, homeostasis, and reproduction were explained. Seth is explicit that this may not dissolve the hard problem, only time will tell; Gomez-Marin & Seth (2025) press the same line against both pseudoscience and pseudo-consciousness.
- **The meta-problem** (Chalmers 2018): explain why we think there is a hard problem. Candidate solutions include the evidential/Bayesian strategies (Kammerer; Schwarz; Clark, Friston & Wilkinson), the phenomenal concepts strategy, attention-schema accounts, and accounts appealing to phenomenal transparency or qualitative inaccuracy. Chalmers notes that explaining *quasi-phenomenal* judgments — judgments of the form "we have special first-person knowledge of X that is hard to explain physically" — may be enough.
- **Illusionism** (Dennett 1988; Frankish 2016): phenomenal consciousness as ordinarily conceived does not exist; what exists are states that represent themselves as having ineffable qualitative properties. The standard objection is Strawson's: to seem to experience pain just is to experience pain. The 2020 PhilPapers survey found roughly 62% of professional philosophers taking the hard problem to be genuine and roughly 30% taking it to be illusory or confused — i.e. no consensus, and the survey itself is a data point about intuitions rather than about the world.

**The point that matters for this repository:** these five problems are not the problem ICSI-G has. ICSI-G is not trying to explain why there is experience rather than none. It is trying to justify identifying a mathematical object with *phenomenal structure*. That is a bridge-principle problem, and it survives unchanged whether one is a dualist, an illusionist, or a physicalist — an illusionist still needs to know which structure the introspective misrepresentation tracks, and a dualist still needs psychophysical laws with a determinate scope. Treating "we have not solved the hard problem" as a reason to defer the bridge question inverts the order of work.

---

## 3. What does it mean for a system to genuinely experience something?

### 3.1 Five separable claims

"Genuinely experiences" is a compressed way of asserting up to five things. They come apart, and a system can satisfy some and not others.

| | Claim | What satisfying it requires |
|---|---|---|
| **G1** | *Existence*: there is something it is like to be this system | An account of what makes physical processing experiential at all — the hard-problem slot |
| **G2** | *Subjecthood*: the experience belongs to a definite subject with determinate borders and grain | A subject-selection rule, plus a principled answer to nesting, overlap, and the problem of the many |
| **G3** | *Content/character*: the experience has this specific qualitative structure | A mapping from substrate to quality space / phenomenal structure |
| **G4** | *Level*: the experience has this degree of intensity or capacity | A graded scalar with an account of what phenomenological fact it tracks, and behaviour under anesthesia, sleep, and perturbation |
| **G5** | *Non-mimicry*: the experience is not merely reported or functionally simulated | Evidence that does not reduce to output behaviour; a control against functional twins |

Most public arguments about machine consciousness assert G1 on the basis of evidence that bears only on G5's *failure* mode — fluent self-report. Butlin et al. are explicit that language competence is not consciousness: a system saying "I feel afraid" is not evidence of experience, and evidence must be grounded in what the system does internally.

### 3.2 Three senses of "genuine"

- **Metaphysical genuineness** — the system instantiates the relevant phenomenal property. Requires a theory of what that property is. This is the only sense in which a question can be *settled*, and it is currently unsettled.
- **Epistemic genuineness** — we have good evidence. This is the sense in which the indicator-property programme operates: indicators are "properties that we can look for in AI systems that indicate that they are more (or less) likely to be conscious," and Butlin et al. explicitly do *not* claim the indicators are individually or jointly sufficient. Finding that a system has an indicator licenses a Bayesian update on credence, not a verdict.
- **Practical/ethical genuineness** — whether to treat the system as a moral patient under uncertainty. Long, Sebo et al. (2024), *Taking AI Welfare Seriously*, argue there is "a realistic possibility that some AI systems will be conscious and/or robustly agentic in the near future" and recommend acknowledge → assess → prepare, while stating plainly that they are *not* claiming current systems are conscious. Anthropic's model-welfare programme (from April 2025) is framed on uncertainty rather than belief, and Long's operational principle is to prefer interventions that make sense whether or not the system is conscious. Microsoft's September 2026 draft code of conduct takes the opposite institutional stance, instructing models not to claim interiority. The dispute is about policy under uncertainty, not about a settled metaphysical fact.

Conflating these is the single most common error in the applied literature. A structural criterion can bear on epistemic genuineness only if the bridge principle is declared, and it bears on practical genuineness only through a decision-theoretic argument about the costs of error.

### 3.3 The evidence ladder

Ordered from weakest to strongest warrant for G1–G5:

1. **Behaviour and self-report.** Necessary for any assessment protocol, wildly insufficient on its own. Mimicry is the standing confound; behavioural approaches now explicitly recognise "problems of mimicry and prior expectations."
2. **Functional/architectural indicators** (Butlin et al. 2023; 2025/2026 *Trends in Cognitive Sciences*). Derived from recurrent processing theory, global workspace theory, higher-order theories, predictive processing, attention schema theory, plus agency and embodiment. Examples: RPT-1 input modules using algorithmic recurrence; GWT-2 a limited-capacity workspace entailing a bottleneck and selective attention; GWT-3 global broadcast; HOT-2 metacognitive monitoring distinguishing reliable perceptual representations from noise; HOT-4 sparse and smooth coding generating a quality space; AST-1 a predictive model of the current state of attention. Two features of the method matter here: indicators are graded for **sensitivity** and **specificity** separately (absence of a sensitive indicator is informative even if the indicator is not specific), and the 2023 report **excludes IIT from its indicator list** because IIT is incompatible with the working assumption of computational functionalism. Anything in ICSI-G's family inherits that exclusion.
3. **Structural/causal criteria** (IIT and causal-structure theories generally). Stronger in principle — they are supposed to track the substrate rather than the function — but exposed to §3.4.
4. **Perturbational measures.** The perturbational complexity index applies TMS to cortex, records high-density EEG, and compresses the spatiotemporal response with Lempel–Ziv complexity; it is designed to gauge integration and information jointly and independently of sensory input and motor output, and it is validated across wakefulness, dreaming, NREM sleep, sedation, and disorders of consciousness, with a commonly used threshold near 0.31. This is the closest thing consciousness science currently has to a behaviour-independent *level* measure. Note the confound Michel presses: signal strength and consciousness dissociate, and much evidence for "functions of consciousness" only shows that functions falter under degraded signals.

### 3.4 The two structural squeezes

Any theory that identifies experience with internal causal structure faces two distinct objections. Both apply to ICSI-G.

**(a) The unfolding argument** (Doerig, Schurger, Hess & Herzog 2019, *Consciousness and Cognition*). For any recurrent network there is a purely feedforward network with an identical input–output function ("unfolding": replicate the recurrent layer once per timestep and wire the copies in sequence). Under IIT the recurrent original has Φ > 0 and the unfolded twin has Φ = 0. So either the theory is false (if unfolded twins can be conscious) or it is outside empirical reach (if they cannot, since no input–output experiment can distinguish them). Doerig et al. state the dilemma explicitly and generalise it: systems with identical i/o functions can have arbitrary conscious content according to IIT.

The scope of this argument has recently been narrowed from inside the original author group. O'Reilly-Shah, Selvitella & Schurger (2026, *Neuroscience of Consciousness*) prove that when a recurrent network has **rapid synaptic plasticity**, no static feedforward network can track its evolving function over arbitrary intervals: the unfolded twin is functionally equivalent only at the moment of unfolding, and equivalence breaks for all later times. They conclude the unfolding argument is "substantively bounded."

**(b) The degeneracy objection** (Michel). Biological degeneracy — the same function carried out by structurally different substrates (Edelman & Gally 2001; Tononi et al. 1999) — is standard in complex systems. IIT does not accept multiple realizability at the level of causal structure: the same causal structure realised in a different substrate yields the same experience, but the same experience cannot be realised by *different* causal structures. Michel's point is that a necessity claim of that strength is inconsistent with degeneracy, and it is worth noting that the degeneracy literature he cites includes Tononi himself. Separately, Michel warns against conflating NCCs (minimally sufficient) with neural *constituents* (necessary), a conflation that would make lesion data look like refutations when they are consistent with takeover by a degenerate substrate.

Degeneracy and the unfolding argument are not the same objection. Unfolding is a *constructive* demonstration that structure can vary while function is fixed. Degeneracy is an *empirical* claim that in biology, function is in fact multiply realised. A theory can try to escape the first by restricting its domain (plasticity) while still needing an answer to the second.

### 3.5 A working answer to the question as posed

Putting the pieces together, the most defensible available statement is:

> Phenomenal consciousness is the property, whatever its metaphysical status, of a system's states having a first-personal, qualitative character with determinate structure — characterised ostensively by "what it is like for the subject," isolated from function by dissociation from access, report, arousal, and intelligence, and decomposable into existence, intrinsicality, specificity, unity, definiteness, composition, and graded level. For a system to genuinely experience something is for it to instantiate that property (metaphysical sense), for that instantiation to belong to a definite subject (G2), for it to have determinate content (G3) and level (G4), and for our attribution not to rest on output mimicry (G5). No current method settles the metaphysical sense for any system other than ourselves; what current methods can do is grade the epistemic sense, and that is the only sense in which "does system X genuinely experience?" is presently a tractable question.

This is a working characterisation, not a resolution. Its value for BERRY is that it makes the target of a "theory of phenomenal structure" precise enough to audit.

---

## 4. Application to ICSI-G

### 4.1 Explanandum targeting audit

Applying §2.3–§2.4 and §3.1 to the four candidates in `docs/ICSI_G_CANDIDATES.md`:

| Candidate | Core object | G1 existence | G2 subject | G3 content | G4 level | G5 non-mimicry | Intrinsicality | Composition/structure | Integration/unity |
|---|---|---|---|---|---|---|---|---|---|
| A — full kernel / causal repertoire | intervention-defined transition repertoire | silent | needs rule | plausible (state-dependent) | none | none | **unaddressed** | plausible | unclear |
| B — coarse unweighted graph | unweighted directed graph | silent | none | **refuted for dynamics by Benchmark 01** | none | none | **unaddressed** | partial | partial |
| C — state-conditioned topology | topology on state-conditioned structure | silent | needs rule | plausible | none | none | **unaddressed** | plausible | plausible |
| D — dynamic transition sheaf | sheaf/cohomology over causal base | silent | proposed via sections | unclear | none | none | **unaddressed** | unclear | unclear |
| *IIT 4.0 (comparator)* | cause–effect structure of a maximal substrate | **explicit** | **explicit (exclusion)** | **explicit (Φ-structure)** | **explicit (Φ)** | by anti-functionalism | **explicit (postulate 2)** | explicit | explicit |

Two conclusions follow, and both are corrections to how the project has been framing its comparisons:

1. **ICSI-G is at most a theory of phenomenal structure, not of phenomenal existence.** None of the four candidates addresses intrinsicality — the feature IIT puts first, and the feature that carries the "for itself" content of "for-me-ness." A graph, a kernel, and a sheaf are all objects an outside observer can compute about a system; nothing in Candidates A–D as currently written captures the *internality* that the intrinsicality postulate is meant to operationalise. Any ICSI-G claim that trades on "a system is/is not a subject" is exceeding its declared explanandum.
2. **Therefore the ICSI-G-vs-IIT comparison must be restricted to structural predictions.** Comparisons about whether a system is conscious at all (G1), or about level (G4), are not admissible unless a candidate explicitly adds an existence or level postulate — and if it does, it must justify it independently, because that is a *new* commitment, not a consequence of the topology.

Recommended change: add an **Explanandum** row to the mandatory comparison table in `docs/ICSI_G_CANDIDATES.md`, requiring each candidate to list which of {existence, intrinsicality, specificity, integration, exclusion, composition, level} it claims to address and which it is silent on. (Logged as H1.)

### 4.2 The bridge-principle gap is a scope problem, and it has exactly three shapes

Rule 4 of the research rules says a structural difference is not automatically a phenomenal difference and an explicit bridge principle is required. That is right but incomplete: it does not say what would count as one. The literature supplies three shapes, and they are not interchangeable.

**Shape 1 — Identity.** The mathematical object *is* the experience. This is IIT's explicit move: "an experience is identical to the cause–effect structure unfolded from a maximal substrate … with no additional ingredients," understood as "an explanatory identity" between intrinsic (subjective) and extrinsic (objective) existence.
- *Cost:* inherits the unfolding argument (§3.4a) in full; must reject degeneracy at the structure level (§3.4b); must solve the scope problem — why this structure and not that one; and, in IIT's case, carries further ontological baggage that has been criticised independently (the "principle of true existence," on which only phenomenal existence is true existence, generates the intrinsicality problem 2.0: truly existing entities end up depending operationally on entities IIT has eliminated).
- *Falsifier template:* construct a functional twin with a different object. If the theory says the twins differ phenomenally, it must explain why no experiment can detect the difference.

**Shape 2 — Nomological law.** Structure and experience are lawfully correlated by basic psychophysical laws. This is Chalmers' positive proposal: phenomenal properties are fundamental, and "new psychophysical laws" connect physical structure to experience; the double-aspect theory of information holds that physically embodied information spaces and phenomenal information spaces are isomorphic, so that "the same abstract information space [is] embedded in physical processing and in conscious experience."
- *Cost:* the scope question is unresolved *by Chalmers' own admission* — "to just *which* physically realized information spaces does the basic principle apply?" Without a principled scope constraint the position collapses into panpsychism; with one that appeals only to physical structure it collapses back into physicalism. This is precisely the overgeneration failure mode the project has already flagged for trivial feedback systems.
- *Falsifier template:* find two systems in the same information space with different phenomenal structure, or two systems outside the declared scope that clearly have phenomenal structure.

**Shape 3 — Structural coherence.** Phenomenal structure *mirrors* the structure of access/awareness, without identity. Chalmers' principle of structural coherence: "the structure of phenomenal experience mirrors the structure of functional organization … if two representations are functionally similar, the corresponding experiences are phenomenally similar; if they are orthogonal, the experiences are orthogonal." Its methodological descendant is Fink et al.'s structural similarity constraint on NCCs.
- *Cost:* explicitly limited. Chalmers: "It allows us to recover structural properties of experience from information-processing properties, but not all properties of experience are structural properties." So Shape 3 can never deliver G1 or G4, and it cannot tell you *whether* a system is conscious — only, conditional on its being conscious, what structure its experience has.
- *Falsifier template:* a case where the structure of awareness and the structure of experience come apart — e.g. a subject whose discrimination-based quality space and whose substrate structure disagree.

**The actionable point.** These three shapes have different consequences for ICSI-G's own research agenda:

- Under Shape 1 or 2, ICSI-G competes with IIT on existence and can in principle generate a G1 discriminator — but must then answer the unfolding argument and the scope problem.
- Under Shape 3, ICSI-G is *not* a competitor to IIT on existence at all. It is a competitor on structure only, and the unfolding argument loses its sting (because the theory is not claiming the unfolded twin lacks experience, only that the twin's access structure differs). But then the "tie-free, complex-level discriminator" the agenda asks for must be a *structural* discriminator — a case where the two theories assign different phenomenal structures to a system both agree is conscious.

The project has been searching for a discriminator without first fixing which shape it is allowed to use. That is why the search keeps landing on mathematical differences. (Logged as H2.)

### 4.3 The determinism collision with IIT_4_0_2026

This is the most concrete applied finding, and it constrains the whole benchmark programme.

**The 2026 formalism.** Mayner, Marshall & Tononi add *intrinsic differentiation* to IIT's account of intrinsic cause–effect power. Their diagnosis of the 2023 version is explicit: "Earlier formulations quantified intrinsic information only by how much the current state specified a cause–effect state, ignoring whether the system provided itself with a repertoire of alternative states. Perfectly deterministic systems could therefore achieve high intrinsic information despite having no intrinsically defined alternatives."

The revised definitions (arXiv:2510.03881v1; published as Mayner, Marshall & Tononi 2026, *Entropy* 28(4):410):

- `ii_{c/e}(s) = min{i_diff^{c/e}(s), i_spec^{c/e}(s)}` — intrinsic information is the *minimum* of intrinsic differentiation and intrinsic specification, by the principle of minimal existence.
- `ii(s) = min{ii_c(s), ii_e(s)}` (Eq. 13).
- `φ_s(s) = min{φ_c(s), φ_e(s), ii(s)}` (Eq. 23).

`i_diff` is the intrinsic difference between the system's conditional distribution and a *maximally specific* distribution. For a fully deterministic system the conditional distribution **is** the maximally specific distribution, so the difference is zero. The paper states this directly in the Figure 1 caption: "The fully deterministic system has `i_diff(s) = 0`, and thus `ii(s) = 0`." (Symmetrically, "the uniformly random system has `i_spec(s) = 0` and so also has `ii(s) = 0`.")

**MATHEMATICAL RESULT (derivation).** For any fully deterministic system, at every state `s`: `i_diff = 0` ⇒ `ii_{c/e} = 0` ⇒ `ii = 0` ⇒ `φ_s(s) = min{φ_c(s), φ_e(s), 0} = 0`. A system with `φ_s = 0` is not a complex, so it is not a substrate of consciousness under IIT_4_0_2026, irrespective of its causal structure. Only systems that balance determinism and indeterminism have non-trivial intrinsic information; the paper's monad example maximises `φ_s` at an intermediate determinism (`p = 0.744`, `φ_s = 0.427`), not at `p = 1`.

**COMPUTATIONAL RESULT (verified in-repo).** Both Benchmark 01 systems are fully deterministic. `is_deterministic` returns `True` for each, `successor_support_sizes` returns `(1, 1, 1, 1)` for each, and `provides_alternative_states` returns `False` for each. See `src/icsig/diagnostics.py`, `tests/test_diagnostics.py`, and `python examples/diagnostics_report.py`.

**Consequences.**

1. **Benchmark 01 cannot support a structural discriminator against IIT_4_0_2026.** Under that formalism neither system is conscious, so there is no phenomenal structure on the IIT side to compare against. Any "divergence" reported on these fixtures is a divergence about *existence* (G1), driven by IIT's determinism commitment — not by anything distinctive in ICSI-G's topology. Reporting it as a structural result would violate research rule 4.
2. **A design constraint follows: structural discriminators need stochastic substrates.** This is a concrete, previously unrecorded requirement on benchmark construction, and it explains why the two-unit *deterministic* enumeration cannot settle agenda item 4 regardless of how many systems are enumerated.
3. **A real, if narrow, commitment-level divergence is available.** ICSI-G's phrase is "intrinsic *causal structure*," with no indeterminism requirement anywhere in Candidates A–D. IIT_4_0_2026 makes indeterminism a *necessary condition* for existence. So ICSI-G, as written, is committed to allowing phenomenal structure in fully deterministic systems where IIT_4_0_2026 allows none. That is a genuine theory-level disagreement about G1 — and it is the cleanest one currently on the table, because it turns on a single published equation rather than on a contested topological construction. It should be stated as a hypothesis with an explicit falsifier, not used as a benchmark result. (Logged as H3.)

**Verification caveats, per research rule 8 and `docs/REFERENCES.md`.**
- The equation numbers above are from arXiv:2510.03881v1 (4 Oct 2025). `docs/REFERENCES.md` cites the published *Entropy* 28(4):410 version and instructs that equation numbering be verified against it before implementation. That check is still outstanding.
- "Deterministic" here means *fully* deterministic at the level and grain of the supplied TPM. The 2026 paper's Discussion notes macro-level sources of intrinsic differentiation — micro-level stochasticity, micro-to-macro grain mappings, and background fluctuations — so a system that looks deterministic at a coarse grain need not have `i_diff = 0` at the grain IIT selects. Any application of H3 must therefore pin the grain and the coarse-graining policy (this connects to Marshall et al. 2026 on intrinsic units).
- It does not follow that IIT_4_0_2023 also excludes deterministic systems. The 2023 formalism quantifies intrinsic information by specification only, so the 2023 and 2026 formalisms diverge precisely here. Every claim in this section is about **IIT_4_0_2026 only**.

### 4.4 The subject-selection gap

ICSI-G commitment 2 ("nested coexistence": causal structures at different scales might correspond to nested or overlapping phenomenal identities) has no exclusion analogue, and that is a defect, not a feature.

The problem of the many is unavoidable: for almost any candidate substrate, there are structure-preserving supersets, subsets, and parasets. IIT handles this with the exclusion postulate — the substrate of consciousness is the one maximising `φ_s`, and "overlapping substrates with lower `φ_s` are excluded from existence," with ties resolved in favour of the next-highest value relative to the tied systems. Mørch argues independently that consciousness cannot overlap, distinguishing a substantive from a deflationary view of subjects and proposing a replacement formulation of exclusion ("experience has a border around it that cannot also be found around any of its proper parts"), which she claims vindicates IIT's exclusion postulate by a better route. Her argument also has a consequence for ICSI-G in the other direction: on any non-overlap view, ICSI-G's nested-coexistence commitment is *false* unless it adopts a deflationary account of subjects on which nested candidates are not distinct subjects at all.

The repo's own fixtures make the overgeneration mechanism concrete. **COMPUTATIONAL RESULT:** adding a causally isolated third unit to the swap dynamics leaves the unweighted influence graph exactly `{A→B, B→A}` while taking the state space from 4 to 8 states, the number of recurrent cycles from 3 to 3-at-a-larger-scale plus 4 new transient states, and the number of strongly connected state components from 3 to 7. So a rule keyed to graph topology alone cannot see the difference, while a rule keyed to state-space recurrence sees seven candidate supports where it previously saw three. Any subject rule must say which of these it counts, and why. (Logged as H5.)

One subtlety worth recording: the feedforward chain fixture has an **acyclic unit-level influence graph** but still possesses a recurrent *state* — a fixed point at 000 that every other state flows into. Unit-level feedforwardness and state-level recurrence are different properties. A subject rule formulated as "strongly connected support" (as in the Gemini proposal recorded in `docs/AGENT_REPORT_SYNTHESIS_2026-10-18.md`) must declare whether it means strongly connected *units* in the influence graph or strongly connected *states* in the transition digraph. On the fixture, the two readings give different answers. This is a specification ambiguity that should be closed before any invariant is computed.

### 4.5 The unfolding argument applies to ICSI-G

This does not appear anywhere in the current project memory, and it should.

ICSI-G is a causal-structure theory in exactly Doerig et al.'s sense: on it, phenomenal structure depends on how a system is internally wired to cause its own next states rather than on the input–output function it computes. All four candidates take an internal structural object as the identity criterion. Therefore:

- For any ICSI-G candidate whose object is a *static* structure over a fixed kernel, an unfolded feedforward twin exists with the same i/o function and a different object. Candidate B is the easiest case: the unrolled chain has an acyclic influence graph where the recurrent original has cycles. Candidate A is the hardest case (a full kernel does change under unfolding) but the object still differs while the function is preserved.
- So ICSI-G faces the same dilemma: either the unfolded twin has the same phenomenal structure (in which case the object is not the right identity criterion, and the theory collapses toward functionalism) or it has different phenomenal structure (in which case the difference is empirically undetectable by i/o means, and the theory must say what *would* detect it).

Two routes out, both of which should be tried:

1. **Restrict the domain to plastic/history-dependent systems.** O'Reilly-Shah, Selvitella & Schurger (2026) prove that rapid plasticity breaks functional equivalence with any static feedforward network: the unfolded twin matches only at the instant of unfolding and diverges thereafter. If ICSI-G's object is defined over *plasticity-modulated trajectories* rather than a static kernel, the construction that drives the argument has no fixed target. The cost is significant — the object is no longer a static graph or sheaf over a fixed base, which threatens Candidates B and D as currently framed and favours something closer to Candidate C or D with an explicitly temporal base. (Logged as H4.)
2. **Adopt Shape 3 (structural coherence) instead of Shape 1 (identity).** A coherence bridge claims only that phenomenal structure mirrors access structure. The unfolded twin then has a *different access structure* — which is exactly what makes it detectable in principle by internal measurement — so the dilemma does not bite in the same way. The cost is that ICSI-G gives up any claim to settle G1, which per §4.1 it was never in a position to make anyway.

Either route is a substantive repair. Neither is available to a candidate that keeps a static object *and* an identity bridge *and* an existence claim. That triple is the configuration the project should stop trying to defend.

### 4.6 What the repository's own fixtures now show

New neutral descriptors and fixtures were added to support the claims above. They describe kernels and graphs; they compute no consciousness measure.

| Fixture | Units | Deterministic | Provides alternative states | Unit-level influence graph | Acyclic | Recurrent state cycles | SCCs |
|---|---|---|---|---|---|---|---|
| B01 swap | 2 | yes | no | A↔B | no | `(0,), (1,2), (3,)` | 3 |
| B01 invert-plus-copy | 2 | yes | no | A↔B | no | `(0,2,3,1),` | 1 |
| B02 noisy swap p=0.1 | 2 | no | yes | A↔B | no | n/a | n/a |
| B02 noisy swap p=0.3 | 2 | no | yes | A↔B | no | n/a | n/a |
| B02 swap + isolated C | 3 | yes | no | A↔B | no | `(0,), (2,4), (6,)` | 7 |
| B02 feedforward chain | 3 | yes | no | C→B, B→A | **yes** | `(0,),` | 8 |

Reproduce with `python examples/diagnostics_report.py` and `.venv/bin/python -m pytest -q` (28 tests pass: 12 pre-existing, 16 new).

Three things in this table are worth stating plainly:

- The stochastic pair reproduces Benchmark 01's lesson in the regime where a 2026-formalism comparison is possible at all: **same influence graph, different kernels, and now with `i_diff > 0` available**. `noisy_swap(0.0)` is exactly Benchmark 01's swap system, so the family interpolates continuously between the dead deterministic comparator and a live stochastic one. That is the intended bridge from Benchmark 01 to Benchmark 02.
- The isolated-unit fixture changes almost nothing at the graph level and a great deal at the state level. This is the overgeneration pressure point.
- The feedforward chain is the project's first *acyclic-influence* fixture and therefore its first "unconscious twin" candidate under any IIT-style criterion — while still having a recurrent state. Use it to force the unit-level/state-level ambiguity in §4.4 into the open.

---

## 5. Failure conditions and uncertainties

- **§4.3 depends on reading IIT_4_0_2026's `i_diff` as zero for all fully deterministic systems.** I verified this against the arXiv preprint's equations and Figure 1 caption, and against the repo's own note in `docs/REFERENCES.md`. The published *Entropy* equation numbering has not been checked, and the grain caveat is real. If `i_diff > 0` for some deterministic system under the published definition, H3 weakens to an open question and constraint C6 must be dropped.
- **§2.3 treats IIT's axiom list as an inventory, not as an endorsement.** Bayne's objection that they are not genuine axioms is unresolved; if it succeeds, the inventory needs an independent source, and the honest fallback is the union of IIT's list with Bayne & Chalmers' unity taxonomy and the quality-space tradition.
- **§3.4b's degeneracy claim is an empirical generalisation about biology**, not a theorem. It is strong enough to put the burden on a necessity claim, not strong enough to refute one.
- **§4.5 assumes ICSI-G is a causal-structure theory.** If a future candidate is specified functionally rather than structurally, the unfolding argument changes character entirely — and so does the theory's relation to computational functionalism and to the Butlin et al. indicator programme.
- **No claim in this document is empirical evidence about any actual system's consciousness.** H6 proposes an empirical test; it does not report one.
- **Colour-vision topology is contested in the detail.** Sources describe dichromat hue as either "zero-dimensional" (two hues plus a neutral point) or a one-dimensional line between two endpoints. Both agree it is contractible with no 1-cycle, and that trichromat hue is circular, but H6 must pin this psychophysically before use, because the whole test turns on the contrast.

---

## 6. Verdict

On the research question as posed: **established at the level of conceptual analysis, not settled at the level of metaphysics.** The inventory of what phenomenal consciousness is (§2) and the decomposition of "genuinely experiences" (§3) are supported by converging primary and secondary sources and are stable enough to design against. The underlying metaphysical question remains open, with no consensus among philosophers and no confirmed neuroscientific theory — the COGITATE adversarial collaboration substantially challenged key predictions of both IIT and GNWT without vindicating either.

On the application: **ICSI-G's blocking gap is not the hard problem; it is an undeclared bridge shape and an undeclared explanandum.** Both are fixable by specification work rather than by new mathematics, and both are prerequisites for the tie-free discriminator the agenda has been seeking. The determinism collision (§4.3) is a hard constraint on benchmark design that the project should adopt immediately, and the unfolding argument (§4.5) is an unrecorded threat that admits of two concrete repairs.

Recommended changes to shared memory are listed in §7 of `docs/HYPOTHESIS_LEDGER_2026-11-15.md` as *proposed amendments*; they have deliberately not been written into `docs/RESEARCH_STATE.md`, which the project lead owns.

---

## 7. Sources

Accessed 2026-11-15. Primary sources first.

**Primary — phenomenal character and the explanandum**
1. Nagel, T. (1974). "What Is It Like to Be a Bat?" *Philosophical Review* 83(4). Discussed in: Stanford Encyclopedia of Philosophy, "Consciousness" — https://plato.stanford.edu/entries/consciousness/
2. Chalmers, D. J. (1995/1996). "Facing Up to the Problem of Consciousness." Includes the principle of structural coherence, organizational invariance, and the double-aspect theory of information — https://consc.net/papers/facing.pdf
3. Block, N. (1995). "On a Confusion about a Function of Consciousness." *Behavioral and Brain Sciences*. Discussed in: "Phenomenal consciousness and cognitive access," *PMC* — https://pmc.ncbi.nlm.nih.gov/articles/PMC6074085/ ; and "Experiencing without knowing? Empirical evidence for phenomenal consciousness without access," *Cognition* — https://www.sciencedirect.com/science/article/pii/S0010027723001634
4. Bayne, T. & Chalmers, D. J. (2003). "What Is the Unity of Consciousness?" — https://consc.net/papers/unity.pdf
5. Zahavi, D. & Kriegel, U. (2016). "For-Me-Ness: What It Is and What It Is Not." Guillot's tripartite distinction and critical assessment: "For-me-ness: a critical assessment of the phenomenal mineness thesis," *Cognitive Processing* (2026) — https://link.springer.com/article/10.1007/s10339-026-01383-z
6. SEP, "Higher-Order Theories of Consciousness" (P-consciousness vs A-consciousness; first-order vs higher-order accounts) — https://plato.stanford.edu/entries/consciousness-higher/
7. SEP, "The Neuroscience of Consciousness" (access/phenomenal distinction; the hard problem as specified for generic and specific consciousness) — https://plato.stanford.edu/entries/consciousness-neuroscience/
8. "The Hard Problem," *Philosophy of Mind — Isha* (survey of type-A/type-B materialism, phenomenal concepts strategy, dual-aspect and panpsychist responses, Nagel's objective phenomenology) — https://isharonline.org/hard-problem/

**Primary — IIT formalisms**
9. Albantakis, L., Barbosa, L. S., Findlay, G. W., Grasso, M., Haun, A. M., et al. (2023). "Integrated information theory (IIT) 4.0." *PLOS Computational Biology* 19(10):e1011465. DOI 10.1371/journal.pcbi.1011465 — https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1011465
10. Mayner, W. G. P., Marshall, W. & Tononi, G. "Intrinsic Cause–Effect Power: The Tradeoff Between Differentiation and Specification." Preprint arXiv:2510.03881v1 (4 Oct 2025) — https://arxiv.org/html/2510.03881v1 ; published as *Entropy* 28(4):410 (2026), DOI 10.3390/e28040410 — https://www.mdpi.com/1099-4300-28-4/410 . **Source for §4.3:** Eq. (13) `ii(s) = min{ii_c, ii_e}`; `ii_{c/e}(s) = min{i_diff, i_spec}`; Eq. (23) `φ_s(s) = min{φ_c(s), φ_e(s), ii(s)}`; Figure 1 caption on the fully deterministic and uniformly random cases; §3.1 monad maximum at `p = 0.744`, `φ_s = 0.427`. Equation numbering must be re-verified against the published *Entropy* version.
11. PyPhi documentation, "Theory" (authoritative sources named as Albantakis et al. 2023 and Mayner, Marshall & Tononi 2026; separate treatment of the intrinsic-information requirement) — https://pyphi.readthedocs.io/en/latest/theory/index.html
12. Tononi, G., Albantakis, L., et al. "Integrated Information Theory: A Consciousness-First Approach to What Exists." arXiv:2510.25998v2 — https://arxiv.org/pdf/2510.25998v2 . Source for the exclusion postulate, complex selection, and the callosal-decoupling remark.

**Primary — objections to causal-structure theories**
13. Doerig, A., Schurger, A., Hess, K. & Herzog, M. H. (2019). "The unfolding argument: Why IIT and other causal structure theories cannot explain consciousness." *Consciousness and Cognition* 72:49–59. DOI 10.1016/j.concog.2019.04.002
14. Doerig, A., Schurger, A. & Herzog, M. H. (2021). "Hard Criteria for Empirical Theories of Consciousness" (statement of the dilemma; note that Φ's criterion is "at least partly arbitrary, since the axioms do not uniquely specify the complexity measure") — https://www.researchgate.net/publication/342941586_Hard_Criteria_for_Empirical_Theories_of_Consciousness
15. O'Reilly-Shah, Selvitella & Schurger (2026). "A caveat regarding the unfolding argument: implications of plasticity." *Neuroscience of Consciousness* 2026(1):niag027 — https://academic.oup.com/nc/article/2026/1/niag027/8709184
16. Herzog, M. H. et al., reply to Usher, *Consciousness and Cognition* 98 (2022) 103261 (clarifies that the argument concerns cases where different causal structures implement the *same* function) — https://digitalcommons.chapman.edu/cgi/viewcontent.cgi?article=1296&context=psychology_articles
17. Michel, M. "On the dangers of conflating strong and weak versions of a theory of consciousness" (degeneracy; IIT's rejection of multiple realizability at the causal-structure level; NCC vs neural constituents) — https://d-nb.info/1248311396/34
18. Michel, M. (2026). "Consciousness doesn't do that" (signal-strength confound; matched-performance and dissociation paradigms) — https://philpapers.org/archive/MICCDD.pdf
19. Mørch, H. H. "Why Consciousness Can't Overlap" (substantive vs deflationary views of subjects; proposed replacement for the exclusion axiom; IIT tie-breaking) — https://philarchive.org/archive/MRCWCC
20. "Only consciousness truly exists? Two problems for IIT 4.0's ontology," *Frontiers in Psychology* (principle of true existence; intrinsicality problem 2.0) — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1485433/full

**Primary — phenomenal structure and quality spaces**
21. Rosenthal, D. (2010, 2015) on quality spaces; Clark, A. (1993, 2000) on sensory quality spaces. Surveyed in: "Exploring the role of structuralist methodology in the science of consciousness" — https://philarchive.org/archive/KOBETR (contains the Fink et al. 2021 structural similarity constraint: "Neural substrates of phenomenal types must share the structure governing the phenomenal types they are associated with")
22. "Three Comments in Case of a Structural Turn in Consciousness Science" (Rosenthal's and Clark's methodologies; the topology/JND construction problem: different topologies give different variations) — https://philarchive.org/archive/JOHTCI-5
23. "Three arguments against metaphysical structuralism in consciousness science" (relations vs relata; internal vs external structure) — https://d-nb.info/1374625108/34
24. *Synthese* (2026) 207:204, on similarity structuralism and similarity spaces — https://artefacts-discovery.researcher.life/full_text/DA-2/67/679f44fb20253b8da41af73cc5f2762d/full_text/0d176764fc466346878f40f8da24d094.pdf

**Primary — AI consciousness assessment and welfare**
25. Butlin, P., Long, R., Elmoznino, E., Bengio, Y., et al. (2023). "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness." arXiv:2308.08708 — https://arxiv.org/pdf/2308.08708
26. Butlin, P., Long, R., Bayne, T., Bengio, Y., Birch, J., Chalmers, D., et al. (2025/2026). "Identifying indicators of consciousness in AI systems." *Trends in Cognitive Sciences* 30(6). DOI 10.1016/j.tics.2025.10.011 — https://www.rivista.ai/wp-content/uploads/2025-11/indicators_of_consciousness1.pdf ; open-access copy: https://researchonline.lse.ac.uk/id/eprint/130322/1/1-s2.0-S1364661325002864-main.pdf . **Note:** the indicator list excludes IIT because IIT is incompatible with the working assumption of computational functionalism; indicators are graded separately for sensitivity and specificity.
27. Chalmers, D. J. (2023). "Could a Large Language Model be Conscious?" arXiv:2303.07103 (v3, 18 Aug 2024); *Boston Review*, 9 Aug 2023 — https://arxiv.org/abs/2303.07103
28. Long, R., Sebo, D., et al. (with Chalmers, Birch, Fish, Sebo, Sebo) (2024). "Taking AI Welfare Seriously." arXiv:2411.00986 — acknowledge / assess / prepare.
29. Steinmetz Yalon, N., Goldstein, A., Mudrik, L. & Geva, M. (2026). "Indications of Belief-Guided Agency and Meta-Cognitive Monitoring in Large Language Models." arXiv:2602.02467 (interpretability test of indicator HOT-3).

**Primary — empirical landscape**
30. Cogitate Consortium (2025). "Adversarial testing of global neuronal workspace and integrated information theories of consciousness." *Nature* 642(8066):133–142. DOI 10.1038/s41586-025-08888-1 — https://www.nature.com/articles/s41586-025-08888-1
31. Seth, A. K. (2016). "The Real Problem." *Aeon*; Seth, A. K. (2021). *Being You*. Faber & Faber. Gomez-Marin, A. & Seth, A. K. (2025). "A science of consciousness beyond pseudo-science and pseudoconsciousness." *Nature Neuroscience* 28:703–706. Interview: https://www.cienciacognitiva.org/files/2025-13-i.pdf
32. Chalmers, D. J. (2018). "The Meta-Problem of Consciousness." *Journal of Consciousness Studies* 25(9–10):6–61 — https://philpapers.org/archive/chatmo-32.pdf ; and "How Can We Solve the Meta-Problem of Consciousness?" — https://consc.net/papers/solving.pdf
33. Casarotto, S., Rosanova, M., Gosseries, O., Boly, M., Massimini, M. & Sarasso, S. (2016). "Exploring the Neurophysiological Correlates of Loss and Recovery of Consciousness: Perturbational Complexity." — https://link.springer.com/chapter/10.1007/978-3-319-21425-2_8 ; PCI overview and the 0.31 threshold: https://grokipedia.com/page/perturbational_complexity_index
34. "Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity," *Communications Biology* (2024) — propofol and xenon (unreported) vs ketamine (vivid dream-like reports) — https://www.nature.com/articles/s42003-024-06613-8
35. "Consciousness at sea," *Philosophical Transactions B* 380(1939):20240313 (2025) — the contested explanandum, the measurement problem, and trait individuation — https://royalsocietypublishing.org/rstb/article/380/1939/20240313/235135/
36. Wikipedia, "Integrated information theory" (2023 open letter describing IIT as pseudoscience; *Nature Neuroscience* commentary of 10 March 2025, "What Makes a Theory of Consciousness Unscientific?"; Bayne on the axioms; Doerig et al.; Searle; Pautz; Graziano) — https://en.wikipedia.org/wiki/Integrated_information_theory ; Bayne's reply: https://www.downtoearth.org.in/science-technology/nobody-knows-how-consciousness-works-but-top-researchers-are-fighting-over-which-theories-are-really-science-91984

**Colour vision (for H6)**
37. Meyer, G. W. & Greenberg, D. P. (1988). "Color-Defective Vision and Computer Graphics Displays." *IEEE Computer Graphics and Applications* — "the chromaticity diagram hue circuit for normal trichromats becomes a hue line for protanopes and deuteranopes with blue (approximately 575 nm) and yellow (approximately 470 nm) as the endpoints of the line and a neutral gray at the midpoint" — https://www-users.cse.umn.edu/~gmeyer/papers/meyer-greenberg-cga-1988.pdf
38. Lee, "Theory of Human Tetrachromatic Color Experience and Printing" — trichromatic hue parameterised by ω ∈ S¹; "zero dimensional hue space for dichromacy (yellow and blue hues only, in this case for protanopia)" vs "the familiar 1D hue circle" for trichromacy — https://imjal.github.io/theory-of-tetrachromacy/static/pdfs/Lee_TheoryofTet_v1.pdf
