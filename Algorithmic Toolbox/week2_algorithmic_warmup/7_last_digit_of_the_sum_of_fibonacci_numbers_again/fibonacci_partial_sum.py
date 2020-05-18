# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1 and n>=0:
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
        sum += current
    if q!=0:
        sum += q * pisano_sum
    return sum

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    previous = 0
    current = 1

    chop_off = fibonacci_sum_naive(from_ - 1)

    sum = fibonacci_sum_naive(to)

    return (sum - chop_off) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
