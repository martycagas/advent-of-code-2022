class Solver:
    def __init__(self, file: str) -> None:
        with open(file, 'r') as f:
            self.input: str = f.read().strip()

    def solve_part_one(self) -> int:
        pass

    def solve_part_two(self) -> int:
        pass

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
