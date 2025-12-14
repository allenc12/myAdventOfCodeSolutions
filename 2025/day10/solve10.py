from aoc_utils import aoc_utils

problem_input = aoc_utils.fetch_and_save(2025, 10)

class Machine:
    def __init__(self, machine_diagram="[.] (0) {{1}}"):
        diagram_list = machine_diagram.split(' ')
        self.lights = diagram_list.pop(0)
        self.joltage_reqs = diagram_list.pop(-1)
        self.buttons = [(diag,) if type(diag) is int else diag for diag in map(eval, diagram_list)]
    
    def __str__(self):
        return f"{self.lights} {' '.join(map(lambda x: str(x).replace(' ', '').replace(',)',')'), self.buttons))} {self.joltage_reqs}"

class ElfFactory:
    def __init__(self, machine_diagrams=""):
        self.machines = []
        for machine in machine_diagrams.splitlines():
            self.machines.append(Machine(machine))

test_cases = [
    {
        'level': 1,
        'input': """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""[1:],
        'output': '2',
    }
]

def answer(inputs="", level=0, test=None):
    pass

mine = ElfFactory(test_cases[0]['input'])
print(mine.machines[0])
# aoc_utils.test(answer, test_cases)