class medicos:
    def __init__(self):
        medicos.nombre = ""
        medicos.horario_inicio = 0
        medicos.horario_fin = 0

class paciente:
    def __init__(self):
        paciente.nombre = ""
        paciente.horario_inicio = 0
        paciente.horario_fin = 0

def turnos(medicos, pacientes):
    grafo = Grafo(es_dirigido = True)

    grafo.agregar_vertice("S")
    grafo.agregar_vertice("T")

    for medico in medicos:
        if medico not in grafo:
            grafo.agregar_vertice(medico.nombre)
        for paciente in pacientes:
            if paciente not in grafo:
                grafo.agregar_vertice(paciente.nombre)
            if medico.horario_inicio >= paciente.horario_inicio and medico.horario_fin <= paciente.horario_fin:
                grafo.agregar_arista(medico.nombre, paciente.nombre, 1)
            if not grafo.hay_arista(paciente.nombre, "T"):
                grafo.agregar_arista(paciente.nombre, "T", 1)
        grafo.agregar_arista("S", medico.nombre, 1)

    flujo = ford_fulkerson(grafo, "S", "T")

    parejas = set()

    for medico in medicos:
        for w in grafo.adyacentes(medico):
            if flujo[(medico.nombre, w)] == 1:
                parejas.add((medico.nombre, w))

    return parejas