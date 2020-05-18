# python3
from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class Worker(object):

    def __init__(self, value, id, time_stamp):
        self._value = value
        self._id = id
        self._time_stamp = time_stamp

    @property
    def get_value(self):
        return self._value

    @property
    def get_id(self):
        return self._id

    @property
    def get_time_stamp(self):
        return self._time_stamp

    def __lt__(self, other):
        if self._value == other.get_value:
            return self._id < other.get_id
        return self._value < other.get_value

    def __gt__(self, other):
        if self._value == other.get_value:
            return self._id > other.get_id
        return self._value > other.get_value

    def modify_value(self, new_value):
        self._value = new_value


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
        if l <= self.heap_size - 1 and self.heap[l][0] < self.heap[index][0]:
            index = l
        r = self.right_child(i)
        if r <= self.heap_size - 1 and self.heap[r][0] < self.heap[index][0]:
            index = r
        if i != index:
            self.heap[i], self.heap[index] = self.heap[index], self.heap[i]
            self.min_heapify(index)
        index = i
        if l <= self.heap_size - 1 and self.heap[l][1] < self.heap[index][1] and self.heap[l][0] == self.heap[index][0]:
            index = l
        if r <= self.heap_size - 1 and self.heap[r][1] < self.heap[index][1] and self.heap[r][0] == self.heap[index][0]:
            index = r
        if i != index:
            self.heap[i], self.heap[index] = self.heap[index], self.heap[i]
            self.min_heapify(index)

    def build_min_heap(self):
        for i in range(self.size // 2):
            self.min_heapify(i)

    def heapsort(self):
        self.build_min_heap()
        counter = 0
        for i in range(self.size - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.heap_size -= 1
            counter += 1
            self.min_heapify(0)
        self.heap_size += counter

    def extract_min(self):
        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heap_size -= 1
        self.size -= 1
        self.min_heapify(0)
        return min_element

    def root_insert(self, p):
        self.heap.append(p)
        self.heap_size += 1
        self.size += 1
        self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], self.heap[0]
        # self.sift_up(self.heap_size - 1)
        # self.min_heapify(1)

    def remove(self, i):
        if i < self.heap_size and self.heap_size > 0:
            remove = self.heap[i]
            self.heap[i] = self.heap[self.heap_size - 1]
            self.heap_size -= 1
            self.min_heapify(i)
            self.heap.pop()
            return remove

    def extract_min_and_insert(self, p=None):
        min_element = self.heap[0]
        self.heap[0] = p
        self.min_heapify(0)
        return min_element

    def sift_up(self, i):
        j = i
        while i > 0 and self.heap[self.parent(i)][0] > self.heap[i][0]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
        while j > 0 and self.heap[self.parent(j)][1] > self.heap[j][1] and self.heap[self.parent(j)][0] == self.heap[j][
            0]:
            self.heap[self.parent(j)], self.heap[j] = self.heap[j], self.heap[self.parent(j)]
            j = self.parent(j)

    def decrease_priority(self, i, p):
        if p > self.heap[i][0]:
            return
        else:
            self.heap[i][0] = p
            # self.sift_up(i)

    def insert(self, p):
        self.heap_size += 1
        self.size += 1
        self.heap.append(p)
        self.sift_up(self.heap_size - 1)


def assign_jobs(n_workers, jobs):
    time, ind, nj = 0, 0, len(jobs)
    if n_workers >= nj:
        return [[i, 0] for i in range(n_workers)]
    result = []
    heap = MinHeap([])
    while True:
        if heap.heap_size < n_workers and ind < nj:
            for i in range(n_workers - heap.heap_size):
                heap.insert([jobs[ind], ind % n_workers, time])
                ind += 1
            # heap.build_min_heap()

        while heap.heap_size > 0 and heap.get_minimum[0] <= 0:
            if heap.heap_size <= n_workers:
                if ind < nj:
                    ele = heap.extract_min_and_insert([jobs[ind], ind % n_workers, time])
                    ind += 1
                    result.append([ele[1], ele[2]])
                elif heap.heap_size > 0:
                    ele = heap.extract_min_and_insert()
                    result.append([ele[1], ele[2]])

        if heap.heap_size and not heap.get_minimum[0] <= 0:
            for i in range(heap.heap_size):
                heap.decrease_priority(i, heap.heap[i][0] - 1)
            time += 1
            # heap.build_min_heap()

        if len(result) == nj:
            return result


def main():
    # n_workers, n_jobs = map(int, input().split())
    # jobs = list(map(int, input().split()))
    # assert len(jobs) == n_jobs
    # # #
    # assigned_jobs = assign_jobs(n_workers, jobs)
    # assigned_jobs = assign_jobs(2, [i + 1 for i in range(5)])
    assigned_jobs = assign_jobs(4, [1] * 20)
    # assigned_jobs = assign_jobs(2, [0, 2, 0, 4, 5])
    # assigned_jobs = assign_jobs(4, [5, 9, 8, 4, 2, 7])
    # a = [randint(a=0, b=10**9) for i in range(10**5)]
    # assigned_jobs = assign_jobs(4, a)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
