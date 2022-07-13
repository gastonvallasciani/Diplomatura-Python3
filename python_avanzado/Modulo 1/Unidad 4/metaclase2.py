"""
Unidad 4: Metaclases

Las metaclases permiten exteneder las funcionalidades de las clases con metodos que no se encuentran definidos en principio.

Las clases en Python son un objeto de "type".

"type" es una metaclase.

"type" es la clase a partir de la cual genero mis clases en Python (NO es una superclase).
"""
"""
Ejemplo 2: Metaclases

__new__ e __init__

"""
class MiMetaclase(type):
    def __new__(meta, nombre_de_clase, superclase, diccionariode_clase):
        print("En __new__ de metaclase: ", meta, nombre_de_clase, superclase, diccionariode_clase, sep="\n...")
        return type.__new__(meta, nombre_de_clase, superclase, diccionariode_clase)

    def __init__(Clase, nombre_de_clase, superclase, diccionariode_clase):
        print("En __init__ de metaclase: ", Clase, nombre_de_clase, superclase, diccionariode_clase, sep="\n...")
        print("..init objeto de clase", list(Clase.__dict__.keys()))

class MiSuperClase(): pass

class MiClase(MiSuperClase, metaclass = MiMetaclase):
    atributo1 = 1
    def metodo1(self, arg):
        return self.atributo1 + 3*arg

print("Creando una instancia")
x = MiClase()
print("atributo: ", x.atributo1, x.metodo1(7))
