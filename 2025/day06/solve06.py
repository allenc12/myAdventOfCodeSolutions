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
        self.matrix = None
        self.math_problems = math_problems
    
    def part1_parse(self):
        for l in self.math_problems[:-1]:
            self.numbers.append(list(map(int, filter(lambda x: len(x) > 0, l.split(" ")))))
        self.matrix = np.ndarray(np.shape(self.numbers), dtype=np.int64)
        for i,e in enumerate(self.numbers):
            for j,k in enumerate(e):
                self.matrix[i,j] = k
        self.numbers = list(zip(*self.numbers))
        # self.operations = []
        self.operations = list(map(lambda y: operator.add if y == '+' else operator.mul, 
                                   filter(lambda x: len(x) > 0, self.math_problems[-1].split(" "))))
        print(self.matrix.shape)
        pass


    def part1_sum(self, _):
        self.part1_parse()
        results = []
        for i,op in enumerate(self.operations):
            initial_value = 0 if op == operator.add else 1
            # print(f"{self.matrix[..., i]}  {op}")
            # results.append(functools.reduce(op, self.matrix[..., i], initial_value))
            results.append(functools.reduce(op, self.numbers[i], initial_value))
        return sum(results)
    
    def part2_sum(self, _):
        """
        right to left in columns, msd at top, lsd at bottom
        64
        23
        314
        becomes 4 431 623
        """
        # for i in range(1000, 0, -1):
        length = 1000
        if len(self.math_problems[0] < 16):
            length = 4
        h_offset = 0
        columns = []
        for i in range(length):
            h_end = h_offset + 1
            # use operator row as a guide for column width
            while self.math_problems[-1][h_end] == ' ':
                h_end += 1
            if length == 4:
                # example input? why did I put this here
                pass
            else:
                column = []
                for j in range(len(self.math_problems)):
                    column.append(self.math_problems[j][h_offset:h_end])
            columns.append(column)
            # ok now we need to parse the columns :|
        pass




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