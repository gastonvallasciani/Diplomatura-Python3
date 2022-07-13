"""
Manipulación de atributos

Descriptores: permite declarar una clase a partir de la cual puedo agregar una accion cuando llamo, borro o seteo un comentario.
"""
class DescriptorUsuario:

    "Documentacion para el descriptor"
    def __get__(self, instance, owner):
        print("Recuperar el atributo usuario ...")
        return(instance._usuario.upper())
    
    def __set__(self, instance, valor):
        print("Modificar el atributo usuario ...")
        instance._usuario = valor
    
    def __delete__(self, instance ):
        print("Remover el atributo usuario ...")
        del instance._usuario

class Cliente:
    def __init__(self, usuario):
        self._usuario = usuario
    usuario = DescriptorUsuario()

if __name__ == "__main__":

    cliente1 = Cliente("Anna")
    print(cliente1.usuario)

    cliente1.usuario = "juan"
    print(cliente1.usuario)

    print(cliente1.__doc__)