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

def quickSortWrapper(arr):
    quickSort(arr, 0, len(arr))
    

def group(arr, limit):
    groups = []
    quickSortWrapper(arr)
    numElements = len(arr)
    i = 0
    while i < numElements:
        group = []
        startOfGroup = arr[i]
        while i < numElements and arr[i]-startOfGroup < limit:
            group.append(arr[i])
            i += 1
        groups.append(group)
    return groups


if __name__ == "__main__":
    print(group([3, 4, 9, 7, 2, 5, 8, 6, 7, 2, 3, 4, 6, 9, 7, 9, 2, 3, 1, 4, 7, 10, 11, 13, 12,
                 16, 14, 15, 19, 18, 17, 20, 16, 14, 15, 7, 10, 11, 13, 13, 12, 16, 14, 15, 19, 18, 17], 3))
