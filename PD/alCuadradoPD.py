#Opt(i) = min(opt(j) + opt(i-j))
#j = 1,2,..,i-1 --> O(N al cuadrado)
#Otra forma:
#Opt(i) = min(opt(j al cuadrado) + opt(i-j al cuadrado))
# ==> Opt(i) = min(1 + opt(i-j al cuadrado))
#Si j = 1,2,..raiz(i) --> O(N a la 3/2)

#Iteramos hasta que j*j < i

def min_cuadrados(n):
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

    return optimos[-1]

print(min_cuadrados(10))

#Opciones para 7
# con j = 1 --> 2ʌ2 + 1ʌ2 + 1ʌ2 + 1ʌ2 --> 4 veces 
# con j = 2 --> 2ʌ2 + 1ʌ2 + 1ʌ2 + 1ʌ2 --> 4 veces 