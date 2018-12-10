import re
from dataclasses import dataclass, field
from typing import Dict, Iterable, Mapping, Set, Tuple


STEP_REGEX = re.compile(
    r'Step (?P<tag>[A-Z])'
    r' must be finished before'
    r' step (?P<dependent>[A-Z]) can begin.'
)

WEIGHTS = {t: w for w, t in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)}


class InvalidStep(Exception):
    pass


@dataclass
class Step:
    tag: str
    dependencies: Set[str] = field(default_factory=set)
    dependents: Set[str] = field(default_factory=set)


def parse_steps(step_specs: Iterable[str]) -> Mapping[str, Step]:
    steps: Dict[str, Step] = {}

    for step_spec in step_specs:
        m = STEP_REGEX.match(step_spec)
        if m is None:
            raise InvalidStep()

        tag = m.group('tag')
        dependent_tag = m.group('dependent')

        try:
            step = steps[tag]
            step.dependents.add(dependent_tag)
        except KeyError:
            step = Step(
                tag=tag,
                dependents=set([dependent_tag]),
            )
            steps[tag] = step

    for step in list(steps.values()):
        for dependent_tag in step.dependents:
            try:
                steps[dependent_tag].dependencies.add(step.tag)
            except KeyError:
                dependent = Step(
                    tag=dependent_tag,
                    dependencies=set([step.tag]),
                )
                steps[dependent_tag] = dependent

    return steps


def find_roots(steps: Mapping[str, Step]) -> Set[str]:
    roots = set()
    for step in steps.values():
        if not step.dependencies:
            roots.add(step.tag)
    return roots


def linearise_steps(
        steps: Mapping[str, Step],
        workers: int = 1,
        base_weight: int = 0,
        ) -> Tuple[str, int]:

    work_in_progress: Dict[str, int] = {}
    steps_available = find_roots(steps)
    linearised = ''
    time_taken = 0

    while work_in_progress or steps_available:
        for step in list(sorted(steps_available)):
            if len(work_in_progress) >= workers:
                break
            work_in_progress[step] = WEIGHTS[step] + base_weight
            steps_available.remove(step)

        for step in list(sorted(work_in_progress)):
            work_in_progress[step] -= 1
            if work_in_progress[step]:
                continue

            work_in_progress.pop(step)
            linearised += step

            for dependent in steps[step].dependents:
                dependencies = steps[dependent].dependencies
                if all(d in linearised for d in dependencies):
                    steps_available.add(dependent)

        time_taken += 1

    return linearised, time_taken
