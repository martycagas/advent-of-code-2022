class Solver:
    ENEMY_MOVES = ('A', 'B', 'C')
    PLAYER_MOVES = ('X', 'Y', 'Z')
    ENEMY_MOVES_MAP = {'A': 0, 'B': 1, 'C': 2}
    PLAYER_MOVES_MAP = {'X': 0, 'Y': 1, 'Z': 2}
    MOVE_SCORES = (1, 2, 3)
    RESULT_SCORES = (3, 6, 0)

    def __init__(self, file: str) -> None:
        with open(file, 'r') as f:
            self.input = f.read().strip()

    @staticmethod
    def eval_move(enemy_move: str, player_move: str) -> int:
        index = Solver.ENEMY_MOVES_MAP[enemy_move]
        PLAYER_INDEX = Solver.PLAYER_MOVES_MAP[player_move]
        distance = 0
        while index != PLAYER_INDEX and distance < 3:
            distance += 1
            index = (index + 1) % len(Solver.RESULT_SCORES)
        return Solver.RESULT_SCORES[distance]

    @staticmethod
    def decode_move(enemy_move: str, desired_outcome: str) -> str:
        ENEMY_MOVE_INDEX = Solver.ENEMY_MOVES_MAP[enemy_move]
        OUTCOME_MAP = {'X': 2, 'Y': 0, 'Z': 1}
        return Solver.PLAYER_MOVES[(ENEMY_MOVE_INDEX + OUTCOME_MAP[desired_outcome]) % len(Solver.PLAYER_MOVES)]

    def solver_part_one(self) -> int:
        total_score = 0
        for line in self.input.split('\n'):
            enemy_move, player_move = line.split(' ')
            total_score += Solver.MOVE_SCORES[Solver.PLAYER_MOVES_MAP[player_move]]
            total_score += Solver.eval_move(enemy_move, player_move)
        return total_score

    def solver_part_two(self) -> int:
        total_score = 0
        for line in self.input.split('\n'):
            enemy_move, player_move = line.split(' ')
            player_move = Solver.decode_move(enemy_move, player_move)
            total_score += Solver.MOVE_SCORES[Solver.PLAYER_MOVES_MAP[player_move]]
            total_score += Solver.eval_move(enemy_move, player_move)
        return total_score

    def solve(self) -> None:
        print(self.solver_part_one())
        print(self.solver_part_two())


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Advent of Code 2022 day one puzzle solver')
    parser.add_argument('-i', '--input', type=str,
                        required=True, help='The puzzle\'s input file.')
    args = parser.parse_args()
    solver = Solver(args.input)
    solver.solve()
