from pathlib import Path
from enum import Enum, auto


class ProcState(Enum):
    READY = auto()
    ADDITION = auto()


class Solver:
    def __init__(self, file: Path) -> None:
        with file.open() as f:
            self.input: list[str] = f.read().splitlines()

    def solve_part_one(self) -> int:
        cycle = 0
        index = 0
        register = 1
        operand: int | None = None
        accumulator = 0
        state = ProcState.READY

        while True:
            cycle += 1

            if cycle == 20:
                accumulator += register * cycle
            elif (cycle - 20) % 40 == 0:
                accumulator += register * cycle

            if state == ProcState.READY:
                try:
                    line = self.input[index]
                    index += 1
                except IndexError:
                    break

                match line.split():
                    case ["noop"]:
                        state = ProcState.READY
                    case ["addx", op]:
                        operand = int(op)
                        state = ProcState.ADDITION
                    case _:
                        raise ValueError(f"Unable to parse a line: {line}!")
            elif state == ProcState.ADDITION:
                if operand:
                    register += operand
                    operand = None
                else:
                    raise RuntimeError(f"Tried to add NULL operand, cycle={cycle}!")
                state = ProcState.READY
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
