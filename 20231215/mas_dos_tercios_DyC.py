#Tiene que ser O(n)
def mas_dos_tercios(arreglo):
    resultado = mas_dos_tercios_rec(arreglo)
    if resultado == None:
        return False
    else:
        return True


def mas_dos_tercios_rec(arreglo):

    if len(arreglo) == 1:
        return aux[0]

    if len(arreglo) == 0:
        return None

    aux = []

    for i in range(0, len(arreglo)-1, 2):
        if arreglo[i] == arreglo[i+1]:
            aux.append(arreglo[i])

    candidato = mas_dos_tercios_rec(aux)

    un_tercio = len(arreglo) % 3

    if len(arreglo) % 2 != 0 and arreglo.count(-1) >  2*un_tercio:
        return arreglo[-1]  

    if candidato is not None and arreglo.count(candidato) > 2*un_tercio:
        return aux[0]
    return None


