# python3

class Heap(object):
    def __init__(self, arr):
        self.size = len(arr)
        self.sort_size = self.size
        self.swaps = []
        self.heap = arr
        for i in range(self.size, -1, -1):
            self.sift_down(i)
        self.sorted_heap = []
    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return (2 * i) + 1

    def right_child(self, i):
        return (2 * i) + 2

    def sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swaps.append((self.parent(i), i))
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def sift_down(self, i):
        index = i
        l = self.left_child(i)
        if l <= self.sort_size - 1 and self.heap[l] < self.heap[index]:
            index = l
        r = self.right_child(i)
        if r <= self.sort_size - 1 and self.heap[r] < self.heap[index]:
            index = r
        if i != index:
            self.swaps.append((i, index))
            self.heap[i], self.heap[index] = self.heap[index], self.heap[i]
            self.sift_down(index)

    def insert(self, e):
        self.size += 1
        self.heap.append(e)
        self.sift_up(self.size - 1)

    def sort(self):
        for i in range(self.size, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.sift_down(0)

def main():
    # n = int(input())
    # data = list(map(int, input().split()))
    # assert len(data) == n
    # heap = Heap(data)
    #
    heap = Heap([5, 4, 3, 2, 1, 7, 3, 9, 8])
    # heap = Heap([1, 2, 3, 4, 5])
    swaps = heap.swaps
    print(heap.heap)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
