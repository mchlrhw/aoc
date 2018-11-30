import pytest

from aoc.year_2015.day_01 import basement_entered, find_floor
from aoc.year_2015.day_01 import BasementNotEntered
from aoc.year_2015.day_01 import puzzle_input as real_instructions


def test_find_floor_invalid_characters_skipped():
    instructions = '((xyz))'
    floor = find_floor(instructions)

    assert floor == 0


@pytest.mark.parametrize(
    'instructions, expected_floor',
    [
        ('(())', 0),
        ('()()', 0),
        ('(((', 3),
        ('(()(()(', 3),
        ('))(((((', 3),
        ('())', -1),
        ('))(', -1),
        (')))', -3),
        (')())())', -3),
    ],
)
def test_find_floor_examples(instructions: str, expected_floor: int):
    floor = find_floor(instructions)

    assert floor == expected_floor


def test_find_floor_real_instructions():
    floor = find_floor(real_instructions)

    assert floor == 232


def test_basement_not_entered_no_instructions():
    with pytest.raises(BasementNotEntered):
        basement_entered('')


def test_basement_not_entered():
    with pytest.raises(BasementNotEntered):
        basement_entered('(((')


@pytest.mark.parametrize(
    'instructions, expected_position',
    [
        (')', 1),
        ('()())', 5),
    ],
)
def test_basement_entered_examples(instructions: str, expected_position: int):
    position = basement_entered(instructions)

    assert position == expected_position


def test_basement_entered_real_instructions():
    position = basement_entered(real_instructions)

    assert position == 1783
