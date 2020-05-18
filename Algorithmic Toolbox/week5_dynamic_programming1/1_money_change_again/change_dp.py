# Uses python3
import sys

def get_change(m):
    change = [m*2] * (m + 1)
    change[0] = 0
    for i in range(1 , m + 1):
        for coin in [4,3,1]:
            if i >= coin:
                min_change=(change[i - coin]+1)
                if change[i] > min_change:
                    change[i] = min_change
    return change[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
