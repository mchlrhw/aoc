def react_polymer(polymer: str) -> str:
    reactions = True

    while reactions:
        last = len(polymer)
        new_polymer = ''
        reactions = False
        skip = False

        for i, c in enumerate(polymer, start=1):
            if skip:
                skip = False
                continue
            if i == last:
                new_polymer += c
                break

            next_c = polymer[i]
            if c != next_c and c.lower() == next_c.lower():
                reactions = True
                skip = True
            else:
                new_polymer += c

        polymer = new_polymer

    return polymer


def clean_polymer(polymer: str, unit_type: str) -> str:
    unit_types = set((unit_type.lower(), unit_type.upper()))
    polymer = ''.join(u for u in polymer if u not in unit_types)

    return polymer


def optimise_polymer(polymer: str) -> str:
    unit_types = set(polymer.lower())

    best = None
    for unit_type in unit_types:
        cleaned = clean_polymer(polymer, unit_type)
        reacted = react_polymer(cleaned)
        units = len(reacted)
        if best is None or len(best) > units:
            best = reacted

    return best
