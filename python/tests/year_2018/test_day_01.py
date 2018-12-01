from operator import add, sub

import pytest

from aoc.year_2018.day_01 import apply_changes, parse_frequency_changes
from aoc.year_2018.day_01 import InvalidChange
from aoc.year_2018.day_01.data import puzzle_input


def test_invalid_change_direction():
    with pytest.raises(InvalidChange):
        parse_frequency_changes('+3, *4')


def test_invalid_change_amount():
    with pytest.raises(InvalidChange):
        parse_frequency_changes('+3, -a')


@pytest.mark.parametrize(
    'changes, expected',
    [
        ('+6', [(add, 6)]),
        ('-3', [(sub, 3)]),
        (
            '+1, -2, +3, +1',
            [(add, 1), (sub, 2), (add, 3), (add, 1)],
        ),
    ],
)
def test_parse_fequency_changes_examples(changes, expected):
    parsed = parse_frequency_changes(changes)

    assert parsed == expected


@pytest.mark.parametrize(
    'changes, expected',
    [
        ('+1, +1, +1', 3),
        ('+1, +1, -2', 0),
        ('-1, -2, -3', -6),
    ],
)
def test_apply_changes_examples(changes, expected):
    frequency = apply_changes(parse_frequency_changes(changes))

    assert frequency == expected


def test_apply_changes_puzzle_input():
    frequency = apply_changes(parse_frequency_changes(puzzle_input))

    assert frequency == 540
