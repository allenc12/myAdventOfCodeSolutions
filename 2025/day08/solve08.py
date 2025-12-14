from aoc_utils import aoc_utils
from collections import defaultdict

problem_input = aoc_utils.fetch_and_save(2025, 8)

class JunctionBoxGrid:
    def __init__(self, input_str=""):
        self.grid = defaultdict(str)
        for i,l in enumerate(input_str.splitlines()):
            if ':' in l:
                l, idx = l.split(': ')
            xyz = tuple(map(int, l.split(',')))
            self.grid[xyz] += str(i)
    
    def __str__(self) -> str:
        out_str = ""
        for k,v in self.grid.items():
            out_str += f"{','.join(map(str, k))}" + f": {v}\n" if v else "\n"
        return out_str
    
    def find_circuits(self) -> int:
        circuits = [0]*3
        return circuits[0] * circuits[1] * circuits[2]

test_cases = [
    {
        'level': 1,
        'input': """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""[1:],
        'output': '40',
    }
]

def answer(inputs="", level=0, test=None):
    junctions = JunctionBoxGrid(inputs)
    return junctions.find_circuits()

junctions = JunctionBoxGrid(test_cases[0]['input'])
print(junctions)
# aoc_utils.test(answer, test_cases)