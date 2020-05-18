# Uses python3
import sys


def Merge(p, q, inversions):
    a, b = len(p), len(q)
    d = [0] * (a + b)
    i, pt, qt = 0, 0, 0
    while pt != a and qt != b:
        if p[pt] <= q[qt]:
            d[i] = p[pt]
            pt += 1
            i += 1
        elif p[pt] > q[qt]:
            d[i] = q[qt]
            qt += 1
            i += 1
            inversions += 1
            inversions += a - (pt + 1)




    if pt == a:
        d[i:] = q[qt:]
    else:
        d[i:] = p[pt:]
    return d, inversions


def MergeSortWithInversions(a):
    length = len(a)
    if length == 1:
        return a, 0
    mid = (length // 2)

    p, x = MergeSortWithInversions(a[:mid])
    q, y = MergeSortWithInversions(a[mid:])
    return Merge(p, q, x + y)


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    sorted_a, number_of_inversions = MergeSortWithInversions(a)
    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, n))
    #
    # a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # n = len(a)
    # b = [0] * n
    # print(get_number_of_inversions(a, b, 0, n))

# 9 8 7 3 2 1
