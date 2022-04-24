class OperacionesM():

    def sumar(self, a ,b):
        print(id(self))
        print(self)
        c = a + b
        return c

# Instancio el objeto de la clase OperacionesM()
obj = OperacionesM()
# Ejecuto el metodo "sumar" de la clase OperacionesM()
print(obj.sumar(2, 3))
# verifico la posicion en memoria del objeto creado es la misma que la de "self" dentro de la clase
# El objeto es referenciado dentro de la clase por medio de "self"
print(id(obj))
print(obj)
