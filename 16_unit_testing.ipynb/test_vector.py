from pytest import raises
from vector import Vector


def test_valid_init():
    v = (1,2)
    assert v.numbers == (1,2)