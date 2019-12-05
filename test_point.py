"""
docstring
"""
import point


def test_repr():
    """

    :return:
    """
    p = point.Point(2, 3)
    assert repr(p) == "Point(2, 3)"


def test_str():
    """

    :return:
    """
    p = point.Point(2, 3)
    assert str(p) == "(2, 3)"


def test_eq():
    """

    :return:
    """
    p1 = point.Point(2, 3)
    p2 = point.Point(2, 3)
    assert p1 == p2


def test_hash():
    """

    :return:
    """
    p = point.Point(2, 3)
    d = {p: 1}
    assert d[p] == 1
