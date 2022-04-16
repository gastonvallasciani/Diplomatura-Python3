"""
Ejercicio 2 : Dificultad media

 Crear una función lambda que sea equivalente a la siguiente función:

def multiplicar_por_tres(valor):
        res = 3 * valor
        return res
"""
multiplicar_por_tres = lambda num: num*3

valor_test = input("Ingrese el valor a multiplicar por tres: ")

print(f"El valor multiplicado por tres es {multiplicar_por_tres(int(valor_test))}")
