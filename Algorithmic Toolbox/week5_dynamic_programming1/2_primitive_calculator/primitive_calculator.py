# Uses python3
import sys

def memoize(n):
    if n <= 1:
        return [1]
    sequence = [0] * (n + 1)
    sequence[0], sequence[1] = 0, 0
    for i in range(2, n + 1):
        ops = []
        if i % 3 == 0:
            ops.append(sequence[i // 3])
        elif i % 2 == 0:
            ops.append(sequence[i // 2])
        ops.append(sequence[i - 1])
        sequence[i] = min(ops) + 1
    return sequence


def optimal_sequence(n):
    if n == 1:
        return [1]
    sequence = memoize(n)
    mod_sequence = []
    mod_sequence.insert(0, n)
    while n > 1:
        check = []
        if n % 3 == 0:
            ind = n // 3
            check.append((sequence[ind], ind))
        if n % 2 == 0:
            ind = n // 2
            check.append((sequence[ind], ind))
        check.append((sequence[n - 1], n - 1))
        _, n = sorted(check, key=lambda x: x[0])[0]
        mod_sequence.insert(0, n)
    return mod_sequence


input = sys.stdin.read()
n = int(input)
# n = 11809
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
