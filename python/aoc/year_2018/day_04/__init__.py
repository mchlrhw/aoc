from collections import defaultdict
from datetime import date, datetime
from typing import Iterable, Mapping, Set, Tuple


class InvalidEvent(Exception):
    pass


def parse_log_line(line: str) -> Tuple[datetime, str]:
    timestamp_raw, event = line.split(']')

    timestamp = datetime.strptime(timestamp_raw.strip('['), '%Y-%m-%d %H:%M')

    return timestamp, event.strip()


def parse_shift_start_event(event: str) -> int:
    parts = event.split()
    if parts[0] != 'Guard':
        raise InvalidEvent()
    elif ' '.join(parts[2:]) != 'begins shift':
        raise InvalidEvent()

    try:
        guard_id = int(parts[1].strip('#'))
    except ValueError:
        raise InvalidEvent()

    return guard_id


def compile_schedule(log: Iterable[Tuple[datetime, str]]) \
        -> Mapping[int, Mapping[date, Set[int]]]:

    schedule: defaultdict = defaultdict(lambda: defaultdict(set))

    current_guard = None
    sleep_start = 0

    for timestamp, event in sorted(log):
        d, t = timestamp.date(), timestamp.time()

        if event.endswith('begins shift'):
            current_guard = parse_shift_start_event(event)
        elif event == 'wakes up':
            schedule[current_guard][d].update(range(sleep_start, t.minute))
        elif event == 'falls asleep':
            sleep_start = t.minute
        else:
            raise InvalidEvent()

    return schedule


def find_sleepiest_guard(schedule: Mapping[int, Mapping[date, Set[int]]]) \
        -> int:

    sleep_times: defaultdict = defaultdict(int)

    for guard_id, sleep_schedule in schedule.items():
        for sleep_block in sleep_schedule.values():
            sleep_times[guard_id] += len(sleep_block)

    sleepiest, _ = max(sleep_times.items(), key=lambda i: i[1])

    return sleepiest


def find_sleepiest_minute(sleep_schedule: Mapping[date, Set[int]]) \
        -> int:

    minute_scores: defaultdict = defaultdict(int)

    for sleep_block in sleep_schedule.values():
        for minute in sleep_block:
            minute_scores[minute] += 1

    sleepiest, _ = max(minute_scores.items(), key=lambda i: i[1])

    return sleepiest
