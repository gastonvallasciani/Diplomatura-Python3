def dividir(x, y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print("Dividir por 0")
    else: 
        # El else se ejecuta siempre y cuando el try se ejecute de forma correcta 
        print("El resultado es: ", resultado)
    finally:
        # Este bien lo que este adentro del try o no se ejecuta el finally.
        print("Finally")

dividir(1, 2)
