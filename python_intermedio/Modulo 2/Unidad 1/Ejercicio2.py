"""

Ejercicio 2
Agregue un método de instancia “imprimir” en el ejercicio anterior de forma de que, 
a partir de los objetos creados se pueda imprimir en pantalla un texto personalizado 
con una descripción de los atributos de instancia existentes. 

"""

class Vehiculos():
    def __init__(self, color_auto, matricula, velocidad_maxima):
        self.color_auto = color_auto
        self.matricula = matricula
        self.velocidad_maxima = velocidad_maxima

    def imprimir(self, ):
        print(f"Color de auto: {self.color_auto}, Matrícula: {self.matricula}, Velocidad máxima: {self.velocidad_maxima}")


objeto_vehiculo1 = Vehiculos("rojo", "KSU342", "140")
objeto_vehiculo2 = Vehiculos("azul", "IMG342", "100")
objeto_vehiculo3 = Vehiculos("negro", "ONE142", "120")

objeto_vehiculo1.imprimir()
objeto_vehiculo2.imprimir()
objeto_vehiculo3.imprimir()