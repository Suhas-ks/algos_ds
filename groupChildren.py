def group(arr):
    groups = []
    arr = sorted(arr)
    numElements = len(arr)
    i = 0
    while i < numElements:
        group = []
        startOfGroup = arr[i]
        while i < numElements and arr[i]-startOfGroup < 4:
            group.append(arr[i])
            i += 1
        groups.append(group)
    return groups


if __name__ == "__main__":
    print(group([3, 4, 9, 7, 2, 5, 8, 6, 7, 2, 3, 4, 6, 9, 7, 9, 2, 3, 1, 4, 7, 10, 11, 13, 12,
                 16, 14, 15, 19, 18, 17, 20, 16, 14, 15, 7, 10, 11, 13, 13, 12, 16, 14, 15, 19, 18, 17]))
