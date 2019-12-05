"""
docstring
"""


class Point:
    """
    class doc
    """
    def __init__(self, x_cord, y_cord):
        """

        :param x_cord:
        :param y_cord:
        """
        self.x_cord = x_cord
        self.y_cord = y_cord

    def xp_yp(self):
        """

        :return:
        """
        return "({}, {})".format(self.x_cord, self.y_cord)

    def __repr__(self):
        """

        :return:
        """
        return "Point{}".format(self.xp_yp())

    def __str__(self):
        """

        :return:
        """
        return self.xp_yp()

    def __eq__(self, other):
        """

        :param other:
        :return:
        """
        return self.x_cord == other.x_cord and self.y_cord == other.y_cord

    def __hash__(self):
        """

        :return:
        """
        return hash((self.x_cord, self.y_cord))
