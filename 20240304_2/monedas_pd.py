# 3 7 5 2
# opt = [0, 3, 7, 12, 10]
#opt_empieza_otro = [0, 0, 7, 5, 10]
#opt_empiezo_yo = [0, 3, 7, 12, 10]

#opt(i) = max(opt[0][i-2] + Mi, opt[1][i-1] + Mi, opt[1][i-1] + M0, opt[2][i] + M0)

def problema_monedas(monedas):
    if len(monedas) == 0:
        return 0
    if len(monedas) == 1:
        return monedas[0]

    optimos = []
    aux = [0] * (len(monedas)+1)
    for i in range(len(monedas)+1):
        optimos.append(aux)
    optimos[1] = monedas[0]
    optimos[2] = max(monedas[0], monedas[1])

    for i in range(3,len(monedas)):
        op1 = optimos[0,i-2] + monedas[i]
        op2 = optimos[1][i-1] + monedas[i]
        op3 = optimos[1][i-1] + monedas[0]
        op4 = optimos[2][i] + monedas[0]
        optimos[i] = max(op1, op2, op3, op4)

    return optimos

#print(problema_monedas([3, 7, 5, 2]))

#i = inicio y j = fin                                                        
#opt[i][j] = max(M[i] + opt[i+2][j], M[i] + opt[i+1][j-1], M[j] + opt[i+1][j-1], M[j] + opt[i][j-2]) 

def monedas(valores):
    n = len(valores)
    opt = [[0] * n for _ in range(n)]

    for i in range(n):
        opt[i][i] = valores[i]

    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            
            if i + 1 <= j - 1:
                opcion_tomar_primero_1 = opt[i + 1][j - 1]
            else:
                opcion_tomar_primero_1 = 0

            if i + 2 <= j:
                opcion_tomar_primero_2 = opt[i + 2][j]
            else:
                opcion_tomar_primero_2 = 0
                
            tomar_primero = valores[i] + min(opcion_tomar_primero_1, opcion_tomar_primero_2)

            if i <= j - 2:
                opcion_tomar_ultimo_1 = opt[i][j - 2]
            else:
                opcion_tomar_ultimo_1 = 0

            if i + 1 <= j - 1:
                opcion_tomar_ultimo_2 = opt[i + 1][j - 1]
            else:
                opcion_tomar_ultimo_2 = 0

            tomar_ultimo = valores[j] + min(opcion_tomar_ultimo_1, opcion_tomar_ultimo_2)

            opt[i][j] = max(tomar_primero, tomar_ultimo)

    return opt[0][n - 1]

print(monedas([3, 7, 5, 2]))