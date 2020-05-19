# python3

import queue


class Node(object):
    def __init__(self, index, distance):
        self.index = index
        self.distance = distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __ne__(self, other):
        return self.distance != other.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __ge__(self, other):
        return self.distance >= other.distance


def distance(adj, cost, s, t):
    dist = [float('inf')] * len(adj)
    dist[s] = 0
    pq = queue.PriorityQueue()
    pq.put(Node(s, dist[s]))
    while not pq.empty():
        u = pq.get()
        u_index = u.index
        for v in adj[u_index]:
            v_index = adj[u_index].index(v)
            if dist[v] > dist[u_index] + cost[u_index][v_index]:
                dist[v] = dist[u_index] + cost[u_index][v_index]
                pq.put(Node(v, dist[v]))
    if dist[t] == float('inf'):
        return -1
    return dist[t]


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = map(int, input().split())
    s, t = s - 1, t - 1
    print(distance(adj, cost, s, t))
