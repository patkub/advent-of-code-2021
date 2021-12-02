import pytest
from day01 import count_increased, count_increased_part2


def test_example_report():
    with open("./day01/example-report") as f:
        values = [int(line) for line in f.readlines()]
        increased = count_increased(values)
        assert increased == 7


def test_part1():
    with open("./day01/input") as f:
        values = [int(line) for line in f.readlines()]
        increased = count_increased(values)
        assert increased == 1722


def test_part2():
    with open("./day01/input") as f:
        values = [int(line) for line in f.readlines()]
        increased = count_increased_part2(values)
        assert increased == 1748
