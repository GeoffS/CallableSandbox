from abc import ABC, abstractmethod
from typing import Callable


class Foo(ABC):
    @abstractmethod
    def param(self) -> str:
        pass


class FooImpl(Foo):
    def __init__(self, foo_param: str):
        self._param = foo_param

    def param(self) -> str:
        return self._param


def foo_client(factory: Callable[[str], Foo]) -> str:
    foo = factory("foo_client value-added parameter")
    return f'foo.param() = {foo.param()}'


def foo_factory(foo_param: str) -> Foo:
    return FooImpl(foo_param)


if __name__ == "__main__":
    res1 = foo_client(lambda foo_param: FooImpl(foo_param))
    print(f"lambda factory:   '{res1}'")

    res2 = foo_client(foo_factory)
    print(f"def factory:      '{res2}'")

    res3 = foo_client(FooImpl)
    print(f"Class as factory: '{res3}'")

    print('Done!')
