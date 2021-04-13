def getChange(money, coins):
    minCoins = [0] + ([money] * money)
    for m in range(1, money+1):
        for c in coins:
            if m >= c:
                numCoins = minCoins[m-c] + 1
                if numCoins < minCoins[m]:
                    minCoins[m] = numCoins

    return minCoins


if __name__ == "__main__":
    coins = [7, 1, 3, 2, 5]
    money = 50
    change = getChange(money, coins)
    print(coins)
    for i in range(len(change)):
        print(f"{i}: {change[i]}")
