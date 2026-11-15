# References and Versioned Comparator Notes

Accessed / checked: 2026-10-18. This file records authoritative sources and what each supports, not endorsement of any consciousness theory.

## Primary IIT papers

1. **Albantakis, L. et al. (2023).** “Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms.” *PLOS Computational Biology*, 19(10), e1011465. Published 2023-10-17. DOI: [10.1371/journal.pcbi.1011465](https://doi.org/10.1371/journal.pcbi.1011465). Full text: [PLOS article](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1011465).
   - Primary source for the first published IIT 4.0 mathematical formalism, its five axioms/postulates, maximal-substrate/complex selection, and unfolding of a complex's cause-effect structure.
   - The article reports that code used for the paper's analyses was available at [PyPhi's feature/iit-4.0 branch](https://github.com/wmayner/pyphi/tree/feature/iit-4.0).
   - Do not assume the 2023 paper's numerical examples equal results under later IIT 4.0 updates.

2. **Marshall, W., Findlay, G., Albantakis, L., & Tononi, G. (2026).** “Intrinsic units: identifying a system's causal grain.” *Neuroscience of Consciousness*, 2026(1), niag013. Published 2026-04-15. DOI: [10.1093/nc/niag013](https://doi.org/10.1093/nc/niag013). Full text: [Oxford Academic](https://academic.oup.com/nc/article/2026/1/niag013/8654505).
   - Primary source for the 2026 treatment of intrinsic units / macro-grain within IIT's framework.
   - Its claims are to be audited as theory-specific proposals; they are not empirical proof that IIT is correct.

3. **Mayner, W. G. P., Marshall, W., & Tononi, G. (2026).** “Intrinsic Cause–Effect Power: The Tradeoff Between Differentiation and Specification.” *Entropy*, 28(4), 410. Published 2026-04-04. DOI: [10.3390/e28040410](https://doi.org/10.3390/e28040410). Full text: [MDPI article](https://www.mdpi.com/1099-4300/28/4/410).
   - Relevant to the 2026 changes to intrinsic cause-effect power and the system-level intrinsic-information requirement. Verify equation numbering against the published version before implementing it.

## Computational reference implementation

4. **PyPhi project** — [GitHub repository](https://github.com/wmayner/pyphi), [current README](https://github.com/wmayner/pyphi/blob/main/README.md), [changelog](https://github.com/wmayner/pyphi/blob/main/CHANGELOG.md), [formalism version guide](https://pyphi.readthedocs.io/en/latest/theory/formalism-versions.html), and [IIT 4.0 demo notebook](https://pyphi.readthedocs.io/en/latest/examples/IIT_4.0_demo.html).
   - Current documentation distinguishes IIT_3_0, IIT_4_0_2023, and IIT_4_0_2026. The 2023 and 2026 formalisms can produce different system-integrated-information values on the same system/state.
   - The 2026 formulation adds the condition φ_s = min{φ_c, φ_e, ii(s)} (check the primary paper's precise definitions and equation before independent implementation). The PyPhi changelog says deterministic examples may have φ_s = 0 under IIT_4_0_2026; this must not be generalized without checking system, state, and formalism assumptions.
   - The current PyPhi implementation is an important replication tool, not a substitute for reading primary theory sources. Pin the commit hash, Python version, formalism preset, and all configuration parameters in every benchmark. A mutable main branch is not a permanent reproduction environment.

## Research claims to handle carefully

- The statement “IIT 4.0 excludes every overlapping system with a lower φ_s” is a theory-text description of its substrate-selection principle; predictions in a particular biological intervention require additional derivation and measurement assumptions.
- A nonzero Betti number or cohomology group does not by itself imply consciousness, intrinsic causal power, or a nontrivial subject.
- Identifying distinct mathematical objects is not evidence that their corresponding experiences differ. That conclusion needs a bridge principle and a way to test it.
- A computation that uses IIT 3.0 cannot establish a result about IIT 4.0. A computation under IIT 4.0 (2023) should not silently be reported as IIT 4.0 (2026).

---

## Addendum — sources checked 2026-11-15

Added by the Claude workstream for `docs/PHENOMENAL_CONSCIOUSNESS_2026-11-15.md`, `docs/HYPOTHESIS_LEDGER_2026-11-15.md`, and `benchmarks/02_stochasticity_subject_rules_and_twins.md`. Full annotations, including which specific claim each source supports, are in §7 of the parent report. Nothing here endorses a theory.

### Bearing directly on the IIT comparator

5. **Mayner, W. G. P., Marshall, W., & Tononi, G.** "Intrinsic Cause–Effect Power: The Tradeoff Between Differentiation and Specification." Preprint arXiv:2510.03881v1 (2025-10-04); published as entry 3 above (*Entropy* 28(4):410, 2026).
   - **Verified in this session against the preprint:** Eq. (13) `ii(s) = min{ii_c(s), ii_e(s)}`; `ii_{c/e}(s) = min{i_diff^{c/e}(s), i_spec^{c/e}(s)}`; Eq. (23) `φ_s(s) = min{φ_c(s), φ_e(s), ii(s)}`; Figure 1 caption states that the fully deterministic system has `i_diff(s) = 0` and thus `ii(s) = 0`, and that the uniformly random system has `i_spec(s) = 0` and thus `ii(s) = 0`; §3.1 reports the monad's `φ_s` maximised at intermediate determinism (`p = 0.744`, `φ_s = 0.427`).
   - **Outstanding obligation (unchanged from entry 3):** equation numbering was checked against the arXiv preprint, *not* against the published *Entropy* version. Verify before implementing.
   - **Grain caveat:** the paper's Discussion lists micro-level stochasticity, micro-to-macro grain mappings, and background fluctuations as macro-level sources of intrinsic differentiation. Determinism at a coarse grain does not entail `i_diff = 0` at the grain IIT selects.

### Objections to causal-structure theories (apply to ICSI-G, not only to IIT)

6. **Doerig, A., Schurger, A., Hess, K., & Herzog, M. H. (2019).** "The unfolding argument: Why IIT and other causal structure theories cannot explain consciousness." *Consciousness and Cognition* 72, 49–59. DOI: [10.1016/j.concog.2019.04.002](https://doi.org/10.1016/j.concog.2019.04.002).
   - Source for the false-or-untouchable dilemma: any recurrent network can be unfolded into a functionally equivalent feedforward network, and feedforward systems have Φ = 0. Applies to ICSI-G because ICSI-G is a causal-structure theory; this had not previously been recorded in project memory.
7. **O'Reilly-Shah, Selvitella & Schurger (2026).** "A caveat regarding the unfolding argument: implications of plasticity." *Neuroscience of Consciousness* 2026(1), niag027. DOI: [10.1093/nc/niag027](https://doi.org/10.1093/nc/niag027).
   - Source for the bounded scope of the unfolding argument: rapid plasticity negates functional equivalence between a recurrent network and any static feedforward network for all times after the moment of unfolding. Basis for hypothesis H4.
8. **Doerig, A., Schurger, A. & Herzog, M. H. (2021).** "Hard Criteria for Empirical Theories of Consciousness."
   - Note recorded here because it bears on rule 5 and on candidate specificity: the authors state that IIT's criterion is "at least partly arbitrary, since the axioms do not uniquely specify the complexity measure."
9. **Michel, M.** "On the dangers of conflating strong and weak versions of a theory of consciousness."
   - Source for the degeneracy objection (Edelman & Gally 2001; Tononi et al. 1999) and for the point that IIT does not accept multiple realizability at the level of causal structure. Also for the NCC-versus-neural-constituents distinction.
10. **Michel, M. (2026).** "Consciousness doesn't do that."
    - Source for the signal-strength confound and for the recommendation of matched-performance and dissociation paradigms. Applied as prerequisite 2 of hypothesis H6.
11. **Mørch, H. H.** "Why Consciousness Can't Overlap."
    - Source for the substantive/deflationary distinction between views of subjects, for a proposed replacement formulation of the exclusion axiom, and for IIT's tie-breaking behaviour. Basis for hypothesis H5.

### Phenomenal structure and quality spaces

12. **Fink, B., et al. (2021)** and the structuralist methodology literature (Clark 1993, 2000; Rosenthal 2010, 2015).
    - Source for the **structural similarity constraint** on neural correlates: "Neural substrates of phenomenal types must share the structure governing the phenomenal types they are associated with." Basis for hypothesis H6.
    - Also records a known methodological defect that H6 must handle: different topologies on the stimulus space give different variation classes, so the construction must be pinned before use.
13. **Bayne, T. & Chalmers, D. J. (2003).** "What Is the Unity of Consciousness?"
    - Source for the subsumptive / objectual / spatial unity taxonomy and the Unity Thesis.
14. **Zahavi, D. & Kriegel, U. (2016).** "For-Me-Ness: What It Is and What It Is Not." Plus Guillot (2017) on the for-me-ness / me-ness / mineness tripartition.
    - Source for treating intrinsicality and first-personal givenness as a distinct explanandum slot from qualitative character. Basis for the intrinsicality gap identified in ICSI-G candidates A–D.

### Bridge-principle templates

15. **Chalmers, D. J. (1995/1996).** "Facing Up to the Problem of Consciousness."
    - Source for all three bridge shapes catalogued in hypothesis H2: the principle of **structural coherence** (phenomenal structure mirrors the structure of awareness; explicitly limited — "not all properties of experience are structural properties"), the **double-aspect theory of information** (the same abstract information space embedded in physical processing and in conscious experience), and psychophysical laws as basic principles.
    - Also records the unresolved scope question that H2 attributes to shape (ii): "to just *which* physically realized information spaces does the basic principle apply?"

### Empirical landscape and measurement

16. **Cogitate Consortium (2025).** "Adversarial testing of global neuronal workspace and integrated information theories of consciousness." *Nature* 642(8066), 133–142. DOI: [10.1038/s41586-025-08888-1](https://doi.org/10.1038/s41586-025-08888-1).
    - Preregistered adversarial collaboration. Results align with some predictions of both IIT and GNWT while substantially challenging key tenets of both: for IIT, absence of sustained posterior synchronisation; for GNWT, general lack of ignition at stimulus offset and limited prefrontal representation of certain conscious dimensions. Proponents dispute the operationalisation. Relevant to rule 8: this is the current empirical ceiling, and it does not confirm any structural theory.
17. **Casarotto, S., Rosanova, M., Gosseries, O., Boly, M., Massimini, M. & Sarasso, S. (2016).** "Exploring the Neurophysiological Correlates of Loss and Recovery of Consciousness: Perturbational Complexity."
    - Source for the perturbational complexity index as a behaviour-independent level measure (TMS–EEG response compressed with Lempel–Ziv complexity; commonly used threshold near 0.31). Used in hypothesis H7.
18. **"Consciousness at sea" (2025).** *Philosophical Transactions B* 380(1939):20240313.
    - Source for the contested explanandum, the measurement problem, and the trait-individuation problem. Supports the requirement in hypothesis H1 that a candidate declare which explanandum it targets.

### Assessment frameworks for artificial systems

19. **Butlin, P., Long, R., Bayne, T., Bengio, Y., Birch, J., Chalmers, D., et al. (2025/2026).** "Identifying indicators of consciousness in AI systems." *Trends in Cognitive Sciences* 30(6). DOI: [10.1016/j.tics.2025.10.011](https://doi.org/10.1016/j.tics.2025.10.011). Builds on arXiv:2308.08708 (2023).
    - **Recorded because of a specific exclusion:** the indicator list omits IIT, on the stated ground that IIT is incompatible with the working assumption of computational functionalism. ICSI-G, as a causal-structure theory, inherits that exclusion from the indicator programme. Indicators are graded separately for sensitivity and specificity, and are explicitly not claimed to be individually or jointly sufficient.
20. **Chalmers, D. J. (2023).** "Could a Large Language Model be Conscious?" arXiv:2303.07103; *Boston Review*, 2023-08-09.
    - Source for the standing obstacles (absence of recurrent processing, global workspace, unified agency) and for the point that language competence is not evidence of experience.
21. **Long, R., Sebo, D., et al. (2024).** "Taking AI Welfare Seriously." arXiv:2411.00986.
    - Source for the acknowledge / assess / prepare framing and for distinguishing practical from metaphysical attributions. Used in §3.2 of the parent report to separate the three senses of "genuine."

### Colour-vision topology (hypothesis H6 only)

22. **Meyer, G. W. & Greenberg, D. P. (1988).** "Color-Defective Vision and Computer Graphics Displays." *IEEE Computer Graphics and Applications*.
    - Source for: "the chromaticity diagram hue circuit for normal trichromats becomes a hue line for protanopes and deuteranopes with blue (approximately 575 nm) and yellow (approximately 470 nm) as the endpoints of the line and a neutral gray at the midpoint."
23. **Lee.** "Theory of Human Tetrachromatic Color Experience and Printing."
    - Source for the trichromatic hue circle parameterised by ω ∈ S¹, and for describing dichromatic hue space as zero-dimensional (two hues) against the trichromat's 1-D hue circle.
    - **Contested detail, recorded deliberately:** entries 22 and 23 describe dichromat hue differently (a line between two endpoints versus two hues with a neutral point). Both agree there is no 1-cycle and that trichromat hue is circular. H6 must pin the psychophysical construction before use, because the test turns entirely on this contrast.
