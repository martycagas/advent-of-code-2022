from pathlib import Path
from typing import NamedTuple


class Dimensions(NamedTuple):
    x: int
    y: int


class Solver:
    def __init__(self, file: Path) -> None:
        with file.open() as f:
            input: str = f.read()

        self.in_matrix = [[int(x) for x in row] for row in input.splitlines()]
        self.dimensions = Dimensions(len(self.in_matrix[0]), len(self.in_matrix))

    def solve_part_one(self) -> int:
        vis_matrix = [[False for _ in row] for row in self.in_matrix]

        for y in range(self.dimensions.y):
            highest = -1
            for x in range(self.dimensions.x):
                if self.in_matrix[y][x] > highest:
                    vis_matrix[y][x] = True
                    highest = self.in_matrix[y][x]

        for y in range(self.dimensions.y):
            highest = -1
            for x in reversed(range(self.dimensions.x)):
                if self.in_matrix[y][x] > highest:
                    vis_matrix[y][x] = True
                    highest = self.in_matrix[y][x]

        for x in range(self.dimensions.x):
            highest = -1
            for y in range(self.dimensions.y):
                if self.in_matrix[y][x] > highest:
                    vis_matrix[y][x] = True
                    highest = self.in_matrix[y][x]

        for x in range(self.dimensions.x):
            highest = -1
            for y in reversed(range(self.dimensions.y)):
                if self.in_matrix[y][x] > highest:
                    vis_matrix[y][x] = True
                    highest = self.in_matrix[y][x]

        accumulator = 0
        for y in range(self.dimensions.y):
            for x in range(self.dimensions.x):
                if vis_matrix[y][x] == True:
                    accumulator += 1

        return accumulator

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
