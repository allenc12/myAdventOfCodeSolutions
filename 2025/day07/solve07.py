from aoc_utils import aoc_utils
import re
# import networkx as nx

problem_input = aoc_utils.fetch_and_save(2025, 7)
pattern = r"(\^|S)"
class TachyonManifold:
    def __init__(self, input_diagram: str):
        self.splitters = []
        lines = input_diagram.splitlines()
        for line in lines:
            current_splitters = []
            for match in re.finditer(pattern, line):
                if match.group() == 'S':
                    self.beam_start = match
                else:
                    current_splitters.append(match)
            self.splitters.append(current_splitters[:])
    
    def step_beam_simulation(self):
        pass

    def calc_beam_splits(self) -> int:
        return len(self.splitters)


test_cases = [
    {
        'level': 1,
        'input': """.......S.......\n...............\n.......^.......\n...............\n......^.^......\n...............\n.....^.^.^.....\n...............\n....^.^...^....\n...............\n...^.^...^.^...\n...............\n..^...^.....^..\n...............\n.^.^.^.^.^...^.\n...............""",
        'output': '21',
    }
]

def answer(inputs="", level=0, test=None):
    diagram = TachyonManifold(inputs)
    return diagram.calc_beam_splits()


aoc_utils.test(answer, test_cases)
# diagram1 = TachyonManifold(test_cases[0]['input'])
# check_test(diagram1.calc_beam_splits, expected_result=21)