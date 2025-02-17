#opt(n) = min(opt[n-2] + Vi, opt[n-3] + Vi-1, opt[n-1] + Vi)

#No contempla el caso de 3 5 7 que el optimo es 5
#opt(i) = min(opt(i-2) + v[i], opt(i-1) + v[i-1])

#Creo que era: opt(i) = min(opt[i-1] + Vi, opt[i-2] + Vi-1)

# 3 5 7 2 1
# opt = [0, 3, 3, 5, 5 (3+2), 7 (5+2)]

def camino_ds_min(grafo):
    if len(grafo) == 0:
        return set()
    if len(grafo) == 1:
        return set(grafo.obtener_vertices()[0])
    
    optimos = [0] * (len(grafo.obtener_vertices())+1)
    optimos[1] = grafo.obtener_vertices()[0]
    optimos[2] = max(grafo.obtener_vertices()[0], grafo.obtener_vertices()[1])

    for i in range(3, len(grafo.obtener_vertices())):
        op1 = optimos[i-2] + grafo.obtener_vertices()[i-1]
        op2 = optimos[i-3] + grafo.obtener_vertices()[i-2]
        op2 = optimos[i-1] + grafo.obtener_vertices()[i-1]
        optimos[i] = min(op1, op2, op3)

    return reconstruccion(grafo, optimos)

def reconstruccion(grafo, optimos):
    solucion = set()
    i = len(optimos)-1
    while i >= 0:
        if optimos[i] == optimos[i-2] + grafo.obtener_vertices()[i-1]:
            solucion.add(grafo.obtener_vertices()[i-1])
            i -= 2
        elif optimos[i] == optimos[i-3] + grafo.obtener_vertices()[i-2]:
            solucion.add( grafo.obtener_vertices()[i-2])
            i -= 3
        else:
            solucion.add(grafo.obtener_vertices()[i-1])
            i -= 1
    
    return solucion