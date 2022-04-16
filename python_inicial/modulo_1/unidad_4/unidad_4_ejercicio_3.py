"""
Ejercicio 3 : Dificultad media
 
 Crear una función lambda que sea equivalente a la siguiente función:

def sumar(valor1, valor2):
        res = valor1 + valor2
        return res

"""
suma_2_valores = lambda valor1, valor2: valor1 + valor2

valor1_aux, valor2_aux = input("Ingrese valor1 y valor2 a sumar separados por coma: ").split(",")

print(f"El resultado de sumar valor 1 y valor 2 es {suma_2_valores(int(valor1_aux), int(valor2_aux))}")
