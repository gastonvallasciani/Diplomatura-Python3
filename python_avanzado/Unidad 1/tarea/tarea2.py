"""
TAREA 2
De un ejemplo de en donde podría ser útil implementar el método __add__
"""

class Socios():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self,):
        return("El nombre y el apellido del socio son: " + self.nombre + " " + self.apellido)

    def __add__(self, dato):
        return("el nombre completo del socio con su numero de socio es: " + self.nombre + " " + self.apellido + " numero de socio: " + dato)

if __name__ == "__main__":
    objeto_socio = Socios("Juan", "Perez")
    print(objeto_socio)
    objeto_socio2 = objeto_socio + "1"
    print(objeto_socio2)
    
