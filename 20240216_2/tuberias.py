def tuberias(plano):
    grafo = Grafo(es_dirigido = True)

    grafo.agregar_vertice("S")
    grafo.agregar_vertice("T")

    for (zona_riego, cantidad) in plano:
        if zona_riego.nombre not in grafo:
            grafo.agregar_vertice(zona_riego.nombre)
        grafo.agregar_arista("S", zona_riego.nombre, cantidad)
        grafo.agregar_arista(zona_riego.nombre, zona_riego.nombre, cantidad)
        grafo.agregar_arista(zona_riego.nombre, "T", cantidad)
    
    flujo_max = ford_fulkerson(grafo, "S", "T")
    mayor = -1
    tuberia = None

    #Creo que por como es mi grafo safo pero si no deberia ver las aristas que son parte del corte min
    for zona_riego in plano:
        if flujo_max[("S", zona_riego.nombre)] > mayor or tuberia == None:
            mayor = flujo_max[("S", zona_riego.nombre)] 
            tuberia = ("S", zona_riego.nombre)
    
    return mayor, tuberia

#O(V+E) por ser con forma bipartito