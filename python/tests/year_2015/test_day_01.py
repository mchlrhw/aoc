import pytest

from aoc.year_2015.day_01 import find_floor
from aoc.year_2015.day_01 import puzzle_input as real_instructions


def test_invalid_characters_skipped():
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
def test_example_instructions(instructions: str, expected_floor: int):
    floor = find_floor(instructions)

    assert floor == expected_floor


def test_real_instructions():
    floor = find_floor(real_instructions)

    assert floor == 232
