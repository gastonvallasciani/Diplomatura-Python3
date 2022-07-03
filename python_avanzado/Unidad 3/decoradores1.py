# Declaracion de funcion decoradora
def decorador_muliplicar_por10(funcion):
    def envoltura(*args):
        print(funcion(*args)*10)
    return envoltura

# Se puede usar para decorar una funcion
@decorador_muliplicar_por10
def sumar(a, b):
    c = a + b
    return(c)

# Tambien se puede utilizar para decorar un metodo
class Operaciones():
    @decorador_muliplicar_por10
    def sumar(self, a, b):
        c = a + b
        return(c)       



sumar(2, 3)
objeto_operaciones = Operaciones()
objeto_operaciones.sumar(2, 3)

