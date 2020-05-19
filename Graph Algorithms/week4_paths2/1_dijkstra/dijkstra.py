#Uses python3

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

class Worker(object):

    def __init__(self, value, dist):
        self.value = value
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist

    def __gt__(self, other):
        return self.dist > other.dist

    def __le__(self, other):
        return self.dist <= other.dist

    def __ge__(self, other):
        return self.dist >= other.dist

    def __eq__(self, other):
        return self.dist == other.dist

    def __ne__(self, other):
        return self.dist != other.dist

class MinHeap(object):

    def __init__(self, arr, key=lambda x: x):
        self.key=key
        self.size = len(arr)
        self.heap_size = self.size
        self.heap = list(arr)
        self.build_min_heap()

    def __len__(self):
        return self.size

    @property
    def get_minimum(self):
        return self.heap[0]

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return (2 * i) + 1

    def right_child(self, i):
        return (2 * i) + 2

    def min_heapify(self, i):
        index = i
        l = self.left_child(i)
        if l <= self.heap_size - 1 and self.key(self.heap[l]) < self.key(self.heap[index]):
            index = l
        r = self.right_child(i)
        if r <= self.heap_size - 1 and self.key(self.heap[r]) < self.key(self.heap[index]):
            index = r
        if i != index:
            self.heap[i], self.heap[index] = self.heap[index], self.heap[i]
            self.min_heapify(index)

    def build_min_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.min_heapify(i)

    def extract_min(self):
        min_element = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.size -= 1
        self.heap.pop()
        self.min_heapify(0)
        return min_element

    def extract_min_without_heapify(self):
        min_element = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.size -= 1
        self.heap.pop()
        return min_element

    def extract_min_and_insert(self, p):
        min_element = self.heap[0]
        self.heap[0] = p
        self.min_heapify(0)
        return min_element

    def insert_and_extract_min(self, p):
        if p < self.heap[0]:
            return p
        self.heap[0], p = p, self.heap[0]
        self.min_heapify(0)
        return p

    def remove(self, i):
        remove = self.heap[i]
        self.heap[i] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.heap.pop()
        self.min_heapify(i)
        return remove

    def sift_up(self, i):
        while i > 0 and self.key(self.heap[self.parent(i)]) > self.key(self.heap[i]):
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def decrease_priority(self, i, p):
        if p > self.heap[i]:
            return
        else:
            self.heap[i] = p
            self.sift_up(i)

    def insert(self, p):
        self.heap_size += 1
        self.size += 1
        self.heap.append(p)
        self.sift_up(self.heap_size - 1)

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
            self.dist = 10**5

        def __str__(self):
            return str(self.value)

        def __int__(self):
            return int(self.value)

        def __index__(self):
            return int(self)

        def __float__(self):
            return float(self.value)

        def __eq__(self, other):
            return self.value == other.value

        def __ne__(self, other):
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
            node.dist = 10**5
            node.prev = None

    def breadth_first_search(self, src):
        q = Queue()
        self.reset_dist_prev()
        self.reset_visit_flags()
        color = True
        src.dist = 0
        src.color = color
        q.enqueue(src)
        for node in self.nodes_list:
            while q.full:
                u = q.dequeue()
                u.visited = True
                color = not u.color
                for nbr in self.nodes[u]:
                    if not nbr.visited:
                        if nbr.dist == None:
                            nbr.color = color
                            q.enqueue(nbr)
                            nbr.dist = u.dist + 1
                            nbr.prev = u
            if not node.visited:
                color = True
                node.color = color
                q.enqueue(node)

    def reconstruct_shortest_path(self, src, u):
        result = []
        self.breadth_first_search(src)
        while u != src and u != None:
            result.append(u)
            u = u.prev
        return reversed(result)


    def dijkstra(self, src):
        self.reset_visit_flags()
        self.reset_dist_prev()
        self.region = set()
        src.dist = 0
        self.region.add(src)
        heap = MinHeap(self.nodes, key=lambda x: x.dist) # build heap on self.dist keys...in the heap compare distances by indexing the hash map
        while len(heap):
            # flag = False
            u = heap.extract_min()
            self.region.add(u)
            for v in self.nodes[u]:
                if v.dist > u.dist + self.weights[(u, v)]:
                    v.dist = u.dist + self.weights[(u, v)]
                    # flag = True
            # if flag:
                # heap.build_min_heap()





    def read(self):
        self.num_nodes, self.num_edges = map(int, input().split(' '))
        edges = []
        nodes = [None] + [self.Vertex(i + 1) for i in range(self.num_nodes)]
        for n in nodes:
            if n:
                self.nodes[n] = []
        for _ in range(self.num_edges):
            u, v, e = map(int, input().split(' '))
            edges.append([u, v, e])
        u, v = map(int, input().split(' '))
        for ed in edges:
            p, q, e = ed
            if p == u:
                self.u = nodes[p]
            elif q == u:
                self.u = nodes[q]
            elif q == v:
                self.v = nodes[q]
            elif p == v:
                self.v = nodes[p]
            self.nodes[nodes[p]].append(nodes[q])
            self.weights[(nodes[p],nodes[q])] = e
        self.nodes_list = nodes




if __name__ == '__main__':
    g = Graph()
    g.read()
    g.dijkstra(g.u)
    if g.v.dist < 10**5:
        print(g.v.dist)
    else:
        print(-1)



# 3

# 4 4
# 1 2 1
# 4 1 2
# 2 3 2
# 1 3 5
# 1 3

# 6

# 5 9
# 1 2 4
# 1 3 2
# 2 3 2
# 3 2 1
# 2 4 2
# 3 5 4
# 5 4 1
# 2 5 3
# 3 4 4
# 1 5

# -1

# 3 3
# 1 2 7
# 1 3 5
# 2 3 2
# 3 2