def quicksort(arr, inicio, fin):
    if inicio >= fin:
        return
    
    pivote = particion(arr, inicio, fin)
    
    quicksort(arr, inicio, pivote - 1)
    quicksort(arr, pivote + 1, fin)

def particion(arr, inicio, fin):
    pivote = arr[fin]  # Elegimos el último elemento como pivote
    i = inicio - 1
    
    for j in range(inicio, fin):
        if arr[j] < pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Intercambiar elementos
    
    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]  # Colocar el pivote en su posición final
    return i + 1

# Ejemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
quicksort(arr, 0, len(arr) - 1)
print("Array ordenado:", arr)
