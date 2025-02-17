def juan_el_vago(trabajos):
    if len(trabajos) == 0:
        return []
    if len(trabajos) == 1:
        return [0]

    lista = [trabajos[0]]
    lista.append(max(trabajos[0], trabajos[1]))
    for i in range(2,len(trabajos)):
        if lista[i-2] + trabajos[i] >= lista[i-1]:
            lista.append(lista[i-2] + trabajos[i])
        else:
            lista.append(lista[i-1])
    return reconstruccion(lista, trabajos)

def reconstruccion(solucion, trabajos):
    indices = []
    aux = len(solucion)
    for i in range(len(solucion)):
        aux -= 1
        if solucion[aux] - trabajos[aux] == solucion[aux-2]:
            indices.append(aux)
            aux -= 1
        if aux == 0:
            if len(solucion) == 2:
                if trabajos[0] > trabajos[1]:
                    indices.append(0)
                else:
                    indices.append(1)
            elif trabajos[0] > trabajos[1] or indices[-1] == 2:
                indices.append(0)
            else:
                indices.append(1)
            break
    indices.reverse()
    return indices

print(juan_el_vago([5,5,1,1,1,1,1,1,1,1,1,1,1,11,11,1,1,1,11,1]))