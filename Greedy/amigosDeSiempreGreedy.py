#Transformamos un problema a un problema de grafos

from grafo import Grafo
# conocidos: lista de pares de personas que se conocen, cada elemento es un (a,b)
def obtener_invitados(conocidos):
    grafo = Grafo()
    #Siendo n la cant de conocidos
    #Para crear el grafo tenemos un coste O(V + E). Siendo V aprox N y siendo E = N. V <= E
    for (a,b) in conocidos:
        if a not in grafo:
            grafo.agregar_vertice(a)
        if b not in grafo:
            grafo.agregar_vertice(b)
        if not grafo.estan_unidos(a,b):
            grafo.agregar_arista(a,b)
    
    terminar = True

    while terminar:
        eliminados = set()
        #A lo sumo es O(V al cuadrado)
        for v in grafo.obtener_vertices():
            if len(grafo.obtener_adyacentes(v)) < 4:
                eliminados.add(v)
        
        if len(eliminados) == 0:
            terminar = False

        #Esta parte O(v)
        for v in eliminados:
            grafo.borrar_vertice(v)

    return grafo.obtener_vertices()

#El algoritmo es optimo! ya que solo saca cuando no conoces a otros 4 invitados

#El coste del algoritmo es O(N al cuadrado)
#Sale del O(V al cuadrado)