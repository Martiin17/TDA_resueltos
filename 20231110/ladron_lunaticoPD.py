#opt(i) = max(opt_no_primera(i), opt_no_ultima(i)), i = 0,...,n
#opt_no_primera(i) = max(opt(i-2) + Gi, opt(i-1)), i = 1,...,n
#opt_no_ultima(i) = max(opt(i-2) + Gi, opt(i-1)), i = 0,...,n-1

def lunatico(ganancias):
    # Manejo de casos base
    if len(ganancias) == 0:
        return []
    if len(ganancias) == 1:
        return [ganancias[0]]
    if len(ganancias) == 2:
        if ganancias[0] >= ganancias[1]:
            return [ganancias[0]]  
        else:
            return [ganancias[1]]

    # Considerar ambos casos: sin la última casa y sin la primera casa
    primer_caso = lunatico_acortado(ganancias[:-1])
    segundo_caso = lunatico_acortado(ganancias[1:])

    # Determinar cuál opción da mayor ganancia y reconstruir el camino
    if primer_caso[-1] >= segundo_caso[-1]:
        camino = reconstruir_camino(primer_caso, ganancias[:-1])
        return camino
    else:
        camino = reconstruir_camino(segundo_caso, ganancias[1:])
        return [x + 1 for x in camino]


def lunatico_acortado(ganancias):
    OPT = [0] * (len(ganancias))
    OPT[0] = ganancias[0]
    OPT[1] = max(ganancias[0], ganancias[1])
    for n in range(2, len(ganancias)):
        OPT[n] = max(OPT[n - 1], OPT[n - 2] + ganancias[n])
    return OPT


def reconstruir_camino(OPT, ganancias):
    camino = []
    n = len(OPT) - 1

    while n >= 0:
        if n == 0:
            camino.append(0)
            break
        
        if n == 1: #No uso n-2 para no excederme del index
            if OPT[n] > OPT[n-1]:
                camino.append(n)
                break
            n -= 1
        
        elif OPT[n - 1] >= OPT[n - 2] + ganancias[n]:
                # No se roba esta casa
                n -= 1
        else:
            # Se roba
            camino.append(n)
            n -= 2
    camino.reverse()
    return camino

print(ladron([5,3,2,1,10]))