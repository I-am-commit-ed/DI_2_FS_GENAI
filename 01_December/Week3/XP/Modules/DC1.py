"""
Circle Class — Copy/Paste Ready

Features:
- Define Circle by radius OR diameter (property decorators)
- Query radius/diameter
- Area computation
- __str__/__repr__
- __add__ (add two circles -> new Circle)
- __gt__ (bigger)
- __eq__ (equal)
- __lt__ (sortable)

Bonus (optional):
- Turtle drawing for sorted circles (requires: pip install PythonTurtle)
"""

from __future__ import annotations
import math
from typing import Union


Number = Union[int, float]


class Circle:
    def __init__(self, *, radius: Number = None, diameter: Number = None):
        """
        Create a Circle by providing exactly one of:
        - radius=...
        - diameter=...

        Examples:
            Circle(radius=5)
            Circle(diameter=10)
        """
        if (radius is None) == (diameter is None):
            raise ValueError("Provide exactly one of radius or diameter (not both, not neither).")

        if radius is not None:
            self.radius = radius  # uses the property setter
        else:
            self.diameter = diameter  # uses the property setter

    # -------------------------
    # radius / diameter (decorators)
    # -------------------------
    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: Number) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number (int or float).")
        if value <= 0:
            raise ValueError("radius must be > 0.")
        self._radius = float(value)

    @property
    def diameter(self) -> float:
        return self._radius * 2

    @diameter.setter
    def diameter(self, value: Number) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("diameter must be a number (int or float).")
        if value <= 0:
            raise ValueError("diameter must be > 0.")
        self._radius = float(value) / 2

    # -------------------------
    # core behavior
    # -------------------------
    @property
    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    # -------------------------
    # dunder methods
    # -------------------------
    def __repr__(self) -> str:
        # Clear debug-style representation
        return f"Circle(radius={self.radius:g}, diameter={self.diameter:g}, area={self.area:.4f})"

    def __str__(self) -> str:
        # Friendly printout
        return f"Circle(r={self.radius:g}, d={self.diameter:g})"

    def __add__(self, other: "Circle") -> "Circle":
        if not isinstance(other, Circle):
            return NotImplemented
        # "Add circles" => new circle with radius = sum of radii
        return Circle(radius=self.radius + other.radius)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return False
        # Float-safe comparison
        return math.isclose(self.radius, other.radius, rel_tol=1e-9, abs_tol=0.0)

    def __gt__(self, other: "Circle") -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    def __lt__(self, other: "Circle") -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius


# -------------------------
# Tests / Demo
# -------------------------
if __name__ == "__main__":
    c1 = Circle(radius=3)
    c2 = Circle(diameter=8)     # radius = 4
    c3 = Circle(radius=1.5)
    c4 = Circle(diameter=6)     # radius = 3

    print("Printing circles:")
    print(c1)       # Circle(r=3, d=6)
    print(repr(c2)) # Circle(radius=4, diameter=8, area=...)

    print("\nQuerying radius/diameter:")
    print("c2 radius:", c2.radius)
    print("c2 diameter:", c2.diameter)

    print("\nArea:")
    print("c1 area:", c1.area)

    print("\nAdd circles:")
    c5 = c1 + c2
    print("c1 + c2 =", c5, "| radius:", c5.radius)

    print("\nCompare circles:")
    print("c2 > c1:", c2 > c1)        # True (4 > 3)
    print("c1 == c4:", c1 == c4)      # True (3 == 3)
    print("c3 == c1:", c3 == c1)      # False

    print("\nSort circles:")
    circles = [c1, c2, c3, c4, c5]
    circles_sorted = sorted(circles)  # uses __lt__
    for c in circles_sorted:
        print(c, "| radius:", c.radius)

    # -------------------------
    # Bonus: Draw sorted circles with Turtle (Optional)
    # -------------------------
    # Requires: pip install PythonTurtle
    #
    # Uncomment to try. If you get an import error, install PythonTurtle first.
    #
    # import turtle
    # t = turtle.Turtle()
    # t.speed(0)
    # t.penup()
    # t.goto(-200, 0)
    # t.pendown()
    #
    # # Draw circles left-to-right, scaled for visibility
    # scale = 15  # increase/decrease if too big/small
    # x = -250
    # y = 0
    # for circle in circles_sorted:
    #     r = circle.radius * scale
    #     t.penup()
    #     t.goto(x, y - r)
    #     t.pendown()
    #     t.circle(r)
    #     x += (2 * r) + 30  # spacing
    #
    # turtle.done()
