"""
Ejercicio 1
-----------
Cree una clase llamada “Vehiculos” que permita registrar:
Color de auto
Matricula
Velocidad máxima
Los valores deben ser presentados por pantalla para tres objetos diferentes mediante un print()
"""

class Vehiculos():
    def __init__(self, color_auto, matricula, velocidad_maxima):
        self.color_auto = color_auto
        self.matricula = matricula
        self.velocidad_maxima = velocidad_maxima


objeto_vehiculo1 = Vehiculos("rojo", "KSU342", "140")
objeto_vehiculo2 = Vehiculos("azul", "IMG342", "100")
objeto_vehiculo3 = Vehiculos("negro", "ONE142", "120")

print(f"{objeto_vehiculo1.color_auto}, {objeto_vehiculo1.matricula}, {objeto_vehiculo1.velocidad_maxima}")
print(f"{objeto_vehiculo2.color_auto}, {objeto_vehiculo2.matricula}, {objeto_vehiculo2.velocidad_maxima}")
print(f"{objeto_vehiculo3.color_auto}, {objeto_vehiculo3.matricula}, {objeto_vehiculo3.velocidad_maxima}")
