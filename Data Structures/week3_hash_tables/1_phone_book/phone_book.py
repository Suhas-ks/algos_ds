# python3

class QueryProcessor:
    _multiplier = 263
    _prime = 10000007

    def __init__(self, num_queries):
        self.n = num_queries
        self.bucket_count = int(self.n ** 0.5)
        self.elems = [[] for i in range(self.bucket_count)]

    # polyhash is used here
    def _hash_func(self, o):
        ans = 0
        for c in o:
            ans = (ans * self._multiplier + int(c)) % self._prime
        return ans % self.bucket_count

    def find(self, o):
        for e in self.elems[self._hash_func(o)]:
            if e[0] == o:
                return e[1]
        return False

    def add(self, o, v):
        hash = self._hash_func(o)
        if self.find(o):
            for i in range(len(self.elems[hash])):
                if self.elems[hash][i][0] == o:
                    self.elems[hash][i][1] = v
                    return
        self.elems[hash].append([o, v])

    def remove(self, o):
        if not self.find(o):
            return
        hash = self._hash_func(o)
        l = self.elems[hash]
        for e in l:
            if e[0] == o:
                self.elems[hash].remove(e)
                return

    def read_query(self):
        return input().split(' ')

    def process_query(self, query):
        if query[0] == 'add':
            self.add(query[1], query[2])
        elif query[0] == 'del':
            self.remove(query[1])
        elif query[0] == 'find':
            out = self.find(query[1])
            if not out:
                print('not found')
            else:
                print(out)

    def process_queries(self):
        for i in range(self.n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    proc = QueryProcessor(int(input()))
    proc.process_queries()
