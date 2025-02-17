
def dominating_set_min(grafo):
    copia = grafo.copy()

    resultado = set()
    
    while len(copia.obtener_vertices()) != 0:

        if len(copia.obtener_vertices()) == 1:
            resultado.add(copia.obtener_vertices()[0])

        for v in copia.obtener_vertices():
            if len(copia.adyacentes(v)) == 1:
                continue
            else:
                for w in copia.adyacentes(v):
                    resultado.add(v)
                    copia.eliminar_vertice(w)
            copia.eliminar_vertice(v)

    return resultado

#El algoritmo es Greedy ya que en cada iteracion seguimos una regla Greedy que es si no es una hoja
#agregamos al vertice en el conjunto y sacamos a a el y a sus adyacentes del grafo
#siguiendo esta regla iterativamente esperamos llegar a un optimo global

#El algoritmo es optimo ya que al esquivar las hojas nos permite elegir un padre y de esta forma
#obtener un dominating set mas pequeño dado que el grafo es un arbol