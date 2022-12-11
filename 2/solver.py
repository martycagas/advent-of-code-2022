class Solver:
    def __init__(self, file: str) -> None:
        with open(file, 'r') as f:
            # Split the input to lines
            self.input = f.read().strip()

    @staticmethod
    def eval_move(enemy: str, player: str) -> int:
        combined = enemy + player
        match combined:
            case 'AX':
                # Rock and rock
                return 3
            case 'AY':
                # Rock and paper
                return 6
            case 'AZ':
                # Rock and scisors
                return 0
            case 'BX':
                # Paper and rock
                return 0
            case 'BY':
                # Paper and paper
                return 3
            case 'BZ':
                # Paper and scisors
                return 6
            case 'CX':
                # Scisors and rock
                return 6
            case 'CY':
                # Scisors and paper
                return 0
            case 'CZ':
                # Scisors and scisors
                return 3
            case _:
                print(
                    'Make sure the left argumement contains only [ABC] and right one contains only [XYZ]')
                raise ValueError

    @staticmethod
    def decode_move(enemy_move: str, desired_outcome: str) -> str:
        combined = enemy_move + desired_outcome
        # Enemy move:      A = X = rock
        #                  B = Y = paper
        #                  C = Z = Scisors
        # Desired outcome: X = lose
        #                  Y = draw
        #                  Z = win
        match combined:
            case 'AX':
                # Lose against a rock
                return 'Z'
            case 'AY':
                # Draw against a rock
                return 'X'
            case 'AZ':
                # Win against a rock
                return 'Y'
            case 'BX':
                # Lose against a paper
                return 'X'
            case 'BY':
                # Draw against a paper
                return 'Y'
            case 'BZ':
                # Win against a paper
                return 'Z'
            case 'CX':
                # Lose against a scisors
                return 'Y'
            case 'CY':
                # Draw against a scisors
                return 'Z'
            case 'CZ':
                # Win against a scisors
                return 'X'
            case _:
                print(
                    'Make sure the left argumement contains only [ABC] and right one contains only [XYZ]')
                raise ValueError

    def solver_part_one(self) -> int:
        total_score = 0
        # A = X = rock
        # B = Y = paper
        # C = Z = Scisors
        move_values = {'X': 1, 'Y': 2, 'Z': 3}
        # Read the file contents, strip them, split them to lines and iterate over them
        for line in self.input.split('\n'):
            enemy_move, player_move = line.split(' ')
            total_score += move_values[player_move]
            total_score += Solver.eval_move(enemy_move, player_move)
        # Print out the result
        return total_score

    def solver_part_two(self) -> int:
        total_score = 0
        # A = X = rock
        # B = Y = paper
        # C = Z = Scisors
        move_values = {'X': 1, 'Y': 2, 'Z': 3}
        # Read the file contents, strip them, split them to lines and iterate over them
        for line in self.input.split('\n'):
            enemy_move, player_move = line.split(' ')
            player_move = Solver.decode_move(enemy_move, player_move)
            total_score += move_values[player_move]
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
