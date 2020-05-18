# Uses python3
import sys


# def get_pisano_period(n, m):
#     if m == 2:
#         return 3
#     previous = 0
#     current = 1
#     for i in range(max(m, n) ** 2):
#         previous, current = current, (previous + current) % m
#
#         if previous == 0 and current == 1:
#             return i + 1


def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    sum = 1

    pisano_length = 60
    q = n // pisano_length
    n = n % pisano_length
    pisano_sum = 0
    for i in range(pisano_length):
        previous, current = current, (previous + current) % 10
        pisano_sum = (pisano_sum + current) % 10

    if n == 0:
        return 0
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        sum = (sum + current) % 10
    if q!=0:
        sum += q * pisano_sum
    return sum % 10


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    print(fibonacci_sum_naive(1000))
