import re
from collections import deque
from dataclasses import dataclass, field
from typing import Iterable, List, Mapping, Set


STEP_REGEX = re.compile(
    r'Step (?P<tag>[A-Z])'
    r' must be finished before'
    r' step (?P<dependent>[A-Z]) can begin.'
)


@dataclass
class Step:
    tag: str
    dependencies: Set[str] = field(default_factory=set)
    dependents: Set[str] = field(default_factory=set)


def parse_steps(step_specs: Iterable[str]) -> Mapping[str, Step]:
    steps = {}

    for step_spec in step_specs:
        m = STEP_REGEX.match(step_spec)
        tag = m.group('tag')
        dependent = m.group('dependent')

        try:
            step = steps[tag]
            step.dependents.add(dependent)
        except KeyError:
            step = Step(
                tag=tag,
                dependents=set([dependent]),
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


def linearise_steps(steps: Mapping[str, Step]) -> List[str]:
    steps_available = find_roots(steps)
    linearised = ''

    while steps_available:
        next_step = list(sorted(steps_available))[0]
        steps_available.remove(next_step)
        linearised += next_step

        for dependent in steps[next_step].dependents:
            dependencies = steps[dependent].dependencies
            if all(d in linearised for d in dependencies):
                steps_available.add(dependent)

    return linearised
