import pytest
from day02 import calc_horizontal_depth, calc_horizontal_depth_part2


def test_horizontal_depth():
    with open("./day02/input") as f:
        res = calc_horizontal_depth(f)
        assert res == 1660158


def test_horizontal_depth_part2():
    with open("./day02/input") as f:
        res = calc_horizontal_depth_part2(f)
        assert res == 1604592846
