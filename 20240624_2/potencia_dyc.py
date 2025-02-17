#Tiene que ser O(log n)
def potencia(b, n):
    if n == 0:
        return 1  # Caso base: cualquier número elevado a 0 es 1
    elif n % 2 == 0:
        mitad = potencia(b, n // 2)
        return mitad * mitad  # Si es par, reducimos el problema a n/2
    else:
        return b * potencia(b, n - 1)  # Si es impar, sacamos una 'b' y reducimos a n-1

print(potencia(2,4))