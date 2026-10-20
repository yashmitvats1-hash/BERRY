# Benchmark 03 — Version-pinned IIT comparison of the two-unit baseline

Status: **COMPUTATIONAL RESULT** (reproducible; see pinned
versions below). Every IIT number in this benchmark was
computed by the pinned PyPhi build under an explicitly named
formalism. No consciousness claim is made or implied.

## Pinned comparator versions

| Component | Identity |
|---|---|
| PyPhi | `2.0.0rc5.dev10+g134a8f31b` |
| PyPhi source | `github.com/wmayner/pyphi` commit `134a8f31b49db512322465ed3ba5da7194d362fd` (`main`, 2026-10-16) |
| Formalisms | `IIT_4_0_2023`, `IIT_4_0_2026` (PyPhi presets) |
| Python | CPython 3.13.16 (built from source, tag `v3.13.16`, with OpenSSL 3.5.9 and zlib built from source) |
| numpy / scipy / pandas | 2.5.4 / 1.18.1 / 3.0.6 |
| msgspec / joblib / more-itertools / psutil / PyYAML / tqdm | 0.22.0 / 1.6.0 / 11.2.1 / 7.2.2 / 6.0.3 / 4.70.1 |

PyPhi 2.0 is not published on PyPI; it is installed from the
pinned commit. PyPhi 1.2.0 (the latest PyPI release) cannot
run on Python 3.11+ and implements no IIT 4.0 formalism, so it
is not a valid comparator for this benchmark.

**Formalism difference (per PyPhi's documentation and
changelog):** under `IIT_4_0_2023`, system integrated
information is `φ_s = min{φ_c, φ_e}`. Under `IIT_4_0_2026`
(Mayner et al. 2026, Eq. 23), `φ_s = min{φ_c, φ_e, ii(s)}`
with `ii(s) = min_d min(i_spec_d, i_diff_d)`, the intrinsic
information of the specified state. PyPhi documents that
deterministic systems compute `φ_s = 0` under the 2026
formalism; this benchmark confirms that across the entire
enumeration.

## Result 1 — Benchmark 01's pair, pinned

For the swap system `S` (`A' = B, B' = A`, code 172) and the
invert-and-copy system `N` (`A' = ¬B, B' = A`, code 92), both
wholly analyzed (whole network is the unique complex at every
state under 2023):

| Quantity | `S` (swap) | `N` (invert+copy) |
|---|---|---|
| unweighted influence graph | `{A→B, B→A}` | `{A→B, B→A}` (identical) |
| transition kernel | — | — (different; Benchmark 01) |
| `φ_s` at all 4 states, `IIT_4_0_2023` | 2.0 | 2.0 |
| `φ_s` at all 4 states, `IIT_4_0_2026` | 0.0 | 0.0 |
| complex set at all 4 states, 2023 | `{(A,B)}`, `φ_s = 2.0` | `{(A,B)}`, `φ_s = 2.0` |
| complex set at all 4 states, 2026 | `{}` (none) | `{}` (none) |
| cause-effect structure, 2023 | 2 distinctions, **2 relations**, `Φ = 4.0` | 2 distinctions, **0 relations**, `Φ = 2.0` |

**COMPUTATIONAL RESULT:** under `IIT_4_0_2023`, `S` and `N`
are tie-free at the complex level: both are complexes with
identical scalar `φ_s = 2.0`, but their unfolded cause-effect
structures differ — `S` has `Φ = 4.0` with 2 integrated
relations; `N` has `Φ = 2.0` with no relations, and its
distinctions specify negated cause states (e.g. at state `00`,
mechanism `A` specifies cause state `(1)` over purview `B`
and effect state `(0)`, while in `S` both are `(0)`). The
unweighted influence graph — the object of ICSI-G candidate B
— identifies the two systems; IIT's cause-effect structure
under the 2023 formalism distinguishes them.

**COMPUTATIONAL RESULT:** under `IIT_4_0_2026`, neither
system is a complex at any state (`φ_s = 0` everywhere,
because deterministic systems have `ii(s) = 0`), so no
complex-level comparison between `S` and `N` exists under the
default formalism. The discrimination above is therefore
**formalism-version-dependent**: it exists under the 2023
publication and vanishes under the 2026 update.

## Result 2 — full baseline sweep (256 systems × 4 states × 2 formalisms)

**COMPUTATIONAL RESULT:** across the 700 analyzable
(system, state) pairs (the 324 Garden-of-Eden pairs are
rejected by PyPhi itself, matching Benchmark 02's reachability
definition):

| Measure | `IIT_4_0_2023` | `IIT_4_0_2026` |
|---|---|---|
| states with `φ_s > 0` (whole network) | 134 | 0 |
| systems with at least one `φ_s > 0` state | 96 | 0 |
| states with non-empty complex set | 518 | 0 |
| states where the whole network is the complex | 134 | 0 |
| states where only singleton complexes exist | 384 | 0 |
| maximum `Φ` (CES big-phi) | 12.0 (system 75, state 10) | 12.0 |
| distinct state-conditioned CES profiles | 244 | 244 |

Whole-network `φ_s` values under 2023: 566 states at 0.0, 26
states at 1.0, 108 states at 2.0. The 12 systems with
`φ_s > 0` at **all four** states are codes 83, 86, 89, 92,
99, 108, 147, 156, 163, 166, 169, 172 — all bijective
(permutation) systems; `S` (172) and `N` (92) are among them.

## Result 3 — subject-selection check (whole network vs selected complex)

**COMPUTATIONAL RESULT:** in 384 of the 700 analyzable
states, the whole network has `φ_s = 0` and IIT's exclusion
postulate selects **singleton** complexes instead (488
singleton-complex appearances in total, with `φ_s` up to 2.0;
e.g. system 1, `f_A ≡ 0, f_B = NOR(A,B)`, state `00`: whole
network `φ_s = 0`, complex `{B}` with `φ_s ≈ 0.1578`).
Minimal example: `A' = A` (self-loop), `B' ≡ 0` — the whole
network is reducible, and no singleton qualifies either
(`A`'s conditioned self-map is the identity, which IIT 4.0
scores `φ_s = 0`).

**Consequence:** any comparison that analyzes the whole
network while IIT selects a singleton (or vice versa)
compares a non-complex against a complex. In this baseline
that error would occur in 384 of 700 states. The prior
report's caution about complex-vs-non-complex comparisons is
confirmed and quantified; all comparisons in this benchmark
record the selected complex set explicitly.

## Result 4 — the earlier "identical IIT structures" claim, corrected

**CORRECTED CLAIM.** The earlier report that "full transition
kernels can differ even when reported IIT structures are
identical" holds only in the degenerate sense: the only
kernel-distinct systems with identical state-conditioned CES
profiles are the 16 systems in four classes (codes {3, 6, 9,
12}, {80, 96, 144, 160}, {95, 111, 159, 175}, {243, 246,
249, 252}), and in every one of these classes **all**
reachable states have an **empty** cause-effect structure
(`φ_s = 0`, zero distinctions, zero relations, `Φ = 0`).
No two systems in the baseline share a non-empty CES profile:
IIT's unfolded structure distinguishes every pair of systems
that has any structure at all. A kernel difference with an
empty IIT structure is, by IIT's own standard, a difference
with no cause-effect content — not a case where IIT "fails to
distinguish" two structured systems.

## Result 5 — coarse-graph merging (candidate B test)

**COMPUTATIONAL RESULT:** all 16 unweighted influence-graph
classes contain systems with distinct `IIT_4_0_2023` CES
profiles. The largest class (the complete graph with
self-loops, 100 systems) contains 100 distinct profiles. The
Benchmark-01 class `{A→B, B→A}` contains 4 systems (codes 83,
92, 163, 172) with 4 distinct profiles. A formulation that
identifies systems by the unweighted influence graph therefore
merges systems that IIT 4.0 (2023) distinguishes at the
complex level, throughout the baseline.

## Result 6 — state dependence

**COMPUTATIONAL RESULT:** 236 of 256 systems have a
state-dependent non-empty CES (the fingerprint changes across
states); 0 systems have a constant non-empty CES; 20 systems
have an empty CES at every reachable state. IIT's object is
intrinsically state-conditioned in this baseline: any
state-independent topological invariant cannot reproduce it.

## Reproduction

```bash
# one-time: create the Python 3.13 environment with PyPhi 2.0
# (see docs/REFERENCES.md for the build provenance)
.venv313/bin/pip install -e .
.venv313/bin/pip install "pyphi @ git+https://github.com/wmayner/pyphi.git@134a8f31b49db512322465ed3ba5da7194d362fd"

PYPHI_WELCOME_OFF=1 .venv313/bin/python \
    examples/iit_version_pinned_sweep.py results/iit_two_unit_sweep.json
PYPHI_WELCOME_OFF=1 .venv313/bin/python -m pytest -q tests/test_iit_comparison.py
```

The sweep is deterministic and takes under a minute. Results:
`results/iit_two_unit_sweep.json` (per-state `φ_s`, complex
sets, and CES fingerprints for all 256 systems under both
formalisms; summary block reproduces every count above).

## Failure conditions and uncertainties

* All results are conditioned on the pinned PyPhi commit;
  PyPhi 2.0 was still a release-candidate-line build at the
  time of computation (`2.0.0rc5.dev10`), and the final 2.0.0
  tag was not yet present on GitHub. Re-running after a final
  tag exists is a required re-verification step.
* `IIT_4_0_2026` results are only as faithful as PyPhi's
  implementation of Mayner et al. (2026); the equations were
  not independently re-derived from the paper for this
  benchmark (the paper's Eq. numbering still needs checking
  against the published text, as flagged in REFERENCES.md).
* The CES fingerprint compares mechanisms, purviews,
  specified states, directional `φ` values, relations, and
  `Φ`; it does not compare full cause-effect repertoires
  (probability vectors), so two structures could in principle
  share a fingerprint yet differ in repertoire shape. No such
  pair was observed; the fingerprint's distinction-level
  fields are derived from the repertoires' maximizers.
* Two-unit deterministic systems are a small, fully
  deterministic slice; stochastic kernels, larger substrates,
  macro units, and grain searches are out of scope until this
  baseline is accepted (per the agent protocol).
