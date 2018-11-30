from .data import puzzle_input


def find_floor(instructions: str) -> int:
    floor = 0
    for c in instructions:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
    return floor
