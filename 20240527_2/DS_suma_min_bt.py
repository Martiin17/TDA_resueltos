
def ds_suma_min(grafo):
    vertices = grafo.obtener_vertices()
    #sol = suma, vertices
    sol_parcial = [0, set()]
    aux = 0
    for v in grafo.obtener_vertices():
        aux += v.obtener_valor()
    sol_opt = [aux, set()]
    return ds_suma_min_rec(grafo, vertices, 0, sol_parcial, sol_opt)

def ds_suma_min_rec(grafo, vertices, indice, sol_parcial, sol_opt):

    if es_dominating_set(grafo, sol_parcial) and sol_parcial[0] > sol_opt[0]:
        sol_opt = [sol_parcial[0], set(sol_parcial[1])]
    
    if len(vertices) == indice:
        return sol_opt
    
    v_actual = vertices[indice]

    sol_parcial[0] += v_actual.obtener_valor()
    sol_parcial[1].add(v_actual)

    sol_opt = ds_suma_min_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)
    sol_parcial[0] -= v_actual.obtener_valor()
    sol_parcial[1].remove(v_actual)
    sol_opt = ds_suma_min_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    return sol_opt

def es_dominating_set(grafo, sol_parcial):
    for v in grafo.obtener_vertices():
        if v in sol_parcial: continue
        else:
            esta_dominado = False
        for w in grafo.adyacentes(v):
            if w in sol_parcial:
                esta_dominado = True
                break
        if esta_dominado == False:
            return False
    return True