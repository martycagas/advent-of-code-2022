try:
    from part1.solution import solution as solution_1
    solution_1('input.txt')
except FileNotFoundError:
    pass

try:
    from part2.solution import solution as solution_2
    solution_2('input.txt')
except FileNotFoundError:
    pass
