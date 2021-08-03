from typing import Callable

import class_or_factory
import factory_or_class
from foo import Foo


# This function:
#   1) takes a factory-method parameter,
#   2) uses it to create a 'Foo' instance, and
#   3) calls the 'do_som_foo()' method on the instance.
def foo_client(foo_creator: Callable[[str], Foo], creator_param: str) -> None:
    foo: Foo = foo_creator(creator_param)
    print(foo.do_some_foo("from foo_client()..."))


# The game here is to figure out which 'FooImpl' is a class
# and which is a function-based factory.
# Place your bets...
# (no cheating by looking in the modules...)
if __name__ == "__main__":
    # Call 'foo_client' with two "factory-methods":
    foo_client(class_or_factory.FooImpl, 'class_or_factory')
    foo_client(factory_or_class.FooImpl, 'factory_or_class')
    print("--------------")

    # Create two 'Foo' instances using the two "factory-methods":
    foo1 = class_or_factory.FooImpl("foo1")
    foo2 = factory_or_class.FooImpl("foo2")
    # Check the two instances:
    print(f"Not the same instance: foo1 == foo2 = {foo1 == foo2}")
    print(f"Same type: type(foo1) == type(foo2) = {type(foo1) == type(foo2)}")
    print("--------------")

    # The big reveal:
    print(f"foo1.__module__: {foo1.__module__}")