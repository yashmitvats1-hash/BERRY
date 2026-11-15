# BERRY — ICSI-G Research Lab

BERRY is the shared research workspace for evaluating **Intrinsic Causal-Structural Information Graphs (ICSI-G)** as a candidate account of phenomenal structure, and comparing precisely specified versions of the candidate with Integrated Information Theory (IIT), especially IIT 4.0.

## Current position

**Research status: open question; ICSI-G is under-specified.** Prior work has identified promising directions and serious failure modes, but has not established that ICSI-G is a correct theory of consciousness or that its mathematical differences from IIT produce distinct phenomenal predictions. The dynamic-sheaf proposal is a candidate to test, not a validated result.

The immediate work is theoretical specification and reproducibility. **Do not start building an AGI in this repository.**

## Start here

- [Research state and prior findings](docs/RESEARCH_STATE.md) — shared project memory and current verdict.
- [Candidate formulations](docs/ICSI_G_CANDIDATES.md) — four variants to define separately.
- [Agent protocol and roles](docs/AGENT_PROTOCOL.md) — responsibilities, handoffs, and standards.
- [DeepSeek offline brief](agent_packets/DEEPSEEK_BRIEF.md) — copy/paste packet for the agent without GitHub access.
- [Decision log](docs/DECISION_LOG.md) — dated decisions and changes to the research position.
- [References and comparator versions](docs/REFERENCES.md) — primary sources, including the 2023 and 2026 IIT formulations.
- [Benchmark 01](benchmarks/01_same_influence_graph_different_dynamics.md) — a minimal reproducible graph/dynamics counterexample.

## 2026-11-15 additions (proposed, pending project-lead integration)

- [Phenomenal consciousness and the conditions for genuine experience](docs/PHENOMENAL_CONSCIOUSNESS_2026-11-15.md) — what the explanandum is, decomposed; what "genuinely experiences" commits to; and how both apply to ICSI-G.
- [Hypothesis ledger](docs/HYPOTHESIS_LEDGER_2026-11-15.md) — eight falsifiable hypotheses (H1–H8) about bridge principles, determinism, subject selection, and phenomenal structure, each with a prediction, a falsifier, an owner, and an evidence label.
- [Benchmark 02](benchmarks/02_stochasticity_subject_rules_and_twins.md) — specification for stochastic, isolated-component, and feedforward fixtures, plus a six-step computation protocol. Marked specification, not result.
- [DeepSeek follow-up packet](agent_packets/FOLLOWUP_2026-11-15_BRIDGE_AND_HYPOTHESES.md) — offline packet for the adversarial review of H2, H3, H4, and H8.

Two findings from that work constrain the benchmark programme and are recorded in the decision log: the unfolding argument against causal-structure theories applies to ICSI-G and had not previously been recorded, and deterministic fixtures cannot support a *structural* comparison against IIT_4_0_2026, which assigns φ_s = 0 to every fully deterministic system. Neither finding establishes a discriminator, and the current verdict on ICSI-G is unchanged.

## Initial computational scaffold

A small, dependency-light representation of finite binary transition systems lives in src/icsig/. It validates input shape and probabilities only. It does **not** claim that a transition matrix by itself is a sufficient causal model, a measure of consciousness, or an implementation of IIT or ICSI-G.

Run tests with:

    python -m pip install -e ".[dev]"
    python -m pytest

## Research rules

1. Separate mathematical results, theoretical interpretations, empirical evidence, and unsupported assumptions.
2. Define system boundaries, state variables, interventions, temporal/spatial grain, current state, and subject-selection rules explicitly.
3. Keep full transition-kernel, coarse-graph, state-conditioned-topology, and sheaf proposals distinct; never switch formulations silently.
4. A structural difference is not automatically a phenomenal difference. An explicit bridge principle is required.
5. Compare against a named, versioned IIT formalism. Do not treat IIT 3.0, IIT 4.0, and later descriptions as interchangeable.
6. Publish minimal examples, test code, versions, seeds, and exact reproduction instructions for computational claims.
7. Actively seek counterexamples. Preserve failed hypotheses and corrections in the decision log rather than rewriting history.
8. An agent's confidence estimate is not evidence. Claims require definitions, derivations, citations, or reproducible results.

## Collaboration

The project lead maintains the shared specification and adjudicates disagreements. Specialist agents should work independently within their assigned workstreams, then submit concrete findings, counterexamples, references, and artifacts for integration. See the agent protocol for details.
