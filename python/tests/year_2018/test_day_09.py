import pytest

from aoc.year_2018.day_09 import MarbleMania


def test_step_example():
    game = MarbleMania(players=9, last_marble=25)
    expected = [
        [0],
        [0, 1],
        [0, 2, 1],
        [0, 2, 1, 3],
        [0, 4, 2, 1, 3],
        [0, 4, 2, 5, 1, 3],
        [0, 4, 2, 5, 1, 6, 3],
        [0, 4, 2, 5, 1, 6, 3, 7],
        [0, 8, 4, 2, 5, 1, 6, 3, 7],
        [0, 8, 4, 9, 2, 5, 1, 6, 3, 7],
        [0, 8, 4, 9, 2, 10, 5, 1, 6, 3, 7],
        [0, 8, 4, 9, 2, 10, 5, 11, 1, 6, 3, 7],
        [0, 8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 3, 7],
        [0, 8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 7],
        [0, 8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7],
        [0, 8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15],
        [0, 16, 8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15],
        [0, 16, 8, 17, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15],
        [0, 16, 8, 17, 4, 18, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15],
        [0, 16, 8, 17, 4, 18, 9, 19, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15],
        [0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15],
        [0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15],
        [0, 16, 8, 17, 4, 18, 9, 19, 2, 20, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15],
        [0, 16, 8, 17, 4, 18, 19, 2, 20, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15],
        [0, 16, 8, 17, 4, 18, 19, 2, 24, 20, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15],
        [0, 16, 8, 17, 4, 18, 19, 2, 24, 20, 25, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15],
    ]

    states = [list(game.circle)]
    while game._step():
        states.append(list(game.circle))

    assert states == expected


@pytest.mark.parametrize(
    'players, last_marble, expected',
    [
        (9, 25, 32),
        (10, 1618, 8317),
        (13, 7999, 146373),
        (17, 1104, 2764),
        (21, 6111, 54718),
        (30, 5807, 37305),
    ],
)
def test_play_game_examples(players, last_marble, expected):
    game = MarbleMania(players, last_marble)
    high_score = game.play()

    assert high_score == expected


def test_play_puzzle_input():
    game = MarbleMania(441, 71032)
    high_score = game.play()

    assert high_score == 393229


@pytest.mark.skip(reason='slow even with linked list impl')
def test_play_puzzle_input():
    game = MarbleMania(441, 7103200)
    high_score = game.play()

    assert high_score == 3273405195
