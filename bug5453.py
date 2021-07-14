# Functions can't be passed as callable protocol #5453
# https://github.com/python/mypy/issues/5453

from typing import Protocol


class Caller(Protocol):
    def __call__(self) -> None: ...


def call() -> None:
    pass


def func(caller: Caller) -> None:
    pass


func(call)
