"""
El metodo getitem/setitem permite realizar acciones sobre los objetos que no hubieran sido posible ejecutar con la funcionalidad del metodo original.
"""

class Indice:
    lista = ['M', 'A', 'N', 'Z', 'A', 'N', 'A']
    def __getitem__(self, mi_indice):
        return mi_indice**0.5

    def __setitem__(self, mi_indice, valor):
        self.lista[mi_indice] = valor

x = Indice()
x[2] = 'o'
print(x.lista)
