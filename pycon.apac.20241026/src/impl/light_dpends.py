import inspect
import typing
from collections.abc import Callable
from dataclasses import dataclass, field
from functools import wraps
from typing import Annotated


@dataclass
class Depends:
    dependencies: Callable
    use_cache: bool = True


@dataclass
class Dependant:
    call: Callable
    name: str | None = None
    dependencies: list["Dependant"] = field(default_factory=list)
    use_cache: bool = True


@dataclass
class SolvedDependency:
    values: dict


def resolve(f: Callable):
    dependant = get_dependant(call=f)

    @wraps(f)
    def inner(*args, **kwargs):
        solved = solve_dependencies(dependant)
        v = f(*args, **solved.values | kwargs)
        return v

    return inner


def get_dependant(
    call: Callable, name: str | None = None, use_cache: bool = True
) -> Dependant:
    dependant = Dependant(call=call, name=name, use_cache=use_cache)
    sig = inspect.signature(call)
    for name, param in sig.parameters.items():
        depends = analyze_param(name, param.annotation, param.default)
        if depends is not None:
            sub_dependant = get_dependant(
                call=depends.dependencies, name=name, use_cache=depends.use_cache
            )
            dependant.dependencies.append(sub_dependant)
    return dependant


def solve_dependencies(
    dependant: Dependant,
    dependency_cache: dict | None = None,
) -> SolvedDependency:
    values: dict = {}
    dependency_cache = dependency_cache or {}
    for sub_dependant in dependant.dependencies:
        call = sub_dependant.call
        solved_result = solve_dependencies(sub_dependant, dependency_cache)
        if sub_dependant.use_cache and sub_dependant.call in dependency_cache:
            solved = dependency_cache[sub_dependant.call]
        else:
            solved = call(**solved_result.values)

        if sub_dependant.name is not None:
            values[sub_dependant.name] = solved
        if sub_dependant.call not in dependency_cache:
            dependency_cache[sub_dependant.call] = solved

    return SolvedDependency(values=values)


def analyze_param(name, annotation, default_value) -> Depends | None:
    if typing.get_origin(annotation) is Annotated:
        annotated_args = typing.get_args(annotation)
        depends = [d for d in annotated_args[1:] if isinstance(d, Depends)]
        if depends:
            return depends[0]

    if isinstance(default_value, Depends):
        return default_value

    return None

