# sol = {b1: (coordenada i del 1er barco, coordenada j del 1er barco), ...}
# barcos = {b1: largo 1er barco, ...}
def validador(n, m, barcos, restriccion_i, restriccion_j, sol):
    if len(sol) != len(barcos):
        return False
    
    posiciones_vistas = set()
    for clave, valor in sol.items():
        #Si me salgo de los limites
        if i > n or j > m:
            return False
        #Pruebo que no haya adyacentes
        if (i+1, j) in posiciones_vistas:
            return False
        if (i+1, j+1) in posiciones_vistas:
            return False
        if (i+1, j-1) in posiciones_vistas:
            return False
        if (i, j+1) in posiciones_vistas:
            return False
        if (i-1, j) in posiciones_vistas:
            return False
        if (i-1, j-1) in posiciones_vistas:
            return False
        if (i-1, j+1) in posiciones_vistas:
            return False
        if (i, j-1) in posiciones_vistas:
            return False    
        posiciones_vistas.add(valor) 
        esta = False
        for barco, largo in barcos.items():
            if clave == barco:
                esta = True
                #Si el largo no es el mismo al del problema --> return false
                if largo != abs(i-j):
                    return False
                break
        if esta == False:
            return False
    
    return True
            
