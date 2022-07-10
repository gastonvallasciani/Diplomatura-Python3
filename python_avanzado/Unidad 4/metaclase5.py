"""
Unidad 4: Metaclases

Las metaclases permiten exteneder las funcionalidades de las clases con metodos que no se encuentran definidos en principio.

Las clases en Python son un objeto de "type".

"type" es una metaclase.

"type" es la clase a partir de la cual genero mis clases en Python (NO es una superclase).

Las metaclases tambien pueden ser heredadas.
"""
"""
Ejemplo 5: Herencia de metaclases
"""

class Control(type):
    estado = "inspeccion"

class ControlMotor(Control):
    encendido = False

    def recuperar_hora(cls):
        return "Hora del evento"

class Material():
    material = "plastico"

class Auto(Material, metaclass = ControlMotor):

    #atributo de clase
    marca = "Renault"

    def __init__(self, color):
        self.color = color

    def retornar_color(self, valor):
        return self.color + str(valor)

"""
Una instancia de Auto NO iene acces a lso atributos y metodos de la metaclase. 
"""

print(Auto.estado)
print(Auto.encendido)
print(Auto.recuperar_hora())

objeto = Auto("Rojo")

try:
    print(objeto.encendido)
except:
    print("El objeto de la clase no puede acceder al atributo")

try:
    print(objeto.recuperar_hora())
except:
    print("El objeto de la clase no puede acceder al metodo")
