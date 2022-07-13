"""
Los slots permiten limitar los atributos que la clase puede implementar
"""

class Limites:
    __slots__ = ['edad', 'sexo', 'trabajo', 'salario']
    pass


x = Limites()
x.edad = 4
print(x.edad)

x.peso = 4
print(x.peso)
