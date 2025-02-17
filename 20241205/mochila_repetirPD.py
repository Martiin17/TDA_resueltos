#opt(n,w) = max(opt(n-1, W-Pi) + Vi, opt(n-1, W), opt(n-1, W-peso_acum-Pi) + Vi)

#elementos = (peso, valor)
def mochila_repetir(elementos, W):
    if len(elementos) == 0:
        return 0

    #En este caso, aux seria como un elem extra de todos 0
    aux = [0] * W
    optimos = []
    optimos.append(aux)
    j = -1

    for elem in elementos:
        j += 1
        if elem[0] == 0:
            aux = [elem[0]] 
        else:
            aux = [0] 
        peso_llevado = 0
        for i in range(1, W+1):
            if elem[0] <= i:
                op1 = optimos[j][i-elem[0]] + elem[1]
            else:
                op1 = 0

            if peso_llevado + elem[0] <= i:
                #No creo que este bien porque solo estamos viendo el mundo del aux pero bueno
                op3 = aux[i-1] + elem[1]
                #peso_llevado += elem[0]

            op2 = optimos[j][i]
            if op1 >= op2 or op3 >= op2:
                peso_llevado += elem[0]
            aux.append(max(op1,op2))
        optimos.append(aux)

    return optimos

print(mochila_repetir([(1,5), (3,2), (3,11)], 6))