#opt(i) = min(1 + opt(i - j al cuadrado))
#j = 1, ..., raiz de i

def suma_cuadrados(n):
    optimos = [0] * (n+1)
    optimos[0] = 0
    optimos[1] = 1

    for i in range(2, n+1):
        actual = 0
        mejor = -1
        for j in range((n+1)**0,5):
            if j*j == i:
                mejor = 1
            if j*j < i:
                actual = 1 + optimos[i-j*j]
                if mejor == -1:
                    mejor = actual
            if actual < mejor:
                mejor = actual
        optimos[i] = mejor

    return reconstruccion(n, optimos)

def reconstruccion(n, optimos):
    solucion = []
    nro = optimos[-1] 
    i = 0

    while nro > 0:
        if nro != 1:
            actual = optimos[n-i]
            nro -= 1
            solucion.append(1)
        else:
            solucion.append(n-i)
            nro = -1
        i += 1
    return solucion
            
print(suma_cuadrados(25))

#O(N a la 3/2)
#Medio rara la reconstruccion pero da