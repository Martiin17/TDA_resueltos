
#congeladores = {A: [1,7,3], B: [5,2], C:[9]}
def laboratorio(congeladores):
    mayor = 0
    for clave, valor in congeladores.items():
        actual = 0
        if len(valor) == 0:
            actual = -1
        for nro in valor:
            actual += nro
        if actual > mayor:
            mayor = actual
            congelador_mayor = clave

    resultado = 0

    for clave, valor in congeladores.items():
        if clave == congelador_mayor: 
            continue
        else:
            for nro in valor:
                resultado += nro
    
    return resultado

print(laboratorio({"A": [1,7,3], "B": [5,2], "C":[9]}))

#El algoritmo cuesta O(C*N) siendo  C los congeladores y N la cant de elementos 
#Creo que eso seria en una sola iteracion pero bueno...

#El algoritmo es Greedy ya que sigue una regla sencilla la cual busca obtener el optimo local
#La misma se realiza iterativamente intento llegar al optimo global
#En este caso nuestra regla es agregar elementos al congelador que mas perdida nos genere

#Este algoritmo es optimo ya que al haber un unico congelador estamos minimizando la perdida