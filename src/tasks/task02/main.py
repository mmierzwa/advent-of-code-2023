import sys
from game import Game


def main() -> None:
    args = sys.argv[1:]

    if len(args) < 1:
        print("input file name required", file=sys.stderr)
        sys.exit(-1)

    input_filename = args[0]

    total_ids = 0
    total_power = 0

    with open(input_filename, 'r') as input_file:
        base_game_str: str = input_file.readline().rstrip()
        base_game = Game.from_str(base_game_str)

        for l in input_file:
            line_str = l.rstrip()
            game = Game.from_str(line_str)

            if game.is_possible(base_game):
                total_ids += game.id

            total_power += game.power_of_set()

    print(f"total ids: {total_ids}")
    print(f"total power: {total_power}")


if __name__ == '__main__':
    main()
