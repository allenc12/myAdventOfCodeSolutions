import itertools
import functools
from aoc_utils import aoc_utils

problem_input = aoc_utils.fetch_and_save(2025, 3)

digits = [(x,y) for x in range(10) for y in range(10)][::-1]

def find_max_joltage(input_bank: list[int]) -> int:
    for (l,r) in digits:
        try:
            lidx = input_bank.index(l)
            ridx = input_bank.index(r, lidx + 1)
        except:
            continue
        if lidx < ridx:
            return l*10 + r

def part1(input_banks: list[list[int]]) -> int:
    result = 0
    for bank in input_banks:
        tmp = down_down_to_goblin_town(bank, 0, 2)
        result += (tmp[0]*10) + tmp[1]
    return result #sum(map(find_max_joltage, input_banks))


def check_joltage(bank: list[int], jolt: int) -> tuple[list[int], int]:
    if not bank:
        return (bank, jolt)
    cm = max(bank)
    ci = bank.index(cm)
    
def down_down_to_goblin_town(bank: list[int], depth: int, depth_max: int) -> list[int]:
    ret = []
    if len(bank) > 0 and depth < depth_max:
        idx_max = bank.index(max(bank))
        cur = bank[idx_max+1:]
        if len(cur) == 0:
            cur = cur[:idx_max]
        ret += [bank[idx_max]] + down_down_to_goblin_town(cur, depth + 1, depth_max)
    elif depth == depth_max:
        ret.append(max(bank))
    return ret

def find_max_joltage_big(bank: list[int]) -> int:
    max_joltage = 0
    lst = list(enumerate(bank)) # (index, value)
    high_idx = 0
    # take groups of 12 digits?
    # fuggit we do this recursively later
    #return max(map(lambda x: functools.reduce(lambda y,z: y*10 + z, x), itertools.combinations(bank, 12)))
    for high in range(9, 0, -1):
        try:
            high_idx = bank.index(high)
            if high_idx > len(bank)-12:
                continue
            
        except:
            continue
    
    return max_joltage
            


def part2(input_banks: list[list[int]]) -> int:
    """12 digits this time"""
    joltages = []
    for bank in input_banks:
        find_max_joltage_big(bank)
    return sum(joltages)

def lines_to_ints(lines: list[str]) -> list[list[int]]:
    ret = []
    for line in lines:
        ret.append(list(map(int, line)))
    return ret

def check_test(fn, test_input, expected_result=None):
    result = fn(test_input)
    print(f"{fn.__name__}(): {result}", end="")
    if expected_result is not None:
        print(f" == {expected_result}: {result == expected_result}", end="")
    print()


battery_banks = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()
battery_banks = [[int(ch) for ch in line] for line in battery_banks]

escalator_battery_banks = lines_to_ints(problem_input.splitlines())
# print(down_down_to_goblin_town())
check_test(find_max_joltage_big, lines_to_ints(["987654321111111"])[0], 987654321111)

check_test(part1, battery_banks, 357)
check_test(part1, escalator_battery_banks, 16812)
print("==================")


# check_test(part2, battery_banks, 3121910778619)
# check_test(part2, escalator_battery_banks)