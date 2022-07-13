from re import X
"""
Permite atrapar la instancia y retornar algo cuando recupero el valor de la instancia
El metodo str permite retornar una informacion extra en formato de string de la instancia 
en el momento en que consulto por la instancia.
"""

class Usuarios():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self, ):
        return "El nombre de usuario es: " + self.nombre

x = Usuarios("Anna")
print(x)