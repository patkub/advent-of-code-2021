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


def calc_oxygen_generator_rating(lines):
    """
    Calculate oxygen generator rating

    :param lines: List of lines from file
    :returns: Oxygen generator rating
    """
    # oxygen generator rating
    filtered_lines = lines.copy()
    index = 0
    while len(filtered_lines) > 1 and index < len(filtered_lines[0]):
        bit_column = [int(l[index]) for l in filtered_lines]
        num_zeros = bit_column.count(0)
        num_ones = bit_column.count(1)
        if num_zeros == num_ones:
            # keep 1s
            filtered_lines = [l for l in filtered_lines if int(l[index]) == 1]
        elif num_zeros > num_ones:
            # keep 0s
            filtered_lines = [l for l in filtered_lines if int(l[index]) == 0]
        else:
            # keep 1s
            filtered_lines = [l for l in filtered_lines if int(l[index]) == 1]
        index += 1
    oxygen_generator_rating = int(filtered_lines[0], 2)
    return oxygen_generator_rating


def calc_c02_scrubber_rating(lines):
    """
    Calculate CO2 scrubber rating

    :param lines: List of lines from file
    :returns: CO2 scrubber rating
    """
    # CO2 scrubber rating
    filtered_lines = lines.copy()
    index = 0
    while len(filtered_lines) > 1 and index < len(filtered_lines[0]):
        bit_column = [int(l[index]) for l in filtered_lines]
        num_zeros = bit_column.count(0)
        num_ones = bit_column.count(1)
        if num_zeros == num_ones:
            # keep 0s
            filtered_lines = [l for l in filtered_lines if int(l[index]) == 0]
        elif num_zeros < num_ones:
            # keep 0s
            filtered_lines = [l for l in filtered_lines if int(l[index]) == 0]
        else:
            # keep 1s
            filtered_lines = [l for l in filtered_lines if int(l[index]) == 1]
        index += 1
    c02_scrubber_rating = int(filtered_lines[0], 2)
    return c02_scrubber_rating


def calc_life_support_rating(lines):
    """
    Calculate life support rating

    :param lines: List of lines from file
    :returns: Life support rating
    """
    # life support rating = oxygen generator rating * CO2 scrubber rating
    return calc_oxygen_generator_rating(lines) * calc_c02_scrubber_rating(lines)


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
    res = calc_life_support_rating(lines)
    print(res)
