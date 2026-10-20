# Pending patches

Patches here are ready but **not applied** to the repository,
because the submitting agent's GitHub token lacks the
`workflows` permission required to modify
`.github/workflows/tests.yml`. A maintainer with the needed
permission should review and apply them.

## add_iit_tests_job.patch

Adds an `iit-tests` job to the CI workflow: it installs the
package plus PyPhi 2.0 pinned by commit
`134a8f31b49db512322465ed3ba5da7194d362fd` on Python 3.13,
runs the full test suite (the PyPhi-dependent tests skip
automatically without it), and reproduces the Benchmark 03
sweep plus the Benchmark 02 enumeration.

Apply with:

    git apply patches/add_iit_tests_job.patch

If PyPhi publishes a final `2.0.0` tag, switch the pin in
both this patch and `docs/REFERENCES.md` to the tag and
re-verify before applying.
