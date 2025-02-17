#Devolver un subgrafo con un ciclo de tamaño exactmanete k
def K_ciclo(grafo, k):
    vertices = grafo.obtener_vertices()
    sol_parcial = set()
    sol_opt = set()
    return K_ciclo_rec(grafo, vertices, 0, sol_parcial, sol_opt)

def K_ciclo_rec(grafo, vertices, indice, sol_parcial, sol_opt):

    if es_k_ciclo(grafo, sol_parcial):
        return set(sol_parcial)
    
    if len(indice) == vertices:
        if es_k_ciclo(grafo, sol_opt):
            return sol_opt
        else:
            return None

    v_actual = vertices[indice]
    
    sol_parcial.add(v_actual)
    sol_opt = K_ciclo_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    sol_parcial.remove(v_actual)
    sol_opt = K_ciclo_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    return sol_opt

def es_k_ciclo(grafo, sol_parcial):
    if len(sol_parcial) == 0:
        return False

    v_incial = sol_parcial[0]

    visitados = set()

    aux = dfs(grafo, sol_parcial, visitados, v_incial)

    if len(visitados) == len(sol_parcial):
        return True
        
    return False

def dfs(grafo, sol_parcial, visitados, v):
    visitados.add(v)

    for w in sol_parcial:
        for h in grafo.adyacentes(w):
            if h not in visitados and h in sol_parcial:
                dfs(grafo, sol_parcial, visitados, h)
    
    return visitados
