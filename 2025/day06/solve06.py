from typing import LiteralString, Sequence
from aoc_utils import aoc_utils
import functools
import operator
import numpy as np

problem_input = aoc_utils.fetch_and_save(2025, 6)

class MathsHomework:
    def __init__(self, math_problems: Sequence[str|LiteralString]):
        self.numbers = []
        self.operations = []
        for l in math_problems[:-1]:
            self.numbers.append(list(map(int, filter(lambda x: len(x) > 0, l.split(" ")))))
        self.matrix = np.ndarray(np.shape(self.numbers), dtype=np.int64)
        for i,e in enumerate(self.numbers):
            for j,k in enumerate(e):
                self.matrix[i,j] = k
        self.numbers = list(zip(*self.numbers))
        # self.operations = []
        self.operations = list(map(lambda y: operator.add if y == '+' else operator.mul, 
                                   filter(lambda x: len(x) > 0, math_problems[-1].split(" "))))
        print(self.matrix.shape)
        
    def part1_sum(self, _):
        results = []
        for i,op in enumerate(self.operations):
            initial_value = 0 if op == operator.add else 1
            # print(f"{self.matrix[..., i]}  {op}")
            # results.append(functools.reduce(op, self.matrix[..., i], initial_value))
            results.append(functools.reduce(op, self.numbers[i], initial_value))
        return sum(results)




def check_test(fn, test_input, expected_result=None):
    result = fn(test_input)
    print(f"{fn.__name__}(): {result}", end="")
    if expected_result is not None:
        print(f" == {expected_result}: {result == expected_result}", end="")
    print()

test_cases = [
    {
        'level': 1,
        'input': """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """,
        'output': 4277556,
    }
]

test_str1 = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.splitlines()


def answer(inputs="", level=0, test=False):
    homework = MathsHomework(inputs.splitlines())
    return homework.part1_sum(test)


t1 = MathsHomework(test_str1)
check_test(t1.part1_sum, None, 4277556)
# aoc_utils.test(answer, test_cases)
if problem_input is not None:
    maths_work = MathsHomework(problem_input.splitlines())
# """
# 1725757359 too low"""
    check_test(maths_work.part1_sum, None, expected_result=1725757360)