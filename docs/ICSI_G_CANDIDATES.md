# Candidate Formulations to Keep Separate

This is a specification worksheet, not a claim that any formulation is correct. Each variant must be independently defined, tested, and compared with a fixed IIT version. Do not combine the strongest-sounding properties of different variants without an explicit rule.

## Shared physical-system notation

A first benchmark family may use a finite binary substrate with units U = {u1, ..., un}, state space S = {0,1}^n, and a one-step transition kernel K(s' | s). For an *intrinsic causal* interpretation, the kernel must be defined from an intervention protocol or an equivalent causal model; an observational transition table is not automatically sufficient.

A complete specification must state: (i) system boundary; (ii) admissible interventions and background distribution; (iii) temporal and spatial grain; (iv) stochastic/deterministic assumptions; (v) current-state dependence; (vi) subsystem and partition rules; (vii) invariance under relabeling; (viii) subject selection; and (ix) the mapping from the mathematical object to phenomenal claims.

## Candidate A — Full causal-repertoire / kernel ICSI

**Tentative object:** a complete intervention-defined transition/cause-effect repertoire, possibly including state-conditioned repertoires.

Questions that must be answered:
- Is K alone the object, or must it include intervention semantics, causal background distributions, and cause/effect repertoires?
- Which equivalence relation counts as the same object: exact labeled equality, relabeling isomorphism, or another relation?
- Does the object encode current state s, all possible states, or both?
- Which differences matter for phenomenal identity, rather than merely differing physically?
- Does it collapse to, contain, or diverge from the structured distinctions and relations in the selected IIT formalism?

**Failure mode:** raw kernel differences may be ubiquitous and lack principled phenomenal relevance.

## Candidate B — Coarse qualitative causal graph

**Tentative object:** an unweighted or finitely weighted directed graph derived from the system's causal dependencies.

Questions:
- Precisely how are edges inferred from interventions?
- What threshold removes weak/irrelevant links, if any?
- Are signs, weights, stochastic dependencies, and state dependence retained?
- Which graph invariant or isomorphism class defines identity?
- How does it distinguish systems with the same graph but different transition rules?

**Failure mode:** structural graph topology can discard dynamics and state information; static graph isomorphism alone is not an adequate specification of a causal theory.

## Candidate C — State-conditioned global topology

**Tentative object:** a topological/graph representation derived from an explicit state-conditioned causal structure K_s.

Questions:
- What exactly is K_s, and how is it estimated or computed from the full intervention model?
- What topology is placed on the state or causal space, and why?
- Which invariants are used, at what resolution, and with what stability guarantees?
- Can different states with different phenomenal qualities be distinguished while remaining invariant to arbitrary labels?
- How are disconnected, irrelevant, or weakly coupled elements treated?

**Failure mode:** may either erase current-state differences or let irrelevant topological changes alter the predicted subject.

## Candidate D — Dynamic state-space transition sheaf

**Tentative object:** a sheaf or related structure over an explicitly defined causal/state-space base, as suggested in earlier exploratory work.

Minimum definitions required before evaluating the proposal:
1. The base set X and topology or Alexandrov partial order on X.
2. The stalk/fiber E_x at every base point.
3. Restriction maps between comparable points, including domain/codomain and composition rules.
4. The transition dynamics and their relationship to local sections.
5. The exact global/local sections being interpreted.
6. The invariant being used (e.g. a specified cohomology group), how it is computed, and its dependence on modeling choices.
7. The proposed inclusion / exclusion / subject rule, with independent justification.
8. A bridge from sections or invariants to phenomenal structure.
9. At least one counterexample, one invariance test, and one minimal executable example.
10. A formal derivation of any IIT-discriminating prediction.

Earlier notes proposed a nonzero first Betti number or H^1 condition and graded interhemispheric-decoupling predictions. Both are **unverified hypotheses**. Do not repeat them as results unless the mathematical construction is complete and the comparison is correctly derived.

## Mandatory comparison table

For each candidate and one named IIT version, record:

| Dimension | Required answer |
|---|---|
| Physical input | What is the system and how are interventions defined? |
| Core object | Exact mathematical type, domain, codomain, and construction |
| State dependence | Is the present state an input to the object? |
| Identity criterion | When do two systems count as equivalent? |
| Subject boundary | Which subset is a candidate subject, and why? |
| Exclusion / coexistence | Can systems overlap or nest? Under what rule? |
| Level / amount | Is there a scalar, ordinal ranking, or no such prediction? |
| Phenomenal bridge | What justifies identifying this object with experience? |
| Discriminator | A case where predictions differ and ties are absent |
| Falsifier | A possible result that counts against the candidate |
| Reproduction | Sources, code version, input files, exact commands |

## Minimum standard for a claimed discriminator

A valid theoretical discriminator is not just K_A != K_B or different graph/sheaf objects. It must:
- satisfy each theory's own system and subject definitions;
- compare like with like (especially complex with complex if the claim concerns a conscious subject);
- avoid ties and underspecified boundary choices;
- derive different predictions about phenomenal structure from explicit bridge principles;
- survive relabeling and reasonable perturbation checks;
- be independently reproducible.

Until those conditions hold, classify the result as a mathematical distinction or exploratory example, not a consciousness-theoretic result.
