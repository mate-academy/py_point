"""sqrt func used in calculations"""
from math import sqrt


class Point:
    """Class representing point in 2D space"""
    def __init__(self, x_coord: int, y_coord: int):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def find_distance(self, other_point):
        """
        Calculate distance between two points in 2D space
        :param other_point:
        :return: distance
        """
        return sqrt((other_point.x_coord - self.x_coord) ** 2 +
                    (other_point.y_coord - self.y_coord) ** 2)

    def __repr__(self):
        """
        :return: the Point object representation
        """
        return f"Point({self.x_coord}, {self.y_coord})"

    def __str__(self):
        """
        :return:the string representation of the Point object
        """
        return f"({self.x_coord}, {self.y_coord})"

    def __hash__(self):
        """
        :return: return hash for Point object
        """
        return hash(self.x_coord ** self.y_coord)

    def __eq__(self, other_point):
        """
        Check equality of two points in 2D space
        :param other_point:
        :return: boolean
        """
        return self.x_coord == other_point.x_coord and self.y_coord == other_point.y_coord
