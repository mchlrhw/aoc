from aoc.year_2018.day_08 import parse_licence, sum_metadata
from aoc.year_2018.day_08 import Node
from aoc.year_2018.day_08.data import puzzle_input


def test_parse_licence_example():
    licence_raw = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
    licence = [int(p.strip()) for p in licence_raw.split()]
    expected = Node(
        children=[
            Node(
                children=[],
                metadata=[10, 11, 12],
            ),
            Node(
                children=[
                    Node(
                        children=[],
                        metadata=[99],
                    ),
                ],
                metadata=[2],
            ),
        ],
        metadata=[1, 1, 2],
    )

    tree, _ = parse_licence(licence)

    assert tree == expected


def test_sum_metadata_example():
    tree = Node(
        children=[
            Node(
                children=[],
                metadata=[10, 11, 12],
            ),
            Node(
                children=[
                    Node(
                        children=[],
                        metadata=[99],
                    ),
                ],
                metadata=[2],
            ),
        ],
        metadata=[1, 1, 2],
    )
    expected = 138

    total = sum_metadata(tree)

    assert total == expected


def test_sum_metadata_puzzle_input():
    licence = [int(p.strip()) for p in puzzle_input.split()]
    tree, _ = parse_licence(licence)
    total = sum_metadata(tree)

    assert total == 41849
