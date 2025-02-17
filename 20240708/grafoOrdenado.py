#opt(i) = max(opt(i-1), opt(j) + 1)
#tal que j es un vertice adyacente a i

def problema_grafo_ordenado_2(grafo, vertices_ordenados):
    if len(vertices_ordenados) <= 1:
        return 0

    optimos = [0]*len(vertices_ordenados)
    optimos[0] = [0]

    llegan = {}
    vistos = set()

    #La forma de hacerlo es haciendo un dicc de que vertices llegan a cuales
    for v in vertices_ordenados:
        llegan[v] = set()
        for w in grafo.adyacente(v):
            if w not in vistos:
                llegan[v].add(w)
                vistos.add(w)

    for i in range(1,len(vertices_ordenados)):
        op1 = optimos[i-1]
        aux = 0
        j = 0
        for clave, valor in llegan.items():
            j += 1
            if vertices_ordenados[i] == valor:
                op2 = optimos[j] + 1
            if op2 > aux:
                aux = op2
        optimos[v] = max(op1, op2)

    return reconstruccion(grafo, vertices_ordenados, optimos, llegan)

def reconstruccion(grafo, vertices_ordenados, optimos, llegan):
    falta = True
    contador = optimos[-1]
    i = len(vertices_ordenados) - 1
    solucion = set()
    while falta:
        for clave, valor in llegan.items():
            j += 1
            if vertices_ordenados[i] == valor:
                if vertices_ordenados[i-j] - 1 == optimos[i-1]:
                    solucion.add(vertices_ordenados[i])
                    break
        i -= 1
        if i == 0:
            falta = False
    
    return solucion
