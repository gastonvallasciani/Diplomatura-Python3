"""
Ejercicio 4 : Dificultad alta

 Crear una función lambda que tome como parámetro una frase y la escriba al revés. 

"""
def frase_invertida(frase):
        frase_invertida_local = ""
        counter = 1
        for letra in frase:
                frase_invertida_local = frase_invertida_local + frase[-counter]
                counter += 1
        return  frase_invertida_local


"""
Python slice string. 
sintaxis: str_object[start_pos:end_pos:step]
https://www.journaldev.com/23584/python-slice-string#:~:text=The%20slicing%20starts%20with%20the,for%20any%20index%20'i'.
"""
def frase_invertida_simplificada(frase):
        frase_invertida_local = frase[::-1]
        return frase_invertida_local


# Resolucion con funcion lambda
frase_invertida_lambda = lambda frase: frase[::-1]

frase_test = input("Ingresar una frase: ")

print(f"La frase invertida es {frase_invertida_lambda(frase_test)}")
