import pytest
from day02 import calc_horizontal_depth, calc_horizontal_depth_part2


def test_example_horizontal_depth():
    with open("./day02/example-input") as f:
        lines = [tuple(line.strip().split()) for line in f.readlines()]
        res = calc_horizontal_depth(lines)
        assert res == 150


def test_example_horizontal_depth_part2():
    with open("./day02/example-input") as f:
        lines = [tuple(line.strip().split()) for line in f.readlines()]
        res = calc_horizontal_depth_part2(lines)
        assert res == 900


def test_horizontal_depth():
    with open("./day02/input") as f:
        lines = [tuple(line.strip().split()) for line in f.readlines()]
        res = calc_horizontal_depth(lines)
        assert res == 1660158


def test_horizontal_depth_part2():
    with open("./day02/input") as f:
        lines = [tuple(line.strip().split()) for line in f.readlines()]
        res = calc_horizontal_depth_part2(lines)
        assert res == 1604592846
