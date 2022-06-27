"""
Manipulación de atributos

Descriptores dentro de clases

El descriptor se puede poner dentro de la clase o fuera de la clase.

Si el descriptor va a ser utilizado por varias clases no deberia estar dentro de una clase.
Si es propio de una clase podria empaquetarse y ponerse dentro de esta.
"""

class AccederInstanciaMail():
    def __get__(self, instance, owner):
        return instance._mail + ".ar"
    
    def __set__(self, instance, valor):
        instance._mail = valor

class Cliente:
    def __init__(self, usuario, _mail):
        self._usuario = usuario
        self._mail = _mail

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

    usuario = DescriptorUsuario()
    mail = AccederInstanciaMail()

if __name__ == "__main__":

    cliente1 = Cliente("Anna", "anna@gmail.com")
    print(cliente1.usuario, cliente1._mail, cliente1.mail)

    cliente1.usuario = "juan"
    print(cliente1.usuario)