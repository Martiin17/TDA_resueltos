def colorear(grafo, n):
    n_colores = 0
    colores = {}
    vertices = grafo.obtener_vertices()
    k = colorear_rec(grafo, vertices, colores, 0, n_colores, len(vertices))
    #Creo que n_colores es como la sol_parcial
    #y len(vertices) es como la sol_optima
    if k <= n:
        return True
    else:
        return False

def colorear_rec(grafo, vertices, colores, indice, n_colores, sol_min):
    if sol_min <= n_colores:
        return sol_min
    if indice == len(vertices):
        #return sol_min
        return n_colores

    v = vertices[indice]
    for color in range(n_colores+1):
        colores[v] = color
        if not compatible(grafo, v, colores):
            continue
        if color != n_colores:
            sol = colorear_rec(grafo, vertoces, colores, indice+1, n_colores, sol_min)
        else:
            sol = colorear_rec(grafo, vertoces, colores, indice+1, n_colores+1, sol_min)
        
        if sol < sol_min:
            sol_min = sol

    del colores[v]
    return sol_min

def compatible(grafo, v, colores):
    for w in grafo.adyacentes(v):
        if w in colores and colores[v] == colores[w]:
            return False
    return True