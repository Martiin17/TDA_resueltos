def mas_de_la_mitad(arr):
    resultado = mas_de_la_mitad_rec(arr)
    if resultado != None:
        return True
    else:
        return False
        
def mas_de_la_mitad_rec(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    aux = []
    for i in range(0, len(arr)-1, 2):
        if arr[i] == arr[i+1]:
            aux.append(arr[i])
    
    candidato = mas_de_la_mitad_rec(aux)

    if candidato is not None and arr.count(candidato) > len(arr)//2:
        return candidato

    if len(arr)%2 != 0 and arr.count(arr[-1]) > len(arr)//2:
        return arr[-1]

    return None        

print(mas_de_la_mitad([1, 2, 1, 2, 3])) #False
print(mas_de_la_mitad([1, 1, 2, 3])) #False
print(mas_de_la_mitad([1, 2, 3, 1, 1, 1])) #True
print(mas_de_la_mitad([1])) #True

#T(n) = T(n/2) + O(n)

#log en base 2 de 1 = 0
# A = 1, B = 2, C = 1
# ==> O(n) siendo n la cant de elementos