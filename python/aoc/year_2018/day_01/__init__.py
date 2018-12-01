from operator import add, sub
from typing import Callable, List, Tuple


class InvalidChange(Exception):
    pass


def parse_frequency_changes(changes: str) -> List[Tuple[Callable, int]]:
    change_list = [c.strip() for c in changes.split(',')]

    parsed = []
    for change in change_list:
        direction_char, amount_str = change[0], change[1:]

        if direction_char == '+':
            direction = add
        elif direction_char == '-':
            direction = sub
        else:
            raise InvalidChange()

        try:
            amount = int(amount_str)
        except ValueError:
            raise InvalidChange()

        parsed.append((direction, amount))

    return parsed


def apply_changes(
        changes: List[Tuple[Callable, int]], frequency: int = 0) -> int:

    for direction, amount in changes:
        frequency = direction(frequency, amount)
    return frequency


def find_duplicate_frequency(
        changes: List[Tuple[Callable, int]], frequency: int = 0) -> int:

    seen = set([frequency])
    found = False

    while not found:
        for direction, amount in changes:
            frequency = direction(frequency, amount)
            if frequency in seen:
                found = True
                break
            seen.add(frequency)

    return frequency
