# import aoctools
import itertools
import functools
import operator
import numpy as np

class MathsHomework:
    def __init__(self, math_problems: list[str]):
        self.numbers = []
        self.operations = []
        for l in math_problems[:-1]:
            self.numbers.append(list(map(int, filter(lambda x: len(x) > 0, l.split(" ")))))
        self.numbers = list(zip(*self.numbers))
        self.operations = list(map(lambda y: operator.add if y == '+' else operator.mul, 
                                   filter(lambda x: len(x) > 0, test_str1[-1].split(" "))))
        
    def part1_sum(self, _):
        results = []
        for i,op in enumerate(self.operations):
            results.append(functools.reduce(op, self.numbers[i]))
        return sum(results)




def check_test(fn, test_input, expected_result=None):
    result = fn(test_input)
    print(f"{fn.__name__}(): {result}", end="")
    if expected_result is not None:
        print(f" == {expected_result}: {result == expected_result}", end="")
    print()


test_str1 = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".splitlines()

t1 = MathsHomework(test_str1)
check_test(t1.part1_sum, None, 4277556)

maths_work = MathsHomework(open("2025/inputs/day06.txt").read().splitlines())
"""
1725757359 too low"""
check_test(maths_work.part1_sum, None)