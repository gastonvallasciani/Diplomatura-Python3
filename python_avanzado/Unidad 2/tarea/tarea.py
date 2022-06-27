"""
Tarea
Crear una clase que registre datos personales de empleados, como:
·         nombre,
·         edad,
·         salario,
·         etc.
Crear un descriptor que permita cuando se ingresa el valor de la edad de la persona 
lanzar una excepción si el valor es negativo o que informe cuando la persona está a un 
año de la edad de jubilación. 
"""
class DescriptorEmpleado():
    def __get__(self, instance, owner):
        print("Recuperar usuario ..")
        return instance._edad
    
    def __set__(self, instance, edad_nueva):
        print("Modificar usuario ..")
        if(edad_nueva < 0):
            raise AttributeError("Edad negativa")
        if(instance.genero == "hombre"):
            if(edad_nueva == 69):
                print("El empleado se encuentra a un año de su jubilación")
            instance._edad = edad_nueva
        elif(instance.genero == "mujer"):
            if(edad_nueva == 64):
                print("El empleado se encuentra a un año de su jubilación")
            instance._edad = edad_nueva
        else:
            if(edad_nueva == 69):
                print("El empleado se encuentra a un año de su jubilación")
            instance._edad = edad_nueva

    def __delete__(self, instance):
            print('Remover el usuario....')
            del instance._edad
            
class Empleado():
    def __init__(self, nombre = "Pedro", edad = 10, salario = 1500, genero = "hombre"):
        self.nombre = nombre
        self._edad = edad
        self.salario = salario
        self.genero = genero

    edad = DescriptorEmpleado()

if __name__ == "__main__":
    obj_empleado = Empleado()
    try:
        obj_empleado.edad = -1
    except AttributeError:
        print("Error")
    obj_empleado.edad = 69
    print("Edad del empleado: ", obj_empleado.edad)
        
