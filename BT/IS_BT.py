def independent_set(grafo):
    vertices = grafo.obener_vertices()
    sol_opt = set()
    sol_parcial = set()
    return list(independent_set_rec(grafo, vertices, 0, sol_parcial, sol_opt))

def independent_set_rec(grafo, vertices, indice, sol_parcial, sol_opt):
    if len(vertices) == indice:
        if len(sol_parcial) > len(sol_opt):
            return set(sol_parcial)
        else:
            return sol_opt

    v_actual = vertices[indice]

    sol_parcial.add(v_actual)
    if es_independent_set(grafo, sol_parcial):
        sol_opt = independent_set_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    sol_parcial.remove(v_actual)
    sol_opt = independent_set_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    return sol_opt

def es_independent_set(grafo, sol_parcial):
    for v in sol_parcial:
        for w in grafo.adyacentes(v):
            if w in sol_parcial:
                return False
    return True

#Empiezo con sol_opt llena
def independent_set_2(grafo):
    vertices = grafo.obener_vertices()
    sol_opt = set(vertices)
    sol_parcial = set()
    return list(independent_set_rec_2(grafo, vertices, 0, sol_parcial, sol_opt))

def independent_set_rec_2(grafo, vertices, indice, sol_parcial, sol_opt):
    if len(sol_opt) > len(sol_parcial):
        return sol_opt
    
    if es_independent_set(grafo, sol_parcial):
        return set(sol_parcial)

    if len(vertices) == indice:
        return sol_opt

    v_actual = vertices[indice]

    sol_parcial.remove(v_actual)
    sol_opt = independent_set_rec_2(grafo, vertices, indice+1, sol_parcial, sol_opt)

    sol_parcial.add(v_actual)
    sol_opt = independent_set_rec_2(grafo, vertices, indice+1, sol_parcial, sol_opt)

    return sol_opt