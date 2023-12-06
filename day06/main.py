import math

from utils_py.main import read_file


def calculate(time, distance):
    sqrt_delta = (time * time - 4 * distance) ** 0.5
    return math.floor((time - sqrt_delta) / 2) + 1, math.ceil((time + sqrt_delta) / 2) - 1


def part1(lines):
    result = 1
    times = [int(x) for x in lines[0].split("Time:")[1].strip().split()]
    distances = [int(x) for x in lines[1].split("Distance:")[1].strip().split()]

    for (time, distance) in zip(times, distances):
        min_x, max_x = calculate(time, distance)
        diff = max_x - min_x + 1
        result *= diff
    return result


def part2(lines):
    time = int(lines[0].split("Time:")[1].replace(" ", ""))
    distance = int(lines[1].split("Distance:")[1].replace(" ", ""))

    min_x, max_x = calculate(time, distance)
    return max_x - min_x + 1


if __name__ == '__main__':
    lines = read_file('input/day06.txt')
    print(part1(lines))
    print(part2(lines))
