
def eval(a, b, op):
    if op == '-':
        return a - b
    if op == '+':
        return a + b
    if op == '*':
        return a*b


def min_max(i, j, max_arr, min_arr, dataset):
    small = 10 ** 10
    large = -10 ** 10
    for k in range(i, j):
        op = dataset[(2*k)+1]
        p = max_arr[i][k]
        q = max_arr[k+1][j]
        r = min_arr[i][k]
        s = min_arr[k+1][j]
        a = eval(p, q, op)
        b = eval(p, s, op)
        c = eval(q, r, op)
        d = eval(r, s, op)
        large = max(large, a, b, c, d)
        small = min(small, a, b, c, d)
    return large, small


def max_arith(dataset):
    digits = [int(dataset[n]) for n in range(0, len(dataset), 2)]
    dataset = [int(d) if d not in ['-', '+', '*'] else d for d in dataset]
    num = len(digits)
    min_arr = [[0] * num for n in range(num)]
    max_arr = [[0] * num for n in range(num)]
    for i in range(num):
        min_arr[i][i] = digits[i]
        max_arr[i][i] = digits[i]
    for s in range(1,num):
        for i in range(num - s):
            j = i + s
            max_arr[i][j], min_arr[i][j] = min_max(i, j, max_arr, min_arr, dataset)
    return max_arr, min_arr


if __name__ == "__main__":
    # print(max_arith(input()))
    print(max_arith("5-8+7*4-8+9"))
    # print(max_arith("7*4-8"))
