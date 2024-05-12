from enum import Enum, unique
from pathlib import Path
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


@unique
class Direction(Enum):
    RIGHT = 1, 0
    LEFT = -1, 0
    UP = 0, 1
    DOWN = 0, -1

    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.x = x
        self.y = y


class Rope:
    @staticmethod
    def cap_vector(x: int, y: int) -> Point:
        if x > 1:
            x = 1
        elif x < -1:
            x = -1

        if y > 1:
            y = 1
        elif y < -1:
            y = -1

        return Point(x, y)

    def __init__(self, length: int) -> None:
        if length < 2:
            raise ValueError("Length must be at least 2!")
        self.knots: list[Point] = []
        for _ in range(length):
            self.knots.append(Point(0, 0))
        self.visited: set[Point] = set()
        self.visited.add(self.knots[-1])

    def step(self, dir: Direction) -> None:
        self.knots[0] = Point(self.knots[0].x + dir.x, self.knots[0].y + dir.y)
        for i in range(1, len(self.knots)):
            distance_x = self.knots[i - 1].x - self.knots[i].x
            distance_y = self.knots[i - 1].y - self.knots[i].y
            if abs(distance_x) > 1 or abs(distance_y) > 1:
                dir_vec = Rope.cap_vector(distance_x, distance_y)
                self.knots[i] = Point(
                    self.knots[i].x + dir_vec.x, self.knots[i].y + dir_vec.y
                )
        self.visited.add(self.knots[-1])

    def move(self, dir: Direction, steps: int) -> None:
        for _ in range(steps):
            self.step(dir)


class Solver:
    def __init__(self, file: Path) -> None:
        with file.open() as f:
            self.input: list[str] = f.read().splitlines()

    def solve_part_one(self) -> int:
        rope = Rope(2)
        for line in self.input:
            match line.split():
                case ["R", steps]:
                    rope.move(Direction.RIGHT, int(steps))
                case ["L", steps]:
                    rope.move(Direction.LEFT, int(steps))
                case ["U", steps]:
                    rope.move(Direction.UP, int(steps))
                case ["D", steps]:
                    rope.move(Direction.DOWN, int(steps))
                case _:
                    raise ValueError(f"Unable to parse a line: {line}!")
        return len(rope.visited)

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
