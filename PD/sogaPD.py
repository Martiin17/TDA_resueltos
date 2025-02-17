#OPT(i) = max(max(j, opt(j)) * max(i-j, opt(i-j)))
# j = 1,2,...,i-1
#Otra forma:
#Opt(i) = max(j * (i-j), j * opt(i-j), opt(j) * (i-j), opt(j) * opt(i-j))

def problema_soga(n):
    if n < 2:
        return 0
    optimos = [0] *(n+1)
    optimos[0] = 0
    optimos[1] = 1
    optimos[2] = 1

    for i in range(3, n+1):
        mejor = 0
        actual = 0
        for j in range(i):
            primera_op = j * (i-j)
            segunda_op = j * optimos[i-j]
            tercera_op = optimos[j] * (i-j)
            cuarta_op = optimos[j] * optimos[i-j]
            actual = max(primera_op, segunda_op, tercera_op, cuarta_op)
            if actual > mejor:
                mejor = actual
        optimos[i] = mejor
    
    return optimos[-1]

print(problema_soga(10))
