import pytest
from day02 import calc_horizontal_depth

def test_input():
    with open("./day02/input") as f:
        res = calc_horizontal_depth(f)
        assert res == 1660158