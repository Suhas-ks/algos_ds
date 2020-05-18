#Uses python3

import sys


def is_greater_or_equal(a, b):
    if int(a+b) >= int(b+a):
        return 1
    else:
        return 0


def largest_number(a):
    # a = sorted([int(i) for i in a], reverse=True)
    # a = [int(i) for i in a]

    result = ""
    max_digit = '0'
    while a != []:

        for num in a:
            if is_greater_or_equal(num, max_digit):
                max_digit = num
        result+=max_digit
        a.remove(max_digit)
    return result

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = input.split()
    # a = data[1:]
    # print(largest_number(a))
    print(largest_number(['21', '2', '321', '79', '17']))

