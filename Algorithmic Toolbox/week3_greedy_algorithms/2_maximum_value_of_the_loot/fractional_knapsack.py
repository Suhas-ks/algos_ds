# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    total_value = 0
    data = {v / w: (w, v) for w, v in zip(weights, values)}
    sorted_values = list(sorted(data.keys()))
    items = len(sorted_values)
    while capacity > 0 and items > 0:
        unit = sorted_values.pop()
        weight = data[unit][0]
        value = data[unit][1]
        if capacity > weight:
            capacity -= weight
            total_value += value
            items -= 1
        else:
            total_value += (capacity * unit)
            capacity = 0
            items -= 1

    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
