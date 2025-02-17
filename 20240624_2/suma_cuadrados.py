#opt(n) = (1 +opt[i - j al cuadrado])
#j = 1, ..., raiz de n

def suma_cuadrados(n):
    optimos = [0] * (n+1)
    optimos[0] = 0
    optimos[1] = 1

    for i in range(2, n+1):
        actual = 0
        mejor = -1
        for j in range((i+1)**0,5):
            if j*j == i:
                mejor = 1
            if j*j < i:
                actual = 1 + optimos[i-j*j]
                if mejor == -1:
                    mejor = actual
            if actual < mejor:
                mejor = actual
        optimos[i] = mejor
    
    return reconstruccion(optimos, n)

def reconstruccion(optimos, n):
    solucion = []
    indice = len(optimos)-1
    while indice > 0:
        if optimos[indice] != 1:
            solucion.append(1)
        else:
            solucion.append(indice**0.5)
            indice = -1
        indice -= 1
    return solucion

print(suma_cuadrados(10))
