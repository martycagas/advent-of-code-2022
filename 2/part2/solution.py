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


def solution(file: str):
    # Open the file
    with open(file, 'r') as f:
        total_score = 0
        # A = X = rock
        # B = Y = paper
        # C = Z = Scisors
        move_values = {'X': 1, 'Y': 2, 'Z': 3}
        # Read the file contents, strip them, split them to lines and iterate over them
        for line in f.read().strip().split('\n'):
            enemy_move, player_move = line.split(' ')
            player_move = decode_move(enemy_move, player_move)
            total_score += move_values[player_move]
            total_score += eval_move(enemy_move, player_move)

        # Print out the result
        print(total_score)
