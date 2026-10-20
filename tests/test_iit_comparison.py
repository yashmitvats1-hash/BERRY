"""Tests for the version-pinned PyPhi comparison layer.

These tests require PyPhi >= 2.0 (which provides the
IIT_4_0_2023 and IIT_4_0_2026 formalism presets). They are
skipped when PyPhi is not installed, so the dependency-free
core test suite still runs everywhere.
"""

import pytest

try:
    import pyphi

    from icsig.iit_comparison import (  # noqa: E402
        IIT_4_0_2023,
        IIT_4_0_2026,
        STATE_ORDER,
        be_index,
        ces_fingerprint,
        le_index,
        to_pyphi_substrate,
    )
    from icsig.enumeration import enumerate_two_unit_systems  # noqa: E402

    HAS_PYPHI = True
except ImportError:
    HAS_PYPHI = False

pytestmark = pytest.mark.skipif(
    not HAS_PYPHI, reason="PyPhi 2.0 is an optional dependency"
)


def test_index_conventions_are_inverses():
    for a in (0, 1):
        for b in (0, 1):
            assert be_index(a, b) == 2 * a + b
            assert le_index(a, b) == a + 2 * b


def test_substrate_tpm_round_trips():
    """The PyPhi TPM must reproduce the icsig successor map."""
    systems = enumerate_two_unit_systems()
    swap = next(s for s in systems if s.code == 172)
    substrate = to_pyphi_substrate(swap)
    joint = substrate.joint_tpm()
    # Axes: (current A, current B, node, next value), with the
    # state axes in PyPhi's little-endian unit order.
    assert joint.shape == (2, 2, 2, 2)

    for state_index, successor in enumerate(swap.successors):
        a, b = STATE_ORDER[state_index]
        next_a, next_b = STATE_ORDER[successor]
        assert joint[a, b, 0, next_a] == 1.0
        assert joint[a, b, 1, next_b] == 1.0
        assert joint[a, b, 0].sum() == 1.0
        assert joint[a, b, 1].sum() == 1.0


def test_swap_and_invert_copy_differ_under_iit_4_0_2023():
    systems = enumerate_two_unit_systems()
    swap = next(s for s in systems if s.code == 172)
    invert = next(s for s in systems if s.code == 92)

    swap_ces = ces_fingerprint(
        pyphi.analyze(
            to_pyphi_substrate(swap), (0, 0), formalism=IIT_4_0_2023
        ).ces
    )
    invert_ces = ces_fingerprint(
        pyphi.analyze(
            to_pyphi_substrate(invert), (0, 0), formalism=IIT_4_0_2023
        ).ces
    )
    assert swap_ces != invert_ces
    assert swap_ces["big_phi"] == 4.0
    assert invert_ces["big_phi"] == 2.0
    assert swap_ces["num_relations"] == 2
    assert invert_ces["num_relations"] == 0


def test_deterministic_systems_have_zero_phi_s_under_2026():
    systems = enumerate_two_unit_systems()
    swap = next(s for s in systems if s.code == 172)
    analysis = pyphi.analyze(
        to_pyphi_substrate(swap), (0, 0), formalism=IIT_4_0_2026
    )
    assert float(analysis.phi) == 0.0


def test_fingerprint_is_json_serializable_and_stable():
    import json

    systems = enumerate_two_unit_systems()
    swap = next(s for s in systems if s.code == 172)
    analysis = pyphi.analyze(
        to_pyphi_substrate(swap), (0, 0), formalism=IIT_4_0_2023
    )
    fingerprint = ces_fingerprint(analysis.ces)
    # JSON-serializable (tuples become lists; compare through JSON).
    serialized = json.dumps(fingerprint, sort_keys=True)
    assert json.loads(serialized) == json.loads(json.dumps(fingerprint))
    # Stable across repeated computation.
    again = ces_fingerprint(
        pyphi.analyze(
            to_pyphi_substrate(swap), (0, 0), formalism=IIT_4_0_2023
        ).ces
    )
    assert json.dumps(again, sort_keys=True) == serialized


def test_garden_of_eden_states_are_rejected_by_pyphi():
    """IIT requires the current state to be reachable."""
    systems = enumerate_two_unit_systems()
    # System 1: A_next = 0 always, B_next = 0 always; every state
    # maps to 00, so 01, 10, 11 are Garden-of-Eden states.
    constant_zero = next(
        s for s in systems if s.f_a == (0, 0, 0, 0) and s.f_b == (0, 0, 0, 0)
    )
    substrate = to_pyphi_substrate(constant_zero)
    with pytest.raises(pyphi.exceptions.StateUnreachableForwardsError):
        pyphi.analyze(substrate, (1, 1), formalism=IIT_4_0_2023)
