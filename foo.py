from abc import ABC, abstractmethod

class Foo(ABC):
    @abstractmethod
    def do_some_foo(self, param: str) -> str:
        pass