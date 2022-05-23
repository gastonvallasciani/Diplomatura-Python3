import sys

try:
    frutas = ["pera", "manzana"]
    print(frutas[7])
except IndexError as e:
    print("Mi error: ", e)
    # Imprimo info del tipo de error
    print(sys.exc_info())
    # Customizo el error capturado
    mi_except = IndexError("Hay un error en el indice") 
    raise mi_except
