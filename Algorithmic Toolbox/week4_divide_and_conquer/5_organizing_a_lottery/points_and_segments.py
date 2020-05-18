# Uses python3
import sys


# def get_point_count(point, segments, left, right):
#     if left > right:
#         return point
#     value, count = point
#     mid = int(left + (right - left) / 2)
#     start, end = segments[mid]
#     if value >= start and value <= end:
#         count += 1
#     # if value > start:
#     value, count = get_point_count([value, count], segments, mid + 1, right)
#     # elif value < end:
#     value, count = get_point_count([value, count], segments, left, mid - 1)
#     return value, count

# def point_distributer(points, segments):
#     length = len(points)
def fast_count_segments(starts, ends, points):
    length = len(points)
    counts = [0] * length
    starts = [(start, 'START') for start in starts]
    ends = [(end, 'END') for end in ends]
    sorted_points = []
    for point in range(length):
        sorted_points.append([points[point], 'POINT', point, 0])
    super_list = sorted(starts + ends + sorted_points, key=lambda x: x[0])
    counter = 0
    for point in super_list:
        if point[1] == 'START':
            counter += 1
            continue
        elif point[1] == 'POINT':
            point[3] += counter
            continue
        elif point[1] == 'END':
            counter -= 1
    for point in super_list:
        if point[1] == 'POINT':
            counts[point[2]] = point[3]

    return counts


# def naive_count_segments(starts, ends, points):
#     cnt = [0] * len(points)
#     for i in range(len(points)):
#         for j in range(len(starts)):
#             if starts[j] <= points[i] <= ends[j]:
#                 cnt[i] += 1
#     return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

    # starts = [0, 7]
    # ends = [5, 10]
    # points = [1, 6, 11]
    # cnt = fast_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')
    # print()
    # starts = [-10]
    # ends = [10]
    # points = [-100, 100, 0]
    # cnt = fast_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')
    # print()
    # starts = [0, -3, 7]
    # ends = [5, 2, 10]
    # points = [1, 6]
    # cnt = fast_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')
#