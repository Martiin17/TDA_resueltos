#opt(i, p) = max(opt(i-1,P). opt(i-1,P-pi) + Gi)
#cada campaña publicitaria i de la forma (Gi, Ci)
#Es mochila
def carlitos(c_publicitaria, P):    
    if len(c_publicitaria) == 0:
        return []
    
    optimos = []

    for i in range(len(c_publicitaria)):
        aux = []
        for p in range(P+1):
            op2 = 0 
            if c_publicitaria[i][1] <= p:
                if i-1 < 0:
                    op2 = c_publicitaria[i][0]
                else:
                    op2 = optimos[i-1][p-c_publicitaria[i][1]] + c_publicitaria[i][0]
            if i-1 < 0:
                op1 = 0
            else:
                op1 = optimos[i-1][p]
            aux.append(max(op1, op2))
        optimos.append(aux)

    return reconstruccion(c_publicitaria, P, optimos)

def reconstruccion(c_publicitaria, P, optimos):
    solucion = []
    i = len(c_publicitaria)-1
    
    while (i >= 0):
        if optimos[i][P] != optimos[i-1][P]:
            solucion.append(c_publicitaria[i])
            P -= c_publicitaria[i][1]
        if i == 0:
            if c_publicitaria[i][1] <= P:
                solucion.append(c_publicitaria[i])
        i -= 1
    solucion.reverse()
    return solucion

print(carlitos([(3,2), (4,3)], 5))