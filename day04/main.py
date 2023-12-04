from utils_py.main import read_file


def get_winning_and_player_numbers(game):
    line = game.split(": ")[1].split(" | ")
    winning_numbers = [int(x) for x in line[0].split() if x.isdigit()]
    player_numbers = [int(x) for x in line[1].split() if x.isdigit()]
    return winning_numbers, player_numbers


def get_card_number(card):
    return int(card.split("Card ")[1].split(":")[0])


def part01(games):
    result = 0
    for game in games:
        winning_numbers, player_numbers = get_winning_and_player_numbers(game)
        score = len([x for x in player_numbers if x in winning_numbers])
        result += 2 ** (score - 1) if score > 0 else 0

    return result


def part02(games):
    card = [1] * len(games)

    for game in games:
        card_number = get_card_number(game)
        winning_numbers, player_numbers = get_winning_and_player_numbers(game)
        score = len([x for x in player_numbers if x in winning_numbers])
        for j in range(1, score+1):
            card[card_number-1+j] += card[card_number-1]

    return sum(card)


if __name__ == '__main__':
    lines = read_file('input/day04.txt')
    print(part01(lines))
    print(part02(lines))
