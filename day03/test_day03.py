import pytest
from day03 import most_common, calc_power_consumption, calc_life_support_rating


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


def test_example_life_support_rating():
    with open("./day03/example-input") as f:
        lines = [line.strip() for line in f.readlines()]
        res = calc_life_support_rating(lines)
        assert res == 230


def test_life_support_rating():
    with open("./day03/input") as f:
        lines = [line.strip() for line in f.readlines()]
        res = calc_life_support_rating(lines)
        assert res == 1370737
