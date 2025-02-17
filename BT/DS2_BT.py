def dominating_set(grafo):
    vertices = grafo.obtener_vertices()
    sol_parcial = set()
    sol_opt = set(vertices)
    return dominating_set_rec(grafo, vertices, 0, sol_parcial, sol_opt)

def dominating_set_rec(grafo, vertices, indice, sol_parcial, sol_opt):
    if len(sol_parcial) >= len(sol_opt):
        return sol_opt
    
    if es_dominating_set(grafo, sol_parcial):
        return set(sol_parcial)

    if len(vertices) == indice:
        return sol_opt

    v_actual = vertices[indice]

    sol_parcial.add(v_actual)
    sol_opt = dominating_set_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    sol_parcial.remove(v_actual)
    sol_opt = dominating_set_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    return sol_opt

def es_dominating_set(grafo, sol_parcial):
    for v in grafo.obtener_vertices():
        if v in sol_parcial: continue
        esta_dominado = False
        for w in grafo.adyacentes(v):
            if w in sol_parcial:
                esta_dominado = True
                break
        if esta_dominado == False:
            return False
    return True

#Con los 2 sets llenos
def dominating_set_rec_2(grafo, vertices, indice, sol_parcial, sol_opt):
    if len(vertices) == indice:
        if len(sol_parcial) < len(sol_opt):
            return set(sol_parcial)
        else:
            return sol_opt

    v_actual = vertices[indice]

    sol_parcial.remove(v_actual)
    if es_dominating_set(grafo, sol_parcial):
        sol_opt = dominating_set_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    sol_parcial.add(v_actual)
    sol_opt = dominating_set_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    return sol_opt
    