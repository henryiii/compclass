
import pytest  # only needed for pytest.raises


def square(x):
    return x ** 2


def test_square():
    assert square(2) == 4
    assert square(0) == 0
    assert square(-2) == 4

    with pytest.raises(TypeError):
        square("hi")
