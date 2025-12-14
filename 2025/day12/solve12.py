from aoc_utils import aoc_utils

problem_input = aoc_utils.fetch_and_save(2025, 12)

RIGHT = (1,0)
LEFT = (-1,0)
DOWN = (0,1)
UP = (0,-1)

DIRS = [
    RIGHT,
    LEFT,
    DOWN,
    UP,
]

class Present:
    def __init__(self, present_str=""):
        lines = present_str.splitlines()
        self.index = int(lines.pop(0)[:-1])
        self.width = len(lines[0])
        self.height = len(lines)
        self.grid = {}
        for i,line in enumerate(lines):
            for j,ch in enumerate(line):
                self.grid[(i,j)] = ch
    
    def __str__(self) -> str:
        out_str = f"{self.index}:\n"
        for i in range(self.height):
            for j in range(self.width):
                out_str += self.grid[(i,j)]
            out_str += '\n'
        return out_str

class Region:
    def __init__(self, region_str=""):
        l = region_str.split(' ')
        tree = l.pop(0)
        self.width, self.height = list(map(int, tree[:-1].split('x')))
        self.gifts = list(map(int, l))
        self.grid = {}

    def __str__(self):
        out_str = f"{self.width}x{self.height}: " + ' '.join(map(str, self.gifts))
        if len(self.grid):
            out_str += '\n' + self.grid_str()
        return out_str + '\n'

    def grid_str(self):
        out_str = ""
        for i in range(self.width):
            for j in range(self.height):
                out_str += self.grid[(i,j)]
            out_str += '\n'
        return out_str

class TreePresentCavern:
    def __init__(self, summary_str=""):
        self.presents: list[Present] = []
        self.regions: list[Region] = []
        split = summary_str.split('\n\n')
        tree_regions = split.pop()
        for p in split:
            self.presents.append(Present(p))
        for ln in tree_regions.splitlines():
            self.regions.append(Region(ln))
    
    def __str__(self):
        out_str = ""
        for present in self.presents:
            out_str += f"{present}\n"
        for tr in self.regions:
            out_str += str(tr)
        return out_str
        
    def total_regions_fit(self):
        total = 0

        return 0

test_cases = [
    {
        'level': 1,
        'input': """
0:\n###\n##.\n##.\n\n1:\n###\n##.\n.##\n\n2:\n.##\n###\n##.\n\n3:\n##.\n###\n##.\n\n4:\n###\n#..\n###\n\n5:\n###\n.#.\n###\n
4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""[1:],
        'output': '2',
    }
]

def answer(inputs="", level=0, test=None):
    cave = TreePresentCavern(inputs)
    return cave.total_regions_fit()

cove = TreePresentCavern(test_cases[0]['input'])
print(cove)
# aoc_utils.test(answer, test_cases)