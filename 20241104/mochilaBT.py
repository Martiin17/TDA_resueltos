#Resolver, utilizando backtracking, el problema de la mochila con cantidades mínimas. Este tiene el mismo planteo al
#original pero además cuenta con un parámetro K, donde además de las condiciones impuestas para el problema original,
#se deben utilizar al menos K elementos

#elem = (peso, valor)
def mochila_min(elementos, W, K):
    sol_parcial = [0,0]
    sol_opt = [0,0]
    return mochila_min_rec(elementos, 0, W, K, sol_parcial, sol_opt)

def mochila_min_rec(elementos, indice, W, K, sol_parcial, sol_opt):

    if sol_parcial[0] > W:
        return sol_opt

    if len(sol_parcial) >= K and sol_parcial[1] > sol_opt[1]:
        sol_opt = sol_parcial.copy()
    
    if len(elementos) == indice:
        #Para evitar --> sol_opt = sol_parcial.copy()
        #if len(sol_parcial) >= K and sol_parcial[1] > sol_opt[1]:
            #return sol_parcial.copy()
        #else:
            #return sol_opt
        return sol_opt

    peso_acutal = elementos[indice][0]
    valor_actual = elementos[indice][1]

    sol_parcial[0] += peso_acutal
    sol_parcial[1] += valor_actual

    sol_opt = mochila_min_rec(elementos, indice+1, W, K, sol_parcial, sol_opt)
    

    sol_parcial[0] -= peso_acutal
    sol_parcial[1] -= valor_actual
    sol_opt = mochila_min_rec(elementos, indice+1, W, K, sol_parcial, sol_opt)

    return sol_opt

print(mochila_min([(3,2), (1,7), (2,4)], 5, 2))

#Del video
#soluciones = (peso_total, valor_total, [elememtos])
#elem = (peso, valor)
def mochila_min_rec_2(elementos, indice, W, K, sol_parcial, sol_opt):

    if len(elementos) == indice:
        return sol_opt
    
    #Poda que no es necesaria pero estaria bueno incluirla
    if len(sol_parcial) + (len(elementos) - indice - 1) < K:
        return sol_opt
    
    elem_actual = elementos[indice]

    #Se podria hacer arriba tmb
    if sol_parcial[0] + elem_actual[0] <= W:
        #Agrego elem
        sol_parcial[0] += elem_actual[0]
        sol_parcial[1] += elem_actual[1]
        sol_parcial[2].append(elem_actual)
        if len(sol_parcial) >= K and sol_parcial[1] > sol_opt[1]:
            sol_opt = sol_parcial.copy()
        sol_opt = mochila_min_rec_2(elementos, indice+1, W, K, sol_parcial, sol_opt)

        sol_parcial[0] -= elem_actual[0]
        sol_parcial[1] -= elem_actual[1]
        sol_parcial[2].pop()

    sol_opt = mochila_min_rec_2(elementos, indice+1, W, K, sol_parcial, sol_opt)
    return sol_opt