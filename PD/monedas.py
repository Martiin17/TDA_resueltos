#opt[n] = min(Para toda moneda M: opt[n - M]) + 1
#Siempre que n >= M
# El +1 porque agrego la moneda que estoy viendo
#Ej: [1, 5, 10], cambio a dar 70
#Me fijo: min(opt[69] + 1, opt[65] + 1, opt[60] + 1)

def problema_del_cambio(cambio, monedas):
    if cambio == 0:
        return []
    
    opt = [0] * (cambio + 1)
    
    for i in range(1, cambio+1):
        #minimo = None
        #Asumimos que siempre tiene un 1
        minimo = i
        for moneda in monedas:
            if moneda > i: continue
            #if minimo == None:
                #minimo = opt[i-moneda] + 1
            elif opt[i-moneda] + 1 < minimo:
                minimo = opt[i-moneda] + 1
        opt[i] = minimo
    
    return reconstruccion(cambio, monedas, opt)

def reconstruccion(cambio, monedas, opt):
    solucion = []
    i = len(opt) - 1

    while i > 0:
        for moneda in monedas:
            if opt[cambio - moneda] == opt[i] - 1:
                i -= moneda
                cambio -= moneda
                solucion.append(moneda)
                break
    
    return solucion

print(problema_del_cambio(21, [1,5,10]))