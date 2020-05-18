# Uses python3
import sys
from random import shuffle
def MergeSortWithInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:int(len(arr)/2)]
        b = arr[int(len(arr)/2):]
        a, x = MergeSortWithInversions(a)
        b, y = MergeSortWithInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + x + y
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, inversions


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    # sorted_a, number_of_inversions = MergeSortWithInversions(a, number_of_inversions)

    sorted_a, number_of_inversions = MergeSortWithInversions(a)

    return number_of_inversions


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # b = n * [0]
    # print(get_number_of_inversions(a, b, 0, n))

    a = [9, 10, 1, 2, 3]
    n = len(a)
    b = [0] * n
    print(get_number_of_inversions(a, b, 0, n))
#
# 9 8 7 3 2 1