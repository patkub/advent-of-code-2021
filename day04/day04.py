#!/usr/bin/env python3

import sys


def mark_board_number(boards, n):
    """
    Mark board number by setting it to -1 on all boards

    :param boards: list of boards
    :param n: number to mark
    """
    for i in range(len(boards)):
        for j, row in enumerate(boards[i]):
            for col in range(len(row)):
                if row[col] == n:
                    boards[i][j][col] = -1


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
        # mark number by setting board number to -1
        mark_board_number(boards, numbers[n])

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
