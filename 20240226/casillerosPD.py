#opt[i][j] = max(opt[i-1][j], opt[i][j-1]) + tablero[i][j]

#tablero = [[0,0,0,0], [0,0,X,-1], [0,0,-3,0]]
def casilleros(tablero, V):

    aux = [0] * (len(tablero)+1)
    optimos = []
    for j in range(len(tablero[0])-1):
        optimos.append(aux)

    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
    return optimos


print(casilleros([[0,0,0,0], [0,0,"X",-1], [0,0,-3,0]], 5))

#Del resuelto

def vida_maxima(matriz, vida, trampas):
    n = len(matriz)
    m = len(matriz[0])
    opt = [[0 for _ in range(m)] for _ in range(n)]
    opt[0][0] = vida - trampas[0][0]
    #inicializamos la primer fila y la primer columna    
    for j in range(1, m):
        if opt[0][j-1] >= 0:
            opt[0][j] = opt[0][j-1] - trampas[0][j] # puede seguir el camino
        else:
            opt[0][j] = -float('inf') #hardcodeado para que vea el algoritmo que desde aca ni en pedo se puede llegar
    #idem
    for i in range(1, n):
        if opt[i-1][0] >= 0:
            opt[i][0] = opt[i-1][0] - trampas[i][0]
        else:
            opt[i][0] = -float('inf')
    #aplicar la ec de recurrencia para el resto de las celdas
    for i in range(1, n):
        for j in range(1, m):
            vida_arriba = None
            vida_izquierda = None
            if opt[i][j-1] >= 0:
                vida_izquierda = opt[i][j-1] - trampas[i][j]
            else:
                vida_izquierda = -float('inf')

            if opt[i-1][j] >= 0:
                vida_arriba = opt[i-1][j] - trampas[i][j]
            else:
                vida_arriba = -float('inf')

            opt[i][j] = max(vida_arriba, vida_izquierda)

    return opt[n-1][m-1]

def reconstruccion(opt, n, m):
    i, j = n-1, m-1
    camino = [(i, j)]
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if opt[i-1][j] >= opt[i][j-1]:
                i -= 1
            else:
                j -= 1
        elif i > 0:
            i -= 1
        else:
            j -= 1
        camino.append((i, j))
    return camino[::-1]
