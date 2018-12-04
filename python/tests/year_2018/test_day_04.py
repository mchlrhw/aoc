from collections import defaultdict
from datetime import date, datetime

import pytest

from aoc.year_2018.day_04 import compile_schedule
from aoc.year_2018.day_04 import find_sleepiest_guard, find_sleepiest_minute
from aoc.year_2018.day_04 import parse_log_line, parse_shift_start_event
from aoc.year_2018.day_04.data import puzzle_input


@pytest.mark.parametrize(
    'line, expected',
    [
        (
            '[1518-11-01 00:00] Guard #10 begins shift',
            (datetime(1518, 11, 1, 0, 0), 'Guard #10 begins shift'),
        ),
        (
            '[1518-11-01 00:05] falls asleep',
            (datetime(1518, 11, 1, 0, 5), 'falls asleep'),
        ),
        (
            '[1518-11-01 00:25] wakes up',
            (datetime(1518, 11, 1, 0, 25), 'wakes up'),
        ),
    ],
)
def test_parse_log_line_examples(line, expected):
    parsed = parse_log_line(line)

    assert parsed == expected


@pytest.mark.parametrize(
    'event, expected',
    [
        ('Guard #10 begins shift', 10),
        ('Guard #99 begins shift', 99),
    ]
)
def test_parse_shift_start_event_examples(event, expected):
    guard_id = parse_shift_start_event(event)

    assert guard_id == expected


LOG_LINES_EXAMPLE = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
"""


def test_compile_schedule_example():
    log_lines = \
        (parse_log_line(l)
            for l in LOG_LINES_EXAMPLE.splitlines()
            if l.strip())
    schedule = compile_schedule(log_lines)

    expected_10 = defaultdict(date, {
        date(1518, 11, 1): {
            5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 30, 31,
            32, 33, 34, 35, 36, 37, 38,
            39, 40, 41, 42, 43, 44, 45,
            46, 47, 48, 49, 50, 51, 52,
            53, 54,
        },
        date(1518, 11, 3): {
            24, 25, 26, 27, 28,
        },
    })

    expected_99 = defaultdict(date, {
        date(1518, 11, 2): {
            40, 41, 42, 43, 44, 45, 46,
            47, 48, 49,
        },
        date(1518, 11, 4): {
            36, 37, 38, 39, 40, 41, 42,
            43, 44, 45,
        },
        date(1518, 11, 5): {
            45, 46, 47, 48, 49, 50, 51,
            52, 53, 54,
        },
    })

    assert schedule[10] == expected_10
    assert schedule[99] == expected_99


def test_find_sleepiest_guard_example():
    log_lines = \
        (parse_log_line(l)
            for l in LOG_LINES_EXAMPLE.splitlines()
            if l.strip())
    schedule = compile_schedule(log_lines)
    guard_id = find_sleepiest_guard(schedule)

    assert guard_id == 10


@pytest.mark.parametrize(
    'guard_id, expected',
    [
        (10, 24),
        (99, 45),
    ],
)
def test_find_sleepiest_minute_examples(guard_id, expected):
    log_lines = \
        (parse_log_line(l)
            for l in LOG_LINES_EXAMPLE.splitlines()
            if l.strip())
    schedule = compile_schedule(log_lines)
    sleep_schedule = schedule[guard_id]
    minute = find_sleepiest_minute(sleep_schedule)

    assert minute == expected


def test_find_sleepiest_guard_minute_puzzle_input():
    log_lines = \
        (parse_log_line(l)
            for l in puzzle_input.splitlines()
            if l.strip())
    schedule = compile_schedule(log_lines)

    guard_id = find_sleepiest_guard(schedule)
    sleep_schedule = schedule[guard_id]

    minute = find_sleepiest_minute(sleep_schedule)
    result = guard_id * minute

    assert result == 65489
