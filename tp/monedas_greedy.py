
def monedas_greedy(monedas):
    if len(monedas) == 0:
        return 0
    
    #Pongo que moneda agarra cada uno
    monedas_s = []
    monedas_m = []

    i = 0
    j = len(monedas) - 1

    while i < j:
        if monedas[i] >= monedas[j]:
            monedas_s.append(monedas[i])
            i += 1
            if monedas[i] >= monedas[j]:
                monedas_m.append(monedas[j])
                j -= 1
            else:
                monedas_m.append(monedas[i])
                i += 1
        else:
            monedas_s.append(monedas[j])
            j -= 1
            if monedas[i] >= monedas[j]:
                monedas_m.append(monedas[j])
                j -= 1
            else:
                monedas_m.append(monedas[i])
                i += 1
    
    if len(monedas_m) + len(monedas_s) < len(monedas):
        #Si es impar me va a quedar i=j sin agregar
        #Como S tiene los impares se lo agregamos
        monedas_s.append(monedas[i])

    return monedas_m, monedas_s

print(monedas_greedy([1, 5, 7, 2, 11, 3, 4]))

#Como lo hicimos en el tp

def tp1(monedas):
    turno_sofia = True
    suma_sofia = 0
    decisiones = [] 
    i = 0
    j = len(monedas) - 1

    while i <= j:
        if turno_sofia == True:
            if monedas[i] > monedas[j]:
                suma_sofia += monedas[i]
                decisiones.append("Primera moneda para Sophia")
                i += 1
            else:
                suma_sofia += monedas[j]
                decisiones.append("Última moneda para Sophia")
                j -= 1

            turno_sofia = False
            
        else:
            if monedas[i] < monedas[j]:
                i += 1
                decisiones.append("Primera moneda para Mateo")
            else:
                j -= 1
                decisiones.append("Última moneda para Mateo")
            
            turno_sofia = True

    return decisiones, suma_sofia


