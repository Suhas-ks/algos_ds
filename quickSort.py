#######################################################3-WAY PARTITION#################################################################


def partition(A, l, r):
    p = l
    m1, m2 = p+1, p+1
    for i in range(l+1, r):
        if A[i] < A[p]:
            m2 += 1
            m1 += 1
            A[i], A[m2] = A[m2], A[i]
            A[m2], A[m1] = A[m1], A[m2]

        elif A[i] == A[p]:
            m2 += 1
            A[i], A[m2] = A[m2], A[i]
    A[m1-1], A[p] = A[p], A[m1-1]
    return m1, m2


def quickSort(A, l, r):
    if l >= r-1:
        return None
    m1, m2 = partition(A, l, r)
    quickSort(A, l, m1)
    quickSort(A, m2, r)

# #######################################################2-WAY PARTITION#################################################################

# # The partition function takes last element as pivot, places
# # the pivot element at its correct position in sorted
# # array, and places all smaller (smaller than pivot)
# # to left of pivot and all greater elements to right
# # of pivot
# def partition(arr, low, high):
#     m = low-1	 # index of smaller element
#     pivot = arr[high]	 # pivot

#     for j in range(low, high):

#         # If current element is smaller than the pivot
#         if arr[j] < pivot:

#             # increment index of smaller element
#             m += 1
#             arr[m], arr[j] = arr[j], arr[m]

#     arr[m+1], arr[high] = arr[high], arr[m+1]
#     return (m+1)

# # Quick sort function


# def quickSort(arr, low, high):
#     if low < high:

#         # pi is partitioning index, arr[pi] is now
#         # at right place
#         pi = partition(arr, low, high)

#         # Separately sort elements before
#         # partition and after partition
#         quickSort(arr, low, pi-1)
#         quickSort(arr, pi+1, high)


if __name__ == '__main__':
    a = [9, 1, 3, 7, 5, 6, 8, 2, 4]
    # a = [15, 98, 62, 984, 651, 516519, 44, 5188, 566, 2, 3, 5, 62,
    #      3, 1, 4, 6, 3, 1, 2, 6, 79, 6, 78, 7, 5, 6, 9, 8, 6, 68, 4]
    quickSort(a, 0, len(a)-1)
    print(a)