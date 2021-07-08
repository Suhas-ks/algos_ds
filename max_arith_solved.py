# Uses python3
def eval(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return 0

def MinAndMax(i, j, M, m, data):
    large = -10 ** 11
    small = 10 ** 11
    for k in range(i, j):
        op = data[(2*k)+1]
        s = M[i][k]
        t = M[k + 1][j]
        p = m[i][k]
        q = m[k+1][j]
        a = eval(s, t, op)
        b = eval(s, q, op)
        c = eval(p, t, op)
        d = eval(p, q, op)
        large = max(large, a, b, c, d)
        small = min(small, a, b, c, d)
    return small, large


def get_maximum_value(dataset):
    digits = [i for i in range(0, len(dataset), 2)]
    dataset = [int(d) if d not in ['+', '-', '*'] else d for d in dataset]
    num = len(digits)
    m = [[0] * num for i in range(num)]
    M = [[0] * num for i in range(num)]
    for i in range(num):
        for j in range(num):
            if i == j:
                m[i][i], M[i][i] = int(dataset[digits[i]]), int(dataset[digits[i]])
    
    for s in range(1, num):
        for i in range(num - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, M, m, dataset)
    return M[0][num-1]


if __name__ == "__main__":
    # print(get_maximum_value(input()))
    print(get_maximum_value("5-8+7*4-8+9"))