import string


class Solver:
    class LoopBreakException(Exception):
        pass

    def __init__(self, file: str) -> None:
        with open(file, 'r') as f:
            self.input: str = f.read().strip()

    @staticmethod
    def evaluate_char(char: str) -> int:
        if len(char) != 1:
            raise ValueError(
                f'In: evaluate_char(str) -> int\nError: argument {char} is not a character.')
        if ord('a') <= ord(char) <= ord('z'):
            return ord(char) - ord('a') + 1
        elif ord('A') <= ord(char) <= ord('Z'):
            return ord(char) - ord('A') + 1 + len(string.ascii_uppercase)
        else:
            return 0

    def solve_part_one(self) -> int:
        priority_list = []
        for line in self.input.split():
            compartment_size = len(line) // 2
            try:
                for i in range(compartment_size):
                    for j in range(compartment_size, len(line)):
                        if line[i] == line[j]:
                            priority_list.append(Solver.evaluate_char(line[j]))
                            raise Solver.LoopBreakException
            except Solver.LoopBreakException:
                pass
        return sum(priority_list)

    def solve_part_two(self) -> int:
        input_lines = self.input.split()
        group_list = [input_lines[index:index + 3]
                      for index in range(0, len(input_lines), 3)]
        priority_list = []
        for group in group_list:
            if len(group) != 3:
                continue
            try:
                for i in range(len(group[0])):
                    for j in range(len(group[1])):
                        for k in range(len(group[2])):
                            if group[0][i] == group[1][j] == group[2][k]:
                                priority_list.append(
                                    Solver.evaluate_char(group[0][i]))
                                raise Solver.LoopBreakException
            except Solver.LoopBreakException:
                pass
        return sum(priority_list)

    def solve(self) -> None:
        print(self.solve_part_one())
        print(self.solve_part_two())


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True)
    args = parser.parse_args()
    solver = Solver(args.input)
    solver.solve()
