import sys as s

#imprimo lista de argumentos pasados en la ejecucion del programa
print(s.argv)
#imprimo nombre del programa que por default es el elemento 0 de la lista
print(s.argv[0])

#for loop para verificar si los numeros ingresados son apres o impares
for counter in s.argv:
    if counter != "mod_3_ejercicio_1.py":
        if int(counter)%2 == 0:
            print("Es numero par")
        else:
            print("es numero impar") 