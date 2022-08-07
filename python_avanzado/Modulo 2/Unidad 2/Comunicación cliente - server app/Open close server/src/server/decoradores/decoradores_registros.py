
# Declaracion de decoradores
def decorador_ingreso_nuevo_registro(funcion):
    def envoltura(*args):
        print("Se ha ingresado un nuevo registro desde el cliente remoto")
        funcion(*args)
    return envoltura


def decorador_eliminacion_de_registro(funcion):
    def envoltura(*args):
        print("Se ha eliminado el registro desde el cliente remoto")
        funcion(*args)
    return envoltura

def decorador_actualizacion_de_registro(funcion):
    def envoltura(*args):
        print("Se ha actualizado el registro desde el cliente remoto")
        funcion(*args)
    return envoltura