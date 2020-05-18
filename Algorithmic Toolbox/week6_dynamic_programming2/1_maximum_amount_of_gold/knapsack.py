# Uses python3
import sys


def optimal_weight(W, w):
    # w = sorted(w, reverse=True)
    item_length = len(w)
    value = [[0 for x in range(item_length + 1)] for y in range(W + 1)]
    for val in range(item_length + 1):
        for weight in range(1, W + 1):
            if val - 1 < 0:
                continue
            else:
                value[weight][val] = value[weight][val - 1]
                if w[val - 1] <= weight:
                    v = value[weight - w[val - 1]][val - 1] + w[val - 1]
                    if v > value[weight][val]:
                        value[weight][val] = v
    v = value[W][len(w)]
    del value
    return v


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
    # print(optimal_weight(20, [5, 7, 12, 18]))
