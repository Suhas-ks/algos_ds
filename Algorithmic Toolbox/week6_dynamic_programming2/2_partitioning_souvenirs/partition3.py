# Uses python3
import numpy as np


def partition3(A, k=3):
    # A = sorted(A)
    total = sum(A)
    if total % k != 0:
        return 0
    seq_len = len(A)
    target = total // k
    table = np.zeros((target + 1, seq_len + 1), dtype=np.bool)
    for i in range(len(A) + 1):
        table[0][i] = True
    for i in range(target):
        table[i][0] = False
    counter = 0
    for d in range(0, seq_len):
        curr_sum = sum(A[:d])
        curr = A[d]
                

    return table


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *A = list(map(int, input.split()))
    # print(partition3(A))
    print(partition3([3, 1, 1, 2, 2]))
