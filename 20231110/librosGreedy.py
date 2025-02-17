
#capacidad = L
def libros_en_cajas(libros, L):
    if len(libros) == 0:
        return 0

    cajas = [0]

    for libro in libros:
        se_guardo = False
        for i in range(len(cajas)):
            if cajas[i] + libro <= L:
                cajas[i] += libro
                se_guardo = True
                break
        if se_guardo == False:
            cajas.append(libro)

    return len(cajas)

print(libros_en_cajas([3,2,2,2,5], 5))
            