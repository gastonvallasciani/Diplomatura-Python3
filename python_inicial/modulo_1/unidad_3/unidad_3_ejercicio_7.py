import pprint as pp
import sys as s

total_gastado = 0.0
iniciar_compra = ""
continuar_comprando = ""
index = 0

compras_realizadas = {}

# version.bug
version = 1.0

print(f"Version de programa {version}")

while iniciar_compra != "Y" and iniciar_compra != "N":
    iniciar_compra = input("Desea iniciar una compra Y/N: ")

if(iniciar_compra == "Y"):
    while continuar_comprando != "N":
        producto = input("Ingresar el producto comprado: ")
        cantidad = input("ingrese el peso en kg: ")
        precio = input("Ingrese el precio en pesos: ")

        total_gastado += float(precio)
        
        index += 1
        
        cliente = {f"cliente{index}":{"producto":producto, "peso": cantidad, "precio": precio}}   
        
        compras_realizadas.update(cliente)

        print(compras_realizadas)
        print(f"la fruta o verdura es {producto}, la cantidad comprada es {cantidad} kg, el precio es {precio} pesos")
        
        continuar_comprando = ""
        
        while continuar_comprando != "Y" and continuar_comprando != "N":
            continuar_comprando = input("Desea realizar otra compra Y/N: ")

    print(f"El precio total e la compra es {total_gastado} pesos")
    print(compras_realizadas)
    print("Programa finalizado")
    s.exit()
else:
    #No desea iniciar una compra entonces termino el programa con sys.exit()
    print("Programa finalizado")
    s.exit()