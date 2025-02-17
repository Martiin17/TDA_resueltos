#Asumo que todas las variables vienen dadas en True
def _3_sat(clausulas, variables):
    sol_parcial = set(variables)
    sol_opt = set()
    return _3_sat_rec(clausulas, variables, 0, sol_parcial, sol_opt)

def _3_sat_rec(clausulas, variables, indice, sol_parcial, sol_opt):
    if es_3_sat(clausulas, variables, sol_parcial):
        return set(sol_parcial)

    if len(variables) == indice:
        return sol_opt

    variable_actual = variables[indice]

    variable_actual = False
    sol_opt = _3_sat_rec(clausulas, variables, indice+1, sol_parcial, sol_opt)

    variable_actual = True
    sol_opt = _3_sat_rec(clausulas, variables, indice+1, sol_parcial, sol_opt)

    return sol_opt

def es_3_sat(clausulas, variables, sol_parcial):
    for variable in sol_parcial:
        compatible = False
        for clausula in clausulas:
            for elem in clausula:
                if elem == variable:
                    compatible = True 
                    break
        if compatible == False:
            return False
    return True