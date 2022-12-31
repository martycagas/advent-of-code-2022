import re


class Solver:
    class CargoDeck:
        def __init__(self, box_map_string: str) -> None:
            self.cargo: dict[int, list[str]] = {}
            piles: list[str] = box_map_string.splitlines()
            for column_index in re.split('\s+', piles[-1].strip()):
                self.cargo[int(column_index)] = []
            colum_count: int = len(self.cargo)
            for line in piles[:-1]:
                for i in range(colum_count):
                    try:
                        self.cargo[i + 1].append(line[1 + (i * 4)])
                    except IndexError:
                        pass
            for key in self.cargo.keys():
                self.cargo[key] = [
                    item for item in reversed(self.cargo[key]) if item != ' '
                ]

        def __str__(self) -> str:
            output: str = ''
            for key in self.cargo.keys():
                output += '{}: '.format(key)
                for item in self.cargo[key]:
                    output += '[{}] '.format(item)
                output = output.strip() + '\n'
            return output.strip()

        def move(self, how_many: int, where_from: int, where_to: int):
            for _ in range(how_many):
                self.cargo[where_to].append(self.cargo[where_from].pop())

        def move_multiple(self, how_many: int, where_from: int, where_to: int):
            tmp_list: list = []
            for _ in range(how_many):
                try:
                    tmp_list.append(self.cargo[where_from].pop())
                except IndexError:
                    break
            for _ in range(len(tmp_list)):
                self.cargo[where_to].append(tmp_list.pop())

        def get_top_row(self) -> str:
            accumulator_string: str = ''
            for column in self.cargo.values():
                try:
                    accumulator_string += column[-1]
                except IndexError:
                    pass
            return accumulator_string

    def __init__(self, file: str) -> None:
        with open(file, 'r') as f:
            input = re.split('\n\n', f.read().strip())
            self.cargo_input: str = input[0]
            self.moves_input: list[str] = input[1].splitlines()

    def solver_part_one(self) -> int:
        cargo_deck: Solver.CargoDeck = Solver.CargoDeck(self.cargo_input)
        for line in self.moves_input:
            operands = line.strip().split(' ')
            cargo_deck.move(int(operands[1]), int(
                operands[3]), int(operands[5]))
        return cargo_deck.get_top_row()

    def solver_part_two(self) -> int:
        cargo_deck: Solver.CargoDeck = Solver.CargoDeck(self.cargo_input)
        for line in self.moves_input:
            operands = line.strip().split(' ')
            cargo_deck.move_multiple(
                int(operands[1]), int(operands[3]), int(operands[5]))
        return cargo_deck.get_top_row()

    def solve(self) -> None:
        print(self.solver_part_one())
        print(self.solver_part_two())


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True,)
    args = parser.parse_args()
    solver = Solver(args.input)
    solver.solve()
