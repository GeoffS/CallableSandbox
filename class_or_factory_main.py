from typing import Callable

import class_or_factory
import factory_or_class
from foo import Foo


def foo_client(foo_creator: Callable[[str], Foo], creator_param: str) -> None:
    foo: Foo = foo_creator(creator_param)
    print(foo.do_some_foo("from foo_client()..."))


if __name__ == "__main__":
    foo_client(class_or_factory.FooImpl, 'class_or_factory')
    foo_client(factory_or_class.FooImpl, 'factory_or_class')

    foo1 = class_or_factory.FooImpl("foo1")
    foo2 = factory_or_class.FooImpl("foo2")
    print(f"Not the same instance: foo1 == foo2 = {foo1 == foo2}")
    print(f"Same type: type(foo1) == type(foo2) = {type(foo1) == type(foo2)}")