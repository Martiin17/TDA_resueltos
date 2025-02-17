def escalones(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    aux = []
    aux.append(1)
    aux.append(1)
    aux.append(2)
    for i in range(3,n+1):
        aux.append(aux[i-3] + aux[i-2] + aux[i-1])
    return aux[n]

print(escalones(5))