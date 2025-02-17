#opt(i) = min(opt_caba[i], opt_mdz[i])
#opt_caba(i) = costo_caba[i] + min(opt_caba[i-1], opt_mdz[i-1] + M)
#opt_mdz(i) = costo_mdz[i] + min(opt_mdz[i-1], opt_caba[i-1] + M)

#M son los costos mes a mes
#len(M) = len(costo_caba) -1 porque el primer mes es gratis
def mudanzas(costo_caba, costo_mdz, M):
    if len(costo_caba) == 0:
        return 0
    if len(costo_caba) == 1:
        return min(costo_caba[0], costo_mdz[0])
    
    optimos = [0] * (len(costo_caba)+1)
    optimos_caba = [0] * (len(costo_caba)+1)
    optimos_mdz = [0] * (len(costo_caba)+1)

    optimos_caba[1] = costo_caba[0]
    optimos_mdz[1] = costo_mdz[0]
    optimos[1] = min(optimos_caba[1], optimos_mdz[1])

    for i in range(2, len(optimos)):
        optimos_caba[i] = costo_caba[i-1] + min(optimos_caba[i-1], optimos_mdz[i-1] + M[i-2])
        optimos_mdz[i] = costo_mdz[i-1] + min(optimos_mdz[i-1], optimos_caba[i-1] + M[i-2])
        optimos[i] = min(optimos_caba[i], optimos_mdz[i])
    return reconstruccion(costo_caba, costo_mdz, M, optimos, optimos_caba, optimos_mdz)

def reconstruccion(costo_caba, costo_mdz, M, optimos, opt_caba, opt_mdz):
    solucion = []
    j = len(optimos)
    if opt_caba[-1] > opt_mdz[-1]:
        termine_caba = False
        solucion.append("MDZ")
    else:
        termine_caba = True
        solucion.append("CABA")
    for i in range(2, len(optimos)):
        j -= i
        if termine_caba == True:
            if optimos[j]  == opt_caba[j]:
                solucion.append("CABA")
                termine_caba = True
            else:
                solucion.append("Mdz")
                termine_caba = False
        else:
            if optimos[j]  == opt_mdz[j]:
                solucion.append("MDZ")
                termine_caba = False
            else:
                solucion.append("CABA")
                termine_caba = True
    solucion.reverse()
    return solucion


print(mudanzas([1,100], [50,7], [2]))