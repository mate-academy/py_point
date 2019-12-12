"""
module
"""


class Point:
    """
    point
    """
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __str__(self):
        """
        str
        """
        return "({}, {})".format(self.x_coord, self.y_coord)

    def __eq__(self, point):
        """
        eq
        """
        return self.x_coord == point.x_coord and self.y_coord == point.y_coord

    def __repr__(self):
        """
        repr
        """
        return "Point({}, {})".format(self.x_coord, self.y_coord)

    def __hash__(self):
        """
        hash
        """
        return hash(self.x_coord + self.y_coord)
