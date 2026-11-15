"""Small reproducible examples used by the BERRY benchmarks."""

from .models import FiniteBinaryTransitionSystem


def two_unit_same_graph_different_dynamics() -> tuple[
    FiniteBinaryTransitionSystem, FiniteBinaryTransitionSystem
]:
    """Return a swap system and an inversion-plus-copy system.

    State order is 00, 01, 10, 11 for units (A, B).

    System 1: A_next = B, B_next = A.
    System 2: A_next = NOT B, B_next = A.

    Both have the same unweighted reciprocal influence graph, but distinct
    transition kernels and different state-transition cycles.
    """
    swap = FiniteBinaryTransitionSystem(
        units=("A", "B"),
        kernel=(
            (1.0, 0.0, 0.0, 0.0),  # 00 -> 00
            (0.0, 0.0, 1.0, 0.0),  # 01 -> 10
            (0.0, 1.0, 0.0, 0.0),  # 10 -> 01
            (0.0, 0.0, 0.0, 1.0),  # 11 -> 11
        ),
    )
    invert_b = FiniteBinaryTransitionSystem(
        units=("A", "B"),
        kernel=(
            (0.0, 0.0, 1.0, 0.0),  # 00 -> 10
            (1.0, 0.0, 0.0, 0.0),  # 01 -> 00
            (0.0, 0.0, 0.0, 1.0),  # 10 -> 11
            (0.0, 1.0, 0.0, 0.0),  # 11 -> 01
        ),
    )
    return swap, invert_b


def noisy_swap(noise: float) -> FiniteBinaryTransitionSystem:
    """Return a stochastic two-unit system that copies with independent bit noise.

    Units are (A, B); state order is 00, 01, 10, 11. The intended dynamics are
    A_next = B and B_next = A, with each next-state bit independently flipped
    with probability ``noise``. The two bits are drawn independently, so the
    joint next-state distribution factorises.

    At ``noise == 0.0`` this reduces exactly to Benchmark 01's swap system, so
    the family interpolates between a deterministic kernel and a stochastic one.
    It is a modelling convenience for benchmark construction, not a claim about
    any real system.
    """
    if not 0.0 <= noise <= 1.0:
        raise ValueError("noise must lie in [0, 1]")

    keep, flip = 1.0 - noise, noise
    rows: list[tuple[float, ...]] = []
    for state_index in range(4):
        a_bit = (state_index >> 1) & 1
        b_bit = state_index & 1
        # P(A_next = 1) follows B; P(B_next = 1) follows A.
        p_a1 = keep if b_bit else flip
        p_b1 = keep if a_bit else flip
        row = tuple(
            (p_a1 if (successor >> 1) & 1 else 1.0 - p_a1)
            * (p_b1 if successor & 1 else 1.0 - p_b1)
            for successor in range(4)
        )
        rows.append(row)

    return FiniteBinaryTransitionSystem(units=("A", "B"), kernel=tuple(rows))


def stochastic_same_graph_different_kernel() -> tuple[
    FiniteBinaryTransitionSystem, FiniteBinaryTransitionSystem
]:
    """Return two stochastic systems with the same influence graph but different kernels.

    This is the stochastic counterpart of
    ``two_unit_same_graph_different_dynamics``. Both members have every next
    state reachable with positive probability, so unlike Benchmark 01 neither
    member is deterministic.
    """
    return noisy_swap(0.1), noisy_swap(0.3)


def disconnected_union_with_isolated_unit() -> FiniteBinaryTransitionSystem:
    """Return the swap dynamics on (A, B) plus a causally isolated unit C held at 0.

    Units are (A, B, C); state order is lexicographic 000 ... 111 with A as the
    most significant bit. C has no influence on A or B and is not influenced by
    them, so the unweighted influence graph is unchanged from the two-unit swap
    system while the state space doubles.

    This is the minimal "add an irrelevant component" case listed among the
    project's open questions; it is a test fixture for subject-selection rules.
    """
    successors = (0, 0, 4, 4, 2, 2, 6, 6)
    kernel = tuple(
        tuple(1.0 if column == successor else 0.0 for column in range(8))
        for successor in successors
    )
    return FiniteBinaryTransitionSystem(units=("A", "B", "C"), kernel=kernel)


def feedforward_chain() -> FiniteBinaryTransitionSystem:
    """Return a three-unit system whose influence graph is acyclic.

    Units are (A, B, C); state order is lexicographic 000 ... 111. The update
    rules are A_next = B, B_next = C, C_next = 0. The resulting influence edges
    are C -> B and B -> A only, so the graph is a directed path with no cycle.

    Included as the project's minimal "feedforward" fixture: a deterministic
    system with no recurrent influence at the unit level.
    """
    successors = (0, 2, 4, 6, 0, 2, 4, 6)
    kernel = tuple(
        tuple(1.0 if column == successor else 0.0 for column in range(8))
        for successor in successors
    )
    return FiniteBinaryTransitionSystem(units=("A", "B", "C"), kernel=kernel)
