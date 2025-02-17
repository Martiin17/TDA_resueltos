def determinar_adelantos(arr): 
    arrAnterior = sorted(arr, key=lambda x: x[1])
    posiciones_actuales = {jugador: idx for idx, (jugador, _) in enumerate(arr)}
    adelantos = {jugador: 0 for jugador, _ in arr}
    
    def contar_inversiones(arr, ini, fin):
        if ini >= fin:
            return 0, arr[ini:fin+1] if ini == fin else []
        
        medio = (ini + fin) // 2
        inv_izq, izq_ordenado = contar_inversiones(arr, ini, medio)
        inv_der, der_ordenado = contar_inversiones(arr, medio + 1, fin)
        
        i = j = 0
        inversiones = inv_izq + inv_der
        merged = []
        
        while i < len(izq_ordenado) and j < len(der_ordenado):
            if posiciones_actuales[izq_ordenado[i][0]] <= posiciones_actuales[der_ordenado[j][0]]:
                merged.append(izq_ordenado[i])
                i += 1
            else:
                adelantos[der_ordenado[j][0]] += len(izq_ordenado) - i
                merged.append(der_ordenado[j])
                inversiones += len(izq_ordenado) - i
                j += 1
        
        merged.extend(izq_ordenado[i:])
        merged.extend(der_ordenado[j:])
        
        return inversiones, merged
    
    contar_inversiones(arrAnterior, 0, len(arrAnterior) - 1)
    
    return adelantos

arr = [('A', 3), ('B', 4), ('C', 2), ('D', 8), ('E', 6), ('F', 5)]
adelantos = determinar_adelantos(arr)
print(adelantos)