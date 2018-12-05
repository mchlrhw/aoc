def react_polymer(polymer: str) -> str:
    buf = list(polymer)
    reactions = True
    i = 0

    while reactions:
        while i < len(buf):  # pragma: no branch
            try:
                unit = buf[i]
                next_unit = buf[i+1]
            except IndexError:
                reactions = False
                break
            if unit != next_unit and unit.lower() == next_unit.lower():
                buf.pop(i)
                buf.pop(i)
                i -= 1
            else:
                i += 1

    return ''.join(buf)


def clean_polymer(polymer: str, unit_type: str) -> str:
    unit_types = set((unit_type.lower(), unit_type.upper()))
    polymer = ''.join(u for u in polymer if u not in unit_types)

    return polymer


def optimise_polymer(polymer: str) -> str:
    unit_types = set(polymer.lower())

    best = polymer
    for unit_type in unit_types:
        new_polymer = clean_polymer(polymer, unit_type)
        new_polymer = react_polymer(new_polymer)
        if len(best) > len(new_polymer):
            best = new_polymer

    return best
