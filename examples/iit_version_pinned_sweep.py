"""Version-pinned IIT sweep over all 256 two-unit deterministic systems.

Runs every labeled two-unit deterministic binary system, in every
one-step-reachable state, under both IIT 4.0 formalisms implemented
by the pinned PyPhi build, and records:

* system integrated information phi_s of the whole network;
* the complexes selected at that state (whole-network vs
  selected-complex check);
* a label-independent fingerprint of the cause-effect structure
  (distinctions, relations, big Phi).

Usage::

    python examples/iit_version_pinned_sweep.py [output.json]

The output is the computational evidence for Benchmark 03. States
that are not one-step reachable (Garden-of-Eden states) are skipped:
PyPhi refuses to analyze them, because IIT requires the current
state to be reachable through the system's own dynamics.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pyphi  # noqa: E402

from icsig.enumeration import (  # noqa: E402
    STATE_ORDER,
    enumerate_two_unit_systems,
)
from icsig.iit_comparison import (  # noqa: E402
    IIT_4_0_2023,
    IIT_4_0_2026,
    analyze_ces,
    complexes_at,
    to_pyphi_substrate,
)

pyphi.config.progress_bars = False


def main() -> None:
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(
        "results/iit_two_unit_sweep.json"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    systems = enumerate_two_unit_systems()
    formalisms = (IIT_4_0_2023, IIT_4_0_2026)

    records: list[dict] = []
    for system in systems:
        substrate = to_pyphi_substrate(system)
        for formalism in formalisms:
            per_state: dict[str, dict] = {}
            for state in STATE_ORDER:
                state_key = f"{state[0]}{state[1]}"
                try:
                    result = analyze_ces(substrate, state, formalism)
                except pyphi.exceptions.StateUnreachableForwardsError:
                    per_state[state_key] = {"reachable": False}
                    continue
                result["reachable"] = True
                result["complexes"] = complexes_at(substrate, state, formalism)
                per_state[state_key] = result
            records.append(
                {
                    "code": system.code,
                    "formalism": formalism,
                    "successors": system.successors,
                    "image": sorted(system.image),
                    "cycle_signature": [
                        list(pair)
                        for pair in system.cycle_structure_signature()
                    ],
                    "per_state": per_state,
                }
            )

    summary = summarize(records, systems, formalisms)
    payload = {
        "summary": summary,
        "records": records,
    }
    output_path.write_text(json.dumps(payload, indent=1, sort_keys=True))
    print(f"wrote {output_path}")
    print(json.dumps(summary, indent=1, sort_keys=True))


def summarize(
    records: list[dict], systems: list, formalisms: tuple[str, ...]
) -> dict:
    """Aggregate the sweep into the headline counts."""
    by_formalism: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        by_formalism[record["formalism"]].append(record)

    summary: dict = {"total_labeled_systems": len(systems)}

    for formalism, rows in by_formalism.items():
        analyzed_pairs = 0
        unreachable_pairs = 0
        phi_positive_states = 0
        phi_positive_systems = set()
        complex_states = 0
        whole_network_complex = 0
        big_phi_values: list[float] = []
        for row in rows:
            for state_key, analysis in row["per_state"].items():
                if not analysis.get("reachable"):
                    unreachable_pairs += 1
                    continue
                analyzed_pairs += 1
                if analysis["phi_s"] > 0:
                    phi_positive_states += 1
                    phi_positive_systems.add(row["code"])
                if analysis["complexes"]:
                    complex_states += 1
                    for complex_ in analysis["complexes"]:
                        if complex_["units"] == (0, 1):
                            whole_network_complex += 1
                big_phi_values.append(analysis["ces"]["big_phi"])
        summary[formalism] = {
            "analyzable_state_pairs": analyzed_pairs,
            "garden_of_eden_state_pairs": unreachable_pairs,
            "states_with_phi_s_positive": phi_positive_states,
            "systems_with_any_phi_s_positive_state": len(phi_positive_systems),
            "states_with_nonempty_complex_set": complex_states,
            "states_where_whole_network_is_complex": whole_network_complex,
            "max_big_phi": max(big_phi_values) if big_phi_values else None,
        }

    # Kernel-distinct pairs sharing an identical state-conditioned
    # CES profile (does IIT's object merge different dynamics?).
    for formalism in formalisms:
        profiles: dict[str, list[int]] = defaultdict(list)
        for row in by_formalism[formalism]:
            profile = _state_conditioned_profile(row)
            profiles[json.dumps(profile, sort_keys=True)].append(row["code"])
        collisions = {
            key: codes
            for key, codes in profiles.items()
            if len(codes) > 1
        }
        summary[formalism]["distinct_ces_profiles"] = len(profiles)
        summary[formalism]["systems_sharing_a_ces_profile"] = sum(
            len(codes) for codes in collisions.values()
        )
        summary[formalism]["largest_ces_profile_class"] = max(
            (len(codes) for codes in collisions.values()), default=0
        )

    # Unweighted influence graph classes vs CES profile classes
    # (does the coarse graph merge systems IIT distinguishes?).
    from icsig.influence import unweighted_boolean_influence_edges

    graph_groups: dict[frozenset, list[int]] = defaultdict(list)
    for system in systems:
        graph_groups[
            unweighted_boolean_influence_edges(system.to_transition_system())
        ].append(system.code)
    ces_groups: dict[str, list[int]] = defaultdict(list)
    for row in by_formalism[IIT_4_0_2023]:
        ces_groups[
            json.dumps(_state_conditioned_profile(row), sort_keys=True)
        ].append(row["code"])

    graph_merges_ces_distinct = 0
    for codes in graph_groups.values():
        ces_classes = {
            json.dumps(_state_conditioned_profile(next(r for r in by_formalism[IIT_4_0_2023] if r["code"] == code)), sort_keys=True)
            for code in codes
        }
        if len(ces_classes) > 1:
            graph_merges_ces_distinct += 1
    summary["influence_graph"] = {
        "distinct_unweighted_graphs": len(graph_groups),
        "graphs_containing_ces_distinct_systems_2023": graph_merges_ces_distinct,
        "largest_graph_class": max(len(c) for c in graph_groups.values()),
    }
    return summary


def _state_conditioned_profile(row: dict) -> dict:
    """The per-state CES fingerprint profile of one system."""
    profile = {}
    for state_key, analysis in sorted(row["per_state"].items()):
        if not analysis.get("reachable"):
            profile[state_key] = None
            continue
        profile[state_key] = analysis["ces"]
    return profile


if __name__ == "__main__":
    main()
