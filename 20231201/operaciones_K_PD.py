#opt(i) = min(opt[i//2] + 1, opt[i-1] + 1)
def operaciones(k):
    if k == 0:
        return []

    optimos = [0] * (k+1) 
    optimos[0] = 0
    
    for i in range(1, k+1):
        if i % 2 != 0:
            op1 = optimos[(i//2)] + 2
        else:
            op1 = optimos[i//2] + 1
        op2 = optimos[i-1] + 1
        optimos[i] = min(op1, op2)

    return reconstruccion(k, optimos)

def reconstruccion(k, optimos):
    solucion = []
    while k > 0:
        if optimos[k] == optimos[k-1] + 1:
            solucion.append("mas1")
            k -= 1
        else:
            solucion.append("por2")
            k = k//2
    solucion.reverse()
    return solucion

print(operaciones(7))