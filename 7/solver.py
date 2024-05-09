from __future__ import annotations

from pathlib import Path


type TreeNode = dict[str, int | TreeNode]


class Solver:
    def __init__(self, file: Path) -> None:
        with file.open() as f:
            self.input: str = f.read().strip()

    def construct_tree(self) -> TreeNode:
        term_output = (item.strip() for item in self.input.splitlines())
        tree: TreeNode = {}

        def construct_node(node: TreeNode):
            nonlocal term_output
            nonlocal tree

            while True:
                line = next(term_output)
                match line.split():
                    case ["$", "ls"]:
                        pass
                    case ["$", "cd", path]:
                        if path == "..":
                            return

                        if path not in node:
                            node[path] = {}

                        construct_node(node[path])  # type: ignore
                    case ["dir", name]:
                        pass
                    case [size, name]:
                        node[name] = int(size)
                    case _:
                        raise ValueError(f"Unable to parse a line: {line}!")

        try:
            construct_node(tree)
        except StopIteration:
            pass

        return tree

    def solve_part_one(self) -> int:
        total_accumulator: int = 0

        def accumulate_sizes(node: TreeNode) -> int:
            nonlocal total_accumulator
            inner_accumulator = 0

            for item in node.values():
                if isinstance(item, int):
                    inner_accumulator += item
                else:
                    inner_accumulator += accumulate_sizes(item)

            if inner_accumulator < 100000:
                total_accumulator += inner_accumulator

            return inner_accumulator

        accumulate_sizes(self.construct_tree())

        return total_accumulator

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
