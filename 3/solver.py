import string


class Solver:
    def __init__(self, file: str) -> None:
        with open(file, 'r') as f:
            self.input = f.read().strip()
        self.duplicate_list = []
        self.priority_list = []

    @staticmethod
    def evaluate_char(char: str) -> int:
        if len(char) != 1:
            raise ValueError(
                'In: evaluate_char(str) -> int\nError: argument {} is not a character.'.format(char))
        if ord('a') <= ord(char) <= ord('z'):
            return ord(char) - ord('a') + 1
        elif ord('A') <= ord(char) <= ord('Z'):
            return ord(char) - ord('A') + 1 + len(string.ascii_uppercase)
        else:
            return 0

    def solver_part_one(self) -> int:
        for line in self.input.split('\n'):
            compartment_size = len(line) // 2
            match_list = []
            for i in range(compartment_size):
                for j in range(compartment_size, len(line)):
                    if line[i] == line[j]:
                        match_list.append(line[j])
            self.duplicate_list.append(match_list[0])
        for item in self.duplicate_list:
            self.priority_list.append(Solver.evaluate_char(item))
        return sum(self.priority_list)

    def solver_part_two(self) -> int:
        pass

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
