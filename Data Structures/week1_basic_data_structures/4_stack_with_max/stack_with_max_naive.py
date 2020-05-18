#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_stack = []
        self.__max_sp = 0
    def Push(self, a):
        self.__stack.append(a)
        if self.__max_stack == []:
            self.__max_stack.append(a)
        if a >= self.__max_stack[self.__max_sp]:
            self.__max_stack.append(a)
            self.__max_sp += 1
    def Pop(self):
        assert(len(self.__stack))
        a = self.__stack.pop()
        if a == self.__max_stack[self.__max_sp]:
            self.__max_stack.pop()
            self.__max_sp -= 1

    def Max(self):
        assert(len(self.__stack))
        return self.__max_stack[self.__max_sp]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
