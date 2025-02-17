#opt(n) = max(opt[n-3] + Gi, opt[n-1])

def lazzy_john(ganancias):
    if len(ganancias) == 0:
        return 0
    if len(ganancias) == 1:
        return ganancias[0]
    
    #Pongo dia 0
    optimos = [0] * (len(ganancias)+1)
    optimos[1] = ganancias[0]
    optimos[2] = max(ganancias[0], ganancias[1])
    for i in range(3, len(ganancias)):
        optimos[i] = max(optimos[i-3] + ganancias[i-1], optimos[i-1])
    
    return optimos[-1]

#Lo pedia por PL...