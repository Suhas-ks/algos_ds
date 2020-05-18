# Uses python3
import sys

def optimal_summands(n):
    summands = []
    if n<=2:
        return [n]
    total = 1
    while n>=1:
        if summands==[]:
            summands.append(total)
            n -= total
            continue
        total += 1
        if total > n:
            summands[-1]+=n
            n -= n
        else:
            summands.append(total)
            n -= total




    summands.reverse()
    return summands

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n = int(input)
    # summands = optimal_summands(n)
    # print(len(summands))
    # for x in summands:
    #     print(x, end=' ')
    for n in range(16):
        summands = optimal_summands(n)
        print(len(summands))
        for x in summands:
            print(x, end=' ')
        print()
        print(n, sum(summands))
        print()
    #     summands = optimal_summands(7)
    #     print(len(summands))
    #     for x in summands:
    #         print(x, end=' ')
    #     print()
    #     print(sum(summands))
    #     print()
