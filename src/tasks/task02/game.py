from __future__ import annotations


class Game:
    def __init__(self, game_id: int):
        self.id: int = game_id
        self.max_balls: dict[str, int] = {}

    def set_max_for_balls(self, color: str, number_of_balls: int) -> None:
        if color not in self.max_balls or self.max_balls[color] < number_of_balls:
            self.max_balls[color] = number_of_balls

    def is_possible(self, game: Game) -> bool:
        for ball in game.max_balls.items():
            color: str = ball[0]
            number_of_balls: int = ball[1]
            if color not in self.max_balls or self.max_balls[color] > number_of_balls:
                return False

        return True

    def power_of_set(self) -> int:
        power: int = 1
        for number_of_balls in self.max_balls.values():
            power *= number_of_balls

        return power

    @staticmethod
    def from_str(game_str: str) -> Game:
        split_game: list[str] = game_str.split(": ")

        game_id: int = int(split_game[0][5:])
        game: Game = Game(game_id)

        for turn in split_game[1].split("; "):
            for balls in turn.split(", "):
                number_of_balls: int = int(balls.split(" ")[0])
                color: str = balls.split(" ")[1]

                game.set_max_for_balls(color, number_of_balls)

        return game

    def __str__(self) -> str:
        return f"{self.id}: max_balls: {self.max_balls}"
