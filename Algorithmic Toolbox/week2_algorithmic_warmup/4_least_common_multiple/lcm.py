# Uses python3
import sys


def gcd_naive(a, b):
    temp = 1
    while temp != 0:
        temp = a % b
        a = b
        b = temp
    return a


def lcm_naive(a, b):
    if min(a,b)==0:
        return 0
    return (a * b) // gcd_naive(a, b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
