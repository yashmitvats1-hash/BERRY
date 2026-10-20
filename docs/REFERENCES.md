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
   - The 2026 formulation adds the condition φ_s = min{φ_c, φ_e, ii(s)} (check the primary paper's precise definitions and equation before independent implementation). The PyPhi changelog says deterministic examples may have φ_s = 0 under IIT_4_0_2026; this must not be generalized without checking system, state, and formalism assumptions. Benchmark 03 confirms it holds for all 256 deterministic two-unit systems at all reachable states.
   - The current PyPhi implementation is an important replication tool, not a substitute for reading primary theory sources. Pin the commit hash, Python version, formalism preset, and all configuration parameters in every benchmark. A mutable main branch is not a permanent reproduction environment.

## Pinned computation environment (Benchmarks 02–03, 2026-10-20)

- **PyPhi** `2.0.0rc5.dev10+g134a8f31b`, installed from
  `github.com/wmayner/pyphi` at commit
  `134a8f31b49db512322465ed3ba5da7194d362fd` (`main`,
  2026-10-16). No PyPI release of PyPhi 2.0 existed at
  computation time (PyPI's latest was 1.2.0, which implements
  no IIT 4.0 formalism and does not import on Python 3.10+);
  no final `v2.0.0` git tag existed either. **Re-verification
  against a final tagged release is required when one is
  published.**
- **Python** CPython 3.13.16, built from source (python/cpython
  tag `v3.13.16`) with OpenSSL 3.5.9 and zlib built from
  source: the environment's system Python is 3.11.2 and PyPhi
  2.0 requires Python >= 3.13. libffi 3.4.4 was compiled
  manually from source (generated headers written from the
  libffi templates) because the sandbox has no system libffi
  development headers.
- **Python packages** (PyPhi environment): numpy 2.5.4,
  scipy 1.18.1, pandas 3.0.6, msgspec 0.22.0, joblib 1.6.0,
  more-itertools 11.2.1, psutil 7.2.2, PyYAML 6.0.3,
  tqdm 4.70.1, pytest 9.1.1.
- **Core package environment** (dependency-free): CPython
  3.11.2, pytest 9.1.1, numpy 2.4.6, scipy 1.17.1.
- PyPhi install command:
  `.venv313/bin/pip install "pyphi @ git+https://github.com/wmayner/pyphi.git@134a8f31b49db512322465ed3ba5da7194d362fd"`.

## Research claims to handle carefully

- The statement “IIT 4.0 excludes every overlapping system with a lower φ_s” is a theory-text description of its substrate-selection principle; predictions in a particular biological intervention require additional derivation and measurement assumptions.
- A nonzero Betti number or cohomology group does not by itself imply consciousness, intrinsic causal power, or a nontrivial subject.
- Identifying distinct mathematical objects is not evidence that their corresponding experiences differ. That conclusion needs a bridge principle and a way to test it.
- A computation that uses IIT 3.0 cannot establish a result about IIT 4.0. A computation under IIT 4.0 (2023) should not silently be reported as IIT 4.0 (2026).
