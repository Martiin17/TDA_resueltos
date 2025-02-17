# pedidos: lista de tuplas con (km inicio, km fin)
def asignar_mafias(pedidos):
    pedidos.sort(key=lambda x: x[1])

    permisos_otorgados = []
    ultimo_permiso = None

    for pedido in pedidos:
        if ultimo_permiso == None:
            permisos_otorgados.append(pedido)
            ultimo_permiso = pedido[1]
        else:
            if pedido[0] > ultimo_permiso:
                permisos_otorgados.append(pedido)
                ultimo_permiso = pedido[1]

    return permisos_otorgados

#El algoritmo es Greedy ya que con una regla sencilla busca alcanzar el optimo local 
#y a partir de iterar se busca llegar a un optimo global
#En este caso, la regla sencilla es ordenar por km de fin e ir agregando aquellos pedidos que no se superponen
#En cada iteracion si el pedido de inicio > km de fin del ultimo permiso otorgado este se agregara

#Este algoritmo es optimo (charlas) ya que al ordenar por el que primero termina nos asegura
#de dejar la mayor cant de tiempo disponible para que otros pedidos lo aprovechen

#Coste O(p) siendo p la cant de pedidos