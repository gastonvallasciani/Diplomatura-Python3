"""
Unidad 4: Metaclases

Las metaclases permiten exteneder las funcionalidades de las clases con metodos que no se encuentran definidos en principio.

Las clases en Python son un objeto de "type".

"type" es una metaclase.

"type" es la clase a partir de la cual genero mis clases en Python (NO es una superclase).

Las metaclases tambien pueden ser heredadas.

Se pueden aplicar sobrecarga de operadores dentro de las metaclases.
"""
"""
Ejemplo 6: Sobrecarga de operadores dentro de las metaclases
"""

class ControlMotor(type): 
    def __getitem__(cls, indice):
        return cls.color[indice]*5

class Auto(metaclass = ControlMotor):
    color = "Azul"

    def __getitem__(self, indice):
        return indice**0.5

objeto = Auto()
print(objeto[64])

print(Auto[1])