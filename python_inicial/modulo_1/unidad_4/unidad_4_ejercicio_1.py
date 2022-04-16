"""
Ejercicio 1 : Dificultad baja

Cree una función lamba que compruebe si un número es par o impar.
"""
paridad = lambda num: "par" if (num%2 == 0) else "impar"

valor_test = input("Ingrese un valor para analizar su paridad: ")

print(f"la paridad es {paridad(int(valor_test))}")
