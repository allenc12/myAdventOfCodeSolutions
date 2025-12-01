import operator

def part1(lines: list[str]) -> int:
    times_on_zero = 0
    dial_index = 50
    for rotation in lines:
        rotate_by = int(rotation[1:])
        if rotation[0] == 'R':
            dial_index = (dial_index + rotate_by) % 100
        else: # assume it's 'L'
            dial_index = (dial_index - rotate_by) % 100
        if dial_index == 0:
            times_on_zero += 1
    return times_on_zero

def part2(lines: list[str]) -> int:
    times_passed_zero = 0
    dial_index = 50
    new_index = 0
    for rotation in lines:
        rotate_by = int(rotation[1:])
        times_passed_zero += int(rotate_by / 100)
        rotate_by %= 100
        if rotation[0] == 'R':
            new_index = (dial_index + rotate_by)
        else: # assume it's 'L'
            new_index = (dial_index - rotate_by)
        if new_index == 100 or new_index == 0:
            times_passed_zero += 1
        dial_index = new_index % 100
    return times_passed_zero


# def part2_gubgar_method(lines: list[str]) -> int:
#     ret = 0
#     idx = 50
#     rot = None
#     for l in lines:
#         d,v = l[0], int(l[1:])
#         if d == "R":
#             rot = operator.add
#         else:
#             rot = operator.sub
        

test1 = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()
print("test 1 (expect 3): ", part1(test1))

puzzle_input = open("2025/inputs/day01.txt").read().splitlines()
print("part 1: ", part1(puzzle_input))

test2 = """R1000
L1050
L50""".splitlines()

incorrect = [
    5900,
    6294,
    2496,
    4868
]

print("part2(test1) (expect 6): ", part2(test1))
print("part2(test2) (expect 22): ", part2(test2))
print("part 2: ", part2(puzzle_input))