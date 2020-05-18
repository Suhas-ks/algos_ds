# Uses python3
# import numpy as np


def diff(a, b):
    if a == b:
        return 0
    else:
        return 1


def edit_distance(s, t):
    if s == t:
        return 0
    ed = 0
    sl = len(s)
    tl = len(t)
    # table = np.zeros(shape=(sl + 1, tl + 1), dtype=np.int)
    table = {}
    for i in range(sl + 1):
        table[i, 0] = i
    for i in range(tl + 1):
        table[0, i] = i
    for i in range(1, sl + 1):
        for j in range(1, tl + 1):
            table[i, j] = min(table[i - 1, j - 1] + diff(s[i - 1], t[j - 1]), table[i, j - 1] + 1, table[i - 1, j] + 1)

    return table[sl,tl]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance('exponential', 'polynomial'))
