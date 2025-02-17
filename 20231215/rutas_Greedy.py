
def cobertura(casas, R, K):
    if len(casas) == 0:
        return 0

    casas.sort(reverse = False)

    
    antenas = []
    ultima_casa = casas[0]

    for i in range(len(casas)):
        if casas[i] < 0 or casas[i] > K: continue
        for j in range(len(R)):
            if ultima_casa + R[j] >= casas[i]: 
                continue
            else:
                antenas.append(ultima_casa + R[j])
                ultima_casa = casas[i]
                break

    return antenas

print(cobertura([2, 4], [1], 5))
        
