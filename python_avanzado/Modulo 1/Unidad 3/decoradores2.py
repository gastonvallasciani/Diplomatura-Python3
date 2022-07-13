# Declaracion de clase decoradora
class DecoradorMuliplicarPor10:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args):
        print(self.func(*args)*10)

# Se puede usar para decorar una funcion
@DecoradorMuliplicarPor10
def sumar(a, b):
    c = a + b
    return(c)

"""
Cuando utilizo una clase decoradora NO puedo utilizarla sobre metodos.
Solo puedo utilizarla sobre funciones
"""
"""
class Operaciones():
    @DecoradorMuliplicarPor10
    def sumar(self, a, b):
        c = a + b
        return(c)       

"""

sumar(2, 3)

