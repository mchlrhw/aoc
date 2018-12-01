import pytest

from aoc.year_2015.day_02 import parse_dimensions, side_areas
from aoc.year_2015.day_02 import InvalidDimensions
from aoc.year_2015.day_02.data import puzzle_input


def test_parse_not_an_int():
    with pytest.raises(InvalidDimensions):
        parse_dimensions('1xax3')


def test_parse_negative_int():
    with pytest.raises(InvalidDimensions):
        parse_dimensions('1x2x-3')


def test_parse_too_many_dimensions():
    with pytest.raises(InvalidDimensions):
        parse_dimensions('1x2x3x4')


@pytest.mark.parametrize(
    'dimensions, expected',
    [
        ('2x3x4', (2, 3, 4)),
        ('1x1x10', (1, 1, 10)),
    ],
)
def test_parse_dimensions_examples(dimensions, expected):
    parsed = parse_dimensions(dimensions)

    assert parsed == expected


@pytest.mark.parametrize(
    'dimensions, expected_sides, expected_surface, expected_paper',
    [
        ('2x3x4', (6, 8, 12), 52, 58),
        ('1x1x10', (1, 10, 10), 42, 43),
    ],
)
def test_side_areas_examples(
        dimensions, expected_sides, expected_surface, expected_paper):
    areas = side_areas(*parse_dimensions(dimensions))
    total = sum((2*a for a in areas))
    smallest_side = min(areas)
    required_paper = total + smallest_side

    assert areas == expected_sides
    assert total == expected_surface
    assert required_paper == expected_paper


def test_total_paper_puzzle_input():
    all_dimensions = (d.strip() for d in puzzle_input.splitlines() if d)

    total = 0
    for dimensions in all_dimensions:
        areas = side_areas(*parse_dimensions(dimensions))
        surface = sum((2*a for a in areas))
        smallest_side = min(areas)
        total += surface + smallest_side

    assert total == 1588178
