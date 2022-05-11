"""

Ejercicio 3
------------

a)	Cree una clase hija del ejercicio de la unidad 1 llamada “Trenes” y utilice el método del ejercicio 
(creado en la clase padre) para 2 objetos diferentes. 
 
"""

class Vehiculos():
    def __init__(self, color_auto, matricula, velocidad_maxima):
        self.color_auto = color_auto
        self.matricula = matricula
        self.velocidad_maxima = velocidad_maxima

    def imprimir(self, ):
        print(f"Color de auto: {self.color_auto}, Matrícula: {self.matricula}, Velocidad máxima: {self.velocidad_maxima}")

class Trenes(Vehiculos):
    def __init__(self, color_auto, matricula, velocidad_maxima):
        super().__init__(color_auto, matricula, velocidad_maxima)

objeto_tren1 = Trenes("rojo", "KSU342", "140")
objeto_tren2 = Trenes("azul", "IMG342", "100")

objeto_tren1.imprimir()
objeto_tren2.imprimir()