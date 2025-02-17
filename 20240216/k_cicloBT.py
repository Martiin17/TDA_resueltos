
def k_ciclo(grafo, k):
    vertices = grafo.obtener_vertices()
    sol_parcial = set()
    sol_opt = set()
    respuesta = k_ciclo_rec(grafo, vertices, k, 0, sol_parcial, sol_opt)
    if len(respuesta) == k:
        return respuesta
    else:
        None


def k_ciclo_rec(grafo, vertices, k, indice, sol_parcial, sol_opt):
    if len(sol_parcial) <= len(sol_opt):
        return sol_opt

    if es_k_ciclo(grafo, sol_parcial):
        return set(sol_parcial)

    if len(sol_opt) == k:
        return sol_opt
    
    if indice == len(vertices):
        return sol_opt
    
    v_actual = vertices[indice]

    sol_parcial.add(vertices)
    sol_opt = k_ciclo_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    sol_parcial.remove(vertices)
    sol_opt = k_ciclo_rec(grafo, vertices, indice+1, sol_parcial, sol_opt)

    return sol_opt

def es_k_ciclo(grafo, sol_parcial):
    v_inical = sol_parcial[0]
    for v in sol_parcial:
        if len(grafo.adyacentes(v)) != 1:
            return False
        v_ultimo = v
    if not grafo.estan_unidos(v_ultimo, v_inical):
        return False
    return True

#Creo que el mio esta mal porque no pruebo todos los inicios

def ciclo_k(grafo, k):
    for v in grafo:
        resultado = []
        if bt(grafo, k, resultado, set(), v, v):
            return resultado
    return None

def bt(grafo, k, posible_solucion, visitados, v_inicio, v):
    posible_solucion.append(v)
    visitados.add(v)

    if len(posible_solucion) == k:
        if v_inicio in grafo.adyacentes(v):
            posible_solucion.append(v_inicio)
            return True
        else:
            posible_solucion.pop()
            visitados.remove(v)
            return False

    for w in grafo.adyacentes(v):
        if w not in visitados:
            if bt(grafo, k, posible_solucion, visitados, v_inicio, w):
                return True

    posible_solucion.pop()
    visitados.remove(v)
    return False