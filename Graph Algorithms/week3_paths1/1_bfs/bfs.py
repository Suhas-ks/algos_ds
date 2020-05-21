# Uses python3

import sys


class Stack(object):
    def __init__(self):
        self.stack = []
        self.max_stack = []
        self.max_sp = 0

    def Push(self, a):
        self.stack.append(a)
        if not self.max_stack:
            self.max_stack.append(a)
        else:
            if a >= self.max_stack[self.max_sp]:
                self.max_stack.append(a)
                self.max_sp += 1

    def Pop(self):
        a = self.stack.pop()
        if a == self.max_stack[self.max_sp]:
            self.max_stack.pop()
            if self.max_sp > 0:
                self.max_sp -= 1
        return a

    def Max(self):
        return self.max_stack[self.max_sp]

    @property
    def len(self):
        return len(self)

    def __len__(self):
        return len(self.stack)


class Queue(object):
    def __init__(self):
        self.first = Stack()
        self.second = Stack()

    def enqueue(self, a):
        self.first.Push(a)

    def dequeue(self):
        if not self.second.stack:
            while self.first.stack:
                self.second.Push(self.first.Pop())
        return self.second.Pop()

    def Max(self):
        if self.second.stack and self.first.stack:
            max1 = self.first.Max()
            max2 = self.second.Max()
            return max1 if max1 > max2 else max2
        elif not self.second.stack:
            return self.first.Max()
        elif not self.first.stack:
            return self.second.Max()

    @property
    def full(self):
        return len(self)

    def __len__(self):
        return len(self.first) + len(self.second)

class Graph(object):
    class Vertex(object):
        def __init__(self, value):
            self.value = value
            self.visited = False
            self.pre = None
            self.post = None
            self.component_id = None
            self.color = None
            self.prev = None
            self.heap_index = None
            self.dist = -1

        def __str__(self):
            return str(self.value)

        def __int__(self):
            return int(self.value)

        def __index__(self):
            return int(self)

        def __float__(self):
            return float(self.value)

        def __eq__(self, other):
            return self.value == other.value if other != None else False

        def __ne__(self, other):
            return self.value != other.value if other != None else True

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

        def __mul__(self, other):
            return int(self) * int(other)

        def __truediv__(self, other):
            return float(self) / float(other)

        def __floordiv__(self, other):
            return float(self) // float(other)

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

    def reset_dist_prev(self):
        for node in self.nodes.keys():
            node.dist = -1
            node.prev = None

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

    @property
    def nodes_list(self):
        return list(self.nodes.keys())

    def breadth_first_search(self, src):
        q = Queue()
        self.reset_visit_flags()
        self.reset_dist_prev()
        src.dist = 0
        q.enqueue(src)
        for node in self.nodes_list:
            while q.full:
                u = q.dequeue()
                u.visited = True
                for nbr in self.nodes[u]:
                    if not nbr.visited:
                        if nbr.dist == -1:
                            q.enqueue(nbr)
                            nbr.dist = u.dist + 1
                            nbr.prev = u
            if not node.visited:
                q.enqueue(node)

    def reconstruct_shortest_path(self, src, u):
        result = []
        self.breadth_first_search(src)
        while u != src and u != None:
            result.append(u)
            u = u.prev
        return reversed(result)

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
        u, v = map(int, input().split(' '))
        for e in edges:
            p, q = e
            if p == u:
                self.u = nodes[p]
            elif q == u:
                self.u = nodes[q]
            elif q == v:
                self.v = nodes[q]
            elif p == v:
                self.v = nodes[p]
            self.nodes[nodes[p]].append(nodes[q])
            self.nodes[nodes[q]].append(nodes[p])

    def solve(self):
        self.read()
        self.breadth_first_search(self.u)
        x = self.v
        while x.prev != None:
            x = x.prev
        if x.dist == -1:
            return x.dist
        return self.v.dist


if __name__ == '__main__':
    g = Graph()
    print(g.solve())

# 2
# 4 4
# 1 2
# 4 1
# 2 3
# 3 1
# 2 4

# -1
# 5 4
# 5 2
# 1 3
# 3 4
# 1 4
# 3 5
