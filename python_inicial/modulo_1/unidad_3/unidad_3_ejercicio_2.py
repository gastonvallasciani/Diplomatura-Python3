oracion = input("ingrese una oracion: ")

counter = 0

for var in oracion:
    if var == 'a':
        counter += 1

print(f"la letra a aparece {counter} veces en la oracion")