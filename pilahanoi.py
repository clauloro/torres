class nodoPila:
    def __init__(self, valor):
        self.valor = valor


class Pila:
    def __init__(self):
        self.nodos = []

    def push(self, valor):
        nodo = nodoPila(valor)
        self.nodos.append(nodo)

    def pop(self):
        if not self.is_empty():
            return self.nodos.pop().valor

    def is_empty(self):
        return len(self.nodos) == 0

    def __str__(self):
        return str([nodo.valor for nodo in self.nodos])