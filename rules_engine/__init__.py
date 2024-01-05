from typing import Callable, Union


def unpack(val: Union[int, 'Variable'], data: dict) -> int:
    if isinstance(val, Variable):
        return val(data)
    return val


class Variable:
    def __init__(self, name: str):
        self._name = name

    def __call__(self, data):
        return data[self._name]

    def __eq__(self, other):
        return Rule(lambda data: self(data) == unpack(other, data))

    def __ne__(self, other):
        return Rule(lambda data: self(data) != unpack(other, data))

    def __gt__(self, other):
        return Rule(lambda data: self(data) > unpack(other, data))

    def __ge__(self, other):
        return Rule(lambda data: self(data) >= unpack(other, data))

    def __lt__(self, other):
        return Rule(lambda data: self(data) < unpack(other, data))

    def __le__(self, other):
        return Rule(lambda data: self(data) <= unpack(other, data))

    def __add__(self, other):
        return CalculatedVariable(lambda data: self(data) + unpack(other, data))

    def __sub__(self, other):
        return CalculatedVariable(lambda data: self(data) - unpack(other, data))

    def __mul__(self, other):
        return CalculatedVariable(lambda data: self(data) * unpack(other, data))

    def __truediv__(self, other):
        return CalculatedVariable(lambda data: self(data) / unpack(other, data))

    def __floordiv__(self, other):
        return CalculatedVariable(lambda data: self(data) // unpack(other, data))

    def __mod__(self, other):
        return CalculatedVariable(lambda data: self(data) % unpack(other, data))

    def __pow__(self, other):
        return CalculatedVariable(lambda data: self(data) ** unpack(other, data))


class CalculatedVariable(Variable):
    def __init__(self, calculation: Callable):
        self._calculation = calculation

    def __call__(self, data):
        return self._calculation(data)


class Rule:
    def __init__(self, callable: Callable):
        self._callable = callable

    def __and__(self, other):
        return Rule(lambda data: self(data) and other(data))

    def __or__(self, other):
        return Rule(lambda data: self(data) or other(data))

    def __xor__(self, other):
        return Rule(lambda data: self(data) != other(data))

    def __call__(self, data):
        result = self._callable(data)
        return result
