#!/usr/bin/env python3

import sys


def calc_horizontal_depth(lines):
    """
    Calculate horizontal depth

    :param lines: List of lines from file
    :returns: Horizontal position multiplied by final depth
    """
    horizontal, depth = 0, 0

    for line in lines:
        command = line.strip().split(" ")
        # command = ["forward", "5"]
        if len(command) >= 2:
            units = int(command[1])
            if command[0] == "forward":
                horizontal += units
            elif command[0] == "down":
                depth += units
            elif command[0] == "up":
                depth -= units

    # final horizontal position multiplied by final depth
    return horizontal * depth


def calc_horizontal_depth_part2(lines):
    """
    Calculate horizontal depth with aim

    :param lines: List of lines from file
    :returns: Horizontal position multiplied by final depth
    """
    horizontal, depth, aim = 0, 0, 0

    for line in lines:
        command = line.strip().split(" ")
        # command = ["forward", "5"]
        if len(command) >= 2:
            units = int(command[1])
            if command[0] == "forward":
                # increases horizontal position by X units
                horizontal += units
                # increases depth by "aim * X" units
                depth += aim * units
            elif command[0] == "down":
                # increases aim by X units
                aim += units
            elif command[0] == "up":
                # decreases aim by X units
                aim -= units

    # final horizontal position multiplied by final depth
    return horizontal * depth


if __name__ == "__main__":
    # parse arguments
    if len(sys.argv) < 1:
        print("Usage: ./day02.py input")
        exit(1)

    input_file = sys.argv[1]
    # read file line-by-line
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]

    res = calc_horizontal_depth(lines)
    print(res)

    res = calc_horizontal_depth_part2(lines)
    print(res)
