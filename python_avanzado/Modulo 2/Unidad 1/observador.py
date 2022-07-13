# Permite agregar los observadores que permiten espiar al individuo
class Subject:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self):
        for observador in self.observadores:
            observador.update()

class TemaContreto(Subject):
    def __init__(self,):
        self.estado = None

    def set_estado(self, value):
        self.estado = value
        self.notificar()

    def get_estado(self,):
        return self.estado

class Observador():
    def update(self,):
        raise(NotImplementedError("Delegación de actualización"))

class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observador_a = obj
        self.observador_a.agregar(self)

    def update(self,):
        print("Actualización dentro de Obvservador ConcreteObserverA")
        self.estado = self.observador_a.get_estado()
        print("Estado= ", self.estado)

class ConcreteObserverB(Observador):
    def __init__(self, obj):
        self.observador_b = obj
        self.observador_b.agregar(self)

    def update(self,):
        print("Actualización dentro de Obvservador ConcreteObserverB")
        self.estado = self.observador_b.get_estado()
        print("Estado= ", self.estado)


tema1 = TemaContreto()
observador_a = ConcreteObserverA(tema1)
observador_b = ConcreteObserverB(tema1)
tema1.set_estado(1)
