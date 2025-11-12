# finite_state_machine

Small example library that implements a generic finite state machine and a
concrete "mod three" FSM example. This repository includes a minimal test
suite and packaging metadata so you can install or run the examples locally.

## Features
- A small, generic `FiniteStateMachine` class (type-parameterized for states
  and alphabet values).
- Example FSM in `finite_state_machine/mod_three_fsm.py` that computes a
  binary number modulo 3.
- Tests under `tests/` using `pytest`.

## Requirements
- Python 3.8+

## Quick start (PowerShell)

Create a virtual environment, install dev dependencies, and run tests:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
# Install the package in editable mode with dev extras
python -m pip install -e .[dev]
python -m pytest -q
```

Run the example FSM as a module (prints example outputs):

```powershell
python -m finite_state_machine.mod_three_fsm
```

Or import and use the `mod_three` helper function programmatically:

```python
from finite_state_machine import mod_three

result = mod_three("1101")
print(f"Binary 1101 (13) mod 3 = {result}")  # prints: Binary 1101 (13) mod 3 = 1
```

## API Reference

### `FiniteStateMachine` class

Located in `finite_state_machine/finite_state_machine.py`.

A generic, type-safe implementation of a finite state machine. Use this class to build
FSMs that recognize or validate patterns, compute values based on input sequences, or
model state-based systems.

**How to use:**
1. Define an `Enum` class for your states (e.g., `MyStates`).
2. Define your input alphabet (e.g., a list of symbols or another `Enum`).
3. Write a transition function that returns the next state given a current state and
   an input symbol.
4. Instantiate `FiniteStateMachine` with these components.
5. Call `process_input()` with a sequence of input symbols to run the FSM.

The FSM validates that all states and transitions are well-defined, and raises
`ValueError` with descriptive messages if inputs are invalid or the final state is
not an accepting state.

**Constructor:**

```python
FiniteStateMachine(
    states: Type[Enum],
    input_alphabet: Container[A],
    initial_state: Enum,
    final_states: Iterable[Enum],
    transition_function: Callable[[Enum, A], Enum],
)
```

**Parameters:**
- `states`: An enumeration class defining the FSM's possible states.
- `input_alphabet`: A collection (e.g., list, set, or enum) of valid input symbols.
- `initial_state`: The starting state (must be a member of `states`).
- `final_states`: A collection of accepting states (all must be members of `states`).
- `transition_function`: A function `(state, symbol) -> next_state` defining the FSM's behavior.

**Methods:**

- `process_input(input_iterable: Iterable[A]) -> object`
  - Processes a sequence of input symbols (e.g., a string, list, or generator).
  - Returns the `.value` attribute of the final state if it's an accepting state.
  - **Raises** `ValueError` if:
    - An input symbol is not in the input alphabet.
    - The final state is not in the accepting states.
    - The transition function fails (e.g., missing transition or returns invalid state).

### `mod_three(input: str) -> int`

A helper function that computes a binary number modulo 3.

```python
from finite_state_machine import mod_three

result = mod_three("1101")  # Binary 13 mod 3
assert result == 1
```

## Error Handling

The FSM validates inputs and state transitions. Common errors:

```python
# Invalid symbol in input
fsm.process_input("2")  # ValueError: Input value not in input alphabet

# Ends in non-accepting state
fsm.process_input("0")  # ValueError: Final state not allowed

# Missing transition (incomplete transition function)
fsm.process_input("x")  # ValueError: Transition error for (state, 'x')
```

See the test files (`tests/`) for more usage examples and edge cases.

## Testing

Run the tests:

```powershell
python -m pytest
```

By default, pytest runs with coverage reporting enabled (via `pyproject.toml`
configuration).

## Packaging

This repository includes a minimal `pyproject.toml`. To install locally:

```powershell
python -m pip install -e .
```

To build a wheel:

```powershell
python -m pip install build
python -m build
```

## License

MIT — see the `pyproject.toml` metadata for details.
