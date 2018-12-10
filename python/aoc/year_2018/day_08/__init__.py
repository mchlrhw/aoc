from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Node:
    children: list = field(default_factory=list)
    metadata: List[int] = field(default_factory=list)


def parse_licence(licence: List[int]) -> Tuple[Node, List[int]]:
    child_cnt, pay_len = licence[:2]
    licence = licence[2:]

    if not child_cnt:
        return Node(metadata=licence[:pay_len]), licence[pay_len:]

    node = Node()
    for _ in range(child_cnt):
        child, licence = parse_licence(licence)
        node.children.append(child)

    node.metadata.extend(licence[:pay_len])

    return node, licence[pay_len:]


def sum_metadata(tree: Node) -> int:
    result = 0

    for child in tree.children:
        result += sum_metadata(child)

    result += sum(tree.metadata)

    return result


def sum_values(tree: Node) -> int:
    if not tree.children:
        return sum(tree.metadata)

    result = 0

    indices = [m-1 for m in tree.metadata if m-1 >= 0]
    for index in indices:
        try:
            result += sum_values(tree.children[index])
        except IndexError:
            continue

    return result
