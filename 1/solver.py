class Solver:
    def __init__(self, file: str) -> None:
        with open(file, 'r') as f:
            self.input = f.read().strip()
        self.results = [0]

    def solver_part_one(self) -> int:
        content_lines = self.input.split('\n')
        for line in content_lines:
            if line == '':
                self.results.append(0)
            else:
                self.results[-1] += int(line)
        return max(self.results)

    def solver_part_two(self) -> int:
        top_three = [0, 0, 0]
        for result in self.results:
            top_three.append(result)
            top_three.sort(reverse=True)
            top_three.pop()
        return sum(top_three)

    def print_solve(self) -> None:
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
    solver.print_solve()
