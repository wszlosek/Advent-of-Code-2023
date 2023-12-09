from utils_py.main import read_file

import numpy as np


def part1(histories):
    total_sum = 0
    for history in histories:
        numbers = [int(x) for x in history.split()]

        while any(numbers):
            total_sum += numbers[-1]
            numbers = list(np.diff(numbers))

    return total_sum


def part2(histories):
    total_sum = 0
    for history in histories:
        first_numbers = []
        numbers = [int(x) for x in history.split()]

        while any(numbers):
            first_numbers.append(numbers[0])
            numbers = list(np.diff(numbers))

        for i in range(len(first_numbers)-2, -1, -1):
            first_numbers[i] -= first_numbers[i+1]

        total_sum += first_numbers[0]

    return total_sum


if __name__ == '__main__':
    lines = read_file('input/day09.txt')
    print(part1(lines))
    print(part2(lines))
