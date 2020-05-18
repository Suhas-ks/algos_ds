# python3
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
    def len(self):
        return len(self)

    def __len__(self):
        return len(self.first) + len(self.second)



def max_sliding_window_naive(sequence, m):
    queue = Queue()
    maximums = []
    for i in range(m):
        queue.enqueue(sequence[i])
    maximums.append(queue.Max())
    for i in range(1, len(sequence) - m + 1):
        queue.dequeue()
        queue.enqueue(sequence[i+m-1])
        maximums.append(queue.Max())
    return maximums


if __name__ == '__main__':
    # n = int(input())
    # input_sequence = [int(i) for i in input().split()]
    # assert len(input_sequence) == n
    # window_size = int(input())

    # print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window_naive([2, 7, 3, 1, 5, 2, 6, 2], 4))
