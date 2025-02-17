
def vertex_cover(grafo):
    vertices = grafo.obtener_vertices()
    #Ordeno por la cant de adyacentes
    vertices.sort(key=lambda x: len(grafo.adyacentes(x)))

    solucion = set()

    for v in vertices:
        for w in grafo.adyacentes(v):
            if w not in solucion:
                solucion.add(v)
                break
    return solucion

#El algoritmo es Greedy ya que sigue una regla sencilla para obtener el optimo local:
#agregar al vertice que tenga mayor cantidad de adyacentes ya que va a cubrir mas aristas
#esta regla se aplica iterativamente intentando alcanzar el optimo global

#Este algoritmo no es optimo ya que existen contraejemplos (en el parcial dibujar)
#El algoritmo cuesta O(V al cuadrado)