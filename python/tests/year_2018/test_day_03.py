import pytest

from aoc.year_2018.day_03 import init_fabric, fabric_to_str, get_claim_areas
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


def test_get_claim_areas_example():
    fabric = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '2', '2', '2', '2', '.'],
        ['.', '.', '.', '2', '2', '2', '2', '.'],
        ['.', '1', '1', 'X', 'X', '2', '2', '.'],
        ['.', '1', '1', 'X', 'X', '2', '2', '.'],
        ['.', '1', '1', '1', '1', '3', '3', '.'],
        ['.', '1', '1', '1', '1', '3', '3', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
    ]
    claim_areas = get_claim_areas(fabric)
    expected_1, expected_2, expected_3 = 12, 12, 4

    assert claim_areas['1'] == expected_1
    assert claim_areas['2'] == expected_2
    assert claim_areas['3'] == expected_3


def test_non_overlapping_claim_puzzle_input():
    fabric = init_fabric()
    raw_claims = [r.strip() for r in puzzle_input.splitlines() if r]
    claims = [parse_claim(r) for r in raw_claims]
    for claim in claims:
        place_claim(fabric, claim)

    claim_areas_before = {c.tag: c.width*c.height for c in claims}
    claim_areas_after = get_claim_areas(fabric)

    non_overlapping = set()
    for tag, area in claim_areas_before.items():
        if claim_areas_after[tag] == area:
            non_overlapping.add(tag)

    assert len(non_overlapping) == 1
    assert non_overlapping.pop() == '560'
