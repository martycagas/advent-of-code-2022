from pathlib import Path

class Solver:
    def __init__(self, file: Path) -> None:
        with file.open() as f:
            self.input: str = f.read()
        self.results: list[int] = [0]

    def solve_part_one(self) -> int:
        content_lines = self.input.splitlines()
        for line in content_lines:
            if line == "":
                self.results.append(0)
            else:
                self.results[-1] += int(line)
        return max(self.results)

    def solve_part_two(self) -> int:
        top_three = [0, 0, 0]
        for result in self.results:
            top_three.append(result)
            top_three.sort(reverse=True)
            top_three.pop()
        return sum(top_three)

    def print_solve(self) -> None:
        print(self.solve_part_one())
        print(self.solve_part_two())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    solver = Solver(args.input)
    solver.print_solve()
