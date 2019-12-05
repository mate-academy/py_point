"""Create class to represent point in 2D space."""


class Point:
    """point object"""
    def __init__(self, x_ax, y_ax):
        self.x_ax = x_ax
        self.y_ax = y_ax

    def __repr__(self):
        return f"Point({self.x_ax}, {self.y_ax})"

    def __str__(self):
        return f"({self.x_ax}, {self.y_ax})"

    def __eq__(self, other):
        return self.x_ax == other.x_ax and self.y_ax == self.y_ax

    def __hash__(self):
        return hash(self.x_ax,) ^ hash(self.y_ax)
