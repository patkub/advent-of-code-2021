#!/usr/bin/env python3

import sys


def most_common(List):
    """
    Find most common element in list

    :param lines: List of integers
    :returns: Most common integer
    """
    return max(set(List), key=List.count)


def calc_power_consumption(lines):
    """
    Calculate power consumption

    :param lines: List of lines from file
    :returns: Gamma rate multiplied by epsilon rate
    """
    # gamma rate is most common bits
    gamma_rate_bits = ""

    for i in range(len(lines[0])):
        bit_column = [int(l[i]) for l in lines]
        gamma_rate_bits += str(most_common(bit_column))

    # flip bits to get least common bits for epsilon rate
    epsilon_rate_bits = (
        gamma_rate_bits.replace("1", "2").replace("0", "1").replace("2", "0")
    )

    # convert binary bits to integers
    gamma_rate = int(gamma_rate_bits, 2)
    epsilon_rate = int(epsilon_rate_bits, 2)

    # power consumption is gamma rate multiplied by epsilon rate
    power_consumption = gamma_rate * epsilon_rate

    return power_consumption


if __name__ == "__main__":
    # parse arguments
    if len(sys.argv) < 1:
        print("Usage: ./day03.py input")
        exit(1)

    input_file = sys.argv[1]
    # read file line-by-line
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]

    res = calc_power_consumption(lines)
    print(res)
