# /usr/bin/python3

from random import randint


class Worker(object):

    def __init__(self, id, time=0):
        self.id = id
        self.time = time

    def set_time(self, t):
        self.time = t

    def add_time(self, t):
        self.time += t

    def __lt__(self, other):
        if self.time == other.time:
            return self.id < other.id
        return self.time < other.time

    def __gt__(self, other):
        if self.time == other.time:
            return self.id > other.id
        return self.time > other.time


class MinHeap(object):

    def __init__(self, arr):
        self.size = len(arr)
        self.heap_size = self.size
        self.heap = list(arr)
        self.build_min_heap()

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
        if l <= self.heap_size - 1 and self.heap[l] < self.heap[index]:
            index = l
        r = self.right_child(i)
        if r <= self.heap_size - 1 and self.heap[r] < self.heap[index]:
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
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
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


def assign_jobs(n_workers, jobs):
    nj = len(jobs)
    result = []
    heap = MinHeap([Worker(i) for i in range(n_workers)])
    for j in range(nj):
        free = heap.extract_min()
        result.append([free.id, free.time])
        free.add_time(jobs[j])
        heap.insert(free)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    # #
    assigned_jobs = assign_jobs(n_workers, jobs)
    # assigned_jobs = assign_jobs(2, [i + 1 for i in range(5)])
    # assigned_jobs = assign_jobs(4, [1] * 20)
    # assigned_jobs = assign_jobs(2, [0, 2, 0, 4, 5])
    # assigned_jobs = assign_jobs(4, [5, 9, 8, 4, 2, 7])
    # assigned_jobs = assign_jobs(15, [8, 8, 6, 3, 7, 5, 9, 8, 6])

    # a = [randint(a=0, b=10 ** 9) for i in range(10 ** 5)]
    # assigned_jobs = assign_jobs(4, a)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
