def subset_sum(elementos, v):
    if len(elementos) == 0:
        return []

    todos_ceros = [0] * (v+1)
    resultado = []
    resultado.append(todos_ceros)
    #En mochila no podia hacer esto porque podia ser que tenga peso 0 y valor != 0
    for i in range(len(elementos)):
        aux = []
        for j in range(v+1):
            if j - elementos[i] >= 0:
                primer_op = resultado[i][j-elementos[i]] + elementos[i]
            else:
                primer_op = 0
            segunda_op = resultado[i][j]
            if elementos[i] <= j:
                aux.append(max(primer_op, segunda_op))
            else:
                aux.append(segunda_op)
        resultado.append(aux)
    #return resultado
    return reconstruccion(elementos, v, resultado)

def reconstruccion(elementos, v, matriz):
    solucion = []
    i_elem = len(elementos)-1
    i = len(elementos)

    while v != 0:
        if v >= elementos[i_elem]:
            if matriz[i][v] != matriz[i-1][v]:
            #Hice lo de fijarme si el de arriba cambia (no funciona para todos los problemas)
                solucion.append(elementos[i_elem])
                v -= elementos[i_elem]
        i_elem -= 1
        i -= 1
        if i < 0 or i_elem < 0:
            v = 0
    
    solucion.reverse()
    return solucion

#opt(n, V) = max(opt(n-1, V - Vi) + Vi, opt(n-1, V))
#opt(n-1, V - Vi) + Vi si Vi <= V

print(subset_sum([1,5,2,3,1], 5))
