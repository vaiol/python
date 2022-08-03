# python3 -m pip install mypy

# Example 1

def func(num: int) -> float:
    return num + 2.5

# print(func(1.2))






# Example 2

class SomeClass:
    pass

class OtherClass:
    def __init__(self, some_object: SomeClass):
        self.some_object = some_object


# some_object = SomeClass()
# other_object = OtherClass(some_object)
# print(other_object)