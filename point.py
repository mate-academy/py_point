"""module with class point"""

class Point:
    """class to represent point in 2D space"""
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f"Point({self._x}, {self._y})"

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y

    def __hash__(self):
        return hash(self._x + self._y)
