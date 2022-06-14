"""
Ejemplo de aplicacion de delegacion.

Se delega la responsabilidad de declarar un metodo utilizado por la clase padre a una clase hija.

En este ejemplo la forma de comer arroz sera especificada por la clase hija que seria la nacionalidad de la persona.
"""
class Personas():
    def comer_arroz(self, ):
        self.accion()

class Chinos(Personas):
    def accion(self, ):
        print("Comen arroz con palillos")

if __name__ == "__main__":
    objeto_chinos = Chinos()
    objeto_chinos.comer_arroz()
