"""
 Info de funcionamiento
 -----------------------
 user = admin y password = 1234 para acceder al menu de administrador
 El menu administrador permite dar de alta nuevos usuarios en la "base de datos" simulada con un diccionario
 Si ocurren 3 logins erroneos consecutivos se sale del estado ingresar contraseña y deberia terminar el programa
 Esta implementado en una funcion para poder llamarla de otros modulos
 La funcion devuelvue "autorizado" cuando se valida correctamente el usuario y contraseña y "desautorizado" cuando
 se llego al maximo numero de intentos de login.
"""

aut_aux = {}
aut_global = {}

aut_default = {"user_default":"admin", "password_default":"1234"}


ejecutar_menu_admin = ""

return_status = "no_autorizado"

def autenticacion():
    aut_index = 0
    password_ingresado = "incorrecto"
    user_ingresado = "incorrecto"
    max_aut_intentos = 4
    intentos = 0
    aut_global.update({"aut_default":aut_default})

    while(password_ingresado == "incorrecto" or user_ingresado == "incorrecto"):
        user = input("Ingrese usuario: ")
        password = input("Ingrese password: ")

        #print(aut_default["user_default"], type(aut_default["user_default"]))
        #print(aut_default["password_default"], type(aut_default["password_default"]))

        if user == aut_default["user_default"] and password == aut_default["password_default"]:
            ejecutar_menu_admin = "y"
            while ejecutar_menu_admin == "y":
                print("-------MENU de ADMINISTRADOR-------")
                print(" 1. Ingresar un nuevo usuario y password")
                print(" 2. Salir del menu administrador")
                accion = input("Ingrese la accion que desea realizar: ")
                if accion == "1":
                    new_user = input("Ingrese nuevo usuario:")
                    new_pass = input("Ingrese nuevo password:")
                    aut_index += 1
                    aut_aux = {"user":new_user, "pass":new_pass} 
                    aut_global.update({f"user{aut_index}":aut_aux})
                    #print(aut_global)
                    ejecutar_menu_admin = "n"
                elif accion == "2":
                    print("Ha salido exitosamente del menu administrador")
                    ejecutar_menu_admin = "n"
                else:
                    print("Accion ingresada no soportada")
                    ejecutar_menu_admin == "y"
        else:
            for aut_users_var in aut_global:
                user_aux = list(aut_global[aut_users_var].values())[0]
                pass_aux = list(aut_global[aut_users_var].values())[1]
                #print(user_aux)
                #print(pass_aux)
                if user == user_aux and password == pass_aux:
                    password_ingresado = "correcto"
                    user_ingresado = "correcto"
                    return_status = "autorizado"
                    print("Password y user correctos!!!")
                    break
            if password_ingresado == "incorrecto" or user_ingresado == "incorrecto":
                print("Login erroneo, intentar nuevamente")
                intentos += 1
                if intentos == max_aut_intentos:
                    print("Maxima cantidad de intentos de login!!")
                    return_status = "desautorizado"
                    return return_status
                
    return return_status

    
aux = autenticacion()
print(aux)
