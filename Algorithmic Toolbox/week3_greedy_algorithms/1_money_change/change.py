# Uses python3
import sys


def get_change(m):
    denominations = [10, 5, 1]
    total_change = 0
    for i in denominations:
        if m >= i:
            coins = m // i
            m -= (coins * i)
            total_change += coins
        else:
            continue

    return total_change


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
