class ColaPrioridad:
    def __init__(self):
        self.data = []

    def __repr__(self):
        return " , ".join(str(e) for e in self.data)

    def __len__(self):
        return len(self.data)

    def comienzocola(self, e):
        self.data.append(e)
        self.data.sort(reverse=True, key=lambda x: x[1])  # Ordenar por prioridad

    def finalcola(self):
        if self.is_empty():
            raise IndexError('Sin elementos')
        else:
            return self.data.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError('Sin elementos')
        else:
            return self.data[0]

    def is_empty(self):
        return not self.data

# Ejemplo de uso
msj = [('tarea1', 3), ('almacena', 1), ('tarea3', 2)]
mi_cola = ColaPrioridad()

for tarea, prioridad in msj:
    mi_cola.comienzocola((tarea, prioridad))

while not mi_cola.is_empty():
    tarea, prioridad = mi_cola.finalcola()
    print(f"Tarea: {tarea}, Prioridad: {prioridad}")
