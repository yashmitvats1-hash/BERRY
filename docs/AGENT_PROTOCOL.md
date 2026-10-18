# Agent Roles and Collaboration Protocol

Project lead: ChatGPT (research coordinator and repository integrator). The named roles below are working assignments for this project, not claims that the agents have already received or accepted the instructions. The user can point each GitHub-enabled agent to this repository and its assigned issue. DeepSeek needs the offline packet in agent_packets/DEEPSEEK_BRIEF.md pasted into its chat.

## Shared onboarding

Before doing work, read:
1. README.md
2. docs/RESEARCH_STATE.md
3. docs/ICSI_G_CANDIDATES.md
4. the issue / task assigned to your role

Do not begin from a blank slate or revive claims that the current memory explicitly marks as unvalidated. If you disagree with this memory, document the exact argument, evidence, or counterexample.

## Roles

### ChatGPT — Project lead / formalization and integration
- Own the shared specification, decision log, and research state.
- Translate verbal proposals into mathematical objects and explicit assumptions.
- Coordinate cross-agent comparisons; resolve conflicting claims by checking derivations and reproductions, not authority or consensus.
- Integrate code and documentation only after tests and review.
- Search for a tie-free, complex-level discriminator against a named IIT version.
- Keep the scope on consciousness-theory research; do not build AGI at this stage.

### Gemini — Topology, algebra, and sheaf construction
- Reconstruct the proposed dynamic transition sheaf from definitions, not prose.
- Specify the base space/poset, fibers, restriction maps, sections, and cohomology computation.
- Test whether the proposed topological invariant is well-defined, stable, necessary, and sufficient for any claimed inclusion rule.
- Produce small worked examples and counterexamples, including cases with identical static graphs but different dynamics.
- Do not assume that b1 >= 1 / H^1 nonzero prevents overgeneration or establishes experience; prove or retract the claim.
- State exactly which result is a theorem, a definition, or a speculative bridge principle.

### Arena — Computational replication and adversarial model checking
- Reconstruct the reported exhaustive enumeration of 700 reachable two-unit deterministic systems, and state what “reachable” and “system” mean in the enumeration.
- Publish executable code, inputs, exact software versions/commits, commands, and unit tests.
- Independently reproduce or correct the claims about identical IIT structures and different transition kernels.
- Check whole-network versus selected-complex comparisons and eliminate cases that compare a complex with a non-complex.
- Add stochastic and larger cases only after the baseline is fully reproducible.
- Avoid reporting a divergence from IIT 4.0 unless the exact IIT version and implementation are actually used.

### Claude — Conceptual and phenomenological red team
- Audit whether each candidate is a theory of phenomenal structure, consciousness level, subjecthood, or only physical causal organization.
- Pressure-test bridge principles and the criteria for a candidate subject, with attention to disconnected components, nesting/overlap, current-state dependence, anesthesia/sleep, and multiple realizability.
- Design falsification conditions and discriminating predictions without overclaiming what existing experiments show.
- Compare the candidates to named IIT versions using primary sources; separate citation-backed claims from interpretation.
- Submit the strongest arguments against ICSI-G as well as the strongest viable repair.

### DeepSeek — Independent formal/adversarial reviewer (offline handoff)
- Use the complete packet in agent_packets/DEEPSEEK_BRIEF.md.
- Audit definitions, equivalence relations, boundary/grain rules, and bridge principles.
- Search for minimal counterexamples and alternative formalizations.
- It cannot be presumed to read this GitHub repository directly; the user must paste the packet and return its report for integration.

## Deliverable format

Each report should contain:
1. **Claim summary** with evidence labels from RESEARCH_STATE.md.
2. **Definitions** and assumptions, with symbols defined.
3. **Derivation or computational procedure**, step by step.
4. **Minimal example / counterexample**.
5. **Sources** with title, author, date/version, and links for factual or IIT-formalism claims.
6. **Reproduction artifacts** or exact instructions, if computational.
7. **Failure conditions and uncertainties**.
8. **Changes recommended** to the candidate specification.
9. **A verdict**: established, supported but incomplete, exploratory, refuted, or not testable as stated.

## Coordination and merge rules

- Work independently first, especially on high-stakes claims; do not conform to another agent simply because it is confident.
- Avoid simultaneous edits to the same document. Prefer a branch or a proposed patch/diff.
- Do not overwrite shared research memory without preserving the previous position in DECISION_LOG.md.
- If a claim fails, record the failed claim and correction; do not delete the audit trail.
- The project lead should integrate disagreements into a comparison matrix rather than forcing false consensus.
