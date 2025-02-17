#El grafo es tipo camino con peso v1 -> v2 -> v3
#En cada caso tengo que elegir si me convien el actual o el anterior (quiero sum min de vertices)

#opt(i) = min(opt(i-2) + v[i], opt(i-1) + v[i-1])

def dominating_set_min(grafo):
    if len(grafo) == 0:
        return set()

    optimos = [0] * len(grafo.obtener_vertices())
    optimos[0] = 0
    optimos[1] = grafo.obtener_vertices(1).obtener_valor()

    for i in range(2, len(optimos)):
        op1 = optimos[i-2] + grafo.obtener_vertices(i)
        op2 = optimos[i-1] + grafo.obtener_vertices(i-1)
        optimos[i] = min(op1, op2)

    return reconstruccion(grafo, optimos)

def reconstruccion(grafo, optimos):
    resultado = set()
    aux = len(grafo.obtener_vertices())
    for i in range(len(grafo.obtener_vertices())):
        aux -= 1
        if optimos[aux] - grafo.obtener_vertices(aux) == optimos[aux-2]:
            resultado.add(grafo.obtener_vertices(aux))
            aux -= 1
        if aux == 0:
            if len(grafo.obtener_vertices()) == 2:
                if grafo.obtener_vertices(0) > grafo.obtener_vertices(1):
                    resultado.add(grafo.obtener_vertices(1))
                else:
                    resultado.add(grafo.obtener_vertices(0))
            break
    return resultado
