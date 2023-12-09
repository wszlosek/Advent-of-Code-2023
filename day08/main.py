import math

from functools import reduce
from utils_py.main import read_file


def build_graph(lines):
    desert_graph = {}
    for line in lines:
        line = line.split(" = ")
        s1 = line[0]
        s2 = line[1].split(", ")[0].replace("(", "")
        s3 = line[1].split(", ")[1].replace(")", "")

        desert_graph[s1] = (s2, s3)

    return desert_graph


def part1(lines):
    desert_graph = build_graph(lines[2:])
    steps = lines[0]
    step_num = 0

    node = "AAA"

    while True:
        for step in steps:
            if step == "L":
                node = desert_graph[node][0]
            elif step == "R":
                node = desert_graph[node][1]

            step_num += 1
            if node == "ZZZ":
                return step_num


def part2(lines):
    desert_graph = build_graph(lines[2:])
    steps = lines[0]
    step_num = 0

    nodes = [node for node in desert_graph if node.endswith("A")]
    nodes_i = [-1] * len(nodes)

    while True:
        for step in steps:
            if step == "L":
                nodes = list(map(lambda node: desert_graph[node][0], nodes))
            elif step == "R":
                nodes = list(map(lambda node: desert_graph[node][1], nodes))

            step_num += 1
            for i, node in enumerate(nodes):
                if node.endswith("Z") and nodes_i[i] == -1:
                    nodes_i[i] = step_num

            if all(i != -1 for i in nodes_i):
                return reduce(math.lcm, nodes_i)


if __name__ == '__main__':
    lines = read_file('input/day08.txt')
    print(part1(lines))
    print(part2(lines))
