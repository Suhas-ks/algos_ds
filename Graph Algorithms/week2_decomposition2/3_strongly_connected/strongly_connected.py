# Uses python3
import sys, threading

sys.setrecursionlimit(10 ** 8)  # max depth of recursion
threading.stack_size(2 ** 28)  # new thread will get stack of such size

class Graph(object):
    class Vertex(object):
        def __init__(self, value):
            self.value = value
            self.visited = False
            self.pre = None
            self.post = None
            self.component_id = None

        def __str__(self):
            return str(self.value)

        def __int__(self):
            return int(self.value)

        def __index__(self):
            return self.__int__()

        def __float__(self):
            return float(self.value)

        def __eq__(self, other):
            # return self.value == other.value and self.component_id == other.component_id
            return self.value == other.value

        def __ne__(self, other):
            # return self.value != other.value and self.component_id != other.component_id
            return self.value != other.value

        def __lt__(self, other):
            return self.value < other.value

        def __le__(self, other):
            return self.value <= other.value

        def __gt__(self, other):
            return self.value > other.value

        def __ge__(self, other):
            return self.value >= other.value

        def __hash__(self):
            return hash(self.value)

        def __repr__(self):
            return str(self)

    def __init__(self):
        self.nodes = {}
        self.clock = 0
        self.component_marker = 0
        self.components = 0

    def previsit(self, v):
        v.pre = self.clock
        self.clock += 1

    def postvisit(self, v):
        v.post = self.clock
        self.clock += 1

    def explore(self, v):
        v.visited = True
        self.previsit(v)
        v.component_id = self.component_marker
        for nbr in self.nodes[v]:
            if not nbr.visited:
                self.explore(nbr)
        self.postvisit(v)

    def reverse(self):
        self.nodes_rev = {}
        for node in self.nodes:
            self.nodes_rev[node] = []
        for node in self.nodes:
            for nbr in self.nodes[node]:
                self.nodes_rev[nbr].append(node)
        self.nodes = self.nodes_rev
        del self.nodes_rev

    def depth_first_search(self):
        self.reset_visit_flags()
        for node in self.nodes.keys():
            if not node.visited:
                self.explore(node)
                self.component_marker += 1
        self.components = self.component_marker
        self.component_marker = 0
        self.clock = 0

    def topological_sort(self):
        self.depth_first_search()
        self.rev_topo = sorted(self.nodes.keys(), key=lambda x: x.post, reverse=True)

    def reset_visit_flags(self):
        for node in self.nodes:
            node.visited = False

    def strong_cc(self):
        self.topological_sort()
        self.reverse()
        self.reset_visit_flags()
        for node in self.rev_topo:
            if not node.visited:
                self.explore(node)
                self.component_marker += 1
                self.nodes.pop(node)
        self.components = self.component_marker
        self.component_marker = 0

    def read(self):
        self.num_nodes, self.num_edges = map(int, input().split(' '))
        edges = []
        nodes = [None] + [self.Vertex(i + 1) for i in range(self.num_nodes)]
        for n in nodes:
            if n:
                self.nodes[n] = []
        for _ in range(self.num_edges):
            u, v = map(int, input().split(' '))
            edges.append([u, v])
        for e in edges:
            u, v = e
            self.nodes[nodes[u]].append(nodes[v])

def main():
    gph = Graph()
    gph.read()
    gph.strong_cc()
    print(gph.components)

threading.Thread(target=main).start()

# 2
# 4 4
# 1 2
# 4 1
# 2 3
# 3 1

# 5
# 5 7
# 2 1
# 3 2
# 3 1
# 4 3
# 4 1
# 5 2
# 5 3

# 4
# 4 3
# 1 2
# 3 2
# 4 3

# 98
# 100 100
# 27 96
# 23 51
# 42 10
# 40 22
# 30 41
# 80 40
# 13 70
# 21 94
# 88 35
# 38 86
# 53 83
# 71 84
# 64 26
# 4 46
# 76 43
# 24 76
# 26 83
# 18 75
# 42 98
# 36 39
# 47 63
# 33 96
# 89 54
# 47 80
# 95 8
# 34 41
# 91 45
# 78 1
# 12 74
# 2 37
# 98 81
# 30 32
# 93 30
# 45 71
# 38 44
# 85 18
# 89 10
# 71 35
# 73 52
# 28 42
# 98 20
# 22 69
# 56 79
# 78 63
# 53 58
# 77 13
# 6 11
# 56 36
# 4 11
# 92 63
# 32 78
# 71 24
# 16 79
# 66 89
# 72 6
# 20 15
# 2 91
# 100 75
# 93 7
# 42 100
# 18 88
# 49 75
# 33 78
# 81 1
# 42 95
# 73 64
# 50 66
# 33 68
# 14 38
# 80 89
# 8 16
# 87 18
# 20 80
# 81 38
# 14 35
# 91 20
# 36 5
# 16 8
# 61 11
# 72 91
# 60 83
# 26 57
# 80 11
# 58 1
# 71 36
# 57 46
# 41 30
# 47 82
# 46 74
# 28 9
# 76 70
# 69 58
# 39 73
# 89 55
# 93 54
# 17 92
# 54 44
# 21 69
# 87 58
# 96 34