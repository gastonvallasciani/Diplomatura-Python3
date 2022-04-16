from mod2_ejercicio_5_mod import *

radio = input("Ingresar el radio de una circunferencia: ")

perimetro = calculo_perimetro_circunferencia_en_funcion_del_radio(radio)
area = calculo_area_circunferencia_en_funcion_del_radio(radio)

print("El perimetro es el siguiente: ", perimetro)
print("El area de la circunferencia es: ", area)

valor_entero = input("Ingrese un valor entero por pantalla: ")

valor_incrementado = incrementar_valor_enetero_en_10_porciento(valor_entero)

print("El valor entero incrementado en un 10 porciento es: ", valor_incrementado)