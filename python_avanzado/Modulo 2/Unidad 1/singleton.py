"""
Se utiliza cuando necesitamos que solamente se pueda dar de alta 1 instancia de uan determinada clase.
"""

class Usuarios():
    class __USUARIOS:
        def __init__(self,):
            self.usuario = None

        def __str__(self):
            return repr(self) + " --- " + self.usuario

        def imprimir(self,):
            print("hola")

    instancia = None

    def __new__(cls):
        if not Usuarios.instancia:
            Usuarios.instancia = Usuarios.__USUARIOS()
        return Usuarios.instancia

anna = Usuarios()
anna.usuario = "annita"
print(anna)
anna.imprimir()
print(" --- ")

pedro = Usuarios()
pedro.usuario = "pedrito"
print(pedro)
pedro.imprimir()
print(" --- ")

# Debido a este patrón de desarrollo la clase instanciada ocupa el mismo espacio de memoria que la clase instanciada anterior.