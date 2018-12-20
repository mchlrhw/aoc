from dataclasses import dataclass
from typing import List, Optional, Tuple


def get_power_level(x: int, y: int, serial_no: int) -> int:
    rack_id = x + 10

    power_level = rack_id * y
    power_level += serial_no
    power_level *= rack_id

    power_str = str(power_level)

    try:
        power_level = int(power_str[-3])
    except IndexError:
        power_level = 0
    power_level -= 5

    return power_level


def populate_grid(serial_no: int, width: int = 300, height: int = 300) \
        -> List[List[int]]:

    grid: List[List[int]] = []

    for y in range(height):
        row: List[int] = []
        for x in range(width):
            row.append(get_power_level(x, y, serial_no))
        grid.append(row)

    return grid


def sub_grid_at(x_0: int, y_0: int, grid: List[List[int]]) \
        -> Optional[List[List[int]]]:

    if x_0 < 0 or y_0 < 0:
        return None

    sub_grid = []

    try:
        for y in range(y_0, y_0+3):
            sub_row = []
            for x in range(x_0, x_0+3):
                sub_row.append(grid[y][x])
            sub_grid.append(sub_row)
    except IndexError:
        return None

    return sub_grid


def total_power(grid: List[List[int]]) -> int:
    power = 0
    for row in grid:
        power += sum(row)
    return power


@dataclass
class Best:
    x: int = 0
    y: int = 0
    power: int = 0


def find_highest_power_coords(grid: List[List[int]]) -> Tuple[int, int]:
    best = Best()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            sub_grid = sub_grid_at(x, y, grid)
            if not sub_grid:
                continue
            power = total_power(sub_grid)
            if power > best.power:
                best = Best(x, y, power)

    return best.x, best.y
