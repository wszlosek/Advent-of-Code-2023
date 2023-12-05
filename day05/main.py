from utils_py.main import read_file


def get_mapped_value(key, possible_values):
    if key in range(possible_values[1], possible_values[1] + possible_values[2] + 1):
        return key - possible_values[1] + possible_values[0]
    else:
        return key


def get_seeds_part1(line):
    return [int(x) for x in line.split("seeds: ")[1].split()]


def get_seeds_part2(line):
    seeds_parameters = [int(x) for x in line.split("seeds: ")[1].split()]
    result_set = set()

    for i in range(0, len(seeds_parameters), 2):
        start, count = seeds_parameters[i], seeds_parameters[i + 1]
        result_set.update(range(start, start + count))

    return list(result_set)


def process_mapping(seeds):
    locations = []
    map_section = False

    for seed in seeds:
        for line in lines:
            if "seeds" in line:
                continue
            elif line.strip() == "":
                map_section = False
            elif "map" in line:
                map_section = True

            elif map_section:
                values = [int(x) for x in line.split()]
                new_seed_value = get_mapped_value(seed, values)
                if seed != new_seed_value:
                    seed = new_seed_value
                    map_section = False

        locations.append(seed)

    return locations


def part01(lines):
    seeds = []
    for line in lines:
        if "seeds" in line:
            seeds = get_seeds_part1(line)
            break

    locations = process_mapping(seeds)
    return min(locations)


def part02(lines):
    seeds = []
    for line in lines:
        if "seeds" in line:
            seeds = get_seeds_part2(line)
            break

    locations = process_mapping(seeds)
    return min(locations)


if __name__ == '__main__':
    lines = read_file('input/day05.txt')
    print(part01(lines))
    print(part02(lines))
