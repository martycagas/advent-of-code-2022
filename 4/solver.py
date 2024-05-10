from pathlib import Path
from re import split


class Solver:
    def __init__(self, file: Path) -> None:
        with file.open() as f:
            self.input: str = f.read()
        self.boundaries: list[list[int]] = []
        for line in self.input.splitlines():
            self.boundaries.append([int(i) for i in split(r",|-", line)])

    def solve_part_one(self) -> int:
        fully_contained = 0
        for boundary in self.boundaries:
            first = set(range(boundary[0], boundary[1] + 1))
            second = set(range(boundary[2], boundary[3] + 1))
            if first.issubset(second) or second.issubset(first):
                fully_contained += 1
        return fully_contained

    def solve_part_two(self) -> int:
        overlaps = 0
        for boundary in self.boundaries:
            first = set(range(boundary[0], boundary[1] + 1))
            second = set(range(boundary[2], boundary[3] + 1))
            for item in first:
                if item in second:
                    overlaps += 1
                    break
            else:
                for item in second:
                    if item in first:
                        overlaps += 1
                        break
        return overlaps

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
