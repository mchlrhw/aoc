from .data import puzzle_input


class BasementNotEntered(Exception):
    pass


def find_floor(instructions: str, floor: int = 0) -> int:
    for c in instructions:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
    return floor


def basement_entered(instructions: str) -> int:
    floor = 0
    for i, c in enumerate(instructions, start=1):
        floor = find_floor(c, floor)
        if floor == -1:
            return i
    raise BasementNotEntered()
