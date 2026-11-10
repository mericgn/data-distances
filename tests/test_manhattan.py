from utils.distances import manhattan

def test_manhattan():
    assert manhattan((0, 0), (0, 0)) == 0
    assert manhattan((0, 0), (1, 1)) == 2
    assert manhattan((0, 0), (1, 0)) == 1
    assert manhattan((0, 0), (0, 1)) == 1
    assert manhattan((0, 0), (-1, 0)) == 1
    assert manhattan((0, 0), (0, -1)) == 1
    assert manhattan((0, 0), (-1, -1)) == 2
    assert manhattan((0, 0), (1, -1)) == 2
    assert manhattan((0, 0), (-1, 1)) == 2


def test_manhattan_not_from_origin():
    assert manhattan((1, 1), (4, 5)) == 7
    assert manhattan((-2, 3), (4, -1)) == 10


def test_manhattan_is_symmetric():
    assert manhattan((1, 1), (4, 5)) == manhattan((4, 5), (1, 1))


def test_manhattan_is_never_negative():
    assert manhattan((5, 5), (1, 1)) >= 0
