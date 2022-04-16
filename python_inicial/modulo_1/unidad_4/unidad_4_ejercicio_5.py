"""
Ejercicio 5 : Dificultad media
 
 Cree un programa que utilizando una función, solicite la edad de la persona e 
 imprima todos los años que la persona ha cumplido según el siguiente formato de ejemplo. 

1, 2, 3, 4, 5
Y 
5, 4, 3, 2, 1


"""
def imprimir_anios():
        edad_str_list_invertida = ""
        counter_aux = 0

        edad_local = input("Ingresar la edad de la personda: ")
        lista_anios_cumplidos = list(range(1,int(edad_local) + 1))
        edad_str_list = ""
        for anio in lista_anios_cumplidos:
                if anio == int(edad_local):
                        edad_str_list  = edad_str_list + str(anio)
                        break
                edad_str_list  = edad_str_list + str(anio) + ", "

        
        counter = len(lista_anios_cumplidos)
        while(counter >0):
                if lista_anios_cumplidos[counter-1] == 1:
                        edad_str_list_invertida = edad_str_list_invertida + str(lista_anios_cumplidos[counter-1])
                else:
                        edad_str_list_invertida = edad_str_list_invertida + str(lista_anios_cumplidos[counter-1]) + ", "
                counter -= 1
        
        print(edad_str_list)
        print("Y")
        print(edad_str_list_invertida)
        

print(imprimir_anios())
