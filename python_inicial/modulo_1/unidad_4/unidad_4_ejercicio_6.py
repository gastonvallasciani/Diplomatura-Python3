"""
Ejercicio 6 : Dificultad alta
 
 Cree una función que tome la siguiente lista y reordene de menor a mayor sus componentes:

[3, 44, 21, 78, 5, 56, 9]

"""
def minimo(lista_local):
        minimo_aux = 0
        minimo = 1000
        longitud = len(lista_local)
        if longitud == 1:
                return lista_local[0]
        print(longitud)
        for index_i in range(0,longitud):
                for index_j in range(0,longitud):
                        if lista_local[index_i] < lista_local[index_j]:
                                minimo_aux = lista_local[index_i]
                        else:
                                minimo_aux = lista_local[index_j]
                if minimo_aux < minimo:
                        minimo = minimo_aux
        return minimo

def menor_a_mayor(lista_local):
        lista_menor_a_mayor = []
        longitud = len(lista_local)
        for index_i in range(0,longitud):
                minimo_local = minimo(lista_local)
                lista_menor_a_mayor.append(minimo_local)
                lista_local.remove(minimo_local)
               
        return lista_menor_a_mayor

lista_global = [3, 44, 21, 78, 5, 56, 9]

print(menor_a_mayor(lista_global))
