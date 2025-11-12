from enum import Enum
from collections.abc import Iterable, Container, Callable
from typing import Type, TypeVar, Generic

S = TypeVar("S", bound=Enum)
A = TypeVar("A")


class FiniteStateMachine(Generic[S, A]):
    """A generic finite state machine (FSM) implementation.
    Attributes:
        states: An enumeration of possible states with their output values.
        input_alphabet: A collection of valid input symbols.
        initial_state: The starting state of the FSM, one of the items of the states.
        final_states: A collection of acceptable final states from the states.
        transition_function: A function defining state transitions.
    """

    def __init__(
        self,
        states: Type[S],
        input_alphabet: Container[A],
        initial_state: S,
        final_states: Iterable[S],
        transition_function: Callable[[S, A], S],
    ) -> None:
        self.states = states
        self.input_alphabet = input_alphabet
        self.initial_state = initial_state
        if self.initial_state not in self.states:
            raise ValueError("Initial state must be in states")
        self.final_states = final_states
        for state in self.final_states:
            if state not in self.states:
                raise ValueError("Final states must be in states")
        self.transition_function = transition_function

    def _step(self, current_state: S, input_value: A) -> S:
        """Perform a single state transition based on the current state and input value."""
        if input_value not in self.input_alphabet:
            raise ValueError("Input value not in input alphabet")
        try:
            return self.transition_function(current_state, input_value)
        except Exception as e:
            raise ValueError(
                f"Transition error for ({current_state},{input_value})"
            ) from e

    def process_input(self, input_iterable: Iterable[A]) -> S:
        """Process a sequence of input values and return the resulting state value."""
        current_state = self.initial_state
        for input_item in input_iterable:
            current_state = self._step(current_state, input_item)
        if current_state not in self.final_states:
            raise ValueError("Final state not allowed")
        return current_state.value
