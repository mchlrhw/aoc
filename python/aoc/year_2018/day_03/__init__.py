from dataclasses import dataclass
from typing import List, Mapping, Tuple


class InvalidClaim(Exception):
    pass


@dataclass
class Rectangle:
    x: int
    y: int
    width: int
    height: int
    tag: str = '#'


def init_fabric(width: int = 1000, height: int = 1000) -> List[List[str]]:
    fabric: List[List[str]] = []

    for x in range(width):
        fabric.append([])
        for y in range(height):
            fabric[x].append('.')

    return fabric


def fabric_to_str(fabric: List[List[str]]) -> str:
    string = ''
    for column in fabric:
        for square in column:
            string += square
        string += '\n'
    return string


def parse_x_y(x_y: str) -> Tuple[int, int]:
    x_raw, y_raw = x_y.strip(':').split(',')
    x, y = int(x_raw), int(y_raw)

    return x, y


def parse_w_h(w_h: str) -> Tuple[int, int]:
    width_raw, height_raw = w_h.split('x')
    width, height = int(width_raw), int(height_raw)

    return width, height


def parse_claim(claim: str) -> Rectangle:
    parts = claim.split()
    if len(parts) != 4:
        raise InvalidClaim()

    tag, _, x_y, w_h = parts
    tag = tag.strip('#')

    try:
        x, y = parse_x_y(x_y)
        width, height = parse_w_h(w_h)
    except ValueError:
        raise InvalidClaim()

    return Rectangle(x, y, width, height, tag)


def place_claim(fabric: List[List[str]], claim: Rectangle) -> List[List[str]]:
    x_0, x_1 = claim.x, claim.x + claim.width
    y_0, y_1 = claim.y, claim.y + claim.height

    for x in range(x_0, x_1):
        for y in range(y_0, y_1):
            occupied = True if fabric[y][x] != '.' else False
            if occupied:
                fabric[y][x] = 'X'
            else:
                fabric[y][x] = claim.tag

    return fabric
