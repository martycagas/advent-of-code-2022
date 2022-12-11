class Solver:
    def __init__(self, file: str) -> None:
        with open(file, 'r') as f:
            # Split the input to lines
            self.input = f.read().strip()
            # Prepare the array of results passed in the first step
            self.results = [0]

    def solver_part_one(self) -> int:
        content_lines = self.input.split('\n')
        for line in content_lines:
            if line == '':
                # If the line is empty, append another item to results
                self.results.append(0)
            else:
                # If the line contains a number, add it to the last item in the results
                self.results[-1] += int(line)
        # Return the largest number in the list
        return max(self.results)

    def solver_part_two(self) -> int:
        # Declare the array of the top three results
        top_three = [0, 0, 0]
        # Append each item, sort the list and then remove the lowest one
        # Do this for every result
        for result in self.results:
            top_three.append(result)
            top_three.sort(reverse=True)
            top_three.pop()
        # Return the sum of the top-three list
        return sum(top_three)

    def solve(self) -> None:
        print(self.solver_part_one())
        print(self.solver_part_two())


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Advent of Code 2022 day one puzzle solver')
    parser.add_argument('-i', '--input', type=str,
                        required=True, help='The puzzle\'s input file.')
    args = parser.parse_args()
    solver = Solver(args.input)
    solver.solve()
