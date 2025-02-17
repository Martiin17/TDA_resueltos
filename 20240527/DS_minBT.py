
def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    suma_total = 0
    for v in vertices:
        suma_total += v.obtener_valor()
    sol_parcial = [set(), 0]
    sol_opt = [set(vertices), suma_total]
    return dominating_set_min_rec(grafo, vertices, 0, sol_parcial, sol_opt)

def dominating_set_min_rec(grafo, vertices, indice, sol_parcial, sol_opt):

    if es_dominating_set(grafo, sol_parcial) and sol_parcial[1] < sol_opt[1]:
        return set(sol_parcial)

    if len(vertices) == indice:
        return sol_opt

    v_actual = vertices[indice]

    sol_parcial[0].add(v_actual)
    sol_parcial[1] += v_actual.obtener_valor()
    sol_opt = dominating_set_min_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    sol_parcial[0].remove(v_actual)
    sol_parcial[1] -= v_actual.obtener_valor()
    sol_opt = dominating_set_min_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)
    
    return sol_opt

def es_dominating_set(grafo, sol_parcial):
    aux = set()
    for v in sol_parcial[0]:
        aux.add(v)
        for w in grafo.adyacentes(v):
            if w not in aux:
                aux.add(w)
    
    if len(aux) == len(grafo.obtener_vertices()):
        return True
    else:
        return False