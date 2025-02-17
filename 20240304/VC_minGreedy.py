
def min_vertex_cover(grafo):
    vertices = ordenar_por_cant_adyacentes(grafo.obtener_vertices())

    respuesta = set()
    cubiertos = set()

    for v in vertices:
        if v not in cubiertos:
            cubiertos.add(v)
            respuesta.add(v)
            for w in grafo.adyacentes(v):
                cubiertos.add(w)
        else:
            #Como vamos por orden de cant de adyacentes, nos conviene poner a los que mas adyacentes tiene
            for w in grafo.adyacentes(v):
                if w not in cubiertos:
                    cubiertos.add(v)
                    cubiertos.add(w)
    return respuesta

#O(V al cuadrado)

#Es un algoritmo Greedy ya que sigue una regla sencilla que permite encontrar el optimo local y tiene el objetivo
#de aplicar iterativamente esta regla greedy buscando el optimo global
#la regla greedy es que elegimos el vertice que tenga mayor cantidad de adyacentes
#si no esta siendo cubierto lo agregamos al vc

#Este algoritmo no es optimo ya que, por un lado vc es NP-C por lo que no puede ser polinomico sino p = np
#Por otro lado, hay ciertos grafos donde no conviene siempre elegir el vertice de mayor cant de aristas