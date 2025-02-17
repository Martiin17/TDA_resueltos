def busqueda_binaria(arr, n):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return busqueda_binaria_rec(arr, 0, len(arr), n)

def busqueda_binaria_rec(arr, inicio, fin, n):
    if inicio >= fin:
        return -1

    mitad = (inicio + fin) //2

    if arr[mitad] == n:
        return mitad
    elif arr[mitad] > n:
        return busqueda_binaria_rec(arr, inicio, mitad, n)
    else:
        return busqueda_binaria_rec(arr, mitad+1, fin, n)

    
arr = [3, 9, 10, 27, 38, 43, 82]
print(busqueda_binaria(arr, 1))