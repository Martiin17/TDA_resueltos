def merge_sort(arreglo):
    return merge_sort_rec(arreglo, 0, len(arreglo) - 1)

def merge_sort_rec(arreglo, inicio, fin):
    if inicio >= fin:
        return

    mitad = (inicio + fin) // 2

    merge_sort_rec(arreglo, inicio, mitad)
    merge_sort_rec(arreglo, mitad + 1, fin)

    merge(arreglo, inicio, mitad, fin)

def merge(arr, inicio, mitad, fin):
    lado_izq = mitad - inicio + 1
    lado_der = fin - mitad
    
    left = [0] * lado_izq
    right = [0] * lado_der
    
    for i in range(lado_izq):
        left[i] = arr[inicio + i]
    for j in range(lado_der):
        right[j] = arr[mitad + 1 + j]
    
    i = j = 0
    k = inicio
    
    while i < lado_izq and j < lado_der:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < lado_izq:
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < lado_der:
        arr[k] = right[j]
        j += 1
        k += 1

# Ejemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Array ordenado:", arr)
