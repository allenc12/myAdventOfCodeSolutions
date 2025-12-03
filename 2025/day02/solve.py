from collections import Counter
def part1(id_list: list[tuple[int,int]]) -> int:
    invalid_ids = []
    for start, end in id_list:
        for n in range(start, end+1):
            num_str = str(n)
            if num_str[0:len(num_str)//2] == num_str[len(num_str)//2:]:
                invalid_ids.append(n)
    return sum(invalid_ids)

def consecutive_digits(num: int) -> int:
    """beans"""
    numstr = str(num)
    if numstr[0:len(numstr)//2] == numstr[len(numstr)//2:]:
        return num
    return 0

def check_subsequence(num: int) -> int:
    num_str = str(num)
    for i in range(1,len(num_str)):
        splits = [num_str[j:j+i] for j in range(0,len(num_str),i)]
        if len(set(splits)) == 1:
            # print(splits)
            return num
    return 0

def part2(id_list: list[tuple[int,int]]) -> int:
    invalid_ids = []
    for start,end in id_list:
        for n in range(start, end+1):
            if check_subsequence(n):
                invalid_ids.append(n)
    return sum(invalid_ids)

def split_id_range(s: str) -> tuple[int,int]:
    a,b = s.split('-')
    return (int(a), int(b))

def check_test(fn, test_input, expected_result):
    result = fn(test_input)
    print(f"{result=} == {expected_result=} {result == expected_result}")

test1 = [split_id_range(id_range) for id_range in 
         """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124""".split(',')]

check_test(part1, test1, 1227775554)

id_list_input = [split_id_range(id_range) for id_range in open("2025/inputs/day02.txt").read().split(',')]

check_test(part1, id_list_input, 28844599675)
print("===================================================")
check_test(part2, test1, 4174379265)
check_test(part2, id_list_input, 0)