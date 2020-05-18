# python3
from collections import namedtuple
from heapq import *

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


def heap_length(heap):
    return len(heap)


def assign_jobs(n_workers, jobs):
    time, ind, nj = 0, 0, len(jobs)
    if n_workers >= nj:
        return [[i, 0] for i in range(n_workers)]
    result = []
    h = []

    while True:
        if heap_length(h) < n_workers and ind < nj:
            for i in range(n_workers - heap_length(h)):
                heappush(h, Worker(jobs[ind], ind % n_workers, time))
                ind += 1

        while heap_length(h) > 0 and h[0].get_value <= 0:
            if heap_length(h) <= n_workers:
                if ind < nj:
                    ele = heapreplace(h, Worker(jobs[ind], ind % n_workers, time))
                    ind += 1
                    result.append([ele.get_id, ele.get_time_stamp])
                elif heap_length(h) > 0:
                    ele = heappop(h)
                    result.append([ele.get_id, ele.get_time_stamp])

        if heap_length(h) and not h[0].get_value <= 0:
            for i in range(heap_length(h)):
                h[i].modify_value(h[i].get_value - 1)
            time += 1
            # heap.build_min_heap()

        if len(result) == nj:
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
    # a = [randint(a=0, b=10**9) for i in range(10**5)]
    # assigned_jobs = assign_jobs(4, a)

    for job in assigned_jobs:
        print(job[0], job[1])


if __name__ == "__main__":
    main()
