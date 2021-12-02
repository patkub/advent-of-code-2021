#!/usr/bin/env python3

import sys


def count_increased(f):
    # how many measurements increased
    increased = 0
    # read first line
    previous = int(f.readline().strip())
    # read the rest of the file line-by-line
    for line in f:
        current = int(line.strip())
        if current > previous:
            increased += 1
        previous = current
    return increased


def count_increased_part2(f):
    # how many measurements increased in three-measurement sliding window
    increased = 0
    values = [int(line) for line in f.readlines()]

    for i in range(2, len(values) - 1, 1):
      #print(str(values[i - 2]) + ", " + str(values[i - 1]) + ", " + str(values[i]))
      #print(str(values[i - 1]) + ", " + str(values[i]) + ", " + str(values[i + 1]) + "\n")
      window1 = values[i - 2] + values[i - 1] + values[i]
      window2 = values[i - 1] + values[i] + values[i + 1]
      if window2 > window1:
        increased += 1

    return increased

if __name__ == "__main__":
    # parse arguments
    if len(sys.argv) < 1:
        print("Usage: ./day01.py input")
        exit(1)

    input_file = sys.argv[1]
    with open(input_file) as f:
        increased = count_increased(f)
        print(increased)
        f.seek(0)
        increased = count_increased_part2(f)
        print(increased)
