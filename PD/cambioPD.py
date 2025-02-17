def cambio(monedas, monto):
    #cada valor de este arreglo sería el valor optimo para el cambio de valor i
    #optimos=[10000000]*(monto+1)
    optimos=[-1]*(monto+1)
    #para 0 pesos necesito 0 monedas
    optimos[0]=0
    for moneda in monedas:
        for i in range(moneda,monto+1):
            #el optimo para el valor i (que se encuentra entre la moneda y el monto)
            #es el minimo entre el optimo actual o el valor i-moneda
            #EJ: si tengo el arreglo  [1, 5, 10], y busco el optimo del valor 2 con la moneda 1
            #inicialmente seria hacer min(10000000,2-1+1) diciendome que para el valor 2
            #necesitaría dos monedas
            op1 = optimos[i]
            op2 = optimos[i-moneda]+1
            if op1 == -1:
                optimos[i] = op2
            else:
                optimos[i]=min(op1,op2)
    
    return reconstruccion(optimos,monedas,monto)
    
def reconstruccion(optimos,monedas,monto):
    res=[]
    while monto > 0:
        for moneda in monedas:
            #comparamos para que moneda del arreglo llegamos al optimo del valor monto
            #en caso de que esa moneda cumpla, lo appendeamos
            if optimos[monto]==optimos[monto-moneda]+1 and monto-moneda>=0:
                res.append(moneda)
                monto-=moneda
                #rompo el ciclo porque ya no hace falta seguir buscando para ese valor
                break
    return res

print(cambio([1,5,6,9],11))