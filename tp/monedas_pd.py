#Variante con que Mateo usa el algoritmo Greedy

#op1 = Mateo agarra j-1 y Sophia agarra j
#op1_izq = Mateo agarra i y Sophia agarra j
#opt2_der = Mateo agarra j y Sophia agarra i
#op2_izq = Mateo agarra i+1 y Sophia agarra i
#Esta ec esta mal porque las op 1/2 y 3/4 no las elige Sophia, sino que estan en funcion
#de lo que hace Mateo
#opt[i][j] = max(Mj + opt[i][j-2], Mj + opt[i+1][j-1], Mi + opt[i+1][j-1], Mi + opt[i+2][j])

#p es una funcion que cambia los indice segun lo que elige Mateo
#Si elige la primera p(i,j) = (i+1,j)
#Si elige la ultima p(i,j) = (i,j-1)
#opt[i][j] = max(Mj + opt[p(i,j-1)], Mi + opt[p(i-1, j)])
#op1 --> Tiene j-1 porque Sophia eligio la ultima
#op1_izq --> Tiene i-1 porque Sophia eligio la primera

#Otra forma:
#opt[i][j] = max(Mi + min(opt[i+2][j], opt[i+1][j-1]), Mj + min(opt[i][j-2], opt[i+1][j-1]))

# 1 7 5 2 3 
#opt = [1, 7, 6, 9, ]

#La ec esta mal planteada, no mal implementada
def monedas_pd(monedas):
    if len(monedas) == 0:
        return []
    if len(monedas) == 1:
        return [monedas[0]]
    
    opt = []
    aux = [0] * (len(monedas))
    for i in range(len(monedas)):
        opt.append(aux.copy())

    for i in range(len(monedas)):
        for j in range(len(monedas)):
            if i == j:
                opt[i][j] = monedas[i]
            elif j == 0 or i > j:
                opt[i][j] = 0
            elif i == j:
                opt[i][j] = monedas[i]
            else:
                if j-2 >= 0:
                    #Me quedo con la der y Mateo con la der
                    op1_der = monedas[j] + opt[i][j-2]
                else:
                    op1_der = 0
                if i+1 < len(monedas) and j-1 >= 0:
                    #Me quedo con la der y Mateo con la izq
                    op1_izq = monedas[j] + opt[i+1][j-1]
                    #Me quedo con la izq y Mateo con la der
                    op2_der = monedas[i] + opt[i+1][j-1]
                else:
                    op1_izq = 0
                    op2_der = 0
                if i+2 < len(monedas):
                    #Me quedo con la izq y Mateo con la izq
                    op2_izq = monedas[i] + opt[i+2][j]
                else:
                    op2_izq = 0
                opt[i][j] = max(op1_der,op1_izq,op2_der,op2_izq)

    return reconstruccion(monedas, opt)

def reconstruccion(monedas, opt):
    solucion_s = []
    solucion_m = []
    i = 0
    j = len(opt)-1
    turno_sophia = True

    while i <= j:
        if turno_sophia == True:
            #El ya_selecciono es por no querer poner un if con mil condiciones
            ya_selecciono = False
            if i+1 < len(monedas) and j-1 >= 0 and ya_selecciono == False:
                if monedas[j] + opt[i+1][j-1] == opt[i][j] and monedas[i] >= monedas[j-1]:
                    solucion_s.append(monedas[j])
                    j -= 1
                    #i += 1
                    ya_selecciono = True
                elif monedas[i] + opt[i+1][j-1] == opt[i][j] and monedas[j] >= monedas[i+1]:
                    solucion_s.append(monedas[i])
                    #j -= 1
                    i += 1
                    ya_selecciono = True
            if j-2 >= 0 and ya_selecciono == False:
                if monedas[j] + opt[i][j-2] == opt[i][j] and monedas[j-1] >= monedas[i]:
                    solucion_s.append(monedas[j])
                    #j -= 2
                    j -= 1
                    ya_selecciono = True
            if i+2 < len(monedas) and ya_selecciono == False:
                if monedas[i] + opt[i+2][j] == opt[i][j] and monedas[i+2] >= monedas[j]:
                    solucion_s.append(monedas[i])
                    #i += 2
                    i += 1
                    ya_selecciono = True
        turno_sophia = False
        if turno_sophia == False and j >= i:
            if monedas[i] >= monedas[j]:
                solucion_m.append(monedas[i])
                i += 1
            else:
                solucion_m.append(monedas[j])
                j -= 1
            turno_sophia = True
        
    return solucion_s, solucion_m

print(monedas_pd([1,7,5,2,3]))

#Del tp

def tp2(coins):
    n = len(coins)
    opt = [[0] * n for _ in range(n)]

    # Caso base: Si solo hay una moneda, S toma esa moneda
    for i in range(n):
        opt[i][i] = coins[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            #Mateo agarra i+1, S agarra i
            op1 = coins[i] + (opt[i+2][j] if i+2 <= j and coins[i+1] > coins[j] else 0)
            #Mateo agarra j, S agarra i
            op1_izq = coins[i] + (opt[i+1][j-1] if i+1 <= j-1 and coins[j] > coins [i+1] else 0)
            #Mateo agarra i, S agarra j
            opt2_der = coins[j] + (opt[i+1][j-1] if i+1 <= j-1 and coins[i] > coins[j-1] else 0)
            #Mateo agarra j-1, S agarra j
            op2_izq = coins[j] + (opt[i][j-2] if i <= j-2 and coins[j-1] > coins[i] else 0)

            opt[i][j] = max(op1, op1_izq, opt2_der, op2_izq)

    return opt

#print(tp2([1,7,5,2]))