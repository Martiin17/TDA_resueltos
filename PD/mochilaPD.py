# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    if len(elementos) == 0:
        return []
    
    resultado = []
    for i in range(len(elementos)):
        aux = []
        for j in range(W+1):
            if i == 0 or len(resultado) == 0:
                if elementos[i][1] > j:
                    aux.append(0)
                else:
                    aux.append(elementos[i][0])
                continue
            primera_op = resultado[i-1][j]
            ola = elementos[i][1]
            if elementos[i][1] <= j:
                if j-elementos[i][1] >= 0:
                    segunda_op = resultado[i-1][j-elementos[i][1]] + elementos[i][0]
                else:
                    segunda_op = elementos[i][1]
            else:
                segunda_op = 0
            aux.append(max(primera_op, segunda_op))
        resultado.append(aux)
    return reconstruccion(elementos, W, resultado)

def reconstruccion(elementos, W, matriz):
    i = len(elementos)-1
    j = W
    solucion = []
    termino = False
    while termino != True:
        if i == 0:
            if matriz[i][j] == matriz[i][j-elementos[i][1]] + elementos[i][0]:
                solucion.append(elementos[i])
            j -= elementos[i][1]
        elif matriz[i][j] == matriz[i-1][j-elementos[i][1]] + elementos[i][0]:
            #solucion.append(elementos[i])
            j -= elementos[i][1]
        i -= 1
        if i < 0 or j < 0:
            termino = True
    solucion.reverse()
    return solucion

print(mochila([(5,5), (3,3), (7,7)], 4))

#opt(n,W) = max(opt(n-1, W), opt(n-1, W - Pi) + Vi)
#opt(n-1, W - Pi) + Vi solo si Pi >= W

#Quedo fiera la reconstruccion porque no hice una de todos 0 creo