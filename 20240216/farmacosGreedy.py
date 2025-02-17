#Es mochila donde podemos partir

#elemento = (peso, valor, cantidad)
def farmacos(elementos, L):
    elementos.sort(key=lambda x: x[1] / x[0])

    solucion = []
    robado = 0

    for elem in elementos:
        se_uso = False
        for restante in range(1, elem[2]+1):
            if elem[0] <= L:
                #Asumo que el peso y el valor es por ml
                #El peso tmb es en ml
                robado += elem[1]
                L -= elem[0]
                elem[2] -= 1
                se_uso = True
            else:
                if se_uso == True:
                    solucion.append(elem)
                break
    
    return solucion, robado

print(farmacos([[2,3,2], [4,1,7], [4,55,1]], 7))

#Es un algoritmo Greedy porque sigue la regla sencilla de robar primero los farmacos con mayor relacion valor/peso
#esta regla la realizamos iterativamente para cada elemento esperando llegar al optimo global
#En cada paso obtenemos el optimo local

#Este algoritmo es optimo ya que al poder fraccionar los elementos podemos llevarnos lo que mas nos convenga de
#cada elemento

#El coste es de O(elem * cantidad)


#Del resuelto

#Asumo que precios es un diccionario, cantidades es otro diccionario y medicamentos es una lista
def medicamentos(medicamentos, L, cantidades, precios):
    medicamentos_ordenados = sorted(medicamentos, key=lambda x: precios[x]/cantidades[x], reverse=True)
    cantidad_actual = 0
    resultado = []
    for medicamento in medicamentos_ordenados:
        if cantidad_actual + cantidades[medicamento] <= L:
            resultado.append((medicamento, cantidades[medicamento]))
            cantidad_actual += cantidades[medicamento]
        else:
            cantidad_a_llevarse = L - cantidad_actual
            resultado.append((medicamento, cantidad_a_llevarse))
            cantidad_actual += cantidad_a_llevarse
    return cantidad_actual, resultado