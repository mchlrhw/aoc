from typing import List


def react_polymer(polymer: str) -> str:
    buf: List[str] = []

    for unit in polymer:
        try:
            prev_unit = buf.pop()
        except IndexError:
            buf.append(unit)
            continue

        if unit != prev_unit and unit.lower() == prev_unit.lower():
            continue
        else:
            buf.extend((prev_unit, unit))

    return ''.join(buf)


def clean_polymer(polymer: str, unit_type: str) -> str:
    unit_types = set((unit_type.lower(), unit_type.upper()))
    polymer = ''.join(u for u in polymer if u not in unit_types)

    return polymer


def optimise_polymer(polymer: str) -> str:
    polymer = react_polymer(polymer)
    unit_types = set(polymer.lower())

    best = polymer
    for unit_type in unit_types:
        new_polymer = clean_polymer(polymer, unit_type)
        new_polymer = react_polymer(new_polymer)
        if len(best) > len(new_polymer):
            best = new_polymer

    return best
