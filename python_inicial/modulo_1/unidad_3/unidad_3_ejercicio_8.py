import pprint as pp
import sys as s

total_gastado = 0.0
iniciar_compra = ""
continuar_comprando = ""
index = 0

compras_realizadas = []

# version.bug
version = 1.0

def alta(compras_realizadas_local, total_gastado_local):
    producto = input("Ingresar el producto comprado: ")
    cantidad = input("ingrese el peso en kg: ")
    precio = input("Ingrese el precio en pesos: ")
    total_gastado_local += float(precio)
    cliente = [producto, cantidad, precio] 
    compras_realizadas_local.append(cliente)
    return "Y", total_gastado_local

def baja(compras_realizadas_local, total_gastado_local):
    producto = input("Ingrese el producto de la compra que desea dar de baja: ")
    for compra in compras_realizadas_local:
        if compra[0] == producto:
            total_gastado_local -= float(compra[2])
            compras_realizadas_local.remove([compra[0], compra[1], compra[2]]) 
    return "Y", total_gastado_local

def consulta(compras_realizadas_local):
    index = 0
    print("Las compras realizadas hasta el momento son la siguientes: ")
    for compra in compras_realizadas_local:
        index += 1
        print(f"El producto {index} comprado es {compra[0]}, la cantidad comprada es {compra[1]} y el precio es {compra[2]}")
    return "Y"

def modificar(compras_realizadas_local, total_gastado_local):
    producto = input("Ingrese el producto de la compra que desea modificar: ")
    for compra in compras_realizadas_local:
        if compra[0] == producto:
            total_gastado_local -= float(compra[2])

            producto_aux = input("Ingresar el nuevo producto: ")
            cantidad = input("ingrese el nuevo peso en kg: ")
            precio = input("Ingrese el nuevo precio en pesos: ")

            total_gastado_local += float(precio)
            compra[0] = producto_aux
            compra[1] = cantidad
            compra[2] = precio
 
    return "Y", total_gastado_local

def menu():
    print("----------- MENU --------------")
    print("1- Alta de compra")
    print("2- Baja de compra")
    print("3- Consulta de productos comprados hasta el momento")
    print("4- Modificar compra")
    print("5- Finalizar compra")

print(f"Version de programa {version}")

while iniciar_compra != "Y" and iniciar_compra != "N":
    iniciar_compra = input("Desea iniciar una compra Y/N: ")

if(iniciar_compra == "Y"):
    while continuar_comprando != "N":
        menu()
        tarea = input("Ingrese el numero de tarea que desea llevar a cabo: ")
        if tarea == "1":
            aux = alta(compras_realizadas, total_gastado)
            continuar_comprando = aux[0]
            total_gastado = aux[1]
        elif tarea == "2":
            aux = baja(compras_realizadas, total_gastado)
            continuar_comprando = aux[0]
            total_gastado = aux[1]
        elif tarea == "3":
            continuar_comprando = consulta(compras_realizadas)
        elif tarea == "4":
            aux = modificar(compras_realizadas, total_gastado)
            continuar_comprando = aux[0]
            total_gastado = aux[1]
        elif tarea == "5":
            continuar_comprando = "N"
        else:
            continuar_comprando = "Y"

    print(f"El precio total e la compra es {total_gastado} pesos")
    print(compras_realizadas)
    print("Programa finalizado")
    s.exit()
else:
    #No desea iniciar una compra entonces termino el programa con sys.exit()
    print("Programa finalizado")
    s.exit()
