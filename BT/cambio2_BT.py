
def cambio(n, monedas, cantidad_x_monedas):
    sol_parcial = []
    sol_opt = []
    for clave, valor in cantidad_x_monedas.items():
        for i in range(valor):
            sol_opt.append(clave)
    return cambio_rec(n, monedas, cantidad_x_monedas, 0, sol_parcial, sol_opt)

def cambio_rec(n, monedas, cantidad_x_monedas, indice, sol_parcial, sol_opt):

    if sum(sol_parcial) >= n:
        if sum(sol_parcial) > sum(sol_opt):
            return sol_opt
        else:
            return sol_parcial.copy()

    if len(monedas) == indice:
        return sol_opt
    
    moneda_actual = monedas[indice]
    if cantidad_x_monedas[moneda_actual] > 0:
        sol_parcial.append(moneda_actual)
        cantidad_x_monedas[moneda_actual] -= 1
        sol_opt = cambio_rec(n, monedas, cantidad_x_monedas, indice, sol_parcial, sol_opt)
    
    if len(sol_parcial) > 0:
        sol_parcial.pop()
        cantidad_x_monedas[moneda_actual] += 1
    sol_opt = cambio_rec(n, monedas, cantidad_x_monedas, indice+1, sol_parcial, sol_opt)

    return sol_opt

print(cambio(50, [1, 20, 30, 51], {1:15, 20:2, 30:5, 51:2}))