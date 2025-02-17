#opt[n] = Sum(Para toda moneda M: opt[n-M])
#Con n >= M

def formas_cambio(monto, monedas):
    if monto == 0:
        return 0

    opt = [0] * (monto+1)
    #La forma de dar 0 de cambio es no dando nada
    opt[0] = 1

    for moneda in monedas:
        for i in range(moneda, monto+1):
            opt[i] += opt[i - moneda]
    
    return opt


print(formas_cambio(7, [1,2,5]))