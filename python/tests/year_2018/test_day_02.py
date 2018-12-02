import pytest

from aoc.year_2018.day_02 import calculate_checksum, find_duplicate_letters
from aoc.year_2018.day_02.data import puzzle_input


@pytest.mark.parametrize(
    'box_id, expected',
    [
        ('abcdef', (0, 0)),
        ('bababc', (1, 1)),
        ('abbcde', (1, 0)),
        ('abcccd', (0, 1)),
        ('aabcdd', (1, 0)),
        ('abcdee', (1, 0)),
        ('ababab', (0, 1)),
    ],
)
def test_find_duplicate_letters_examples(box_id, expected):
    duplicates = find_duplicate_letters(box_id)

    assert duplicates == expected


def test_calculate_checksum_example():
    box_ids_raw = """
abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
"""

    box_ids = [i.strip() for i in box_ids_raw.splitlines() if i]
    checksum = calculate_checksum(box_ids)

    assert checksum == 12


def test_calculate_checksum_puzzle_input():
    box_ids = [i.strip() for i in puzzle_input.splitlines() if i]
    checksum = calculate_checksum(box_ids)

    assert checksum == 5727
