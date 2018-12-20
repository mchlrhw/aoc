import pytest

from aoc.year_2018.day_11 import find_highest_power_coords
from aoc.year_2018.day_11 import get_power_level, populate_grid
from aoc.year_2018.day_11 import sub_grid_at, total_power


@pytest.mark.parametrize(
    'x, y, serial_no, expected',
    [
        (3, 5, 8, 4),
        (122, 79, 57, -5),
        (217, 196, 39, 0),
        (101, 153, 71, 4),
    ],
)
def test_get_power_level_examples(x, y, serial_no, expected):
    power_level = get_power_level(x, y, serial_no)

    assert power_level == expected


@pytest.mark.parametrize(
    'serial_no, x_0, y_0, expected',
    [
        (18, 32, 44, [[-2, -4,  4,  4,  4],
                      [-4,  4,  4,  4, -5],
                      [ 4,  3,  3,  4, -4],   # noqa: E201
                      [ 1,  1,  2,  4, -3],   # noqa: E201
                      [-1,  0,  2, -5, -2]],
        ),                                    # noqa: E124
        (42, 20, 60, [[-3,  4,  2,  2,  2],
                      [-4,  4,  3,  3,  4],
                      [-5,  3,  3,  4, -4],
                      [ 4,  3,  3,  4, -3],   # noqa: E201
                      [ 3,  3,  3, -5, -1]],  # noqa: E201
        ),                                    # noqa: E124
    ],
)
def test_populate_grid_examples(serial_no, x_0, y_0, expected):
    grid = populate_grid(serial_no)

    sub_grid = []
    for y in range(y_0, y_0+5):
        sub_grid.append(grid[y][x_0:x_0+5])

    assert sub_grid == expected


@pytest.mark.parametrize(
    'x_0, y_0',
    [
        (-1, -1),
        (0, 299),
        (299, 0),
        (299, 299),
    ],
)
def test_sub_grid_at_out_of_bounds(x_0, y_0):
    sub_grid = sub_grid_at(x_0, y_0, populate_grid(18))

    assert sub_grid is None


@pytest.mark.parametrize(
    'serial_no, x_0, y_0, expected',
    [
        (18, 33, 45, [[4, 4, 4],
                      [3, 3, 4],
                      [1, 2, 4]],
        ),                         # noqa: E124
        (42, 21, 61, [[4, 3, 3],
                      [3, 3, 4],
                      [3, 3, 4]],
        ),                         # noqa: E124
    ],
)
def test_sub_grid_at_examples(serial_no, x_0, y_0, expected):
    grid = populate_grid(serial_no)
    sub_grid = sub_grid_at(x_0, y_0, grid)

    assert sub_grid == expected


@pytest.mark.parametrize(
    'grid, expected',
    [
        ([[4, 4, 4],
          [3, 3, 4],
          [1, 2, 4]], 29,
        ),                # noqa: E124
        ([[4, 3, 3],
          [3, 3, 4],
          [3, 3, 4]], 30,
        ),                # noqa: E124
    ],
)
def test_total_power_examples(grid, expected):
    power = total_power(grid)

    assert power == expected


@pytest.mark.parametrize(
    'serial_no, expected',
    [
        (18, (33, 45)),
        (42, (21, 61)),
    ],
)
def test_find_highest_power_coords(serial_no, expected):
    grid = populate_grid(serial_no)
    coords = find_highest_power_coords(grid)

    assert coords == expected


def test_find_highest_power_coords_puzzle_input():
    grid = populate_grid(1718)
    coords = find_highest_power_coords(grid)

    assert coords == (243, 34)
