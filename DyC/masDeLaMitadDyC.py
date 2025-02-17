def mas_de_la_mitad(arr):
    #Para el primero
    #resultado = mas_de_la_mitad_rec(arr, 0, len(arr)-1)
    #if resultado is not None:
        #return True
    #else:
        #return False
    #Para el segundo
    candidato = mas_de_la_mitad_2(arr)
    if candidato is not None:
        return True
    else:
        return False

#En O(n log n)
def mas_de_la_mitad_rec(arr, inicio, fin):
    if fin - inicio < 1:
        return arr[inicio]
    
    mitad = (inicio + fin)//2

    e1 = mas_de_la_mitad_rec(arr, inicio, mitad)
    e2 = mas_de_la_mitad_rec(arr, mitad+1, fin)
    contador_1 = 0
    contador_2 = 0
    for i in range(inicio, fin + 1):
        if arr[i] == e1:
            contador_1 += 1
        if arr[i] == e2:
            contador_2 += 1
    if contador_1 > (fin-inicio)//2:
        return e1
    if contador_2 > (fin-inicio)//2:
        return e2
    return None
    

#En O(N)
def mas_de_la_mitad_2(arr):
    #En este caso podemos poner len(arr) == 1 porque solo hacemos una llamda recursiva
    #T(N) = T(N/2) + O(N)
    #En el de arriba se hacian 2 llamadas recursivas
    #T(N) = 2T(N/2) + O(N)
    if len(arr) == 1:
        return arr[0]

    if len(arr) == 0:
        return None
    
    aux = []
    for i in range(0, len(arr)-1, 2):
        if arr[i] == arr[i+1]:
            aux.append(arr[i])

    #if aux == []:
        #return None
    #No consideraba el impar

    candidato = mas_de_la_mitad_2(aux)

    if candidato is not None and arr.count(candidato) > len(arr) // 2:
        return candidato
    #Caso impar    
    if len(arr) % 2 != 0 and arr.count(-1) > len(arr) // 2:
        return arr[-1]
    return None

print(mas_de_la_mitad([1, 1, 1, 2, 3]))