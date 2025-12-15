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
    
    def part2_parse(self):
        length = len(self.math_problems[-1].replace(' ',''))
        h_offset = 0
        self.columns = []
        i = 0
        while i < length:
            h_end = h_offset + 1
            # use operator row as a guide for column width
            while h_end < len(self.math_problems[-1]) and self.math_problems[-1][h_end] == ' ':
                h_end += 1
            column = []
            for j in range(len(self.math_problems)):
                column.append(self.math_problems[j][h_offset:h_end-1])
            h_offset = h_end
            self.columns.append(column[:])
            i+=1
            # ok now we need to parse the columns :|
        # self.matrix = np.ndarray(np.shape(self.columns), dtype=np.int64)
        # for i,e in enumerate(self.numbers):
        #     for j,k in enumerate(e):
        #         self.matrix[i,j] = k
    
    def part2_sum(self, _):
        """
        right to left in columns, msd at top, lsd at bottom
        64
        23
        314
        becomes 4 431 623
        """
        self.part2_parse()
        # for i in range(1000, 0, -1):
        for i,column in enumerate(self.columns):
            problorm = []
            for ii in range(len(column[0])):
                tmp = []
                for k in range(len(column)-1):
                    tmp.append(column[k][ii])
                problorm.append(tmp)
            column = list(map(lambda x: int(''.join(x)), problorm)) + [column[-1].strip()]
            res = 0 if column[-1] == '+' else 1
            op = operator.add if column[-1] == '+' else operator.mul
            for j in range(1,len(column)-1):
                res = op(res, column[j])
        return res




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
check_test(t1.part2_sum, None, 3263827)
# aoc_utils.test(answer, test_cases)
if problem_input is not None:
    maths_work = MathsHomework(problem_input.splitlines())
# """
# 1725757359 too low"""
    check_test(maths_work.part1_sum, None, expected_result=1725757360)
    check_test(maths_work.part2_sum, None, expected_result=1725757360)