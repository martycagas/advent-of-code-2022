import sys


class Solver:
    # Tuples of available moves
    ENEMY_MOVES = ('A', 'B', 'C')
    PLAYER_MOVES = ('X', 'Y', 'Z')
    # Translation dictionaries
    ENEMY_MOVES_MAP = {'A': 0, 'B': 1, 'C': 2}
    PLAYER_MOVES_MAP = {'X': 0, 'Y': 1, 'Z': 2}
    # Scoring dictionary, with values defined by the assignment
    MOVE_SCORES = (
        1,  # rock
        2,  # paper
        3  # scisors
    )
    # Result scores, values defined by the assignment
    RESULT_SCORES = (
        3,  # draw
        6,  # win
        0  # loss
    )

    def __init__(self, file: str) -> None:
        with open(file, 'r') as f:
            # Split the input to lines
            self.input = f.read().strip()

    @staticmethod
    def eval_move(enemy_move: str, player_move: str) -> int:
        # The number representation of an enemy move
        index = Solver.ENEMY_MOVES_MAP[enemy_move]
        # The number representation of a player move
        PLAYER_INDEX = Solver.PLAYER_MOVES_MAP[player_move]
        distance = 0
        # Keep incrementing the index until you land on the player move
        # You've now gained the cyclic distance to the player move
        while index != PLAYER_INDEX and distance < 3:
            distance += 1
            index = (index + 1) % len(Solver.RESULT_SCORES)
        # From the cyclic distance, we can now determine the result (and its score)
        return Solver.RESULT_SCORES[distance]

    @staticmethod
    def decode_move(enemy_move: str, desired_outcome: str) -> str:
        # The number representation of an enemy move
        ENEMY_MOVE_INDEX = Solver.ENEMY_MOVES_MAP[enemy_move]
        # The map of desired moves
        OUTCOME_MAP = {'X': 2, 'Y': 0, 'Z': 1}
        # Translate an enemy move to an index and use it as a startpoint
        # Increase that index depending on the desired outcome
        # Select a player move from the PLAYER_MOVES tuple, but don't forget to loop it back to start
        return Solver.PLAYER_MOVES[(ENEMY_MOVE_INDEX + OUTCOME_MAP[desired_outcome]) % len(Solver.PLAYER_MOVES)]

    def solver_part_one(self) -> int:
        total_score = 0
        # Read the file contents, strip them, split them to lines and iterate over them
        for line in self.input.split('\n'):
            enemy_move, player_move = line.split(' ')
            total_score += Solver.MOVE_SCORES[Solver.PLAYER_MOVES_MAP[player_move]]
            total_score += Solver.eval_move(enemy_move, player_move)
        # Print out the result
        return total_score

    def solver_part_two(self) -> int:
        total_score = 0
        # Read the file contents, strip them, split them to lines and iterate over them
        for line in self.input.split('\n'):
            enemy_move, player_move = line.split(' ')
            player_move = Solver.decode_move(enemy_move, player_move)
            total_score += Solver.MOVE_SCORES[Solver.PLAYER_MOVES_MAP[player_move]]
            total_score += Solver.eval_move(enemy_move, player_move)
        # Print out the result
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
