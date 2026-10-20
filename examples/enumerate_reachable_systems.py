"""Reproduce the enumeration behind the reported "700" figure.

Prints the exact counting conventions, so the figure can be
checked rather than recalled:

* 256 labeled deterministic two-unit binary systems exist;
* 700 of the 256 x 4 = 1024 (system, state) pairs have the
  state one-step reachable (in the image of the successor map);
* 324 pairs are Garden-of-Eden states;
* under the stricter "reachable from state 00" notion, only
  6 systems (the single 4-cycles) qualify.

Usage::

    python examples/enumerate_reachable_systems.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from icsig.enumeration import (  # noqa: E402
    enumerate_two_unit_systems,
    fully_reachable_systems,
    image_size_histogram,
    reachable_state_pairs,
)


def main() -> None:
    systems = enumerate_two_unit_systems()
    print("Deterministic two-unit binary systems")
    print("===================================")
    print(f"labeled systems (pairs of Boolean functions): {len(systems)}")
    print(f"(system, state) pairs in total: {len(systems) * 4}")
    print(
        "one-step reachable (system, state) pairs: "
        f"{reachable_state_pairs(systems)}"
    )
    print(
        "Garden-of-Eden (system, state) pairs: "
        f"{len(systems) * 4 - reachable_state_pairs(systems)}"
    )
    print("image-size histogram (size: systems):")
    for size, count in image_size_histogram(systems).items():
        print(f"  {size}: {count}")
    full = fully_reachable_systems(systems, initial_state=0)
    print(
        "systems with every state reachable from 00 "
        f"(single 4-cycles): {len(full)}"
    )
    print()
    print("Conclusion: the reported '700 reachable two-unit")
    print("deterministic systems' is exactly the count of")
    print("(system, state) pairs whose state is one-step")
    print("reachable -- 700 of 1024 -- not a count of systems.")
    print("The labeled system count is 256.")


if __name__ == "__main__":
    main()
