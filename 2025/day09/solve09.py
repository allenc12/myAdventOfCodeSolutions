from aoc_utils import aoc_utils

problem_input = aoc_utils.fetch_and_save(2025, 9)

class CrimbusBSQ:
    def __init__(self, coordinate_string=""):
        self.coords = []
        for l in coordinate_string.splitlines():
            x,y = l.split(',')
            self.coords.append((int(x), int(y)))

    def find_largest_quad(self):
        max_area = 0
        self.coords.sort()
        return max_area

test_cases = [
    {
        'level': 1,
        'input': """7,1\n11,1\n11,7\n9,7\n9,5\n2,5\n2,3\n7,3""",
        'output': '50',
    }
]

def answer(inputs="", level=0, test=None):
    solver = CrimbusBSQ(inputs)
    return solver.find_largest_quad()


# aoc_utils.test(answer, test_cases)