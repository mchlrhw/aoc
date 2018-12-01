from operator import add, sub

import pytest

from aoc.year_2018.day_01 import apply_changes, find_duplicate_frequency
from aoc.year_2018.day_01 import parse_frequency_changes, InvalidChange
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


@pytest.mark.parametrize(
    'changes, expected',
    [
        ('+1, -2, +3, +1', 2),
        ('+1, -1', 0),
        ('+3, +3, +4, -2, -4', 10),
        ('-6, +3, +8, +5, -6', 5),
        ('+7, +7, -2, -7, -4', 14),
    ],
)
def test_find_duplicate_frequency_examples(changes, expected):
    frequency = find_duplicate_frequency(
        parse_frequency_changes(changes))

    assert frequency == expected


def test_find_duplicate_frequency_puzzle_input():
    frequency = find_duplicate_frequency(
        parse_frequency_changes(puzzle_input))

    assert frequency == 73056
