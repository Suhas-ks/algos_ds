def binary_to_dec(num_str):
    n = len(num_str)
    num = 0
    for i in range(n):
        num += int(num_str[i]) * (2 ** i)
    return num


def merge(a, b, total_inversions):

    i, j = 0, 0
    m, n = len(a), len(b)
    c = [0] * (m + n)
    k = 0
    while i < m and j < n:
        if a[i] <= b[j]:
            c[k] = a[i]
            i += 1
            k += 1
        else:
            total_inversions += 1
            c[k] = b[j]
            j += 1
            k += 1
    if j < n:
        while j < n:
            c[k] = b[j]
            j += 1
            k += 1
            # total_inversions += 1

    if i < m:
        while i < m:
            c[k] = a[i]
            i += 1
            # total_inversions+=1
    return c, total_inversions


def merge_sort(arr, total_inversions):
    if len(arr) == 1:
        return arr, total_inversions
    mid = len(arr) // 2
    a, inv_a = merge_sort(arr[:mid], total_inversions)
    b, inv_b = merge_sort(arr[mid:], inv_a)
    c, total_inversions = merge(a, b, inv_b)
    return c, total_inversions


def inversion(M):
    N = len(M)
    M = binary_to_dec(M)
    A = [0] * (2 ** N)
    for i in range(2 ** N):
        A[i] = i ^ M
        # print(f"M: {M}")
        # print(f"i (XOR) M: {i^M}")
    _, inv_count = merge_sort(A, 0)
    return inv_count % 1000000007


if __name__ == "__main__":
    # T = input()
    # for i in range(int(T)):
    #     print(inversion(input()))
    # print(inversion(input()))
    # print(merge_sort([2,1,3], 0))
    print(merge_sort([4,0,1,2,3],0))
