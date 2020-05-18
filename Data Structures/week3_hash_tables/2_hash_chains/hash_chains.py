# python3


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = [[] for i in range(self.bucket_count)]

    # polyhash is used here
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def find(self, s):
        for e in self.elems[self._hash_func(s)]:
            if e == s:
                return True
        return False

    def add(self, s):
        if self.find(s):
            return
        self.elems[self._hash_func(s)].append(s)

    def remove(self, s):
        if not self.find(s):
            return
        self.elems[self._hash_func(s)].remove(s)

    def check(self, i):
        if self.elems[i]:
            return ' '.join(reversed(self.elems[i]))
        else:
            return ''

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return input().split(' ')

    def process_query(self, query):
        if query[0] == 'check':
            print(self.check(int(query[1])))
        elif query[0] == 'add':
            self.add(query[1])
        elif query[0] == 'del':
            self.remove(query[1])
        elif query[0] == 'find':
            if self.find(query[1]):
                print('yes')
            else:
                print('no')

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
