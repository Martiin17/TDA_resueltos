
#elementos = (peso, valor)
def mochila_k(elementos, W, K):
    #sol = (peso, valor, elementos)
    sol_opt = set(0, 0, [])
    sol_parcial = set(0, 0, [])
    return mochila_k_rec(elementos, W, K, 0, sol_parcial, sol_opt)

def mochila_k_rec(elementos, W, K, indice, sol_parcial, sol_opt):

    if sol_parcial[0] > W:
        return sol_opt

    if len(elementos) == indice:
        if len(sol_parcial) >= K and sol_parcial[1] > sol_opt[1]:
            return sol_parcial.copy()
        else:
            return sol_opt
        
    elem_actual = elementos[indice]

    sol_parcial[0] += elem_actual[0]
    sol_parcial[1] += elem_actual[1]
    sol_parcial[2].add(elem_actual)

    sol_opt = mochila_k_rec(elementos, W, K, indice+1, sol_parcial, sol_opt)

    sol_parcial[0] -= elem_actual[0]
    sol_parcial[1] -= elem_actual[1]
    sol_parcial[2].remove(elem_actual)

    sol_opt = mochila_k_rec(elementos, W, K, indice+1, sol_parcial, sol_opt)

    return sol_opt
