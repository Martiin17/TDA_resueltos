class Ambulancia:
    def __init__(self):
        Ambulancia.nombre = ""
        Ambulancia.distancia = 0

class Pedido:
    def __init__(self):
        Pedido.nombre = ""
        Pedido.distancia = 0
 
def cruz_roja_pedidos(pedidos, ambulancias):
    grafo = Grafo(es_dirigido = True)

    grafo.agregar_vertice("S")
    grafo.agregar_vertice("T")

    for ambulancia in ambulancias:
        if ambulancia not in grafo:
            grafo.agregar_vertice(ambulancia.nombre)
        if not grafo.estan_unidos("S", ambulancia.nombre):
            grafo.agregar_arista("S", ambulancia.nombre, 1)
        for pedido in pedidos:
            if pedido not in grafo:
                grafo.agregar_vertice(pedido.nombre)
            if not grafo.estan_unidos(pedido.nombre, "T"):
                grafo.agregar_arista(pedido.nombre, "T", 1)
            if not grafo.estan_unidos(ambulancia.nombre, pedido.nombre) and ambulancia.distancia >= pedido.distancia:
                grafo.agregar_arista(ambulancia.nombre, pedido.nombre, 1)

    flujo_max = ford_fulkerson(grafo)

    conexiones = set()

    for ambulancia in ambulancias:
        for pedido in grafo.adyacentes(ambulancia):
            if flujo_max[ambulancia, pedido] == 1:
                conexiones.add(ambulancia, pedido)

    return conexiones
    