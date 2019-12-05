'''
Module
'''


class Point:
    '''
    Clas for point
    '''
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __repr__(self):
        return f"Point({self.x_coord}, {self.y_coord})"

    def __str__(self):
        return f"({self.x_coord}, {self.y_coord})"

    def __eq__(self, other):
        return self.x_coord == other.x_coord and self.y_coord == other.y_coord

    def __hash__(self):
        return hash(self.x_coord) + hash(self.y_coord)
