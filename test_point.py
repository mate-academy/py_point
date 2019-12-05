import point


def test_repr():
    p = point.Point(2, 3)
    assert repr(p) == "Point(2, 3)"


def test_str():
    p = point.Point(2, 3)
    assert str(p) == "(2, 3)"


def test_eq():
    p1 = point.Point(2, 3)
    p2 = point.Point(2, 3)
    assert p1 == p2


def test_hash():
    p = point.Point(2, 3)
    d = {p: 1}
    assert d[p] == 1

