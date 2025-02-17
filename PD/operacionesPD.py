def operaciones(k):
    optimos = [-1]*(k+1)
    operaciones = [""]*(k+1)
    optimos[0] = 0

    for i in range(1,k+1):
        if optimos[i-1] + 1 < optimos[i] or optimos[i] == -1:
            optimos[i] = optimos[i-1] + 1
            operaciones[i] = "mas1"
        if i%2 == 0 and optimos[i//2] + 1 < optimos[i]:
            optimos[i] = optimos[i//2] + 1
            operaciones[i] = "por2"
    return reconstruccion(k, operaciones)

def reconstruccion(k, operaciones):
    res = []
    while k > 0:
        res.append(operaciones[k])
        if operaciones[k] == "por2":
            k = k//2
        else:
            k -= 1
    res.reverse()
    return res

print(operaciones(10))
#opt(n) = min(opt(n-1) + 1, opt(i//2) + 1)
