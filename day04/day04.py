#!/usr/bin/env python3

import sys
from copy import deepcopy


def mark_all(boards, n, winning_boards_ids=[]):
    """
    Mark board number by setting it to -1 on all boards

    :param boards: list of boards
    :param n: number to mark
    :param winning_boards_ids: list of winning board ids
    """
    # mark number by setting board number to -1
    for i in range(len(boards)):
        if i not in winning_boards_ids:
            mark(boards[i], n)


def mark(board, n):
    """
    Mark board number by setting it to -1

    :param board: board
    :param n: number to mark
    """
    for j, row in enumerate(board):
        for col in range(len(row)):
            if row[col] == n:
                board[j][col] = -1


def check_winner(board):
    """
    Check if board is a winner based on row/column

    :param board: 2d list of lists of integers
    :returns: True if winner, False otherwise
    """
    for row in board:
        if sum(row) == -5:
            return True
    for col in zip(*board):
        if sum(col) == -5:
            return True
    return False


def sum_unmarked(board):
    """
    Sum unmarked numbers in winning board

    :param board: bingo board
    :returns: Sum of unmarked numbers
    """
    # marked numbers are set to -1
    sum = 0
    for i in board:
        for j in i:
            if j != -1:
                sum += j
    return sum


def play_bingo(numbers, boards):
    """
    Play bingo

    :param numbers: bingo numbers to call
    :param boards: list of boards
    :returns: score = sum unmarked * number called
    """
    n, won, score = 0, False, None

    while n < len(numbers) and not won:
        # mark number by setting board number to -1 on all boards
        mark_all(boards, numbers[n])

        # check if a board won
        # row/column sum must be -5
        for i in range(len(boards)):
            if check_winner(boards[i]):
                # won!
                # boards[i] is winner
                won = True

                # print("Called = " + str(numbers[n]))
                sum = sum_unmarked(boards[i])
                # print("Sum unmarked = " + str(sum))

                # sum unmarked * number called
                score = sum * numbers[n]

        n += 1

    return score


def play_bingo_part2(numbers, boards):
    """
    Play bingo

    :param numbers: bingo numbers to call
    :param boards: list of boards
    :returns: score = sum unmarked * number called
    """
    n, score, last_number = 0, None, None

    winning_boards, winning_boards_ids = [], []

    while n < len(numbers):
        # mark number by setting board number to -1
        mark_all(boards, numbers[n], winning_boards_ids)

        # check if a board won
        # row/column sum must be -5
        for i in range(len(boards)):
            if (i not in winning_boards_ids) and check_winner(boards[i]):
                # won!
                # boards[i] is winner
                winning_boards.append(deepcopy(boards[i]))
                winning_boards_ids.append(i)
                last_number = numbers[n]
        n += 1

    last_winner = winning_boards[-1]
    sum = sum_unmarked(last_winner)
    score = sum * last_number

    return score


if __name__ == "__main__":
    # parse arguments
    if len(sys.argv) < 1:
        print("Usage: ./day04.py input")
        exit(1)

    input_file = sys.argv[1]
    # read file line-by-line
    with open(input_file) as f:
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
    print(score)

    boards = list(zip(*(iter(lines),) * 5))
    score = play_bingo_part2(numbers, boards)
    print(score)
