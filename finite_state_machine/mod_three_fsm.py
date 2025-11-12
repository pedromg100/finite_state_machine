from enum import IntEnum

from .finite_state_machine import FiniteStateMachine


class States(IntEnum):
    S0 = 0
    S1 = 1
    S2 = 2


next_state_map = {
    (States.S0, "0"): States.S0,
    (States.S0, "1"): States.S1,
    (States.S1, "0"): States.S2,
    (States.S1, "1"): States.S0,
    (States.S2, "0"): States.S1,
    (States.S2, "1"): States.S2,
}


def mod_three_transition_function(current_state: States, input_value: str) -> States:
    return next_state_map[(current_state, input_value)]


mod_three_fsm = FiniteStateMachine(
    States,
    ["0", "1"],
    States.S0,
    {States.S0, States.S1, States.S2},
    mod_three_transition_function,
)


def mod_three(input: str) -> int:
    """Compute the binary number represented by input modulo 3.

    Args:
        input: A string of '0' and '1' characters representing a binary number.

    Returns:
        The remainder when the binary number is divided by 3 (0, 1, or 2).

    Raises:
        ValueError: If the input contains characters not in '0' or '1'
    """
    return mod_three_fsm.process_input(input)


if __name__ == "__main__":
    # Example runs — only execute when the module is run as a script.
    print("Mod Three 1101 (13): ", mod_three("1101"))  # pragma: no cover
    print("Mod Three 1110 (14): ", mod_three("1110"))  # pragma: no cover
    print("Mod Three 1111 (15): ", mod_three("1111"))  # pragma: no cover
