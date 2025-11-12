from enum import Enum

import pytest

from finite_state_machine.finite_state_machine import FiniteStateMachine


class StatesTest(Enum):
    A = 0
    B = 1


class OtherStates(Enum):
    A = 0


simple_fsm_default_parameters = {
    "states": StatesTest,
    "input_alphabet": ["0", "1"],
    "initial_state": StatesTest.A,
    "final_states": {StatesTest.B},
    "transition_function": lambda s, i: StatesTest.B,
}


def test_invalid_initial_state_raises():
    # initial_state not a member of the provided states enum
    with pytest.raises(ValueError, match="Initial state must be in states"):
        FiniteStateMachine(
            **(simple_fsm_default_parameters | {"initial_state": OtherStates.A})
        )


def test_invalid_final_state_raises():
    # final_states contain values not in the provided states enum
    with pytest.raises(ValueError, match="Final states must be in states"):
        FiniteStateMachine(
            **(simple_fsm_default_parameters | {"final_states": {OtherStates.A}})
        )


def test_process_input_successful():
    # simple FSM that always transitions to state B without errors
    fsm = FiniteStateMachine(**simple_fsm_default_parameters)

    assert fsm.process_input("1101") == 1


def test_process_input_invalid_input_raises():
    # input contains symbols not in the input alphabet
    fsm = FiniteStateMachine(**simple_fsm_default_parameters)
    with pytest.raises(ValueError, match="Input value not in input alphabet"):
        fsm.process_input("12")


def test_process_input_invalid_final_state_raises():
    # FSM that always transitions to state A, which is not a allowed final state
    fsm = FiniteStateMachine(
        **(
            simple_fsm_default_parameters
            | {"transition_function": lambda s, i: StatesTest.A}
        )
    )
    with pytest.raises(ValueError, match="Final state not allowed"):
        fsm.process_input("1")


def test_missing_transition_raises():
    # FSM with incomplete transition map raising error in the transition_function
    next_map = {(StatesTest.A, "0"): StatesTest.A}

    fsm = FiniteStateMachine(
        StatesTest,
        ["0", "1"],
        StatesTest.A,
        {StatesTest.A},
        lambda s, i: next_map[(s, i)],
    )

    with pytest.raises(ValueError, match="Transition error for"):
        fsm.process_input("1")
