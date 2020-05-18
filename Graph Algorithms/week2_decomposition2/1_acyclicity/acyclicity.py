# Uses python3

class Graph(object):
    class Vertex(object):
        def __init__(self, value):
            self.value = value
            self.visited = False
            self.pre = None
            self.post = None
            self.component_id = None
            self.neighbours = []
            self.out_neighbours = []
            self.in_neighbours = []

        def __str__(self):
            return str(self.value)

        def __int__(self):
            return int(self.value)

        def __index__(self):
            return self.__int__()

        def __float__(self):
            return float(self.value)

        def __eq__(self, other):
            return self.value == other.value and self.component_id == other.component_id
            # return self.value == other.value

        def __ne__(self, other):
            return self.value != other.value and self.component_id != other.component_id
            # return self.value != other.value

        def __hash__(self):
            return hash(self.value)

    def __init__(self):
        self.nodes = set()
        self.clock = 0
        self.component_marker = 0
        self.components = 0

    # def add_edge_undirected(self, u, v):
    #     self.add_node(u)
    #     self.add_node(v)
    #     u, v = self.Vertex(u), self.Vertex(v)
    #     u.adjacency.append(v)
    #     v.adjacency.append(u)
    #
    # def add_edge_directed(self, u, v):
    #     u, v = self.Vertex(u), self.Vertex(v)
    #     u.adjacency.append(v)
    #     v.adjacency.append(u)

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
        for nbr in v.neighbours:
            if not nbr.visited:
                self.explore(nbr)
        self.postvisit(v)

    def depth_first_search(self):
        for node in self.nodes:
            node.visited = False
        for node in self.nodes:
            if not node.visited:
                self.explore(node)
                self.component_marker += 1
        self.components = self.component_marker
        self.component_marker = 0
        self.clock = 0

    def cycle_check(self, v):
        v.visited = True
        self.previsit(v)
        v.component_id = self.component_marker
        for nbr in v.out_neighbours:
            if not nbr.visited:
                self.flag = self.cycle_check(nbr)
            elif not nbr.post and nbr.visited:
                return 1
        self.postvisit(v)
        return self.flag

    def cycle_search(self):
        self.flag = 0
        for node in self.nodes:
            node.visited = False
        for node in self.nodes:
            if not node.visited:
                self.flag = self.cycle_check(node)
            if self.flag:
                return 1
            else:
                self.flag = 0
        return self.flag

    def add_edge_undirected(self, u, v):
        u, v = self.Vertex(u), self.Vertex(v)
        u.neighbours.append(v)
        v.neighbours.append(u)
        self.nodes.add(u)
        self.nodes.add(v)

    def add_edge_directed(self, u, v):
        u, v = self.Vertex(u), self.Vertex(v)
        v.in_neighbours.append(u)
        u.out_neighbours.append(v)
        self.nodes.add(u)
        self.nodes.add(v)

    def is_cyclic(self):
        self.num_nodes, self.num_edges = map(int, input().split(' '))
        edges = []
        nodes = [self.Vertex(i) if i > 0 else None for i in range(self.num_nodes + 1)]
        for _ in range(self.num_edges):
            u, v = map(int, input().split(' '))
            edges.append([u, v])
        for e in edges:
            u, v = e
            nodes[u].out_neighbours.append(nodes[v])
        for n in nodes:
            if not n:
                continue
            else:
                self.nodes.add(n)
        return self.cycle_search()


if __name__ == '__main__':
    gph = Graph()
    print(gph.is_cyclic())

# 1
# 4 4
# 1 2
# 4 1
# 2 3
# 3 1

# 0
# 5 7
# 1 2
# 2 3
# 1 3
# 3 4
# 1 4
# 2 5
# 3 5