n = 10
prev = 0
curr = 1

for i in range(n+1):
    if n==0:
        print("previous :", prev)
        print("current :", curr)
        print("remainder :", curr % 10)
        break
    print()
    print("previous :",prev)
    print("current :", curr)
    print("remainder :", curr%10)
    prev, curr = curr, prev+curr
    print()