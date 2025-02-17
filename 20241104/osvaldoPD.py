#opt(i) = max( 0, opt[i-1] + (p[i] - p[i-1]) )

def osvaldo(p):
    if len(p) == 0:
        return 0

    optimos = [0] * (len(p))
    optimos[0] = 0

    for i in range(len(p)):
        primera_op = 0
        if i >= 1:
            segunda_op = optimos[i] + p[i] - p[i-1]
        else:
            segunda_op = 0
        optimos[i] = max(primera_op, segunda_op)

    return optimos


print(osvaldo([2,7,-9,15,3,1]))

#Es lineal O(p)
