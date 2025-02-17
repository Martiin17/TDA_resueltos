#Quedo medio raro pero asumo que anda

#Asumo que ya viene el grafo completo
def TSP(grafo):
    vertices = grafo.obtener_vertices()
    #De la forma [costo, set(vertices)]
    sol_parcial = [-1, set()]
    sol_opt = [-1, set()]
    return TSP_rec(grafo, vertices, vertices[0], set(), 0, 0, sol_parcial, sol_opt)

def TSP_rec(grafo, vertices, v_inicial, visitados, indice, indice_inicial, sol_parcial, sol_opt):

    if len(vertices) == len(visitados):
        #El +1 porque empece con -1
        sol_parcial[0] = calcular_peso(grafo, sol_parcial) +1
        if sol_opt[0] == -1:
            return sol_parcial.copy()
        if sol_parcial[0] < sol_opt[0]:
            return sol_parcial.copy()
        else:
            return sol_opt
    
    if len(vertices) == indice_inicial:
        return sol_opt
    
    if indice < len(vertices):
        v_actual = vertices[indice]

    if len(vertices) == indice:
        #Reinicio todo pero desde otro vertice
        sol_opt = TSP_rec(grafo, vertices, vertices[indice_inicial], set(), indice, indice_inicial+1, [], sol_opt)

    sol_parcial[1].add(v_actual)
    sol_opt = TSP_rec(grafo, vertices, v_inicial, visitados, indice+1, indice_inicial, sol_parcial, sol_opt)

    sol_parcial[1].remove(v_actual)
    sol_opt = TSP_rec(grafo, vertices, v_inicial, visitados, indice+1, indice_inicial, sol_parcial, sol_opt)

    return sol_opt


def calcular_peso(grafo, sol_parcial):
    peso = 0
    for i in range(len(sol_parcial)+1):
        if i == len(sol_parcial)-1:
            #Para la vuelta
            i = -1
        peso += grafo.peso(sol_parcial[i], sol_parcial[i+1])
    return peso