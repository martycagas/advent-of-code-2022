def eval_move(enemy: str, player: str):
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
            total_score += move_values[player_move]
            total_score += eval_move(enemy_move, player_move)

        # Print out the result
        print(total_score)
