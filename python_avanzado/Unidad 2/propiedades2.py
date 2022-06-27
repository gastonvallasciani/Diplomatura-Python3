"""
Manipulación de atributos

Herencia de propiedades --> Las propiedades pueden ser heredadas.
"""
class Empresa:

    def __init__(self, usuario):
        self._usuario = usuario

    def get_usuario(self,):
        print("Recuperar el atributo usuario ...")
        return(self._usuario)
    
    def set_usuario(self, valor):
        print("Modificar el atributo usuario ...")
        self._usuario = valor
    
    def del_usuario(self, ):
        print("Remover el atributo usuario ...")
        del self._usuario
    
    usuario = property(get_usuario, set_usuario, del_usuario, "Datos adicionales")

class Cliente(Empresa): pass

if __name__ == "__main__":

    cliente1 = Cliente("Anna")
    print(cliente1.usuario)
    cliente1.usuario = "Ana"
    print(cliente1.usuario)
    del cliente1.usuario
    try:
        print(cliente1.usuario)
    except:
        print("Error")

    print(Cliente.usuario.__doc__)