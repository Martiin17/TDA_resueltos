def problema_cambio(monedas, valor):
    sol_parcial = []
    sol_opt = []
    lista_claves =  list(monedas.keys())
    return problema_cambio_rec(monedas, valor, 0, sol_parcial, sol_opt, lista_claves)

def problema_cambio_rec(monedas, valor, indice, sol_parcial, sol_opt, lista_claves):

    if sum(sol_parcial) > valor:
        return sol_opt

    if sum(sol_parcial) == valor:
        return sol_parcial.copy()
    
    if sum(sol_parcial) > sum(sol_opt):
        sol_opt = sol_parcial.copy()

    if len(monedas) == indice:
        return sol_opt

    moneda_actual = lista_claves[indice] #La moneda_actual tmb es la key del dicc

    if monedas[moneda_actual] <= 0:
        sol_opt = problema_cambio_rec(monedas, valor, indice+1, sol_parcial, sol_opt, lista_claves)
    else:
        sol_parcial.append(moneda_actual)
        monedas[moneda_actual] -= 1
        sol_opt = problema_cambio_rec(monedas, valor, indice, sol_parcial, sol_opt, lista_claves)

        sol_parcial.pop()
        monedas[moneda_actual] += 1
        sol_opt = problema_cambio_rec(monedas, valor, indice+1, sol_parcial, sol_opt, lista_claves)

    return sol_opt

#print(problema_cambio({1: 3, 5: 0, 100: 5}, 5))
print(problema_cambio({1:15, 20:2, 30:5, 51:2}, 50))
