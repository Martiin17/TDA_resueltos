#Variante con que Mateo elige la moneda mas chica

#opt[i][j] = max(Mi + max(opt[i+1][j-1], opt[i+2][j]), Mj + max(opt[i+1][j-1], opt[i][j-2]))

def monedas_mateo_min(monedas):
    if len(monedas) == 0:
        return []
    if len(monedas) == 1:
        return [monedas[0]]
    
    opt = []
    aux = [0] * len(monedas)
    for i in range(len(monedas)):
        opt.append(aux.copy())

    for i in range(len(monedas)):
        indice = i
        for j in range(len(monedas)):
            i = len(monedas) - indice - 1
            if i == j:
                opt[i][j] = monedas[i]
                continue
            if i > j or j == 0:
                opt[i][j] = 0
                continue
            if i+1 < len(monedas) and j-1 >= 0:
                #S izq, M der
                op_izq_der = opt[i+1][j-1]
                op_der_izq = opt[i+1][j-1]
            else:
                op_izq_der = 0
                op_der_izq = 0
            if i+2 < len(monedas):
                op_izq_izq = opt[i+2][j]
            else:
                op_izq_izq = 0
            if j - 2 >= 0:
                op_der_der = opt[i][j-2]
            else:
                op_der_der = 0
            opt[i][j] = max(monedas[i] + max(op_izq_der, op_izq_izq), monedas[j] + max(op_der_izq, op_der_der))
    
    return reconstruccion(opt, monedas)

def reconstruccion(opt, monedas):
    monedas_s = []
    monedas_m = []
    i = 0
    j = len(opt)-1

    while i <= j:
        if monedas[j] + opt[i][j-2] == opt[i][j] and j-2 >= 0 and monedas[j-1] < monedas[i]:
            monedas_s.append(monedas[j])
            j -= 1
        elif monedas[j] + opt[i+1][j-1] == opt[i][j] and j-1 >= 0 and i+1 < len(monedas) and monedas[i] < monedas[j-1]:
            monedas_s.append(monedas[j])
            j -= 1
        elif monedas[i] + opt[i+1][j-1] == opt[i][j] and j-1 >= 0 and i+1 < len(monedas) and monedas[j] < monedas[i+1]:
            monedas_s.append(monedas[i])
            i += 1
        elif monedas[i] + opt[i+2][j] == opt[i][j] and j-1 >= 0 and i+1 < len(monedas) and monedas[i+1] < monedas[j]:
            monedas_s.append(monedas[i])
            i += 1
        if i <= j:
            if monedas[i] >= monedas[j]:
                monedas_m.append(monedas[j])
                j -= 1
            else:
                monedas_m.append(monedas[i])
                i +=1

    return monedas_s, monedas_m
print(monedas_mateo_min([1,7,5,2,3]))




#El del tp codeado como este:
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
        indice = i
        for j in range(len(monedas)):
            i = len(monedas) - indice - 1
            if i == j:
                opt[i][j] = monedas[i]
            elif j == 0 or i > j:
                opt[i][j] = 0
            elif i == j:
                opt[i][j] = monedas[i]
            else:
                if j-2 >= 0:
                    #Me quedo con la der y Mateo con la der
                    op1_der = opt[i][j-2]
                else:
                    op1_der = 0
                if i+1 < len(monedas) and j-1 >= 0:
                    #Me quedo con la der y Mateo con la izq
                    op1_izq = opt[i+1][j-1]
                    #Me quedo con la izq y Mateo con la der
                    op2_der = opt[i+1][j-1]
                else:
                    op1_izq = 0
                    op2_der = 0
                if i+2 < len(monedas):
                    #Me quedo con la izq y Mateo con la izq
                    op2_izq = opt[i+2][j]
                else:
                    op2_izq = 0
                opt[i][j] = max(monedas[j] + min(op1_izq, op1_der),monedas[i] + min(op2_izq, op2_der))

    return opt
