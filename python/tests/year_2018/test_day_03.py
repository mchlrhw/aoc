import pytest

from aoc.year_2018.day_03 import init_fabric, fabric_to_str
from aoc.year_2018.day_03 import parse_claim, place_claim
from aoc.year_2018.day_03 import InvalidClaim, Rectangle
from aoc.year_2018.day_03.data import puzzle_input


def test_init_fabric_example():
    fabric = init_fabric(9, 11)
    expected = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ]

    assert fabric == expected


def test_fabric_to_str_example():
    fabric = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.'],
        ['.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.'],
        ['.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.'],
        ['.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ]
    string = fabric_to_str(fabric)
    expected = """\
...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
"""

    assert string == expected


def test_place_claim_example():
    claim = Rectangle(3, 2, 5, 4)
    fabric = place_claim(init_fabric(9, 11), claim)
    expected = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.'],
        ['.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.'],
        ['.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.'],
        ['.', '.', '.', '#', '#', '#', '#', '#', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ]

    assert fabric == expected


@pytest.mark.parametrize(
    'claim, expected',
    [
        ('#1 @ 1,3: 4x4', Rectangle(1, 3, 4, 4, '1')),
        ('#2 @ 3,1: 4x4', Rectangle(3, 1, 4, 4, '2')),
        ('#3 @ 5,5: 2x2', Rectangle(5, 5, 2, 2, '3')),
    ],
)
def test_parse_claims_examples(claim, expected):
    rectangle = parse_claim(claim)

    assert rectangle == expected


def test_overlap_visualisation_example():
    fabric = init_fabric(8, 8)
    claims = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
    ]
    for claim in claims:
        place_claim(fabric, parse_claim(claim))
    string = fabric_to_str(fabric)
    expected = """\
........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
"""

    assert string == expected


def test_overlap_puzzle_input():
    fabric = init_fabric()
    claims = [c.strip() for c in puzzle_input.splitlines() if c]
    for claim in claims:
        place_claim(fabric, parse_claim(claim))

    overlap = 0
    for column in fabric:
        for square in column:
            if square == 'X':
                overlap += 1

    assert overlap == 112418
