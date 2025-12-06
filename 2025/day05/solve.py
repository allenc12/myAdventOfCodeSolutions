
def part1(id_list: FreshIngredients):
    return id_list.total_fresh_ingredient_ids()


def ranges_overlap(lhs: tuple[int,int], rhs: tuple[int,int]):
    new_range = ()
    """
    (10,14) (12,18)
    
    """
    if lhs[0] <= rhs[0] and lhs[1] <= rhs[1] and lhs[1] >= rhs[0]:
    #     pass
    # if (lhs[0] >= rhs[0] or lhs[0] <= rhs[1]) and \
    #     (lhs[1] >= rhs[1] or lhs[1] <= rhs[1]):
        new_range = (lhs[0], rhs[1])
    return new_range

def part2(id_list: FreshIngredients):
    """
     10151737175303 too low
    371077840399614 too high
    """
    def quick_check(blambo: list[tuple[int,int]]):
        return all(map(lambda x: ranges_overlap(x[0], x[1])==(), [blambo[i:i+2] for i in range(len(blambo)-1)]))
    prev_ranges = []
    total_ids = 0
    cur_ranges = id_list.fresh_id_ranges[::]
    # print(cur_ranges)
    while True:
        if quick_check(cur_ranges):
            break
        if cur_ranges == prev_ranges:
            break
        prev_ranges = cur_ranges[::]
        range_queue = prev_ranges[::]
        cur_ranges = []
        while range_queue:
            first = range_queue.pop(0)
            if len(range_queue) == 0:
                cur_ranges.append(first)
                break
            second = range_queue.pop(0)
            tmp = ranges_overlap(first, second)
            
        # for i in range(1, len(prev_ranges)):
        #     tmp = ranges_overlap(prev_ranges[i-1], prev_ranges[i])
            if tmp:
                cur_ranges.append(tmp)
                continue
            else:
                cur_ranges.append(first)
                range_queue.insert(0,second)
                # cur_ranges.append(second)
        # cur_ranges.append(prev_ranges[-1])
    # print(cur_ranges)
    total_ids = sum(map(lambda x: x[1]-x[0]+1, cur_ranges))
    return total_ids

class FreshIngredients:
    def __init__(self, input_id_list: str):
        ranges, ids = input_id_list.split("\n\n")
        # example range, way too big for set structure: 161774338930928-162461408006849
        # use list of ranges to check ids
        self.fresh_id_ranges = []
        for pair in ranges.splitlines():
            lower,upper = pair.split('-')
            self.fresh_id_ranges.append((int(lower), int(upper)))
            # self.fresh_id_ranges.append(range(int(lower), int(upper)))
        self.fresh_id_ranges.sort()
        self.ids_to_check = list(map(int, ids.splitlines()))
    
    def total_fresh_ingredient_ids(self):
        total = 0
        for id in self.ids_to_check:
            for id_range in self.fresh_id_ranges:
                # an id is fresh if it is contained in _any_ range
                if id >= id_range[0] and id <= id_range[1]:
                    total += 1
                    break
        return total

def check_test(fn, test_input, expected_result=None):
    result = fn(test_input)
    print(f"{fn.__name__}(): {result}", end="")
    if expected_result is not None:
        print(f" == {expected_result}: {result == expected_result}", end="")
    print()


test_str1 = """3-5
10-14
16-20
12-18
4-5
10-11
10-20

1
5
8
11
17
32
"""
test_ingredient_ids = FreshIngredients(test_str1)

ingredient_ids = FreshIngredients(open("2025/inputs/day05.txt").read())


check_test(part1, test_ingredient_ids, 3)
check_test(part1, ingredient_ids)
print("==================")


check_test(part2, test_ingredient_ids, 14)
check_test(part2, ingredient_ids)