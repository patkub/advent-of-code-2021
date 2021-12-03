import pytest
from day03 import most_common, calc_power_consumption


def test_example_power_consumption():
    with open("./day03/example-input") as f:
        lines = [line.strip() for line in f.readlines()]
        res = calc_power_consumption(lines)
        assert res == 198


def test_power_consumption():
    with open("./day03/input") as f:
        lines = [line.strip() for line in f.readlines()]
        res = calc_power_consumption(lines)
        assert res == 775304
