
def mayor_clique(grafo):
    vertices = grafo.obtener_vertices()
    sol_parcial = set()
    sol_opt = set()
    return mayor_clique_rec(grafo, vertices, 0, sol_parcial, sol_opt)

def mayor_clique_rec(grafo, vertices, indice, sol_parcial, sol_opt):

    if es_clique(grafo, sol_parcial):
        if len(sol_parcial) > len(sol_opt):
            return set(sol_parcial)

    if len(vertices) == indice:
        return sol_opt

    v_actual = vertices[indice]

    sol_parcial.add(v_actual)
    sol_opt = mayor_clique_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    sol_parcial.remove(v_actual)
    sol_opt = mayor_clique_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    return sol_opt

def es_clique(grafo, sol_parcial):
    for v in sol_parcial:
        for w in sol_parcial:
            if v == w: continue
            if not grafo.estan_unidos(v,w):
                return False
    return True