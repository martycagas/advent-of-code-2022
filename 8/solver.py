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
        best_score = 0
        for y in range(1, self.dimensions.y - 1):
            for x in range(1, self.dimensions.x - 1):
                current_height = self.in_matrix[y][x]
                up = down = left = right = 1

                scan_y = y + 1
                while (scan_y < (self.dimensions.y - 1)) and (
                    current_height > self.in_matrix[scan_y][x]
                ):
                    down += 1
                    scan_y += 1

                scan_y = y - 1
                while (scan_y > 0) and (current_height > self.in_matrix[scan_y][x]):
                    up += 1
                    scan_y -= 1

                scan_x = x + 1
                while (scan_x < (self.dimensions.x - 1)) and (
                    current_height > self.in_matrix[y][scan_x]
                ):
                    right += 1
                    scan_x += 1

                scan_x = x - 1
                while (scan_x > 0) and (current_height > self.in_matrix[y][scan_x]):
                    left += 1
                    scan_x -= 1

                score = up * down * left * right
                if score > best_score:
                    best_score = score

        return best_score

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
