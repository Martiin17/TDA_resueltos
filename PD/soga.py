#OPT[n] = max(i*j, opt[i]*opt[j], opt[i]*j, opt[j]*i)
#j = n-i
#i = n-j

def problema_soga(n):
    #No hace falta porque es con n >= 2
    if n == 0:
        return 0
    
    opt = [0]*(n+1)
    opt[0] = 0
    opt[1] = 0
    opt[2] = 1

    for h in range(3, n+1):
        mejor = 0
        for j in range(1,h):
            j = h-j
            i = h-j
            op1 = i*j
            op2 = opt[i]*opt[j]
            op3 = opt[i]*j
            op4 = opt[j]*i
            if op1 > mejor:
                mejor = op1
            if op2 > mejor:
                mejor = op2
            if op3 > mejor:
                mejor = op3
            if op4 > mejor:
                mejor = op4
        opt[h] = mejor
    
    return opt[-1]

print(problema_soga(10))

#Otra forma, mas comoda
#Opt(i) = max(j * (i-j), j * opt(i-j), opt(j) * (i-j), opt(j) * opt(i-j))
#j = 1, ..., n-1
#Obs: en este caso j = 1, ..., n-1 es lo mismo que j = n-i pero yendo al reves
#Es la misma de arriba pero queda mejor el codigo

def problema_soga_2(n):
    if n < 2:
        return 0
    optimos = [0] *(n+1)
    optimos[0] = 0
    optimos[1] = 0
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