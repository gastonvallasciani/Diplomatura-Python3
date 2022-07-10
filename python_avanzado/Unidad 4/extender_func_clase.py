"""
Unidad 4: Metaclases

Las clases son un objeto de la clase type.
Las metaclases permiten exteneder las funcionalidades 
de las clases con metodos que no se encuentran definidos en principio.
"""
"""
Ejemplo como extender las funcionalidades de una clase
NO es una metaclase este caso
"""

def extender_clase(self, arg):
    print(arg)

class MiClase():
    pass

MiClase.extender_clase = extender_clase 

objeto = MiClase()
objeto.extender_clase("Este método se ha agregado a la clase")
