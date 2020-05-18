class MaxHeap(object):

    def __init__(self, arr, limit=None):
        self.size = len(arr)
        self.limit = limit
        if self.limit != None:
            self.heap_size = self.limit
        else:
            self.heap_size = self.size
        self.heap = list(arr)
        self.build_max_heap()

    @property
    def get_maximum(self):
        return self.heap[0]

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return (2 * i) + 1

    def right_child(self, i):
        return (2 * i) + 2

    def max_heapify(self, i):
        index = i
        l = self.left_child(i)
        if l <= self.heap_size - 1 and self.heap[l] > self.heap[index]:
            index = l
        r = self.right_child(i)
        if r <= self.heap_size - 1 and self.heap[r] > self.heap[index]:
            index = r
        if i != index:
            self.heap[i], self.heap[index] = self.heap[index], self.heap[i]
            self.max_heapify(index)

    def build_max_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.max_heapify(i)

    def heapsort(self):
        # self.build_max_heap()
        counter = 0
        for i in range(self.size - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.heap_size -= 1
            counter += 1
            self.max_heapify(0)
        self.heap_size += counter

    def extract_max(self):
        if self.heap_size < 0:
            raise Exception("HeapSizeError: heap underflow")
        max_element = self.heap[0]
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        return max_element

    def remove(self, i):
        if i < self.heap_size:
            if self.heap_size < 0:
                raise Exception("HeapSizeError: heap underflow")
            self.heap[i] = self.heap[self.heap_size - 1]
            remove = self.heap.pop()
            self.heap_size -= 1
            self.max_heapify(i)
            return remove
        else:
            raise Exception("HeapIndexError: heap index out of range")

    def sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def increase_priority(self, i, p):
        if p < self.heap[i]:
            return
        else:
            self.heap[i] = p
            self.sift_up(i)

    def insert(self, p):
        if self.limit == None:
            self.heap_size += 1
            self.size += 1
            self.heap.append(p)
            self.sift_up(self.heap_size - 1)
        elif self.limit:
            if self.limit < self.heap_size + 1:
                raise Exception("HeapSizeError: heap overflow")
            else:
                self.heap_size += 1
                self.size += 1
                self.heap.append(p)
                self.sift_up(self.heap_size - 1)


if __name__ == "__main__":
    a = [5, 13, 2, 25, 7, 17, 20, 8, 4, 200]
    heap = MaxHeap(a)
    # # heap.build_max_heap()
    # # heap.heapsort()
    # print(heap.heap)
    # # heap.__init__(a)
    # print(heap.heap)
    # print(heap.heap_size)
    # print(heap.get_maximum)
    # heap.insert(201)
    # print(heap.get_maximum)
    # print(heap.heap)
    # heap.heapsort()
    # print(heap.heap)
    for i in range(heap.size):
        heap.remove(0)
        print(heap.heap)
