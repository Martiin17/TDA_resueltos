def cambio(monedas, monto):
    #Ordeno de mayor a menor
    monedas.sort(reverse=True)
    indice = 0
    solucion = []
    while monto > 0:
        if monedas[indice] <= monto:
            solucion.append(monedas[indice])
            monto -= monedas[indice]
        else:
            indice += 1
            if indice == len(monedas):
                break
    return solucion

print(cambio([2,5], 1))