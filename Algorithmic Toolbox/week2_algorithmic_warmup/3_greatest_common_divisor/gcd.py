# Uses python3
import sys


def gcd_naive(a, b):
    temp = 1
    while temp != 0:
        temp = a % b
        a = b
        b = temp

    return a


if __name__ == "__main__":
    input = sys.argv[1]
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
