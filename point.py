"""This program initiates a class
with 2 parameters being 2-dimension coordinates"""


class Point:
    """This class represents an object
    with coordinates coordinate_x and coordinate_y"""
    def __init__(self, coordinate_x, coordinate_y):
        """Initiate coordinates of the point"""
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

    def __repr__(self):
        """Show the details on object of the class"""
        return f"Point{self.coordinate_x, self.coordinate_y}"

    def __str__(self):
        """Show the coordinates"""
        return f"{self.coordinate_x, self.coordinate_y}"

    def __eq__(self, other):
        """Check if the object has
        the same coordinates as another object"""
        return self.coordinate_x == other.coordinate_x and self.coordinate_y == other.coordinate_y

    def __hash__(self):
        """Provide unique index for hashing the object"""
        return hash(self.coordinate_x + self.coordinate_y)
