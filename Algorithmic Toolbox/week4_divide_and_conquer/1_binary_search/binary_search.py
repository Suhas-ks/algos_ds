# Uses python3
import sys


def binary_search(a, x, left=None, right=None):
    if left == None and right == None:
        left, right = 0, len(a) - 1
    if right == left:
        if a[left]==x:
            return left
        else:
            return -1

    while left <= right:
        mid = int(left + ((right - left) / 2))
        if a[mid] == x:
            return mid
        elif x > a[mid]:
            return binary_search(a, x, left=mid + 1, right=right)
        elif x < a[mid]:
            return binary_search(a, x, left=left, right=mid)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
    # for x in [8, 1, 23, 1, 11]:
    #     print(binary_search([1, 5, 8, 12, 13], x), end=' ')
