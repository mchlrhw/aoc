import pytest

from aoc.year_2018.day_07 import find_roots, linearise_steps, parse_steps
from aoc.year_2018.day_07 import InvalidStep, Step
from aoc.year_2018.day_07.data import puzzle_input


def test_invalid_step():
    step_specs = [
        'Invalid',
    ]
    with pytest.raises(InvalidStep):
        parse_steps(step_specs)


def test_parse_steps_example():
    steps_raw = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""
    step_specs = (s.strip() for s in steps_raw.splitlines() if s.strip())

    steps = parse_steps(step_specs)
    expected = {
        'A': Step('A', set(['C']), set(['B', 'D'])),
        'B': Step('B', set(['A']), set(['E'])),
        'C': Step('C', set(), set(['A', 'F'])),
        'D': Step('D', set(['A']), set(['E'])),
        'E': Step('E', set(['B', 'D', 'F']), set()),
        'F': Step('F', set(['C']), set(['E'])),
    }

    assert steps == expected


def test_find_roots_example():
    steps = {
        'A': Step('A', set(['C']), set(['B', 'D'])),
        'B': Step('B', set(['A']), set(['E'])),
        'C': Step('C', set(), set(['A', 'F'])),
        'D': Step('D', set(['A']), set(['E'])),
        'E': Step('E', set(['B', 'D', 'F']), set()),
        'F': Step('F', set(['C']), set(['E'])),
    }

    roots = find_roots(steps)
    expected = set(['C'])

    assert roots == expected


def test_linearised_example():
    steps = {
        'A': Step('A', set(['C']), set(['B', 'D'])),
        'B': Step('B', set(['A']), set(['E'])),
        'C': Step('C', set(), set(['A', 'F'])),
        'D': Step('D', set(['A']), set(['E'])),
        'E': Step('E', set(['B', 'D', 'F']), set()),
        'F': Step('F', set(['C']), set(['E'])),
    }

    linearised, _ = linearise_steps(steps)
    expected = 'CABDFE'

    assert linearised == expected


def test_linearised_puzzle_input():
    step_specs = (s.strip() for s in puzzle_input.splitlines() if s.strip())
    steps = parse_steps(step_specs)
    linearised, _ = linearise_steps(steps)

    assert linearised == 'LFMNJRTQVZCHIABKPXYEUGWDSO'


def test_linearised_with_workers_example():
    steps = {
        'A': Step('A', set(['C']), set(['B', 'D'])),
        'B': Step('B', set(['A']), set(['E'])),
        'C': Step('C', set(), set(['A', 'F'])),
        'D': Step('D', set(['A']), set(['E'])),
        'E': Step('E', set(['B', 'D', 'F']), set()),
        'F': Step('F', set(['C']), set(['E'])),
    }

    linearised, time_taken = linearise_steps(steps, workers=2)
    expected_order = 'CABFDE'
    expected_time = 15

    assert linearised == expected_order
    assert time_taken == expected_time
