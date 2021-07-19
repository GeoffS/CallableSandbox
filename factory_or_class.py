from foo import Foo
from class_or_factory import FooImpl as FI

def FooImpl(param: str) -> Foo:
    return FI(param)