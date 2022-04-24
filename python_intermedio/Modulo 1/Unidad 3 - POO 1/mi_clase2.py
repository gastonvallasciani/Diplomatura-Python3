class persona():

    def __init__(self, nombre):
        # Nombre es un atributo de clase
        self.nombre = nombre

    def comer(self): pass

# Intancio un objeto de la clase persona() y ejecuto el constructor
juan = persona("Juan Martín")
# Acceso al atributo "nombre" de la clase persona del objeto instanciado "juan"
print(juan.nombre)