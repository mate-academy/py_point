"""Representation of the point in 2D space."""


class Point:
    """Class of the point"""
    def __init__(self, axis_x, axis_y):
        self.axis_x = axis_x
        self.axis_y = axis_y

    def __repr__(self):
        """Defines behavior for when repr() is called
        on an instance of your class
        """
        return '{0}({1}, {2})'.format(
            self.__class__.__name__,
            self.axis_x,
            self.axis_y
        )

    def __str__(self):
        """Defines behavior for when str()
        is called on an instance of your class.
        """
        return '({0}, {1})'.format(
            self.axis_x,
            self.axis_y
        )

    def __eq__(self, other):
        """Defines behavior for the equality operator, =="""
        return (self.axis_x + self.axis_y) == (other.axis_x + other.axis_y)

    def __hash__(self):
        """Defines behavior for when hash() is called
        on an instance of your class.
        """
        return hash(self.axis_x + self.axis_y)
