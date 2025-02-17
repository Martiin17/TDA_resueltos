#En esta solucion no recordamos las soluciones anteriores. Hay recalculos
#No cumple PD
#Aca vamos de los problemas mas grandes a mas pequeñas
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)

#Aca vamos de los problemas mas pequeñas a mas grandes
#Solo necesitamos recordar las ultimas 2 soluciones
def fib_dinamico(n):
   if n == 0:
       return 0
   if n == 1:
       return 1
   anterior = 0
   actual = 1
   for i in range(1, n+1):
       nuevo = actual + anterior
       anterior = actual
       actual = nuevo
   return actual