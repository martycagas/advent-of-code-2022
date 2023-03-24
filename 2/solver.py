class Solver:
    ENEMY_MOVES_MAP: dict[str, int] = {"A": 0, "B": 1, "C": 2}
    PLAYER_MOVES_MAP: dict[str, int] = {"X": 0, "Y": 1, "Z": 2}
    MOVE_SCORES: tuple[int] = (1, 2, 3)

    def __init__(self, file: str) -> None:
        with open(file, "r") as f:
            self.input: str = f.read().strip()

    @staticmethod
    def eval_move(enemy_move: str, player_move: str) -> int:
        RESULT_SCORES = (3, 6, 0)
        index = Solver.ENEMY_MOVES_MAP[enemy_move]
        PLAYER_INDEX = Solver.PLAYER_MOVES_MAP[player_move]
        distance = 0
        while index != PLAYER_INDEX and distance < 3:
            distance += 1
            index = (index + 1) % len(RESULT_SCORES)
        return RESULT_SCORES[distance]

    @staticmethod
    def decode_move(enemy_move: str, desired_outcome: str) -> str:
        PLAYER_MOVES = ("X", "Y", "Z")
        ENEMY_MOVE_INDEX = Solver.ENEMY_MOVES_MAP[enemy_move]
        OUTCOME_MAP = {"X": 2, "Y": 0, "Z": 1}
        return PLAYER_MOVES[
            (ENEMY_MOVE_INDEX + OUTCOME_MAP[desired_outcome]) % len(PLAYER_MOVES)
        ]

    def solve_part_one(self) -> int:
        total_score = 0
        for line in self.input.splitlines():
            enemy_move, player_move = line.split(" ")
            total_score += Solver.MOVE_SCORES[Solver.PLAYER_MOVES_MAP[player_move]]
            total_score += Solver.eval_move(enemy_move, player_move)
        return total_score

    def solve_part_two(self) -> int:
        total_score = 0
        for line in self.input.splitlines():
            enemy_move, player_move = line.split(" ")
            player_move = Solver.decode_move(enemy_move, player_move)
            total_score += Solver.MOVE_SCORES[Solver.PLAYER_MOVES_MAP[player_move]]
            total_score += Solver.eval_move(enemy_move, player_move)
        return total_score

    def solve(self) -> None:
        print(self.solve_part_one())
        print(self.solve_part_two())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True)
    args = parser.parse_args()
    solver = Solver(args.input)
    solver.solve()
