"""Version-pinned IIT comparisons through PyPhi 2.0.

This module converts the package's deterministic two-unit systems
into PyPhi substrates and computes IIT quantities under explicitly
named formalisms. It requires PyPhi >= 2.0, which distinguishes the
``IIT_4_0_2023`` and ``IIT_4_0_2026`` formalisms; PyPhi 1.x cannot
be used for IIT 4.0 comparisons at all.

Convention bridge: :mod:`icsig` orders states big-endian (unit ``A``
is the most significant bit); PyPhi indexes states little-endian
(unit 0 is the least significant bit). Conversions here are explicit
so the two conventions cannot be silently confused.

Nothing in this module computes a phenomenal quantity. It computes
the IIT formalism's mathematical objects (system integrated
information, complexes, distinctions, relations) for a named,
pinned formalism version.
"""

from __future__ import annotations

from typing import Any

from .enumeration import STATE_ORDER, TwoUnitDeterministicSystem

try:
    import numpy as np
    import pyphi
except ImportError as error:  # pragma: no cover - exercised only without pyphi
    raise ImportError(
        "PyPhi is required for IIT comparisons; install it separately "
        "(see docs/REFERENCES.md for the pinned version)"
    ) from error

#: Formalism names understood by PyPhi 2.0.
IIT_3_0 = "IIT_3_0"
IIT_4_0_2023 = "IIT_4_0_2023"
IIT_4_0_2026 = "IIT_4_0_2026"

FORMALISMS = (IIT_4_0_2023, IIT_4_0_2026)


def be_index(a: int, b: int) -> int:
    """Big-endian index of the state ``(a, b)`` (A most significant)."""
    return (a << 1) | b


def le_index(a: int, b: int) -> int:
    """Little-endian index of the state ``(a, b)`` (PyPhi's convention)."""
    return a | (b << 1)


def to_pyphi_substrate(
    system: TwoUnitDeterministicSystem,
) -> "pyphi.substrate.Substrate":
    """Convert a two-unit system to a PyPhi substrate.

    The joint state-by-state TPM is rebuilt directly from the
    successor map in PyPhi's little-endian row/column convention.
    """
    tpm = np.zeros((4, 4))
    for state_index, successor in enumerate(system.successors):
        a, b = STATE_ORDER[state_index]
        next_a, next_b = STATE_ORDER[successor]
        tpm[le_index(a, b), le_index(next_a, next_b)] = 1.0
    return pyphi.substrate.Substrate(
        tpm=tpm, node_labels=("A", "B")
    )


def _plain_units(value: Any) -> tuple[int, ...]:
    """Coerce a PyPhi unit-index sequence to a plain int tuple."""
    return tuple(int(unit) for unit in value)


def _unit_state_pairs(value: Any) -> tuple[tuple[int, int], ...]:
    """Coerce a PyPhi state specification to sorted (unit, value) pairs.

    Handles both plain index sequences and sequences of
    ``UnitState`` objects (which carry a unit index and a state
    value), so fingerprints are JSON-compatible and independent
    of PyPhi's display classes.
    """
    pairs = []
    for element in value:
        if isinstance(element, int):
            pairs.append((int(element), None))
        else:
            pairs.append((int(element.index), int(element.state)))
    return tuple(sorted(pairs, key=lambda pair: pair[0]))


def _distinction_fingerprint(distinction: Any) -> tuple:
    """Return a label-independent fingerprint of one distinction.

    The fingerprint uses unit indices only, so it is invariant to
    how units are named, and records the mechanism, both purviews,
    both specified states, both directional phis, and the
    distinction's integrated information.
    """
    return (
        _plain_units(distinction.mechanism),
        _plain_units(distinction.cause_purview),
        _plain_units(distinction.effect_purview),
        _plain_units(distinction.mechanism_state),
        _unit_state_pairs(distinction.cause.specified_state),
        _unit_state_pairs(distinction.effect.specified_state),
        round(float(distinction.cause.phi), 10),
        round(float(distinction.effect.phi), 10),
        round(float(distinction.phi), 10),
    )


def _relation_fingerprint(relation: Any) -> tuple:
    """Return a label-independent fingerprint of one relation."""
    return (
        tuple(sorted(_plain_units(mechanism) for mechanism in relation.mechanisms)),
        _unit_state_pairs(relation.purview),
        round(float(relation.phi), 10),
    )


def ces_fingerprint(ces: Any) -> dict[str, Any]:
    """Fingerprint a cause-effect structure up to unit naming.

    Returns a JSON-compatible dict with the structure integrated
    information, the distinction and relation counts, and sorted
    fingerprints of every distinction and relation.
    """
    distinctions = tuple(
        sorted(_distinction_fingerprint(d) for d in ces.distinctions)
    )
    relations = tuple(
        sorted(_relation_fingerprint(r) for r in ces.relations.materialize())
    )
    return {
        "big_phi": round(float(ces.big_phi), 10),
        "num_distinctions": len(distinctions),
        "num_relations": len(relations),
        "distinctions": distinctions,
        "relations": relations,
    }


def analyze_state(
    substrate: Any,
    state: tuple[int, int],
    formalism: str,
) -> dict[str, Any]:
    """Run one IIT analysis of the whole substrate in one state."""
    analysis = pyphi.analyze(
        substrate, state, formalism=formalism, compute="sia"
    )
    return {
        "phi_s": round(float(analysis.phi), 10),
        "mip": str(analysis.mip) if analysis.mip is not None else None,
    }


def analyze_ces(
    substrate: Any,
    state: tuple[int, int],
    formalism: str,
) -> dict[str, Any]:
    """Run one IIT analysis including the cause-effect structure."""
    analysis = pyphi.analyze(substrate, state, formalism=formalism)
    return {
        "phi_s": round(float(analysis.phi), 10),
        "ces": ces_fingerprint(analysis.ces),
    }


def complexes_at(
    substrate: Any,
    state: tuple[int, int],
    formalism: str,
) -> list[dict[str, Any]]:
    """Return the substrate's complexes in one state under one formalism."""
    return [
        {
            "units": tuple(complex_.node_indices),
            "phi_s": round(float(complex_.phi), 10),
        }
        for complex_ in substrate.complexes(state, formalism=formalism)
    ]


def system_fingerprint(
    system: TwoUnitDeterministicSystem,
    formalism: str,
) -> dict[str, Any]:
    """Analyze a system in all four states under one formalism.

    Returns the whole-network phi_s per state, the complexes per
    state, the per-state cause-effect structure fingerprints, and a
    combined fingerprint over all states (the state-conditioned
    profile of the system).
    """
    substrate = to_pyphi_substrate(system)
    per_state: dict[str, Any] = {}
    for state in STATE_ORDER:
        le_state = state  # unit values are convention-independent
        result = analyze_ces(substrate, le_state, formalism)
        result["complexes"] = complexes_at(substrate, le_state, formalism)
        per_state[f"{state[0]}{state[1]}"] = result
    return {
        "code": system.code,
        "formalism": formalism,
        "per_state": per_state,
    }
