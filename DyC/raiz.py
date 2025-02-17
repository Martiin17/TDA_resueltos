def parte_entera_raiz(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return parte_entera_raiz_rec(1, n, 1, n)

def parte_entera_raiz_rec(inicio, fin, resultado, n):
    if inicio >= fin:
        return resultado
    
    mitad = (fin+inicio)//2

    if mitad*mitad <= n and mitad * mitad > resultado*resultado:
        resultado = mitad
    
    if mitad*mitad > n:
        return parte_entera_raiz_rec(inicio, mitad, resultado, n)
    else:
        return parte_entera_raiz_rec(mitad+1,fin, resultado, n)

print(parte_entera_raiz(26))
#Lo habia hecho con una lista de los valores de 1 a n y tuve: O(n)

#T(n) = T(n/2) + O(n)

#A = 1, B = 2, C = 1
#log en base 2 de 1 = 0
# ==> O(n)

#Para que sea O(log n)s

# log en base B de A == C
# ==> C tiene que ser 0
# A = 1, B = 2, C = 0
# ==> O(log n)