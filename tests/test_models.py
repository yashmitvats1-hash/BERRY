import pytest

from icsig import FiniteBinaryTransitionSystem


def test_accepts_valid_one_unit_deterministic_kernel():
    system = FiniteBinaryTransitionSystem(
        units=("A",),
        kernel=((1.0, 0.0), (0.0, 1.0)),
    )

    assert system.number_of_units == 1
    assert system.number_of_states == 2
    assert system.transition_distribution(1) == (0.0, 1.0)


def test_accepts_valid_two_unit_kernel():
    system = FiniteBinaryTransitionSystem(
        units=("A", "B"),
        kernel=(
            (1.0, 0.0, 0.0, 0.0),
            (0.0, 1.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
        ),
    )

    assert system.number_of_states == 4


def test_rejects_wrong_number_of_rows():
    with pytest.raises(ValueError, match="rows"):
        FiniteBinaryTransitionSystem(
            units=("A", "B"),
            kernel=((1.0, 0.0), (0.0, 1.0)),
        )


def test_rejects_non_square_kernel():
    with pytest.raises(ValueError, match="columns"):
        FiniteBinaryTransitionSystem(
            units=("A",),
            kernel=((0.5,), (0.5,)),
        )


def test_rejects_rows_that_do_not_sum_to_one():
    with pytest.raises(ValueError, match="sums to"):
        FiniteBinaryTransitionSystem(
            units=("A",),
            kernel=((0.2, 0.2), (0.0, 1.0)),
        )


def test_rejects_negative_probability():
    with pytest.raises(ValueError, match="outside"):
        FiniteBinaryTransitionSystem(
            units=("A",),
            kernel=((1.1, -0.1), (0.0, 1.0)),
        )


def test_rejects_duplicate_unit_names():
    with pytest.raises(ValueError, match="unique"):
        FiniteBinaryTransitionSystem(
            units=("A", "A"),
            kernel=(
                (1.0, 0.0, 0.0, 0.0),
                (0.0, 1.0, 0.0, 0.0),
                (0.0, 0.0, 1.0, 0.0),
                (0.0, 0.0, 0.0, 1.0),
            ),
        )


def test_rejects_invalid_state_index():
    system = FiniteBinaryTransitionSystem(
        units=("A",),
        kernel=((1.0, 0.0), (0.0, 1.0)),
    )

    with pytest.raises(IndexError):
        system.transition_distribution(2)
