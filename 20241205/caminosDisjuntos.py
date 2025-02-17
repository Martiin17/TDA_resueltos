#Asumo que el grafo viene sin ciclos
def caminos_disjuntos(grafo, v ,w):
    flujo = {}
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            grafo.borrar_arista(v,w)
            #Las hago de peso 1
            grafo.agregar_arista(v,w, 1)
            flujo[(v,w)] = 0
    
    red_residual = grafo.copiar()
    caminos = set()
    
    while (camino = obtener_camino_min(red_residual, v, w)) is not None:
        peso_min = obtener_peso_min(red_residual, v, w)
        for i in range(len(1, camino))
            if grafo.hay_arista(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += peso_min
            else:
                flujo[(camino[i-1], camino[i])] -= peso_min
        actualizar_red_residual(red_residual, camino[i-1], camino[i], peso_min)
        caminos.add(camino)

    return caminos    
    