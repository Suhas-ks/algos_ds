def match(a, b):
    if a == b:
        return 0
    else:
        return 1


def editDistance(src, dst):
    table = {}
    substrings = {}
    srcLen = len(src)
    dstLen = len(dst)

    subString = ''
    matchIndices = []
    for i in range(0, srcLen):
        for j in range(0, dstLen):
            if i == 0:
                table[(0, j)] = j
            if j == 0:
                table[(i, 0)] = i
            if i!=0 and j!=0:
                table[(i, j)] = min(table[i-1, j]+1, table[i, j-1]+1,
                                    table[i-1, j-1]+match(src[i], dst[j]))
            if not match(src[i], dst[j]):
                matchIndices.append((i, j))
    return table[(srcLen-1, dstLen-1)], matchIndices


if __name__ == "__main__":
    src = 'petition'
    dst = 'competition'
    print(editDistance(src, dst))
