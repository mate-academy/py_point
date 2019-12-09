"""Create class to represent point in 2D space. Don't use dataclasses."""


class Point:
    """Class Point represents point in 2D"""
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __repr__(self):
        return 'Point({}, {})'.format(self.point1, self.point2)

    def __eq__(self, cust_object):
        return self.point1 == cust_object.point1 and self.point2 == cust_object.point2

    def __hash__(self):
        return hash((self.point1, self.point2))

    def __str__(self):
        return '({}, {})'.format(self.point1, self.point2)
