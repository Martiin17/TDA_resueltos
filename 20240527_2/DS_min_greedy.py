#Siempre en caso de que el grafo es un arbol

def ds_arbol_min(grafo):
    if len(grafo.obtener_vertices()) == 0:
        return set()
    if len(grafo.obtener_vertices()) < 2:
        return set(grafo.obtener_vertices()[0])

    solucion = set()
    
    for v in grafo.obtener_vertices():
        if len(grafo.adyacentes(v)) > 1:
            solucion.add(v)
    
    return solucion
        
#El algoritmo es Greedy ya que sigue una regla sencilla para obtener el optimo local el cual es 
#agregar en el dominating set a los padres ya que dominan una mayor cantidad de vertice que las hojas.
#Esta regla la aplicamos iterativamente para ir avanzando sobre los vertices esperando que nos lleve al
#optimo global

#En ese caso, el algoritmo es optimo ya que al seleccionar los padres maximizamos la cant de vertices dominados

#El coste es O(v)