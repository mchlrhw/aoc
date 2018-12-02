import pytest

from aoc.year_2018.day_02 import calculate_checksum, find_duplicate_letters
from aoc.year_2018.day_02 import find_neighbouring_ids
from aoc.year_2018.day_02 import reduce_to_common_letters
from aoc.year_2018.day_02 import NeighboursNotFound
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


@pytest.mark.parametrize(
    'box_ids_raw',
    [
        '',
        'abcde',
        'abcde\nfghij',
    ]
)
def test_neighbours_not_found(box_ids_raw):
    box_ids = [i.strip() for i in box_ids_raw.splitlines() if i]
    with pytest.raises(NeighboursNotFound):
        find_neighbouring_ids(box_ids)


def test_find_neighbouring_ids_examples():
    box_ids_raw = """
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
"""

    box_ids = [i.strip() for i in box_ids_raw.splitlines() if i]
    neighbours = find_neighbouring_ids(box_ids)

    assert neighbours == ('fghij', 'fguij')


def test_find_neighbouring_ids_puzzle_input():
    box_ids = [i.strip() for i in puzzle_input.splitlines() if i]
    neighbours = find_neighbouring_ids(box_ids)

    assert neighbours == (
        'uwkfmdjxyxlbgnrotcfpvswaqh', 'uwzfmdjxyxlbgnrotcfpvswaqh')


def test_reduce_to_common_letters_example():
    common = reduce_to_common_letters('fghij', 'fguij')

    assert common == 'fgij'


def test_reduce_to_common_letters_puzzle_input():
    common = reduce_to_common_letters(
        'uwkfmdjxyxlbgnrotcfpvswaqh', 'uwzfmdjxyxlbgnrotcfpvswaqh')

    assert common == 'uwfmdjxyxlbgnrotcfpvswaqh'
