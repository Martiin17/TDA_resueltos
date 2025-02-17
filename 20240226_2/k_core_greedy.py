def k_core(grafo, k):
    vertices = grafo.obtener_vertices()
    vertices.sort(key=lambda x: len(grafo.adyacentes(x)))

    solucion = set()

    for v in vertices:
        if len(grafo.adyacentes(v)) < k:
            continue
        if len(solucion) == 0:
            solucion.add(v)
            continue
        for w in grafo.adyacentes(v):
            if w in solucion:
                solucion.add(v)
    
    return solucion

#Es un algoritmo Greedy ya que sigue una regla sencilla que es agregar a los vertices de mayor
#cantidad de aristas primero, esto nos permite obtener el optimo local y a partir de las iteraciones
#intentamos llegar a un optimo global

#No es optimo ya que existen contraejemplos
#O(V al cuadrado)

#Otra idea es ir eliminando los de menor grado

def k_core_2(grafo, k):
    grafo2 = grafo.copy()
    hubo_cambio = True

    while hubo_cambio == True:
        hubo_cambio = False
        for v in grafo2.obtener_vertices():
            if len(grafo2.adyacentes(v)) < k:
                grafo2.eliminar_vertice(v)
                hubo_cambio = True
                break
    
    solucion = set(grafo2.obtener_vertices())
    return solucion
        