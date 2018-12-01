from itertools import combinations
from typing import Tuple


class InvalidDimensions(Exception):
    pass


def parse_dimensions(dimensions: str) -> Tuple[int, int, int]:
    try:
        parsed = (length, width, height) = \
            tuple(int(d) for d in dimensions.split('x'))
    except ValueError:
        raise InvalidDimensions()

    if len(parsed) != 3 or any([d < 1 for d in parsed]):
        raise InvalidDimensions()

    return length, width, height


def side_areas(length: int, width: int, height: int) -> Tuple[int, int, int]:
    a, b, c = tuple(x*y for x, y in combinations((length, width, height), 2))

    return a, b, c
