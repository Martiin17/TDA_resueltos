#len(v) >= 3 por enunciado
def picos(v):
    return posicion_pico(v, 0, len(v)-1)

def posicion_pico(v, ini, fin):
    if ini >= fin:
        return 0
    
    mitad = (ini + fin)//2

    if v[mitad] >= v[mitad+1] and v[mitad] >= v[mitad-1]:
        return mitad

    if v[mitad+1] < v[mitad]:
        #No tengo en cuenta mitad porque si no ya hubiera entrado arriba
        return posicion_pico(v,ini,mitad-1)
    else:
        return posicion_pico(v,mitad+1,fin)

print(picos([5,3,2,0,-1]))