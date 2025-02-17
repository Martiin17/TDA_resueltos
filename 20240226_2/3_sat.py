def tres_sat(clausulas, variables):
    sol_parcial = [variables]
    sol_opt = [variables]
    return tres_sat_rec(clausulas, variables, 0, sol_parcial, sol_opt)

def tres_sat_rec(clausulas, variables, indice, sol_parcial, sol_opt):

    if es_tres_sat(clausulas, sol_parcial):
        return sol_parcial.copy()

    if len(variables) == indice:
        return None

    variable_actual = variables[indice]

    variable_actual = True
    sol_opt = tres_sat_rec(clausulas, variables, indice+1, sol_parcial, sol_opt)

    variable_actual = False
    sol_opt = tres_sat_rec(clausulas, variables, indice+1, sol_parcial, sol_opt)

    return sol_opt

def es_tres_sat(clausulas, sol_parcial):
    for clausula in clausulas:
        compatible = False
        for variable in sol_parcial:
            if variable not in clausula: continue
            for i in range(3):
                if clausula[i] == variable:
                    compatible = True
                    continue
        if compatible == False:
            return False
    return True