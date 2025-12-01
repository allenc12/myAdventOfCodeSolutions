

def part1(lines: list[str]) -> None:
    times_on_zero = 0
    dial_index = 50
    for rotation in lines:
        rotate_by = int(rotation[1:])
        if rotation[0] == 'R':
            dial_index = (dial_index + rotate_by) % 100
            pass
        else: # assume it's 'L'
            dial_index = (dial_index - rotate_by) % 100
        if dial_index == 0:
            times_on_zero += 1
    return times_on_zero



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
print(part1(test1))
