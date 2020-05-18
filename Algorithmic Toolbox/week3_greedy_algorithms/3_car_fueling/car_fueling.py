# python3
import sys


def compute_min_refills(distance, tank, stops):
    capacity = tank
    if distance < tank:
        return 0
    if tank < stops[0]:
        return -1
    stops.append(distance)
    visited = 0
    diff = 0
    for stop in stops:

        if stop - diff <= tank:
            tank -= stop - diff
            diff = stop
            continue
        elif stop - diff > tank:
            tank = capacity
            visited += 1
            if stop - diff > tank:
                return -1
            else:
                tank -= stop - diff
                diff = stop
                continue
        if stops[-1] == stop:
            return visited

    return visited


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
    # print(compute_min_refills(200, 250, [100, 150]))
