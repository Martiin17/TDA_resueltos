
def k_core(grafo):
    vertices = ordenar_por_cant_adyacentes(grafo.obtener_vertices())

    resultado = set()

    for v in grafo.obtener_vertices():
        if len(resultado) == 0:
            resultado.add(v)
        else:
            conecta_con_todos = False
            for agregado in resultado:
                if grafo.estan_unidos(v, agregado):
                    conecta_con_todos = True
                else:
                    conecta_con_todos = False
            if conecta_con_todos == True:
                resultado.add(v)
    
    if len(resultado) == 1:
        resultado = set()
    
    return resultado

#Es un algoritmo Greedy ya que sigue una regla sencilla que permite llegar al optimo local y al hacer
#esta regla iterativamente se espera llegar al optimo global
#En este caso, la regla Greedy es tratar de agregar al vertice que tenga mayor cantidad de adyacentes

#Este algoritmo no es optimo ya que existen contraejemplo donde por agregar al grafo con mas adyacentes nos
#esta obligando a que mas vertices esten unidos entre si por lo que perdemos k-cores de mayor k

#Es O(V al cuadrado)

#Otra idea --> ir eliminando los vertices de menor cant de adyacentes