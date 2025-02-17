#Para llegar a cada valor de cambio i, debemos llegar de C formas. Para i+1, llegaremos con las C formas que teniamos para i + C+1.
#Osea no es que hay una combinación más, sino que cada combinación que teniamos para i, se le suma una moneda más. Osea prácticamente
# se duplican las combinaciones (No tan así porque es 2C+1).

#Entonces la ecuación de recurrencia sería: opt[i] += opt[i - moneda] para cada moneda en monedas y para i perteneciente a [0, cambio],
#y opt[0] = 1.
#O(n*m), siendo m len(cambio) y n len(monedas).
def problema_del_cambio_mejorado(cambio, monedas):
    opt = [0] * (cambio + 1)
    opt[0] = 1
    for moneda in monedas:
        for i in range(moneda, cambio + 1):
            opt[i] += opt[i - moneda]
    return opt[cambio]
monedas = [1, 2, 5]
cambio = 5
print(f"Formas de dar cambio de {int(cambio)} con monedas {monedas}: {problema_del_cambio_mejorado(cambio, monedas)}")