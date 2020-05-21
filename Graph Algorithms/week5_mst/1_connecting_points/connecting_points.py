# python3
import itertools as itr

class DisjointSet(object):

    def __init__(self):
        self._parent = {}
        self._rank = {}

    @property
    def get_ranks(self):
        return list(self._rank.values())

    @property
    def get_parents(self):
        return list(self._parent.values())

    def make_set(self, e):
        self._parent[e] = e
        self._rank[e] = 0

    def find(self, i):
        """
        With Path Compression
        """
        while i != self._parent[i]:
            self._parent[i] = self.find(self._parent[i])
            i = self._parent[i]
        return i

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self._rank[i_id] > self._rank[j_id]:
            self._parent[j_id] = i_id
        else:
            self._parent[i_id] = j_id
            if self._rank[i_id] == self._rank[j_id]:
                self._rank[j_id] += 1

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
            self.dist = 10 ** 5
            self.in_queue = False

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
        self.weights = {}
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

    def reset_dist_prev(self):
        for node in self.nodes.keys():
            node.dist = 10 ** 5
            node.prev = None

    def kruskal_mst(self):
        ds = DisjointSet()
        for node in self.nodes_list:
            ds.make_set(node)
        x = set()
        edges_sorted = sorted(self.edges, key=lambda x: self.weights[x])
        for edge in edges_sorted:
            if ds.find(edge[0]) != ds.find(edge[1]):
                x.add(edge)
                ds.union(edge[0], edge[1])
        return x



    # def prim_mst(self):
    #     self.reset_visit_flags()
    #     self.reset_dist_prev()
    #     src = self.nodes_list[0]
    #     src.dist = 0
    #     src.in_queue = True
    #     q = MinHeap([], key=lambda x: x.dist)
    #     q.insert(src)
    #     while len(q):
    #         v = q.extract_min()
    #         v.visited = True
    #         for z in self.nodes[v]:
    #             if z.dist > self.weights[(v, z)]:
    #                 z.dist = self.weights[(v, z)]
    #                 z.prev = v
    #                 z.in_queue = True




    def euclid_distance(self, x, y):
        return ((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2) ** 0.5

    def read(self):
        num_points = int(input())
        points = {}
        for i in range(num_points):
            a, b = map(int, input().split(' '))
            points[self.Vertex(i + 1)] = (a, b)
        key_pairs = [pair for pair in itr.combinations(list(points.keys()), r=2)]
        self.edges = {}
        for pair in key_pairs:
            self.edges[pair] = self.euclid_distance(points[pair[0]], points[pair[1]])
        del points, key_pairs[:], key_pairs
        self.nodes_list = set()
        self.weights = {}
        for item in self.edges:
            x, y = item
            self.weights[(x, y)] = self.edges[item]
            self.weights[(y, x)] = self.edges[item]
        for item in self.edges:
            x, y = item
            self.nodes_list.add(x)
            self.nodes_list.add(y)
        self.nodes = {}
        self.nodes_list = list(self.nodes_list)
        for node in self.nodes_list:
            self.nodes[node] = []
        for key in self.edges.keys():
            x, y = key
            self.nodes[x].append(y)
            self.nodes[y].append(x)

    def solve(self):
        sum = 0
        for edge in self.kruskal_mst():
            sum += self.weights[edge]
        return sum

if __name__ == '__main__':
    g = Graph()
    g.read()
    print("{:.12f}".format(g.solve()))

# 3.000000000000

# 4
# 0 0
# 0 1
# 1 0
# 1 1

# 7.0644

# 5
# 0 0
# 0 2
# 1 1
# 3 0
# 3 2