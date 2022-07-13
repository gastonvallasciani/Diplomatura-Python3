# Permite agregar los observadores que permiten espiar al individuo
class Subject:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)

class Observador():
    def update(self,):
        raise(NotImplementedError("Delegación de actualización"))

class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observador_a = obj
        self.observador_a.agregar(self)

    def update(self, *args):
        print("Actualización dentro de Obvservador ConcreteObserverA")
        print("Aqui estan los parametros: ", args)

