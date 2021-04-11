#######################################################2-WAY PARTITION#################################################################


# def partition(A, l, r):
#     pivotInd = l
#     pivot = A[pivotInd]
#     m = l
#     for i in range(l+1, r):
#         if A[i] <= pivot:
#             m += 1
#             A[m], A[i] = A[i], A[m]
#     A[m], A[pivotInd] = A[pivotInd], A[m]
#     return m


# def quickSort(A, l, r):
#     if l < r:
#         m = partition(A, l, r)
#         quickSort(A, l, m)
#         quickSort(A, m, r)


#######################################################3-WAY PARTITION#################################################################

def partition3(A, l, r):
    pivotInd = l
    pivot = A[pivotInd]
    m1, m2 = l, l
    for i in range(l+1, r):
        if A[i] < pivot:
            m2 += 1
            m1 += 1
            A[m2], A[i] = A[i], A[m2]
            A[m2], A[m1] = A[m1], A[m2]
        elif A[i] == pivot:
            m2 += 1
            A[m2], A[i] = A[i], A[m2]
    A[m1], A[pivotInd] = A[pivotInd], A[m1]
    return m1, m2


def quickSort(A, l, r):
    if l >= r:
        return
    m1, m2 = partition3(A, l, r)
    quickSort(A, l, m1)
    quickSort(A, m2+1, r)


if __name__ == '__main__':
    a = [9, 1, 3, 7, 5, 6, 8, 2, 4]
    quickSort(a, 0, len(a))
    print(a)
    print()
    a = [15, 98, 62, 984, 651, 516519, 44, 5188, 566, 2, 3, 5, 62,
         3, 1, 4, 6, 3, 1, 2, 6, 79, 6, 78, 7, 5, 6, 9, 8, 6, 68, 4]
    quickSort(a, 0, len(a))
    print(a)
