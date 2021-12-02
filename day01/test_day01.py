import pytest
from day01 import count_increased, count_increased_part2


def test_example_report():
    with open("./day01/example-report") as f:
        increased = count_increased(f)
        assert increased == 7


def test_part1():
    with open("./day01/input") as f:
        increased = count_increased(f)
        assert increased == 1722


def test_part2():
    with open("./day01/input") as f:
        increased = count_increased_part2(f)
        assert increased == 1748
