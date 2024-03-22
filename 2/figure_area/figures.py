from abc import ABC, abstractmethod
from math import sqrt, pi


class Figure(ABC):
    ...

    @abstractmethod
    def area(self) -> float:
        ...


class Triangle(Figure):

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        sides = sorted([self.a, self.b, self.c])
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            return (sides[0] * sides[1]) / 2
        else:
            half_perimeter = (self.a + self.b + self.c) / 2
            return sqrt(half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c))


class Circle(Figure):

    def __init__(self, radius: float):
        self.radius = radius


    def area(self) -> float:
        return pi * self.radius ** 2


class Area:
    ...

    def __init__(self, figure: Figure):
        self.figure = figure

    def scalar(self) -> float:
        return self.figure.area()

