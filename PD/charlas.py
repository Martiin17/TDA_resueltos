#opt(i) = max(opt[p[i]] + Vi, opt[i-1])
#p[i] es un vector que dice la primera charla anterior con la que no se superpone

#charla = (horario_inicio, horario_fin, valor)
def scheduling(charlas):
    if len(charlas) == 0:
        return []
    if len(charlas) == 1:
        return [charlas[0]]

    optimos = [0] * (len(charlas)+1)
    optimos[1] = charlas[0][2]

    p = generar_p(charlas)

    for i in range(1, len(charlas)):
        optimos[i+1] = max(optimos[p[i]] + charlas[i][2], optimos[i])

    return reconstruccion(charlas, optimos, p)

def reconstruccion(charlas, optimos, p):
    solucion = []
    i = len(optimos) - 1
    j = len(p)-1
    while i >= 0:
        if charlas[j][2] + optimos[p[j]] == optimos[i]:
            if charlas[i-1] in solucion:
                i = -1
                break
            solucion.append(charlas[i-1])
            i = p[j]
            j = p[j]-1
        else:
            i -= 1
            j -= 1
    solucion.reverse()
    return solucion 

def generar_p(charlas):
    charlas.sort(key=lambda x: x[1])
    #Salteo al primero
    p = [0]
    for i in range(1, len(charlas)):
        menor = None
        for j in range(i):
            if charlas[i][0] < charlas[j][1]:
                if menor == None or j < menor:
                    menor = j
        if menor == None:
            p.append(i)
        else:
            p.append(menor)

    return p

charlas = [(1,3,2), (2,5,4), (4,6,4), (1,8,7),(7,10,2),(7, 11, 1)]
charlas2 = [(1, 6, 2), (7, 11, 4), (11, 16, 2)]
charlas3 = [(5, 8, 15), (9, 11, 20)]
print(scheduling(charlas3))

#No pasan las pruebas pero a mi me corre