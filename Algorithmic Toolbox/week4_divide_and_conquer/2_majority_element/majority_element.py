# Uses python3
import sys

def Merge(b, c):
    p = len(b)
    q = len(c)
    d = [0] * (p + q)
    i = 0
    while b != [] and c != []:
        if b[0] < c[0]:
            d[i] = b[0]
            b.pop(0)
            i += 1
        elif b[0] >= c[0]:
            d[i] = c[0]
            c.pop(0)
            i += 1
    if b == []:
        d[i:] = c
    else:
        d[i:] = b
    return d


def MergeSort(a):
    length = len(a)
    if length == 1:
        return a
    mid = length // 2
    b = MergeSort(a[:mid])
    c = MergeSort(a[mid:])
    a2 = Merge(b, c)
    return a2


def get_majority_element(a, left, right):
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]
    length = len(a)
    a = MergeSort(a)
    max_count = 1
    count = 1
    for i in range(1, length):
        if a[i] == a[i - 1]:
            count += 1
        else:
            if count > max_count:
                if count > length:
                    return 1
                max_count = count
                count = 1
                continue
            count = 1
            continue
    if max_count <= count:
        max_count = count
    if max_count > length / 2:
        return 1
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
    # a = [2, 3, 2, 3]
    # print(a)
    # if get_majority_element(a
    #         , 0,
    #         len(a)) != -1:
    #     print(1)
    # else:
    #     print(0)
#
