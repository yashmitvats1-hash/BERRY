# Agent report synthesis — 2026-10-18

Status: independent reports received from DeepSeek and Claude; Gemini's onboarding status and proposed sheaf construction received in the conversation attachment. This is an integration note, not a claim that the proposed implementation has been run or independently verified.

## Shared conclusions

1. ICSI-G remains under-specified; no bridge principle from physical structure to phenomenal structure has been established.
2. The coarse unweighted graph is insufficient to reconstruct a deterministic transition kernel.
3. A nonzero Betti number or nonzero sheaf cohomology is not, alone, a defensible subject-selection or consciousness criterion.
4. IIT comparisons must pin IIT_4_0_2023 versus IIT_4_0_2026 and the exact implementation revision.
5. The next step is an executable, fully specified sheaf on Benchmark 01 plus adversarial tests, not a phenomenal conclusion.

## Claude red-team additions

- A signed graph distinguishes the particular swap / invert-and-copy pair, so Benchmark 01 does not refute every graph candidate. Candidate B must be described as the *unweighted* graph only.
- Add an AND-versus-XOR higher-order interaction benchmark, but define the equivalence relation under bit-flips first. AND and OR are related by complementing all relevant bits.
- Test state dependence, unit relabeling, disconnected components, subject selection, and nested-subject counting.
- State-independent candidates cannot encode phenomenal content if the theory commits to content varying across states while the object stays fixed. This is a conditional theoretical argument, not an empirical proof about any particular system.
- Any proposed falsification condition needs an operationalized phenomenal measure and explicit bridge assumptions.

## Gemini proposal: promising formalization, not yet validated

Gemini proposes:
- a first-order signed cellular sheaf on the influence graph;
- a Walsh/Fourier coalition-complex extension for higher-order Boolean interactions;
- state-conditioned signed couplings and state tension;
- a cut-based partition-loss criterion, alongside a recurrent-support requirement.

These are specific enough to start a mathematical audit, but the attached code and numerical claims have not yet been run against the committed package. Do not merge them as validated results before checking all formulas, dimensions, sign conventions, and invariance claims.

### Immediate audit questions

1. **XOR wording:** XOR does not have vanishing Boolean influence edges: flipping either input changes the output. What can vanish are particular first-order *Walsh correlation coefficients* under the stated uniform measure. Distinguish Boolean sensitivity, correlation coefficients, and Fourier coefficients precisely.
2. **Sheaf/base-cell definition:** specify whether reciprocal directed edges are separate 1-cells, how edge orientations enter the coboundary, and whether parallel/oppositely directed cells are allowed. The claimed H^0/H^1 dimensions depend on this choice.
3. **Partition loss:** write an unambiguous indexed sum over coefficients crossing a bipartition, define which source and target coalitions are cut, and prove non-negativity, relabeling invariance, and the exact condition under which the loss is zero.
4. **State tension:** specify the orientation/sign convention in the coboundary and derive the reported values (S: 0,0,8,8; N: 4 at every state) directly from the formula. Do not treat these values as verified until independently reproduced.
5. **Cohomology and Laplacian:** provide matrices for S and N, calculate ranks/nullities and eigenvalues from those matrices, and state the inner products used to define the sheaf Laplacian.
6. **State dependence:** the first-order global correlation coefficient J is averaged over all states and is not itself state-conditioned. Keep it distinct from J(x).
7. **Invariance:** distinguish bit-label gauge transformations from permutations of units, and prove each separately for the full proposed construction.
8. **Subject rule:** strongly connected support plus positive cut loss is a candidate structural filter, not yet a necessary-and-sufficient criterion for phenomenal subjecthood or even a complete IIT comparator.

## Next experiment protocol

Before any IIT comparison:
- instantiate the sheaf on S and N with explicit cells, stalks, restrictions, matrices, and state convention;
- add the two-input XOR map and compute Boolean sensitivity separately from Walsh coefficients;
- add a disconnected union and a feedforward diamond;
- test all states and all bit relabelings, then unit permutation;
- compare exact computed outputs to every stated analytic value;
- label results as mathematical, theoretical, empirical, or open question.

Only after this passes should the same explicitly defined systems be evaluated under pinned IIT_4_0_2023 and IIT_4_0_2026 presets. A difference in either formal output is not by itself evidence of a phenomenal difference.
