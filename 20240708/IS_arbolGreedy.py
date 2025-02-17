
def independent_set_arbol(grafo):
    if len(grafo) == 0:
        return 0
    
    if len(grafo) <= 2:
        #Devuelvo un vertice
        return grafo.obtener_vertices()[0]

    respuesta = set()

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if w not in respuesta and len(grafo.adyacentes(v)) == 1:
                respuesta.add(v)

    return respuesta

#Este algoritmo es Greedy ya que sigue una regla sencilla:
#Si el vertice tiene grado 1 (hoja) y ninguno de los adyacentes forma parte del IS lo agregamos
#Con esto tenemos el optimo global y a partir de iterar esta regla sencilla queremos llegar al optimo general

#Este algoritmo es optimo por la peculiaridad de los arboles que permiten que las hojas sean parte del IS 
# "molestando" lo menos posible a los otros vertices ya que solo van a "bloquear" al nodo padre que a su vez
# ya fue bloqueado por las otras hojas ==> nos permite maximizar

#Otra op que dijo es que si tengo un vertice de de grado 1 --> lo saco del grafo y a su adyacente (raro)
#Los vertices que queden son parte del IS (raro)

#O(V al caudrado)