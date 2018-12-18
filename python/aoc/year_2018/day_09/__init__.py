from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    anticlockwise: Any
    clockwise: Any
    marble: int


class Circle:
    def __init__(self):
        self.root = Node(None, None, 0)
        self.root.anticlockwise = self.root
        self.root.clockwise = self.root
        self.current = self.root

    def __iter__(self):
        current = self.root
        while True:
            yield current.marble
            current = current.clockwise
            if current.marble == self.root.marble:
                break

    def move_clockwise(self, steps: int):
        for _ in range(steps):
            self.current = self.current.clockwise

    def move_anticlockwise(self, steps: int):
        for _ in range(steps):
            self.current = self.current.anticlockwise

    def insert(self, marble: int):
        node = Node(self.current, self.current.clockwise, marble)
        self.current.clockwise = node
        node.clockwise.anticlockwise = node
        self.current = node

    def pop(self) -> int:
        popped = self.current
        marble = popped.marble

        anticlockwise = popped.anticlockwise
        clockwise = popped.clockwise

        anticlockwise.clockwise = clockwise
        clockwise.anticlockwise = anticlockwise

        self.current = clockwise
        del(popped)

        return marble


class MarbleMania:
    def __init__(self, players, last_marble) -> None:
        self.players = players
        self.last_marble = last_marble

        self.scores = [0 for _ in range(self.players)]

        self.circle = Circle()
        self.marble = 1
        self.player = 0

    def _step(self):
        if not self.marble > self.last_marble:
            if self.marble and self.marble % 23 == 0:
                self.circle.move_anticlockwise(7)
                self.scores[self.player] += \
                    self.marble + self.circle.pop()
            else:
                self.circle.move_clockwise(1)
                self.circle.insert(self.marble)

            self.player = (self.player + 1) % self.players
            self.marble += 1

            return True
        return False

    def play(self) -> int:
        while self._step():
            pass
        return max(self.scores)
