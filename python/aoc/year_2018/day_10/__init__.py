import re
from dataclasses import dataclass
from operator import attrgetter
from typing import Iterable, List, Tuple


COORD = r'[ ]*-?[0-9]+'
X = fr'(?P<x>{COORD})'
Y = fr'(?P<y>{COORD})'
VX = fr'(?P<vx>{COORD})'
VY = fr'(?P<vy>{COORD})'
POINT_REGEX = re.compile(fr'position=<{X},{Y}> velocity=<{VX},{VY}>')


class InvalidPoint(Exception):
    pass


@dataclass
class Point:
    x: int
    y: int
    vx: int = 0
    vy: int = 0


def parse_point(point_spec: str) -> Point:
    m = POINT_REGEX.match(point_spec)
    if m is None:
        raise InvalidPoint()

    try:
        x = int(m.group('x'))
        y = int(m.group('y'))
        vx = int(m.group('vx'))
        vy = int(m.group('vy'))
    except ValueError:  # pragma: no cover
        raise InvalidPoint()

    return Point(x, y, vx, vy)


def get_limits(points: Iterable[Point]) -> Tuple[Point, Point]:
    min_x = min(points, key=attrgetter('x')).x
    min_y = min(points, key=attrgetter('y')).y
    origin = Point(min_x, min_y)

    max_x = max(points, key=attrgetter('x')).x
    max_y = max(points, key=attrgetter('y')).y
    limit = Point(max_x, max_y)

    return origin, limit


def normalise_point(point: Point, origin: Point) -> Point:
    return Point(point.x - origin.x, point.y - origin.y)


def plot_points(points: Iterable[Point]) -> str:
    origin, limit = get_limits(points)
    normalised = [normalise_point(p, origin) for p in points]

    limit = normalise_point(limit, origin)
    origin = normalise_point(origin, origin)

    width, height = limit.x + 1, limit.y + 1
    plane = []
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append('.')
        plane.append(row)

    for p in normalised:
        plane[p.y][p.x] = '#'

    output = ''
    for row in plane:
        output += ''.join(row) + '\n'

    return output


def move_points(points: Iterable[Point]) -> List[Point]:
    return [Point(p.x + p.vx, p.y + p.vy, p.vx, p.vy) for p in points]
