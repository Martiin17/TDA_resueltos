#Es muy similar al de las antenas o al de kilometros de mafia

#K es el tanque completo que tiene el camion
#destino es los kilometros desde el origen al destino
def camion_combustible(K, estaciones, destino):
    resultado = []
    combustible_restante = K
    for i in range(len(estaciones)):
        if combustible_restante >= destino:
            return resultado
        if combustible_restante >= estaciones[i]:
            combustible_restante -= estaciones[i]
            if (estaciones[i] - estaciones[i-1]) > 0:
                    destino -= estaciones[i] - estaciones[i-1]
            else:
                destino -= estaciones[i]
            continue
        else:
            if estaciones[i] == estaciones[0]:
                return []
            else:
                resultado.append(estaciones[i])
                combustible_restante = K
                if (estaciones[i] - estaciones[i-1]) > 0:
                    destino -= estaciones[i] - estaciones[i-1]
                else:
                    destino -= estaciones[i]

    if combustible_restante >= destino:
        return resultado
    else:
        return []


print(camion_combustible(3,[1,3,5,7],100))
