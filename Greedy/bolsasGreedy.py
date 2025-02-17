def bolsas(capacidad, productos):
    if len(productos) == 0:
        return []
    productos.sort(reverse = True)
    bolsas = [0]
    for producto in productos:
        for i in range(len(bolsas)):
            if producto + bolsas[i] <= capacidad:
                bolsas[i] += producto
                break
            if i == len(bolsas)-1:
                bolsas.append(0)
                bolsas[-1] += producto
    return bolsas

print(bolsas(5, [4, 2, 1, 3, 5]))