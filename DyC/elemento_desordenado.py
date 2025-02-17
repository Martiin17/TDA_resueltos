def elemento_desordenado(arr):
    if len(arr) == 0:
        return None
    
    return elemento_desordenado_rec(arr, 0, len(arr)-1)

def elemento_desordenado_rec(arr, inicio, fin):
    if inicio >= fin:
        return arr[0]
    
    mitad = (fin + inicio) // 2

    if mitad+1 < len(arr)-1 and arr[mitad] > arr[mitad+1]:
        return arr[mitad+1]
    if mitad-1 >= 0 and arr[mitad-1] > arr[mitad]:
        return arr[mitad-1]

    lado_izq = elemento_desordenado_rec(arr, inicio, mitad)
    lado_der = elemento_desordenado_rec(arr, mitad+1, fin)

    if lado_izq is not None:
        return lado_izq
    if lado_der is not None:
        return lado_der
    else:
        return None

print(elemento_desordenado([1,3,5,2,7,8]))
print(elemento_desordenado([1,3,5,6,7,-1]))
print(elemento_desordenado([11,3,5,6,7,8]))
#Resultados:
#2
#-1
#11