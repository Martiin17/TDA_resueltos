
#charla = (peso, inicio, fin)
def dar_charlas(charlas):
    #sol = [peso, charlas]
    sol_parcial = [0, []]
    sol_opt = [0, []]
    return dar_charlas_rec(charlas, 0, sol_parcial, sol_opt)

def dar_charlas_rec(charlas, indice, sol_parcial, sol_opt):
    
    if indice == len(charlas):
        if sol_parcial[0] < sol_opt[0]:
            return sol_opt
        else:
            sol_opt = [sol_parcial[0], sol_parcial[1].copy()]
            return sol_opt

    charla_actual = charlas[indice]

    sol_parcial[1].append(charla_actual)
    sol_parcial[0] += charla_actual[0]
    if es_compatible(charlas, sol_parcial):
        sol_opt = dar_charlas_rec(charlas, indice+1, sol_parcial, sol_opt)

    sol_parcial[1].pop()
    sol_parcial[0] -= charla_actual[0]
    sol_opt = dar_charlas_rec(charlas, indice+1, sol_parcial, sol_opt)

    return sol_opt

def es_compatible(charlas, sol_parcial):
    horarios_reservados = set()
    for charla in sol_parcial[1]:
        for horario in horarios_reservados:
            if not(charla[2] <= horario[0] or horario[1] <= charla[1]):
                return False
        aux = (charla[1], charla[2])
        if aux not in horarios_reservados:
            horarios_reservados.add(aux)
    return True  

print(dar_charlas([[5,10,13], [1, 0, 24], [3, 13, 22]]))

    