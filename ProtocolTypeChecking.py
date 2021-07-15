from typing_extensions import Protocol

class HasParam(Protocol):
    def param(self) -> str: ...


class HasName(Protocol):
    def name(self) -> str: ...


class Named():
    def name(self) -> str:
        return "I'm Named..."


class Parametered():
    def param(self):
        return "I'm Parametered..."


class NameAndParameter():
    def name(self) -> str:
        return "I'm NameAndParameter and this is my name..."

    def param(self) -> str:
        return "I'm NameAndParameter and this is my parameter..."


def needs_name(nnp: HasName) -> None:
    print(f"needs_name with {type(nnp)}:")
    try:
        print(f"   nnp.name() = '{nnp.name()}'")
    except Exception as e:
        print(f"   Exception w/ name(): {e}")
    try:
        # mypy: "HasName" has no attribute "param"
        # pycharm: Unresolved attribute reference 'param' for class 'HasName'
        print(f"   nnp.param() = '{nnp.param()}'")
    except Exception as e:
        print(f"   Exception w/ param(): {e}")


if __name__ == "__main__":
    print("Starting...\n")

    main_named = Named()
    main_paramed = Parametered()
    main_name_and_param = NameAndParameter()

    needs_name(main_name_and_param)
    print("\n")

    # runtime: Exception w/ param(): 'Named' object has no attribute 'param'
    needs_name(main_named)
    print("\n")

    # mypy: Argument 1 to "needs_name" has incompatible type "Parametered"; expected "HasName"
    # pycharm: Expected type 'HasName', got 'Parametered' instead
    # runtime: Exception w/ name(): 'Parametered' object has no attribute 'name'
    needs_name(main_paramed)
    print("\n")

    flag1 = False
    if flag1:
        named_var = Named()
    else:
        # mypy: Incompatible types in assignment (expression has type "Parametered", variable has type "Named")
        named_var = Parametered()
    # flag1 = True
    #    runtime: Exception w/ param(): 'Named' object has no attribute 'param'
    # flag1 = False
    #    runtime: Exception w/ name(): 'Parametered' object has no attribute 'name'
    needs_name(named_var)

