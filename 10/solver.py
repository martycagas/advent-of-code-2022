from pathlib import Path


class Solver:
    def __init__(self, file: Path) -> None:
        with file.open() as f:
            self.input: str = f.read().strip()

    def solve_part_one(self) -> int:
        pass

    def solve_part_two(self) -> int:
        pass

    def solve(self) -> None:
        print(self.solve_part_one())
        print(self.solve_part_two())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    solver = Solver(args.input)
    solver.solve()
