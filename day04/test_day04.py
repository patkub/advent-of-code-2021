import pytest
from day04 import play_bingo, play_bingo_part2


def test_example():
    with open("./day04/example-input") as f:
        numbers = [int(n) for n in f.readline().split(",")]
        lines = [
            list(map(int, line.strip().split()))
            for line in f.readlines()
            if line.strip()
        ]
        # chunk into groups of 5
        boards = list(zip(*(iter(lines),) * 5))

        # play bingo!
        score = play_bingo(numbers, boards)
        assert score == 4512


def test_input():
    with open("./day04/input") as f:
        numbers = [int(n) for n in f.readline().split(",")]
        lines = [
            list(map(int, line.strip().split()))
            for line in f.readlines()
            if line.strip()
        ]
        # chunk into groups of 5
        boards = list(zip(*(iter(lines),) * 5))

        # play bingo!
        score = play_bingo(numbers, boards)
        assert score == 33348


def test_example_part2():
    with open("./day04/example-input") as f:
        numbers = [int(n) for n in f.readline().split(",")]
        lines = [
            list(map(int, line.strip().split()))
            for line in f.readlines()
            if line.strip()
        ]
        # chunk into groups of 5
        boards = list(zip(*(iter(lines),) * 5))

        # play bingo!
        score = play_bingo_part2(numbers, boards)
        assert score == 1924


def test_input_part2():
    with open("./day04/input") as f:
        numbers = [int(n) for n in f.readline().split(",")]
        lines = [
            list(map(int, line.strip().split()))
            for line in f.readlines()
            if line.strip()
        ]
        # chunk into groups of 5
        boards = list(zip(*(iter(lines),) * 5))

        # play bingo!
        score = play_bingo_part2(numbers, boards)
        assert score == 8112