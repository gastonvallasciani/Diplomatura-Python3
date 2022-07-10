"""
Unidad 4: Metaclases

Las metaclases permiten exteneder las funcionalidades de las clases con metodos que no se encuentran definidos en principio.

Las clases en Python son un objeto de "type".

"type" es una metaclase.

"type" es la clase a partir de la cual genero mis clases en Python (NO es una superclase).
"""
"""
Ejemplo 1: Metaclases
"""

class Material: pass

# Declaracion de una clase de forma implicita
# Auto NO aparece como un objeto de la clase "type"
class Auto(Material):
    #atributo de clase
    color = "azul"

    def retornar_color(self,):
        return self.color

objeto = Auto()
print(objeto.retornar_color())
print(type(Auto.__class__))

print("---"*23)

# Declaracion de una clase de forma explicita
# Auto aparece como un objeto de la clase "type"
Auto2 = type("Auto2", (Material, ), {"color":"azul", "retornar_color":(lambda x:x.color)})

objeto2 = Auto2()
print(objeto2.retornar_color())
print(type(Auto2.__class__))

print("---"*23)