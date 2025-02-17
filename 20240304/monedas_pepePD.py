#opt(i) = max(opt_agarrar_izq[i], opt_agarrar_der[i])
#opt_agarrar_izq(i) = monedas[0] + opt(i-1)
#opt_agarrar_der(i) = monedas[-1] + opt(i-1)

# 2 7 --> Agarro 7
# 2 7 3 --> Agarro 3 y 7
# 2 7 3 5 --> Agarro 5, agarro 7
# 2 7 3 5 1 --> Agarro 2, agarro 7, agarro 5
#No llegue a nada

#Bueno la ecuacion de recurrencia será -> opt[i][j] = max(v[i] + min(opt[i+2][j], opt[i+1][j-1]), v[j] + min(opt[i+1][j-1], opt[i][j-2])) 



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

valores = [8, 15, 3, 7] 
print(monedas(valores))


#Probandolo el algritmo no da la solcion optima pero bueno, debería devolver 23 pero devuelve 22.