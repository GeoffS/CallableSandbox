from foo import Foo

class FooImpl(Foo):
    def __init__(self, init_param: str):
        self._init_param = init_param

    def do_some_foo(self, param: str) -> str:
        return f"FooImpl({self._init_param}).do_some_foo({param})"