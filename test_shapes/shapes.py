from math import pi, sqrt
from .shape import Shape

def register_shapes(registry):
    @registry.register("circle")
    class Circle(Shape):
        def __init__(self, radius: float):
            if radius <= 0:
                raise ValueError("Radius must be positive")
            self.radius = radius

        def area(self) -> float:
            return pi * self.radius ** 2

    @registry.register("triangle")
    class Triangle(Shape):
        def __init__(self, a: float, b: float, c: float):
            sides = sorted([a, b, c])
            if any(s <= 0 for s in sides):
                raise ValueError("Sides must be positive")
            if sides[0] + sides[1] <= sides[2]:
                raise ValueError("Triangle inequality violated")
            self.a, self.b, self.c = sides

        def area(self) -> float:
            s = (self.a + self.b + self.c) / 2
            return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

        def is_right(self) -> bool:
            # Какая точность для сравнения a^2 + b^2 = c^2 считается допустимой?
            # Нужно ли параметризовать эту точность?
            a, b, c = self.a, self.b, self.c
            return abs(c**2 - (a**2 + b**2)) < 1e-9
