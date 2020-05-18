# Uses python3
import sys
import math


def get_minimum_distance_on_y(sorted_on_y):
    length = len(sorted_on_y)
    if length <= 1:
        return 10 ** 10, sorted_on_y
    if length == 2:
        point1, point2 = sorted_on_y
        x1, y1 = point1
        x2, y2 = point2
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return d, sorted_on_y
    if length > 2:
        mid = int(0 + (length / 2))
        if len(sorted_on_y[:mid]) == 1:
            mod_sorted_y1 = sorted_on_y[:mid + 1]
        else:
            mod_sorted_y1 = sorted_on_y[:mid]
        if len(sorted_on_y[mid:]) == 1:
            mod_sorted_y2 = sorted_on_y[mid + 1:]
        else:
            mod_sorted_y2 = sorted_on_y[mid:]
        d1, sorted_on_y1 = get_minimum_distance_on_y(mod_sorted_y1)
        d2, sorted_on_y2 = get_minimum_distance_on_y(mod_sorted_y2)
        return min(d1, d2), sorted_on_y


def get_minimum_distance_on_x(sorted_on_x, sorted_on_y):
    length = len(sorted_on_x)
    if length <= 1:
        return 10 ** 10, sorted_on_x, sorted_on_y
    if length == 2:
        point1, point2 = sorted_on_x
        x1, y1 = point1
        x2, y2 = point2
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return d, sorted_on_x, sorted_on_y
    if length > 2:
        mid = int(0 + (length / 2))
        if len(sorted_on_x[:mid]) == 1:
            mod_sorted_x1 = sorted_on_x[:mid + 1]
            mod_sorted_y1 = sorted_on_y[:mid + 1]
        else:
            mod_sorted_x1 = sorted_on_x[:mid]
            mod_sorted_y1 = sorted_on_y[:mid]
        if len(sorted_on_x[mid:]) == 1:
            mod_sorted_x2 = sorted_on_x[mid + 1:]
            mod_sorted_y2 = sorted_on_y[mid + 1:]
        else:
            mod_sorted_x2 = sorted_on_x[mid:]
            mod_sorted_y2 = sorted_on_y[mid:]
        d1, sorted_on_x1, sorted_on_y1 = get_minimum_distance_on_x(mod_sorted_x1, mod_sorted_y1)
        d2, sorted_on_x2, sorted_on_y2 = get_minimum_distance_on_x(mod_sorted_x2, mod_sorted_y2)
        d = min(d1, d2)
        cross_partition_y = []
        for y in sorted_on_y:
            if abs(y[0]) <= d:
                cross_partition_y.append(y)
        d_, sorted_on_y = get_minimum_distance_on_y(cross_partition_y)
        return min(d, d_), sorted_on_x, sorted_on_y


def minimum_distance(x, y):
    coordinates = [(i, j) for i, j in zip(x, y)]
    x_sorted = sorted(coordinates, key=lambda x: x[0])
    y_sorted = sorted(coordinates, key=lambda x: x[1])
    return get_minimum_distance_on_x(x_sorted, y_sorted)[0]


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n = data[0]
    # x = data[1::2]
    # y = data[2::2]
    # print("{0:.9f}".format(minimum_distance(x, y)))

    x = [4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2]
    y = [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4]
    print("{0:.9f}".format(minimum_distance(x, y)))
