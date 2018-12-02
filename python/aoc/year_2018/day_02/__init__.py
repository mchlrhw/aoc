from collections import Counter
from typing import Iterable, List, Tuple


class NeighboursNotFound(Exception):
    pass


def find_duplicate_letters(box_id: str) -> Tuple[int, int]:
    double = 0
    triple = 0
    letter_counts = Counter(box_id)

    for _, count in letter_counts.items():
        if count == 2:
            double = 1
        elif count == 3:
            triple = 1

    return double, triple


def calculate_checksum(box_ids: Iterable[str]) -> int:
    doubles = 0
    triples = 0

    for box_id in box_ids:
        double, triple = find_duplicate_letters(box_id)
        doubles += double
        triples += triple

    checksum = doubles * triples

    return checksum


def find_neighbouring_ids(box_ids: List[str]) -> Tuple[str, str]:
    last = len(box_ids)

    for i, box_id in enumerate(box_ids, 1):
        if i == last:
            break

        other_ids = box_ids[i:]

        for other_id in other_ids:
            differences = 0
            for j, char in enumerate(box_id):
                if char != other_id[j]:
                    differences += 1
                if differences > 1:
                    break
            if differences == 1:
                return box_id, other_id

    raise NeighboursNotFound()


def reduce_to_common_letters(id_a: str, id_b: str) -> str:
    common = ''

    for i, char in enumerate(id_a):
        if char == id_b[i]:
            common += char

    return common
