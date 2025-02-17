def max_sumatoria_n(elementos, n):
    sol_opt = []
    sol_parcial = []
    return max_sumatoria_n_rec(elementos, n, 0, sol_opt, sol_parcial)

def max_sumatoria_n_rec(elementos, n, indice, sol_opt, sol_parcial):

    if sum(sol_parcial) > n:
        return sol_opt

    if sum(sol_parcial) == n:
        return sol_parcial.copy()
    
    if sum(sol_parcial) > sum(sol_opt):
        sol_opt = sol_parcial.copy()
    
    if len(elementos) == indice:
        return sol_opt

    elem_actual = elementos[indice]

    sol_parcial.append(elem_actual)

    sol_opt = max_sumatoria_n_rec(elementos, n, indice+1, sol_opt, sol_parcial)

    sol_parcial.pop()

    sol_opt = max_sumatoria_n_rec(elementos, n, indice+1, sol_opt, sol_parcial)

    return sol_opt

print(max_sumatoria_n([3,7,2], 9))
print(max_sumatoria_n([7,5,2,6,1,3], 14))
print(max_sumatoria_n([8,3,1], 5))
