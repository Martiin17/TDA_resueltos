#Dado una lista de alturas que va en orden creciente y en un momento se vuelve decreciente
#encontrar la posicion en la cual cambia
#Ejemplo: [1.2, 1.7, 2.1, 2.0, 1.78, 1.55]
#La respuesta seria 3
#parte 2: validar que la solucion sea correcta en tiempo lineal

def alturas(arr):
    if len(arr) == 0:
        return None
    resultado = alturas_rec(arr, 0, len(arr)-1)
    val = validador(arr, resultado)
    return resultado, val

def alturas_rec(arr, inicio, fin):
    if inicio >= fin:
        return 0
    
    mitad = (inicio + fin)//2

    if mitad+1 < len(arr) and mitad-1 >= 0:
        if arr[mitad] >= arr[mitad+1] and arr[mitad] <= arr[mitad-1]:
            return mitad-1
    
    if arr[mitad] > arr[mitad+1]:
        return alturas_rec(arr, mitad+1, fin)
    else:
        return alturas_rec(arr, inicio, mitad)

print(alturas([1.2, 1.7, 2.1, 2.0, 1.78, 1.55]))

def validador(arr, indice):
    if arr[indice] >= arr[indice+1] and arr[indice] <= arr[indice-1]:
        return True
    else:
        return False