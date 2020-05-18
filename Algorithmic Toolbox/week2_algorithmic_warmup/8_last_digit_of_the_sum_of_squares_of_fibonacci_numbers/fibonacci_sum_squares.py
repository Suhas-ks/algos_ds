# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
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
        pisano_sum = (pisano_sum + current**2) % 10

    if n == 0:
        return 0
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        sum = (sum + current**2) % 10
    if q != 0:
        sum += q * pisano_sum
    return sum % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
