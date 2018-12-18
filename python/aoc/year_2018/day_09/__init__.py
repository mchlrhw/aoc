class MarbleMania:
    def __init__(self, players, last_marble) -> None:
        self.players = players
        self.last_marble = last_marble

        self.scores = [0 for _ in range(self.players)]

        self.circle = [0]
        self.index = 1
        self.marble = 1
        self.player = 0

    def _step(self):
        if not self.marble > self.last_marble:
            if self.marble and self.marble % 23 == 0:
                self.index = (self.index - 9) % len(self.circle)
                self.scores[self.player] += \
                    self.marble + self.circle.pop(self.index)
            else:
                self.circle.insert(self.index, self.marble)

            self.player = (self.player + 1) % self.players
            self.index = (self.index + 2) % len(self.circle)
            if self.index == 0:
                self.index = len(self.circle)
            self.marble += 1

            return True
        return False

    def play(self) -> int:
        while self._step():
            pass
        return max(self.scores)
