class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
    def comer(self):
        print("comer desde persona")

# Las clases "Argentino" y "Chino" heredan los atributos y los metodos de la clase "Persona"
class Argentino(Persona):
    def __init__(self, nombre):
        self.nombre = nombre

# Polimorfismo: Permite pisar la funcionalidad de una clase de la cual hereda dentro de la clase
class Chino(Persona):
    def __init__(self, nombre):
        self.nombre = nombre
    # Prueba la propiedad de polimorfismo
    def comer():
        print("comer desde Chino")

juan = Persona("Juan Peréz")
print(juan.nombre)
print(juan.comer())

martin = Argentino("Martin Peréz")
print(martin.nombre)
print(martin.comer())

federico = Chino("Federico Peréz")
print(federico.nombre)
print(martin.comer())

# El metodo de clase __mro__ permite obtener la estructura interna de la arquitectura de clases
print(Persona.__mro__)
print(Argentino.__mro__)
print(Chino.__mro__)