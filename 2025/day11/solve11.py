from aoc_utils import aoc_utils

problem_input = aoc_utils.fetch_and_save(2025, 11)


class Reactor:
    """
    directed (acyclic?) graph
    source: 'you'
    sink:   'out'
    """
    def __init__(self, device_list=""):
        def split_device(s=""):
            name, connections = s.split(': ')
            return name, connections.split(' ')
        
        self.nodes = list()
        self.edges = dict()
        for name, connections in map(split_device, device_list.splitlines()):
            self.nodes.append(name)
            self.edges[name] = connections[:]

    def __str__(self):
        return '\n'.join(map(lambda x: f"{x[0]}: {' '.join(x[1])}", self.edges.items()))
    
    def count_paths_from_source_to_sink(self, source='you', sink='out'):
        total_paths = 0
        
        return total_paths


test_cases = [
    {
        'level': 1,
        'input': """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""[1:],
        'output': '5',
    }
]

def answer(inputs="", level=0, test=None):
    reactor = Reactor(inputs)
    return reactor.count_paths_from_source_to_sink()

react = Reactor(test_cases[0]['input'])
print(react)


# aoc_utils.test(answer, test_cases)