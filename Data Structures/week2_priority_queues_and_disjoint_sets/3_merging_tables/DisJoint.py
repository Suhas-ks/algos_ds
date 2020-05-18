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


if __name__ == "__main__":
    ds = DisjointSet()
    n = 6
    for i in range(1, n + 1):
        ds.make_set(i)
    ds.union(2, 4)
    ds.union(5, 2)
    ds.union(3, 1)
    ds.union(2, 3)
    ds.union(2, 6)
    print(ds.get_parents)
    print(ds.get_ranks)
