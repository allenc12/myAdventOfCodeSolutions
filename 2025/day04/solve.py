from collections import defaultdict
from aoc_utils import aoc_utils

problem_input = aoc_utils.fetch_and_save(2025, 4)

ADJACENT8 = [
    [0,1],[1,0],[-1,0],[0,-1],
    [1,1],[-1,1],[1,-1],[-1,-1],
]

def strlist_to_grid(strlist: list[str]) -> defaultdict[(int,int, str)]:
    grid = defaultdict(str)
    for y, line in enumerate(strlist):
        for x, ch in enumerate(line):
            grid[(x,y)] = ch
    return grid

def count_adjacent_rolls(grid: defaultdict, x: int, y: int, ch: str) -> int:
    total_adjacent = 0
    for dx, dy in ADJACENT8:
        if grid[(x+dx, y+dy)] == ch:
            total_adjacent += 1
    return total_adjacent

def part1(input_map: list[str]):
    fewer_than_four_adj = 0
    grid = strlist_to_grid(input_map)
    for y in range(len(input_map)):
        for x in range(len(input_map[0])):
            if grid[(x,y)] == '@':
                if count_adjacent_rolls(grid, x, y, '@') < 4:
                    fewer_than_four_adj += 1
    return fewer_than_four_adj


def fewer_than_adj_coords(grid, xmax, ymax, ch, num) -> list[tuple[int,int]]:
    coords = []
    for y in range(ymax):
        for x in range(xmax):
            if grid[(x,y)] == '@':
                if count_adjacent_rolls(grid, x, y, ch) < num:
                    coords.append((x,y))
    return coords


def part2(input_map: list[str]):
    grid = strlist_to_grid(input_map)
    ymax = len(input_map)
    xmax = len(input_map[0])
    total_rolls = 0
    while True:
        to_remove = fewer_than_adj_coords(grid, xmax, ymax, '@', 4)
        if len(to_remove) < 1:
            break
        total_rolls += len(to_remove)
        for coord in to_remove:
            grid[coord] = '.'
    return total_rolls


def check_test(fn, test_input, expected_result=None):
    result = fn(test_input)
    print(f"{fn.__name__}(): {result}", end="")
    if expected_result is not None:
        print(f" == {expected_result}: {result == expected_result}", end="")
    print()


test_map = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".splitlines()

paper_roll_map = problem_input.splitlines()
check_test(part1, test_map, 13)
check_test(part1, paper_roll_map)

print("-=-=-=-=-=-=-=-")
check_test(part2, test_map, 43)
check_test(part2, paper_roll_map)
