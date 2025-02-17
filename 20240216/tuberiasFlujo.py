class rio:
    def __init__(self):
        rio.nombre = ""
        rio.capacidad = 0

class zona_riego:
    def __init__(self):
        zona_riego.nombre = ""
        zona_riego.capacidad = 0

#plano = (rio, zona_riego)
def tuberias(plano):
    grafo = Grafo(es_dirigido = False)

    grafo.agregar_vertice("S")
    grafo.agregar_vertice("T")

    for rio, zona_riego in plano:
        if rio not in grafo:
            grafo.agregar_vertice(rio.nombre)
        if zona_riego not in grafo:
            grafo.agregar_vertice(zona_riego.nombre)
        
        grafo.agregar_arista("S", rio.nombre, rio.capacidad)
        grafo.agregar_arista(rio.nombre, zona_riego.nombre, rio.capacidad)
        grafo.agregar_arista(zona_riego.nombre, "T", zona_riego.capacidad)

    flujo = ford_fulkerson(grafo, "S", "T")

    maximo_flujo = 0
    actual = -1
    tuberia = None
    corte_min = obtener_corte_min(grafo, "S", "T", flujo)
    for rio, zona_riego in plano:
        if flujo[(rio.nombre, zona_riego.nombre)] > actual and (rio.nombre, zona_riego.nombre) in corte_min:
            maximo_flujo = actual
            tuberia = (rio.nombre, zona_riego.nombre)

    return tuberia    