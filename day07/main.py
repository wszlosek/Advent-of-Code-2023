import functools

from utils_py.main import read_file
from collections import Counter


def game_result(game):
    games_sorted_by_card_occurrences = sorted(Counter(game).values(), reverse=True)
    max_count = games_sorted_by_card_occurrences[0]
    second_max_count = games_sorted_by_card_occurrences[1] if len(games_sorted_by_card_occurrences) > 1 else 0

    if max_count == 5:
        return 7
    elif max_count == 4:
        return 6
    elif max_count == 3 and second_max_count == 2:
        return 5
    elif max_count == 3 and second_max_count == 1:
        return 4
    elif max_count == 2 and second_max_count == 2:
        return 3
    elif max_count == 2 and second_max_count == 1:
        return 2
    else:
        return 1


def sort_rule_part1(s1, s2):
    cards = "AKQJT98765432"
    game1, game2 = s1.split()[0], s2.split()[0]

    if game_result(game1) > game_result(game2):
        return 1
    elif game_result(game1) < game_result(game2):
        return -1
    else:
        for i, j in zip(game1, game2):
            if cards.index(i) < cards.index(j):
                return 1
            elif cards.index(i) > cards.index(j):
                return -1


def game_result_with_joker(game):
    joker_count = game.count("J")
    game = game.replace("J", "")
    games_sorted_by_card_occurrences = sorted(Counter(game).values(), reverse=True)

    if not games_sorted_by_card_occurrences:
        return 7

    max_count = games_sorted_by_card_occurrences[0] + joker_count
    second_max_count = games_sorted_by_card_occurrences[1] if len(games_sorted_by_card_occurrences) > 1 else 0

    if max_count >= 5:
        return 7
    elif max_count == 4:
        return 6
    elif max_count == 3 and second_max_count == 2:
        return 5
    elif max_count == 3 and second_max_count == 1:
        return 4
    elif max_count == 2 and second_max_count == 2:
        return 3
    elif max_count == 2 and second_max_count == 1:
        return 2
    else:
        return 1


def sort_rule_part2(s1, s2):
    cards = "AKQT98765432J"
    game1, game2 = s1.split()[0], s2.split()[0]

    if game_result_with_joker(game1) > game_result_with_joker(game2):
        return 1
    elif game_result_with_joker(game1) < game_result_with_joker(game2):
        return -1
    else:
        for i, j in zip(game1, game2):
            if cards.index(i) < cards.index(j):
                return 1
            elif cards.index(i) > cards.index(j):
                return -1


def part1(lines):
    result = 0
    sorted_games = sorted(lines, key=functools.cmp_to_key(sort_rule_part1))
    for i, game in enumerate(sorted_games):
        result += (i + 1) * int(game.split(" ")[1])

    return result


def part2(lines):
    result = 0
    sorted_games = sorted(lines, key=functools.cmp_to_key(sort_rule_part2))
    for i, game in enumerate(sorted_games):
        result += (i + 1) * int(game.split(" ")[1])

    return result


if __name__ == '__main__':
    lines = read_file('input/day07.txt')
    print(part1(lines))
    print(part2(lines))
