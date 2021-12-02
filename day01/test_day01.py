import pytest
from day01 import count_increased


def test_example_report():
    with open("./day01/example-report") as f:
        increased = count_increased(f)
        assert increased == 7


def test_input():
    with open("./day01/input") as f:
        increased = count_increased(f)
        assert increased == 1722
