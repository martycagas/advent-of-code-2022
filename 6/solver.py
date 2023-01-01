from collections import deque


class Solver:
    class CharBuffer:
        def __init__(self, max_len: int = 4) -> None:
            self.buffer: deque[str] = deque('', max_len)

        def __str__(self) -> str:
            ret_str = ''
            for char in self.buffer:
                ret_str += char
            return ret_str

        def push_char(self, char: str) -> None:
            if len(char) == 1:
                self.buffer.append(char)
            else:
                raise ValueError

        def are_all_chars_unique(self) -> bool:
            buffer_as_str = str(self)
            for i in range(len(buffer_as_str)):
                comp_string = buffer_as_str[:i] + buffer_as_str[i + 1:]
                if buffer_as_str[i] in comp_string:
                    return False
            else:
                return True

    def __init__(self, file: str) -> None:
        with open(file, 'r') as f:
            self.input: str = f.read().strip()

    def solver_part_one(self, buffer_len: int = 4) -> int:
        counter: int = buffer_len - 1
        buffer: Solver.CharBuffer = Solver.CharBuffer(buffer_len)
        for char in self.input[:buffer_len - 1]:
            buffer.push_char(char)
        for char in self.input[buffer_len - 1:]:
            buffer.push_char(char)
            counter += 1
            if buffer.are_all_chars_unique():
                return counter

    def solver_part_two(self) -> int:
        pass

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
