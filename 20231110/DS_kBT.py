
def dominating_set_k(grafo, k):
    vertices = grafo.obtener_vertices()
    sol_parcial = set()
    sol_opt = set(vertices)
    return dominating_set_k_rec(grafo, k, vertices, 0, sol_parcial, sol_opt)

def dominating_set_k_rec(grafo, k, vertices, indice, sol_parcial, sol_opt):
    if len(sol_parcial) >= len(sol_opt):
        return sol_opt

    if es_dominating_set(grafo, sol_parcial):
        return set(sol_parcial)

    if len(vertices) == indice:
        if len(sol_opt) <= k:
            return sol_opt
        else:
            return None
    
    v_actual = vertices[indice]

    sol_parcial.add(v_actual)
    sol_opt = dominating_set_k_rec(grafo, k, vertices, indice+1, sol_parcial, sol_opt)

    sol_parcial.remove(v_actual)
    sol_opt = dominating_set_k_rec(grafo, k, vertices, indice+1, sol_parcial, sol_opt)

    return sol_opt

def es_dominating_set(grafo, sol_parcial):
    for v in grafo.obtener_vertices():
        if v in sol_parcial:
            continue
        esta_dominado = False
        for w in grafo.adyacentes(v):
            if w in sol_parcial:
                esta_dominado = True
                break
        if esta_dominado == False:
            return False
    return True