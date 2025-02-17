def min_tsp(grafo, v_inicial):
    visitados = set(v_inicial)
    return min_tsp_rec(grafo, v_inicial, visitados, 0, v_inicial, [])
    
def min_tsp_rec(grafo, v, visitados, acum, v_inicial, camino):
    peso_min = None
    vertice_agregar = None
    for w in grafo.adyacentes(v):
        if (grafo.peso(v,w) < peso_min or peso_min == None) and w not in visitados:
            peso_min = grafo.peso(v,2)
            vertice_agregar = w
    if vertice_agregar != None:
        visitados.add(vertice_agregar)
        camino.append(vertice_agregar)
        min_tsp_rec(grafo, vertice_agregar, visitados, acum + peso_min, v_inicial, camino)

    if len(visitados) == len(grafo.obtener_vertices()):
        acum += grafo.peso(v, v_inicial)
        return acum, camino

#El algoritmo es Greedy ya que en cada iteracion utilizamos una regla sencilla la cual es
#usar el camino (arista) de menor peso, esto nos garantiza el optimo local y usando esta regla
#esperamos llegar al optimo global
#Este algoritmo no es optimo porque si tenemos un camino muy alto que luego nos lleva a caminos muy baratos
#no los tenemos en cuenta

#El algoritmo es O(V al cuadrado)
