from aoc_utils import aoc_utils
from collections import defaultdict
import re
# import networkx as nx

problem_input = aoc_utils.fetch_and_save(2025, 7)
pattern = r"(\^|S)"
class TachyonManifold:
    def __init__(self, input_diagram=""):
        self.grid = defaultdict(str)
        self.total_splits = 0
        self.current_line = 0
        self.splitters: list[re.Match] = []
        lines = input_diagram.splitlines()
        self.width = len(lines[0])
        self.height = len(lines)
        for i,line in enumerate(lines):
            for j,ch in enumerate(line):
                self.grid[(i,j)] = ch
        for line in lines:
            current_splitters = []
            for match in re.finditer(pattern, line):
                if match.group() == 'S':
                    self.beam_start = match
                current_splitters.append(match)
            self.splitters.append(current_splitters[:])
    
    def __str__(self) -> str:
        out_str = ""
        for i in range(self.height):
            for j in range(self.width):
                out_str += self.grid[(i,j)]
            out_str += '\n'
        return out_str + '\n'
    
    def grid_splitters_indices(self):
        for i in range(0,self.height,2):
            yield i

    def step_beam_simulation(self):
        if self.current_line == 0:
            self.grid[(self.current_line+1, self.beam_start.span()[0])] = '|'
        else:
            for spl in self.splitters[self.current_line]:
                if self.grid[(self.current_line-1,spl.span()[0])] == '|':
                    self.total_splits += 1
                    self.grid[(self.current_line, spl.span()[0]-1)] = '|'
                    self.grid[(self.current_line, spl.span()[0]+1)] = '|'
                    self.grid[(self.current_line+1, spl.span()[0]-1)] = '|'
                    self.grid[(self.current_line+1, spl.span()[0]+1)] = '|'
            for i in range(self.width):
                if self.grid[(self.current_line-1, i)] == '|' and self.grid[(self.current_line, i)] == '.':
                    self.grid[(self.current_line, i)] = '|'
        self.current_line += 1

    def calc_beam_splits(self) -> int:
        while self.current_line < self.height:
            self.step_beam_simulation()
        return self.total_splits
    
    def step_quantum_simulation(self):
        pass


test_cases = [
    {
        'level': 1,
        'input': """.......S.......\n...............\n.......^.......\n...............\n......^.^......\n...............\n.....^.^.^.....\n...............\n....^.^...^....\n...............\n...^.^...^.^...\n...............\n..^...^.....^..\n...............\n.^.^.^.^.^...^.\n...............""",
        'output': '21',
    },
    {
        'level': 2,
        'input': """.......S.......\n...............\n.......^.......\n...............\n......^.^......\n...............\n.....^.^.^.....\n...............\n....^.^...^....\n...............\n...^.^...^.^...\n...............\n..^...^.....^..\n...............\n.^.^.^.^.^...^.\n...............""",
        'output': '40'
    },
    # {
    #     'level': 1,
    #     'input': problem_input[:],
    #     'output': '1630',
    # },
    # {
    #     'level': 2,
    #     'input': problem_input[:],
    #     'output': '40'
    # }
]

def answer(inputs="", level=0, test=None):
    diagram = TachyonManifold(inputs)
    return diagram.calc_beam_splits()

# diag = TachyonManifold(test_cases[0]['input'])
# print(diag)
# diag.calc_beam_splits()
# print(diag)
aoc_utils.test(answer, test_cases)
# diagram1 = TachyonManifold(test_cases[0]['input'])
# check_test(diagram1.calc_beam_splits, expected_result=21)