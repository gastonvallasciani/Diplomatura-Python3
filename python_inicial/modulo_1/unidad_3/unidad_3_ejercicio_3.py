oracion = input("ingrese una oracion: ")

counter = 0

for var in oracion:
    if var == 'a' or var == 'A' or var == 'e' or var == 'E' or var == 'i' or var == 'I' or var == 'o' or var == 'O' or var == 'u' or var == 'U':
        counter += 1
    elif var == 'á' or var == 'Á' or var == 'é' or var == 'É' or var == 'í' or var == 'Í' or var == 'ó' or var == 'Ó' or var == 'ú' or var == 'Ú':
        counter += 1

print(f"Aparecen {counter} vocales ya sean en la oracion")