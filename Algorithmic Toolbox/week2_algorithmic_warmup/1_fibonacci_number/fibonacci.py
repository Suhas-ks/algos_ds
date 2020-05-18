# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        fibs = [0]*(n+1)
        fibs[0] = 0
        fibs[1] = 1
        for i in range(2,n+1):
            fibs[i] = fibs[i-1] + fibs[i-2]
        return fibs[n]
n = int(input())
print(calc_fib(n))
