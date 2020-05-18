# Uses python3
import sys
import random


def partition3(a, l, r):
    x, m1, m2 = a[l], l, l
    for i in range(l + 1, r + 1):
        if a[i] == x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
        elif a[i] < x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
            m1 += 1
            a[m1], a[m2] = a[m2], a[m1]
    a[l], a[m1] = a[m1], a[l]
    return m1, m2


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # print(a)
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)
    return a


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
    # a = [1, 6, 7, 3, 4, 9, 8, 5, 3, 5, 9, 3, 5, 4, 9]
    # print(a)
    # print(randomized_quick_sort(a, 0, len(a) - 1))

# THE IDEA IS THAT SINCE m2 GROWS MORE THAN m1, EVEN m2 HAS TO BE UPDATED WHENEVER m1 IS UPDATED AND FIRST SWAP SHOULD BE DONE WITH m2, AND THEN FROM m2 TO m1
