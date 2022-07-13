"""
SOBRECARGA DE OPERADORES
TAREA 3 -  Trabajo de investigación
Elija de la siguiente lista un método e implemente un ejemplo de aplicación:
__add__, __sub__, __mult__, __lt__, __gt__, __le__, __ge__, __eq__, __ne__, __repr__
"""

class funciones_matematicas():
    def __init__(self, a_value):
        self.a_value = a_value

    def __sub__(self, b_value):
        r = self.a_value - b_value
        return(r)

    def __mul__(self, b_value):
        r = self.a_value * b_value
        return(r)

if __name__ == "__main__":
    valor_a = funciones_matematicas(2)
    resultado_resta = valor_a - 1
    print(resultado_resta)
    resultado_mult = valor_a * 1
    print(resultado_mult)
