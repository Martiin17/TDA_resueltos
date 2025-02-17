#opt[i] = max(opt[i-2] + Gi, opt[i-1])

def juan_el_vago(ganancias):
    if len(ganancias) == 0:
        return []
    if len(ganancias) == 1:
        return [0]
    
    if len(ganancias) == 2:
        if ganancias[0] >= ganancias[1]:
            return [0]
        else:
            return [1]
    
    optimos = [0] * (len(ganancias) + 1)
    optimos[0] = 0
    optimos[1] = ganancias[0]
    optimos[2] = max(ganancias[0], ganancias[1])

    for i in range(3, len(ganancias)+1):
        optimos[i] = max(optimos[i-2] + ganancias[i-1], optimos[i-1])

    return reconstruccion(ganancias, optimos)

def reconstruccion(ganancias, optimos):
    solucion = []
    i = len(ganancias)

    while i >= 0:
        if i -2 < 0:
            if ganancias[0] == optimos[i]:
                solucion.append(i-1)
                break
        if optimos[i] - ganancias[i-1] == optimos[i-2]:
            solucion.append(i-1)
            i -= 1
        i -= 1
    
    solucion.reverse()
    return solucion

print(juan_el_vago([100, 5, 50, 1, 1, 200]))