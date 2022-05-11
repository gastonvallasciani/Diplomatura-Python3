"""

Ejercicio 3
------------

b)	Cree una clase hija del ejercicio de la unidad 1 llamada “Trenes” agregándole el atributo “peso” y 
mediante polimorfismo cree un método “imprimir” en la clase hija que sea utilizado por dos objetos con la adición de este último creado. 
 
"""

class Vehiculos():
    def __init__(self, color_auto, matricula, velocidad_maxima):
        self.color_auto = color_auto
        self.matricula = matricula
        self.velocidad_maxima = velocidad_maxima

    def imprimir(self, ):
        print(f"Color de auto: {self.color_auto}, Matrícula: {self.matricula}, Velocidad máxima: {self.velocidad_maxima}")

class Trenes(Vehiculos):
    def __init__(self, color_auto, matricula, velocidad_maxima, peso):
        super().__init__(color_auto, matricula, velocidad_maxima)
        self.peso = peso
    
    def imprimir(self, ):
        print(f"Color de auto: {self.color_auto}, Matrícula: {self.matricula}, Velocidad máxima: {self.velocidad_maxima}, Peso: {self.peso}")

objeto_tren1 = Trenes("rojo", "KSU342", "140", "500")
objeto_tren2 = Trenes("azul", "IMG342", "100", "600")

objeto_tren1.imprimir()
objeto_tren2.imprimir()