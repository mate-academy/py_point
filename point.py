"""
Create class to represent point in 2D space. Don't use dataclasses.
"""



class Point:
    """Class to represent point in 2D space"""
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __repr__(self):
        return "Point({}, {})".format(self.x_coordinate, self.y_coordinate)

    def __str__(self):
        return "({}, {})".format(self.x_coordinate, self.y_coordinate)

    def __eq__(self, other):
        return self.x_coordinate == other.x_coordinate and self.y_coordinate == other.y_coordinate

    def __hash__(self):
        return hash((self.x_coordinate, self.y_coordinate))
