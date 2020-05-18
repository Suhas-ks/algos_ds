# Uses python3
import sys


def get_pisano_period(n, m):
    if m == 2:
        return 3
    previous = 0
    current = 1
    for i in range(max(m, n) ** 2):
        previous, current = current, (previous + current) % m

        if previous == 0 and current == 1:
            return i + 1


def get_fibonacci_huge_naive(n, m):
    # if n <= 1:
    #     return n

    previous = 0
    current = 1
    pisano_length = get_pisano_period(n, m)

    n = n % pisano_length
    if n == 0:
        return 0

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
