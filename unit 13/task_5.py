from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        raise NotImplementedError("Необходимо реализовать метод execute")


class Addition(Strategy):
    def execute(self, a, b):
        return a + b


class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b


class Multiplication(Strategy):
    def execute(self, a, b):
        return a * b


class Division(Strategy):
    def execute(self, a, b):
        return a / b


class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        if self.strategy is None:
            raise ValueError('стратегия не задана')
        return self.strategy.execute(a, b)

calculator = Calculator()

calculator.set_strategy(Addition())
print(calculator.calculate(2, 3))

calculator.set_strategy(Subtraction())
print(calculator.calculate(2, 3))

calculator.set_strategy(Multiplication())
print(calculator.calculate(2, 3))

calculator.set_strategy(Division())
print(calculator.calculate(6, 3))





