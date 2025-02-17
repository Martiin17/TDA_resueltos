#Dejo la op de emepezar con ambos sets llenos para cambiar
def vertex_cover_min(grafo):
    vertices = grafo.obtener_vertices()
    sol_parcial = set(vertices)
    sol_opt = set(vertices)
    return list(vertex_cover_min_rec(grafo, vertices, 0, sol_parcial, sol_opt))

def vertex_cover_min_rec(grafo, vertices, indice, sol_parcial, sol_opt):
    if len(vertices) == indice:
        if len(sol_opt) < len(sol_parcial):
            return sol_opt
        else:
            return set(sol_parcial)

    v_actual = vertices[indice]

    sol_parcial.remove(v_actual)
    if es_vertex_cover(grafo, sol_parcial):
        sol_opt = vertex_cover_min_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    sol_parcial.add(v_actual)
    sol_opt = vertex_cover_min_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    return sol_opt

def es_vertex_cover(grafo, sol_parcial):
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if w not in sol_parcial and v not in sol_parcial:
                return False
    return True