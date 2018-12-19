import pytest

from aoc.year_2018.day_10 import get_limits, move_points
from aoc.year_2018.day_10 import parse_point, plot_points
from aoc.year_2018.day_10 import InvalidPoint, Point
from aoc.year_2018.day_10.data import puzzle_input


@pytest.mark.parametrize(
    'invalid_input',
    [
        '',
        'position=< a,  1> velocity=< 0,  2>',
        'position=< 9,  a> velocity=< 0,  2>',
        'position=< 9,  1> velocity=< a,  2>',
        'position=< 9,  1> velocity=< 0,  a>',
    ],
)
def test_invalid_point(invalid_input):
    with pytest.raises(InvalidPoint):
        parse_point(invalid_input)


@pytest.mark.parametrize(
    'point_spec, expected',
    [
        ('position=< 9,  1> velocity=< 0,  2>', Point(9, 1, 0, 2)),
        ('position=< 7,  0> velocity=<-1,  0>', Point(7, 0, -1, 0)),
        ('position=< 3, -2> velocity=<-1,  1>', Point(3, -2, -1, 1)),
        ('position=< 6, 10> velocity=<-2, -1>', Point(6, 10, -2, -1)),
        ('position=< 2, -4> velocity=< 2,  2>', Point(2, -4, 2, 2)),
        ('position=<-6, 10> velocity=< 2, -2>', Point(-6, 10, 2, -2)),
        ('position=< 1,  8> velocity=< 1, -1>', Point(1, 8, 1, -1)),
        ('position=< 1,  7> velocity=< 1,  0>', Point(1, 7, 1, 0)),
        ('position=<-3, 11> velocity=< 1, -2>', Point(-3, 11, 1, -2)),
        ('position=< 7,  6> velocity=<-1, -1>', Point(7, 6, -1, -1)),
        ('position=<-2,  3> velocity=< 1,  0>', Point(-2, 3, 1, 0)),
        ('position=<-4,  3> velocity=< 2,  0>', Point(-4, 3, 2, 0)),
        ('position=<10, -3> velocity=<-1,  1>', Point(10, -3, -1, 1)),
        ('position=< 5, 11> velocity=< 1, -2>', Point(5, 11, 1, -2)),
        ('position=< 4,  7> velocity=< 0, -1>', Point(4, 7, 0, -1)),
        ('position=< 8, -2> velocity=< 0,  1>', Point(8, -2, 0, 1)),
        ('position=<15,  0> velocity=<-2,  0>', Point(15, 0, -2, 0)),
        ('position=< 1,  6> velocity=< 1,  0>', Point(1, 6, 1, 0)),
        ('position=< 8,  9> velocity=< 0, -1>', Point(8, 9, 0, -1)),
        ('position=< 3,  3> velocity=<-1,  1>', Point(3, 3, -1, 1)),
        ('position=< 0,  5> velocity=< 0, -1>', Point(0, 5, 0, -1)),
        ('position=<-2,  2> velocity=< 2,  0>', Point(-2, 2, 2, 0)),
        ('position=< 5, -2> velocity=< 1,  2>', Point(5, -2, 1, 2)),
        ('position=< 1,  4> velocity=< 2,  1>', Point(1, 4, 2, 1)),
        ('position=<-2,  7> velocity=< 2, -2>', Point(-2, 7, 2, -2)),
        ('position=< 3,  6> velocity=<-1, -1>', Point(3, 6, -1, -1)),
        ('position=< 5,  0> velocity=< 1,  0>', Point(5, 0, 1, 0)),
        ('position=<-6,  0> velocity=< 2,  0>', Point(-6, 0, 2, 0)),
        ('position=< 5,  9> velocity=< 1, -2>', Point(5, 9, 1, -2)),
        ('position=<14,  7> velocity=<-2,  0>', Point(14, 7, -2, 0)),
        ('position=<-3,  6> velocity=< 2, -1>', Point(-3, 6, 2, -1)),
    ],
)
def test_parse_point_examples(point_spec, expected):
    point = parse_point(point_spec)

    assert point == expected


test_input = """
position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
"""


def test_get_limits_example():
    points = [parse_point(p) for p in test_input.splitlines() if p.strip()]
    expected = (Point(-6, -4), Point(15, 11))

    result = get_limits(points)

    assert result == expected


def test_plot_points_example():
    points = [parse_point(p) for p in test_input.splitlines() if p.strip()]
    expected = """\
........#.............
................#.....
.........#.#..#.......
......................
#..........#.#.......#
...............#......
....#.................
..#.#....#............
.......#..............
......#...............
...#...#.#...#........
....#..#..#.........#.
.......#..............
...........#..#.......
#...........#.........
...#.......#..........
"""

    output = plot_points(points)

    assert output == expected


def test_move_points():
    points = [parse_point(p) for p in test_input.splitlines() if p.strip()]
    examples = [
        """\
........#....#....
......#.....#.....
#.........#......#
..................
....#.............
..##.........#....
....#.#...........
...##.##..#.......
......#.#.........
......#...#.....#.
#...........#.....
..#.....#.#.......
""",
        """\
..........#...
#..#...####..#
..............
....#....#....
..#.#.........
...#...#......
...#..#..#.#..
#....#.#......
.#...#...##.#.
....#.........
""",
        """\
#...#..###
#...#...#.
#...#...#.
#####...#.
#...#...#.
#...#...#.
#...#...#.
#...#..###
""",
        """\
........#....
....##...#.#.
..#.....#..#.
.#..##.##.#..
...##.#....#.
.......#....#
..........#..
#......#...#.
.#.....##....
...........#.
...........#.
"""]

    for expected in examples:
        points = move_points(points)
        output = plot_points(points)

        assert output == expected


def test_move_points_puzzle_input():
    expected = """\
######..#....#....##....#.......#.......#....#..#.......#####.
#.......#...#....#..#...#.......#.......#...#...#.......#....#
#.......#..#....#....#..#.......#.......#..#....#.......#....#
#.......#.#.....#....#..#.......#.......#.#.....#.......#....#
#####...##......#....#..#.......#.......##......#.......#####.
#.......##......######..#.......#.......##......#.......#....#
#.......#.#.....#....#..#.......#.......#.#.....#.......#....#
#.......#..#....#....#..#.......#.......#..#....#.......#....#
#.......#...#...#....#..#.......#.......#...#...#.......#....#
######..#....#..#....#..######..######..#....#..######..#####.
"""

    points = [parse_point(p) for p in puzzle_input.splitlines() if p.strip()]
    for i in range(1, 10228):
        points = move_points(points)
    output = plot_points(points)

    assert output == expected  # part 1
    assert i == 10227          # part 2
