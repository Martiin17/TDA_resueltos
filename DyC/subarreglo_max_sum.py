def max_subarray(arr):
    return max_subarray_rec(arr, 0, len(arr)-1, 0, 0, 0)

def max_subarray_rec(arr, inicio, fin, mejor_der, mejor_izq, mejor_mitad):
    if inicio >= fin:
        if arr[inicio] > 0:
            return [arr[inicio]]
        else:
            return []
    
    mitad = (inicio + fin)//2

    lado_izq = max_subarray_rec(arr, inicio, mitad)
    lado_der = max_subarray_rec(arr, mitad+1, fin)

    if sum(lado_izq) > mejor_izq:
        mejor_izq = lado_izq
    if sum(lado_der) > mejor_der:
        mejor_der = lado_der

def max_subarray(arr):
    if(len(arr) <= 1):
        return arr
    mitad = (len(arr)-1) //2
    max_subarray_mezclado(arr, 0, mitad, len(arr)-1)
    izq, der, max_suma = max_subarray_aux(arr, 0, len(arr) - 1)
    return arr[izq:der + 1]

def max_subarray_mezclado(arr, izq, mitad, der):
    suma_izq = arr[mitad]
    max_suma_izq = mitad
    suma = 0
    for i in range(mitad, izq - 1, -1):
        suma += arr[i]
        if suma > suma_izq:
            suma_izq = suma
            max_suma_izq = i
    
    suma_der = arr[mitad + 1]
    max_suma_der = mitad + 1
    suma = 0
    for i in range(mitad + 1, der + 1):
        suma += arr[i]
        if suma > suma_der:
            suma_der = suma
            max_suma_der = i
    
    return (max_suma_izq, max_suma_der, suma_izq + suma_der)
    
def max_subarray_aux(arr, izq, der):
    if izq == der:
        return (izq, der, arr[izq])
    
    mitad = (izq + der) // 2
    
    izq_izq, der_izq, suma_izq = max_subarray_aux(arr, izq, mitad)
    izq_der, der_der, suma_der = max_subarray_aux(arr, mitad + 1, der)
    mezclado_izq, mezclado_der, suma_mezclada = max_subarray_mezclado(arr, izq, mitad, der)
    
    max_suma = max(suma_izq, suma_der, suma_mezclada)
    if max_suma == suma_izq:
        return (izq_izq, der_izq, suma_izq)
    elif max_suma == suma_der:
        return (izq_der, der_der, suma_der)
    else:
        return (mezclado_izq, mezclado_der, suma_mezclada)
    