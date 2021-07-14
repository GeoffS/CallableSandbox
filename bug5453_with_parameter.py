# Functions can't be passed as callable protocol #5453
# https://github.com/python/mypy/issues/5453

from typing import Protocol


class Caller(Protocol):
    def __call__(self, param: str) -> None: ...


def call(param: str) -> None:
    pass


def func(caller: Caller) -> None:
    pass


func(call)
