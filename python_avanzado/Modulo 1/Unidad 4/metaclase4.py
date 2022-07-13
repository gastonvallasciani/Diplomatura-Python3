"""
Unidad 4: Metaclases

Las metaclases permiten exteneder las funcionalidades de las clases con metodos que no se encuentran definidos en principio.

Las clases en Python son un objeto de "type".

"type" es una metaclase.

"type" es la clase a partir de la cual genero mis clases en Python (NO es una superclase).
"""
"""
Ejemplo 4: Acceso de atributos de instancias y metodos  de metaclase desde metaclase
"""

def metodo_instancia_1(obj):
    return obj.valor*4

def metodo_instancia_2(obj, valor):
    return "Estoy en metodo de instancia creado desde metaclase " + valor

class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict["met_inst_1"] = metodo_instancia_1
        classdict["met_inst_2"] = metodo_instancia_2
        return type.__new__(meta, classname, supers, classdict)


class Usuarios(metaclass=Extender):
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self,):
        return self.valor*2

class Usuarios2(metaclass=Extender):
    valor = "3"

objeto = Usuarios("8")
objeto1 = Usuarios2()

print(objeto.imprimir())

print(objeto.met_inst_1())
print(objeto.met_inst_2("4"))

print(objeto1.met_inst_1())
print(objeto1.met_inst_2("4"))