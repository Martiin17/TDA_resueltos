def plan_operativo(arreglo_L, arreglo_C, costo_M):
    if len(arreglo_L) == 0:
        return []

    if len(arreglo_L) == 1:
        if arreglo_C[0] < arreglo_L[0]:
            return["california"]
        else:
            return["londres"]
    
    #Seteo un dia 0
    resultado = []
    resultado.append(0)
    opt_L = []
    opt_L.append(0)
    opt_C = []
    opt_C.append(0)

    for i in range(len(arreglo_C)):
        #El indice esta ok porque en arreglo_L y arreglo_C no tienen 0
        opt_L.append(arreglo_L[i] + min(opt_L[i], opt_C[i] + costo_M))
        opt_C.append(arreglo_C[i] + min(opt_C[i], opt_L[i] + costo_M))
        resultado.append(min(opt_L[i+1], opt_C[i+1]))
    return reconstruccion(arreglo_L, arreglo_C, costo_M, opt_L, opt_C, resultado)

def reconstruccion(arreglo_L, arreglo_C, costo_M, opt_L, opt_C, resultado):
    solucion = []
    k = len(resultado) - 1
    termine_L = False
    if opt_L[k] < opt_C[k]:
        termine_L = True
        solucion.append("londres")
    else:
        solucion.append("california")
    k -= 1
    for i in range(len(resultado)-2):
        if termine_L == True:
            if opt_L[k] < opt_C[k] + costo_M:
                solucion.append("londres")
            else:
                solucion.append("california")
                termine_L = False
        else:
            if opt_C[k] < opt_L[k] + costo_M:
                solucion.append("california")
            else:
                solucion.append("londres")
                termine_L = True
        k -= 1
    solucion.reverse()
    return solucion


print(plan_operativo([1,100], [50,7], 2))



#opt(n) = min(opt_L[n], opt_C[n])
#opt_L(n) = arreglo_L[n] + min(opt_L[n-1], opt_C[n-1] + M)
#opt_C(n) = arreglo_C[n] + min(opt_C[n-1], opt_L[n-1] + M)
