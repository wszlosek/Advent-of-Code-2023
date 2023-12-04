import math
import re

from utils_py.main import read_file


def part1(data):
    nums, symbols = parse_input(data)
    adj_nums = calculate_adjacent_numbers(nums, symbols)
    return sum(num for num, _ in set(adj_nums))


def part2(data):
    nums, symbols = parse_input(data)
    total_sum = 0

    for pos, symbol in symbols.items():
        if symbol == '*':
            adj_nums = calculate_adjacent_numbers(nums, {pos: symbol}, unique=True)
            if len(adj_nums) == 2:
                total_sum += math.prod(num for num, _ in adj_nums)

    return total_sum


def calculate_adjacent_numbers(nums, symbols, unique=False):
    adj_nums = []
    for pos in symbols:
        r, c = pos
        adj_pos = [(r + x, c + y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
        adj_nums.extend([nums[p] for p in adj_pos if p in nums])
    return set(adj_nums) if unique else adj_nums


def parse_input(data):
    nums = {}
    symbols = {}
    idx_num = 0

    for r, line in enumerate(data):
        parse_line(line, r, nums, symbols, idx_num)

    return nums, symbols


def parse_line(line, row, nums, symbols, idx_num):
    number_positions = [(match.start(), match.group()) for match in re.finditer(r"\d+", line)]
    symbol_positions = [(match.start(), match.group()) for match in re.finditer(r"[^\d\s]", line)]

    for pos, number in number_positions:
        for step in range(len(number)):
            nums[(row, pos + step)] = (int(number), idx_num)
        idx_num += 1

    for pos, symbol in symbol_positions:
        symbols[(row, pos)] = symbol


if __name__ == '__main__':
    lines = read_file('input/day03.txt')
    print(part1(lines))
    print(part2(lines))
