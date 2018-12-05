import pytest

from aoc.year_2018.day_05 import clean_polymer, optimise_polymer, react_polymer
from aoc.year_2018.day_05.data import puzzle_input


@pytest.mark.parametrize(
    'polymer, expected',
    [
        ('aA', ''),
        ('abBA', ''),
        ('abAB', 'abAB'),
        ('aabAAB', 'aabAAB'),
        ('dabAcCaCBAcCcaDA', 'dabCBAcaDA'),
    ],
)
def test_react_polymer_examples(polymer, expected):
    reacted = react_polymer(polymer)

    assert reacted == expected


def test_react_polymer_puzzle_input():
    reacted = react_polymer(puzzle_input)
    units = len(reacted)

    assert units == 10598


@pytest.mark.parametrize(
    'unit_type, expected',
    [
        ('a', 'dbcCCBcCcD'),
        ('b', 'daAcCaCAcCcaDA'),
        ('c', 'dabAaBAaDA'),
        ('d', 'abAcCaCBAcCcaA'),
    ],
)
def test_clean_polymer_examples(unit_type, expected):
    polymer = 'dabAcCaCBAcCcaDA'
    cleaned = clean_polymer(polymer, unit_type)

    assert cleaned == expected


def test_optimise_polymer_example():
    polymer = 'dabAcCaCBAcCcaDA'
    optimised = optimise_polymer(polymer)
    units = len(optimised)

    assert units == 4


def test_optimise_polymer_puzzle_input():
    optimised = optimise_polymer(puzzle_input)
    units = len(optimised)

    assert units == 5312
