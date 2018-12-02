from collections import Counter
from typing import Iterable, Tuple


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
