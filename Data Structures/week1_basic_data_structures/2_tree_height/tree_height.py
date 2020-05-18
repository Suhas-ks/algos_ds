# python3

import sys
import threading


def height(root_key, tree, depth):
    root_arr = tree[root_key]
    if root_arr == []:
        return depth + 1
    else:
        depths = []
        for i in root_arr:
            depths.append(height(i, tree, depth + 1))
        return max(depths)


def compute_height(n, parents):
    max_height = 0
    arr = [[] for i in range(n)]
    for p in range(n):
        if parents[p] == -1:
            root = p
        else:
            arr[parents[p]].append(p)
    max_height = height(root, arr, max_height)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))
    # print(compute_height(5, [-1, 0, 4, 0, 3]))
    # print(compute_height(5, [4, -1, 4, 1, 1]))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
