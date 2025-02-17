def sumatorias_n(lista, n):
    return subset_sum(lista, 0, n, [])

def subset_sum(L, index, n, solucion_parcial):
	# Si encuentro una solucion la devuelvo
	if sum(solucion_parcial) == n:
		return solucion_parcial
	
	# Si por esta rama me paso, dejo de probar
	if sum(solucion_parcial) > n or index >= len(L):
		return []

	solucion_parcial.append(L[index])
	solucion = subset_sum(L, index+1, n, solucion_parcial)
    
	if solucion != []: # en este caso hay solución válida
		return solucion
	solucion_parcial.pop()

	return subset_sum(L, index+1, n, solucion_parcial)


#print(sumatorias_n([3,7,2], 9))
#print(sumatorias_n([7,5,2,6,1,3], 14))

