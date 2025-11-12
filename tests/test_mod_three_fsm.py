import pytest
from finite_state_machine.mod_three_fsm import mod_three


@pytest.mark.parametrize(
    "input_string",
    [
        "1101",
        "1110",
        "1111",
        "0",
        "1",
        "0000000",
        "0000001",
        "1111111",
    ],
)
def test_mod_three_examples(input_string: str):
    # Test that the mod_three_fsm computes correct mod 3 values
    assert mod_three(input_string) == int(input_string, 2) % 3


def test_mod_three_empty_input():
    # Test that empty input results in state S0 (0 mod 3)
    assert mod_three("") == 0


def test_mod_three_invalid_input_raises():
    # input contains symbols not in the input alphabet
    with pytest.raises(ValueError, match="Input value not in input alphabet"):
        mod_three("12")
