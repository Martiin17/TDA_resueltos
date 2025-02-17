#elem = (peso, valor)
def mochila_bt(lista, W):
    sol_opt = [0,0]
    sol_parcial = [0,0]
    return mochila_bt_rec(lista, W, 0, sol_opt, sol_parcial)

def mochila_bt_rec(lista, W, indice, sol_opt, sol_parcial):

    if sol_parcial[0] > W:
        return sol_opt

    if sol_parcial[1] > sol_opt[1]:
       sol_opt = sol_parcial.copy()

    if len(lista) == indice:
        return sol_opt

    peso_actual = lista[indice][0]
    valor_actual = lista[indice][1]

    sol_parcial[0] += peso_actual
    sol_parcial[1] += valor_actual

    sol_opt = mochila_bt_rec(lista, W, indice+1, sol_opt, sol_parcial)

    sol_parcial[0] -= peso_actual
    sol_parcial[1] -= valor_actual

    sol_opt = mochila_bt_rec(lista, W, indice+1, sol_opt, sol_parcial)

    return sol_opt

print(mochila_bt([(3,2), (1,7), (2,4)], 5))

