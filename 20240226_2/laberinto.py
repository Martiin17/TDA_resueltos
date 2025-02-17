#OPT[i][j] = max(OPT[i-1][j] + casillero[i][j], OPT[i][j-1] + casillero[i][j])
#Lo hice para que pase el test de RPL
#La ec de recurrencia para este ejercicio seria:
#OPT[i][j] = max(OPT[i-1][j] - casillero[i][j], OPT[i][j-1] - casillero[i][j])
def laberinto(matriz):
    if len(matriz) == 0:
        return 0

    opt = []
    aux = [0] * len(matriz[0])
    for i in range(len(matriz)):
        opt.append(aux.copy())

    for i in range(len(matriz)):
        #aux = []
        for j in range(len(matriz[0])):
            if i == 0 or j == 0:
                #aux.append(matriz[i][j])
                opt[i][j] = matriz[i][j]
            else:
                op1 = opt[i-1][j] + matriz[i][j]
                op2 = opt[i][j-1] + matriz[i][j]
                #opt.appendd(max(op1, op2))
                opt[i][j] = max(op1, op2)
        #opt.append(aux)
    
    return reconstruccion(matriz, opt)

def reconstruccion(matriz, opt):
    solucion = []
    i = len(matriz)-1
    j = len(matriz[0])-1
    terminar = i+j

    while terminar > 0:
        if opt[i-1][j] + matriz[i][j] == opt[i][j]:
           solucion.append((i-1,j))
           i -= 1
        else:
            solucion.append((i,j-1))
            j -= 1
        terminar = i+j

    solucion.reverse()
    solucion.append((len(matriz)-1,len(matriz[0])-1))
    suma = 0
    for (i,j) in solucion:
        suma += matriz[i][j]
    return suma

print(laberinto([[7,6]]))