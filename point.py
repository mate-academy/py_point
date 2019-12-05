"""
Create class to represent point in 2D space. Don't use dataclasses.
"""



class Point:
    """Class to represent point in 2D space"""
    def __init__(self, x_axis, y_axic):
        self.x_axis = x_axis
        self.y_axis = y_axic

    def __repr__(self):
        return "Point({}, {})".format(self.x_axis, self.y_axis)

    def __str__(self):
        return "({}, {})".format(self.x_axis, self.y_axis)

    def __eq__(self, other):
        return self.x_axis == other.x_axis and self.y_axis == other.y_axis

    def __hash__(self):
        return hash(self.x_axis)
