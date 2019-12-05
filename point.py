"""
Module for representing point in 2D space
Classes
-------
Point
"""


class Point:
    """
    Represent a point in 2D space
    """
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def __repr__(self):
        """Modify __repr__ method"""
        return f'Point({self.x_coord}, {self.y_coord})'

    def __str__(self):
        """Modify __str__ method"""
        return f'({self.x_coord}, {self.y_coord})'

    def __eq__(self, other):
        """Modify __eq__ method"""
        return self.x_coord == other.x_coord and self.y_coord == other.y_coord

    def __hash__(self):
        """Modify __hash__ method"""
        return hash((self.x_coord, self.y_coord))
