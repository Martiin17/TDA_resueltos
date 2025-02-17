#farmacos = [[cantidad, valor, nombre]]
#Asumo que el valor es el valor de esa cantidad
def mochila_fraccionada(farmacos, L):
    farmacos.sort(key=lambda x: x[1]/x[0])

    solucion = []
    ganancia = 0

    for farmaco in farmacos:
        if farmaco[0] <= L:
            farmaco[0] = 0
            ganancia += cantidad
            solucion.append(farmaco)
        else:
            total = farmaco[0]
            farmaco[0] -= L
            porcentaje = (L/total) * 100
            ganancia += (porcentaje / 100) * valor[1]
            solucion.append(farmaco)
    return solucion

#El algoritmo es Greedy ya que sigue una regla sencilla: primero poner al farmaco con mejor relacion
#precio/peso. Esto nos asegura el optimo local y esperamos en las iteraciones lograr el optimo global.
#En este caso lo logramos ya que al poder fraccionar los elementos siempre estamos poniendo lo mejor
#que tenemos

#O(n) siendo n la cant de farmacos