# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    segments = sorted(segments, key= lambda x: x[1])
    coordinates = []
    for seg in segments:
        if coordinates==[]:
            coordinates.append(seg[1])
            continue
        else:
            c = coordinates[-1]
        if seg[0] <= c and seg[1] >= c:
            continue
        elif seg[0] > c and seg[1] > c:
            coordinates.append(seg[1])
            continue

    return coordinates


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
    # points = optimal_points([(4, 7), (1, 3), (2, 5), (5, 6)])
    # print(len(points))
    # print(*points)
