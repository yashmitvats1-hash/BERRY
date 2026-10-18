"""Basic finite-system data model for reproducible theory comparisons.

A supplied matrix is only as causally meaningful as its construction. This
class validates a finite binary state-space transition kernel; it does not
establish that the kernel represents interventional/intrinsic causal power.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class FiniteBinaryTransitionSystem:
    """A Markov transition kernel over all states of a finite binary substrate.

    Args:
        units: Unique, non-empty unit labels. State ordering is assumed to be
            lexicographic over binary tuples (all 0/1 tuples in product order).
        kernel: Square matrix K where kernel[i][j] = P(state j at t+1 |
            state i at t). Each row must be a probability distribution.

    Important: this data type does not specify an intervention semantics,
    causal graph extraction, a current state, a subject boundary, or a
    phenomenal interpretation. Those belong to an explicit model specification.
    """

    units: tuple[str, ...]
    kernel: tuple[tuple[float, ...], ...]
    tolerance: float = 1e-9

    def __post_init__(self) -> None:
        units = tuple(self.units)
        kernel = tuple(tuple(float(value) for value in row) for row in self.kernel)
        object.__setattr__(self, "units", units)
        object.__setattr__(self, "kernel", kernel)

        if not units:
            raise ValueError("units must contain at least one binary unit")
        if any(not isinstance(unit, str) or not unit.strip() for unit in units):
            raise ValueError("each unit label must be a non-empty string")
        if len(set(units)) != len(units):
            raise ValueError("unit labels must be unique")
        if not math.isfinite(self.tolerance) or self.tolerance < 0:
            raise ValueError("tolerance must be finite and non-negative")

        expected_states = 2 ** len(units)
        if len(kernel) != expected_states:
            raise ValueError(
                f"kernel must have {expected_states} rows for {len(units)} units"
            )
        if any(len(row) != expected_states for row in kernel):
            raise ValueError(
                f"kernel must be square with {expected_states} columns"
            )

        for row_index, row in enumerate(kernel):
            if any(not math.isfinite(p) for p in row):
                raise ValueError(f"kernel row {row_index} contains a non-finite value")
            if any(p < -self.tolerance or p > 1 + self.tolerance for p in row):
                raise ValueError(
                    f"kernel row {row_index} contains a probability outside [0, 1]"
                )
            if not math.isclose(
                sum(row), 1.0, rel_tol=0.0, abs_tol=self.tolerance
            ):
                raise ValueError(
                    f"kernel row {row_index} sums to {sum(row)}, not 1"
                )

    @property
    def number_of_units(self) -> int:
        """Number of binary units in the model."""
        return len(self.units)

    @property
    def number_of_states(self) -> int:
        """Number of joint states (2**number_of_units)."""
        return len(self.kernel)

    def transition_distribution(self, state_index: int) -> tuple[float, ...]:
        """Return the next-state distribution for a valid row/state index."""
        if isinstance(state_index, bool) or not isinstance(state_index, int):
            raise TypeError("state_index must be an integer")
        if not 0 <= state_index < self.number_of_states:
            raise IndexError(
                f"state_index must be in [0, {self.number_of_states - 1}]"
            )
        return self.kernel[state_index]
