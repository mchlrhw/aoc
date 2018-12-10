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
