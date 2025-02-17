#opt[i] = sum(opt[i - moneda]) desde moneda hasta cambio+1
#y opt[0] = 1.
#O(n*m), siendo m len(cambio) y n len(monedas).
def cant_formas_cambio(moneda, cambio):
    opt = [0] * (cambio + 1)
    opt[0] = 1
    #No es muy PD porque vas tocando todos los opts a la vez y no en orden
    for moneda in monedas:
        for i in range(moneda, cambio + 1):
            opt[i] += opt[i - moneda]
    return opt[cambio]
monedas = [1, 2, 5]
cambio = 7
print(cant_formas_cambio(monedas, cambio))