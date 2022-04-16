edad = input("Ingrese su edad: ")
genero = input("Ingrese el genero que indica su DNI: ")

if genero == "Masculino" and int(edad) >= 65:
    print("Ya esta en edad de jubilarse.")
elif genero == "Masculino" and int(edad) < 65:
    print("Aun esta en edad de trabajar.")
elif genero == "Femenino" and int(edad) >= 60:
    print("Ya esta en edad de jubilarse.")
elif genero == "Femenino" and int(edad) < 60:
    print("Aun esta en edad de trabajar.")