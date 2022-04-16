import pprint as pp
import sys as s

total_gastado = 0.0
iniciar_compra = ""
continuar_comprando = ""
index = 0

compras_realizadas = {}

# version.bug
version = 1.0

def alta(compras_realizadas_local, total_gastado_local, compra_index):
    producto = input("Ingresar el producto comprado: ")
    cantidad = input("ingrese el peso en kg: ")
    precio = input("Ingrese el precio en pesos: ")
    total_gastado_local += float(precio)
    compra_index += 1
    compra = {f"compra{compra_index}":{"producto":producto, "peso": cantidad, "precio": precio}}   
    compras_realizadas_local.update(compra)
    #print(compras_realizadas_local)
    return "Y", total_gastado_local, compra_index

def baja(compras_realizadas_local, total_gastado_local):
    baja_compra_aux = "0"
    producto = input("Ingrese el producto de la compra que desea dar de baja: ")
    for compra in compras_realizadas_local:
        producto_aux = list(compras_realizadas_local[compra].values())[0]
        precio_aux = list(compras_realizadas_local[compra].values())[2]
        if producto == producto_aux:
            baja_compra_aux = compra
    if(baja_compra_aux != "0"):
        total_gastado_local -= float(precio_aux)
        compras_realizadas_local.pop(baja_compra_aux)
    return "Y", total_gastado_local

def consulta(compras_realizadas_local):
    index_aux = 0
    print("Las compras realizadas hasta el momento son la siguientes: ")
    for compra in compras_realizadas_local:
        index_aux += 1
        producto_aux = list(compras_realizadas_local[compra].values())[0]
        cantidad_aux = list(compras_realizadas_local[compra].values())[1]
        precio_aux = list(compras_realizadas_local[compra].values())[2]
        print(f"El producto {index_aux} comprado es {producto_aux}, la cantidad comprada es {cantidad_aux} y el precio es {precio_aux}")
    return "Y"

def modificar(compras_realizadas_local, total_gastado_local):
    producto = input("Ingrese el producto de la compra que desea modificar: ")
    for compra in compras_realizadas_local:
        producto_aux = list(compras_realizadas_local[compra].values())[0]
        precio_aux = list(compras_realizadas_local[compra].values())[2]

        total_gastado_local -= float(precio_aux)
        if(producto == producto_aux):
            producto_nuevo = input("Ingresar el nuevo producto comprado: ")
            cantidad_nuevo = input("ingrese el nuevo peso en kg: ")
            precio_nuevo = input("Ingrese el nuevo precio en pesos: ")
            total_gastado_local += float(precio_nuevo)
            compra_nueva = {"producto":producto_nuevo, "peso": cantidad_nuevo, "precio": precio_nuevo}
            compras_realizadas_local[compra] = compra_nueva
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
            aux = alta(compras_realizadas, total_gastado, index)
            continuar_comprando = aux[0]
            total_gastado = aux[1]
            index = aux[2]
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
    #print(compras_realizadas)
    print("Programa finalizado")
    s.exit()
else:
    #No desea iniciar una compra entonces termino el programa con sys.exit()
    print("Programa finalizado")
    s.exit()