def knapsack(W, items):

    # output- Vtotal filled A-array
    V = 0
    A = []
    values = []
    weights = []
    hashmap = {}
    for i in range(0, len(items), 2):
        weights.append(items[i])
        values.append(items[i+1])
        hashmap[len(weights)-1] = items[i+1]/items[i]
    for u, v in sorted(hashmap.items(), key=lambda x: x[1], reverse=True):
        while W > 0 and weights[u] > 0:
            a = min(weights[u], W)
            W -= a
            weights[u] -= a
            V += a*v
            A.append([a, v])
    return A
if __name__=='__main__':
    out=knapsack(9, [2,3,4,5,1,2,5,5,6,9])
    

    print(out)
