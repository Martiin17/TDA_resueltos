#Grafo pesado, dirigido asumo
def min_tsp(grafo, v_inicio):
    suma_total = 0
    vistos = set()
    v_actual = v_inicio
    camino = [v_inicio]
    while len(vistos) != len(grafo.obtener_vertices()):
        coste_min = -1
        v_menor_coste = None
        for w in grafo.adyacentes(v_actual):
            if coste_min == -1:
                coste_min = grafo.obtener_peso(v_actual, w)
                v_menor_coste = w
            if grafo.obtener_peso(v_actual, w) < coste_min:
                coste_min = grafo.obtener_peso(v_actual, w)
                v_menor_coste = w
        suma_total += grafo.obtener_peso(v_actual, v_menor_coste)
        v_actual = v_menor_coste
        vistos.add(v_menor_coste)
        camino.append(v_menor_coste)
    
    #El grafo es completo asi que para pegar la vuelta volvemos del ultimo que vimos
    suma_total += grafo.obtener_peso(v_menor_coste, v_actual)
    camino.append(v_menor_coste)

    return suma_total, camino

#Es un algoritmo Greedy ya que sigue una regla sencilla para obtener el optimo local esperando obtener un optimo global
#la regla sencilla es ir al vertice adyacente con menor coste

#Este algoritmo no es optimo ya que por ejemplo podemos tener una arista de peso mayor pero que luego nos lleve a otras
#con un peso menor

#El coste del algoritmo es O(v al cuadrado)