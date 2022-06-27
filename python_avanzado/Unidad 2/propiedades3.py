"""
Manipulación de atributos

Forma alternativa de escribir una propiedad utilizando decoradores.
"""
class Empresa:

    def __init__(self, usuario):
        self._usuario = usuario

    @property
    def usuario(self,):
        """Datos adicionales"""
        print("Recuperar el atributo usuario ...")
        return(self._usuario)
    
    @usuario.setter
    def usuario(self, valor):
        print("Modificar el atributo usuario ...")
        self._usuario = valor
    
    @usuario.deleter
    def usuario(self, ):
        print("Remover el atributo usuario ...")
        del self._usuario
    
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