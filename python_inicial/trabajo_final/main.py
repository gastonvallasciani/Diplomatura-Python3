#----------------------------------- Imports ----------------------------------
#------------------------------------------------------------------------------
from pickle import FALSE, TRUE
from tkinter import *
from tkinter import ttk
from tkinter import W, messagebox
import datetime as date
from tkinter.font import BOLD
from sqlite_mod import *
import re
#------------------------------------------------------------------------------
#---------------------------- Variables globales ------------------------------
#------------------------------------------------------------------------------
app_version = "1.0.0"
inicio = FALSE
#---------------------------- Variables auxiliares-----------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Creo la base de datos
db = crear_base()
# Creo la tabla en la base de datos para alamacenar informacion de socios si
# no hay ninguna base creada con el mismo nombre
crear_tabla(db)

root=Tk()
root.title("GYM MANAGER")
root.geometry("690x285")
root['bg'] = '#49A'
#------------------------------------------------------------------------------
# Declaro variables de tkinter
edad_socio = StringVar() 
nombre_socio = StringVar()
apellido_socio = StringVar()
vencimiento_apto_medico = StringVar()
estado_apto_medico = StringVar()
estado_apto_medico.set("NO PRESENTADO")
#------------------------------------------------------------------------------
def borrar_variables_control():
    nombre_socio.set("")
    apellido_socio.set("")
    edad_socio.set("")
    vencimiento_apto_medico.set("")
    estado_apto_medico.set("NO PRESENTADO")
#------------------------------------------------------------------------------
"""
Borra los datos del treeview y los actualiza con la informacion de la 
base de datos.
"""
def actualizar_treeview(mitreeview):
    records = mitreeview.get_children()
    for element in records:
        mitreeview.delete(element)
    
    resultado = seleccionar_todos(db)

    for fila in resultado:
        print(fila)
        mitreeview.insert(
            "", " 0", text=fila[0], tag = 'fuente', 
            values=(fila[1], fila[2], fila[3], fila[4], fila[5])
            )
#------------------------------------------------------------------------------
"""
Funcion que devuelve la fila seleccionada del treeview segun el numero 
de socio.
"""
def item_seleccionado_treeview(mitreeview):
    item = mitreeview.focus()
    if item != "":
        num_socio = mitreeview.item(item, option="text")
        return num_socio
#------------------------------------------------------------------------------
"""
Funcion utilizada para modificar un socio existente en la base 
de datos y el treeview.
"""
def modificar_socio_existente():
    guardar_cliente = FALSE
    
    num_socio_a_modificar = item_seleccionado_treeview(tree)
    if num_socio_a_modificar:
        str_aux = vencimiento_apto_medico.get()

        patron = re.compile("[a-zA-Z áéíóú]")
        patron_numeros = re.compile("[1-9][0-9]{0,1}")
        patron_fecha = re.compile("^[\d]{4}-[\d]{2}-[\d]{2}$")

        if patron.match(nombre_socio.get()) == None:
            guardar_cliente = FALSE
            str_aux_2 = " No se ha cargado el nombre del socio de forma correcta"
            messagebox.showwarning(message=str_aux_2)
        elif patron.match(nombre_socio.get()) == None:
            guardar_cliente = FALSE
            str_aux_2 = " No se ha cargado el apellido del socio de forma correcta"
            messagebox.showwarning(message=str_aux_2)
        elif patron_numeros.match(edad_socio.get()) == None:
            guardar_cliente = FALSE
            str_aux_2 = " No se ha cargado la edad del socio de forma correcta"
            messagebox.showwarning(message=str_aux_2)
        elif len(str_aux) != 10 and len(str_aux) > 0:
            guardar_cliente = FALSE
            str_aux_2 = " El formato de la fecha del apto médico es incorrecto"
            messagebox.showwarning(message=str_aux_2)    
        elif len(str_aux) == 0:
            # No se cargo la fecha de vencimiento del apto medico. Puedo 
            # guardar el socio.
            guardar_cliente = TRUE
        else:
            # Ejecuto el parseo de la fecha del apto medico ingresada. 
            # Puedo guardar el socio.
            if patron_fecha.match(str_aux) != None:
                guardar_cliente = TRUE
                list_local = str_aux.split("-")
                # Formato de fecha: AAAA-MM-DD
                date_apto_medico = date.datetime(
                    int(list_local[0]), int(list_local[1]), 
                    int(list_local[2])
                    )
                date_actual = date.datetime.now()
                # Verifico si el certificado presentado esta vencido
                if (date_apto_medico.year < date_actual.year or 
                    date_apto_medico.year == date_actual.year and 
                    date_apto_medico.month < date_actual.month or 
                    date_apto_medico.year == date_actual.year and 
                    date_apto_medico.month == date_actual.month and 
                    date_apto_medico.day < date_actual.day):
                    str_aux_2 = " El apto medico presentado esta vencido"
                    messagebox.showwarning(message=str_aux_2)
                    estado_apto_medico.set("VENCIDO")
                else:
                    estado_apto_medico.set("VIGENTE")
            else:
                guardar_cliente = FALSE
                str_aux_2 = " El formato de fecha ingresado es incorrecto"
                messagebox.showwarning(message=str_aux_2)
    else:
        str_aux_2 = "No se ha modificado el socio "
        str_aux_2 = str_aux_2 + "ya que no ha seleccionado ninguno!"
        messagebox.showwarning(message=str_aux_2)

    if(guardar_cliente == TRUE):
        actualizar(
            db, num_socio_a_modificar, nombre_socio.get(), 
            apellido_socio.get(), edad_socio.get(), 
            vencimiento_apto_medico.get(), estado_apto_medico.get()
            )
        actualizar_treeview(tree)
        messagebox.showinfo(message="El socio ha sido modificado exitosamente!")
    else:
        str_aux_2 = " El socio no ha sido modificado "
        str_aux_2 = str_aux_2 + "por un error en la carga de datos"
        messagebox.showwarning(message=str_aux_2)
#------------------------------------------------------------------------------
"""
Funcion utilizada para borrar a un socio de la base de datos y del treeview.
"""
def borrar_socio():
    num_socio_a_borrar = item_seleccionado_treeview(tree)
    if num_socio_a_borrar:
        borrar(db, num_socio_a_borrar)
        actualizar_treeview(tree)
    else:
        str_aux = "No se ha borrado el socio ya que no ha seleccionado ninguno!"
        messagebox.showwarning(message=str_aux)
#------------------------------------------------------------------------------
"""
Funcion utilizada guardar el formulario de cada socio en base de datos y 
actualizarlo en treeview.
"""
def guardar_nuevo_socio():
    global numero_de_socio

    guardar_cliente = FALSE

    str_aux = vencimiento_apto_medico.get()

    patron = re.compile("[a-zA-Z áéíóú]")
    patron_numeros = re.compile("[1-9][0-9]{0,1}")
    patron_fecha = re.compile("^[\d]{4}-[\d]{2}-[\d]{2}$")

    if patron.match(nombre_socio.get()) == None:
        guardar_cliente = FALSE
        str_aux_2 = " No se ha cargado el nombre del socio de forma correcta"
        messagebox.showwarning(message=str_aux_2)
    elif patron.match(nombre_socio.get()) == None:
        guardar_cliente = FALSE
        str_aux_2 = " No se ha cargado el apellido del socio de forma correcta"
        messagebox.showwarning(message=str_aux_2)
    elif patron_numeros.match(edad_socio.get()) == None:
        guardar_cliente = FALSE
        str_aux_2 = " No se ha cargado la edad del socio de forma correcta"
        messagebox.showwarning(message=str_aux_2)
    elif len(str_aux) != 10 and len(str_aux) > 0:
        guardar_cliente = FALSE
        str_aux_2 = " El formato de la fecha del apto médico es incorrecto"
        messagebox.showwarning(message=str_aux_2)
    elif len(str_aux) == 0:
        # No se cargo la fecha de vencimiento del apto medico. 
        # Puedo guardar el socio.
        guardar_cliente = TRUE
    else:
        # Ejecuto el parseo de la fecha del apto medico ingresada. 
        # Puedo guardar el socio.
        if patron_fecha.match(str_aux) != None:
            guardar_cliente = TRUE
            list_local = str_aux.split("-")
            # Formato de fecha: AAAA-MM-DD
            date_apto_medico = date.datetime(
                int(list_local[0]), int(list_local[1]), 
                int(list_local[2])
                )
            date_actual = date.datetime.now()
            # Verifico si el certificado presentado esta vencido
            if (date_apto_medico.year < date_actual.year or 
                date_apto_medico.year == date_actual.year and 
                date_apto_medico.month < date_actual.month or 
                date_apto_medico.year == date_actual.year and 
                date_apto_medico.month == date_actual.month and 
                date_apto_medico.day < date_actual.day):
                str_aux_2 = " El apto medico presentado esta vencido"
                messagebox.showwarning(message=str_aux_2)
                estado_apto_medico.set("VENCIDO")
            else:
                estado_apto_medico.set("VIGENTE")
        else:
            guardar_cliente = FALSE
            str_aux_2 = " El formato de fecha ingresado es incorrecto"
            messagebox.showwarning(message=str_aux_2)

    if(guardar_cliente == TRUE):
        insertar(
            db, nombre_socio.get(), apellido_socio.get(), 
            edad_socio.get(), vencimiento_apto_medico.get(), 
            estado_apto_medico.get()
            )
        actualizar_treeview(tree)
        messagebox.showinfo(message="El socio ha sido guardado exitosamente!")
    else:
        str_aux_2=" El socio no ha sido cargado "
        str_aux_2 = str_aux_2 + "por un error en la carga de datos"
        messagebox.showwarning(message=str_aux_2)
#------------------------------------------------------------------------------
"""
Ventana hija para preguntar la version de software
"""
def help_acercade_win():
    global app_version

    tl =Toplevel(root)
    tl['bg'] = '#49A'
    tl.title("Acerca de...")
    tl.geometry('195x150')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)
    
    str1 = "Python 3 - Nivel Inicial\n\n Autor: Gaston Vallasciani"
    str2 = f"\n\n Versión de software: {app_version}" 
    str = str1 + str2
    label1 = Label(
        tl, text = str, anchor= W, bg="#49A", fg='#ffffff', 
        font=("Arial", 10)
        )
    label1.place(x = 15, y = 15)

    boton = Button(
        tl, text = "Cerrar" ,bg='#0052cc', fg='#ffffff',
        command=tl.destroy
        )
    boton.place(x = 75, y = 110)
#------------------------------------------------------------------------------
"""
Ventana hija para dar de baja un socio
"""
def abm_socios_baja_win():
    global Numero_de_socio
    tl = Toplevel(root, bg="white")
    tl.title("Baja socio")
    tl.geometry('320x100')
    tl['bg'] = '#49A'
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    l1=Label(
        tl, text="¿Desea dar de baja al socio seleccionado? ", 
        anchor= W, bg="#49A", fg='#ffffff', font=("Arial", 10)
        )
    l1.place(x = 27, y = 20)

    boton1 = Button(
        tl, text = "Dar de baja", height=1, width=10, bg='#0052cc', 
        fg='#ffffff', command=lambda:[borrar_socio(), 
        borrar_variables_control(), tl.destroy()]
        )
    boton1.place(x = 60, y = 60)

    boton2 = Button(
        tl, text = "Cerrar", height=1, width=10, bg='#0052cc', 
        fg='#ffffff', 
        command=lambda:[borrar_variables_control(), tl.destroy()]
        )
    boton2.place(x = 180, y = 60)
#------------------------------------------------------------------------------
"""
Ventana hija para dar de alta al nuevo socio
"""
def abm_socios_alta_win():
    tl = Toplevel(root, bg="white")
    tl.title("Alta socio")
    tl.geometry('310x170')
    tl['bg'] = '#49A'
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    l2=Label(
        tl, text="Nombre del socio: ", anchor= W, bg="#49A", 
        fg='#ffffff', font=("Arial", 10)
        )
    l2.grid(padx=5, pady=5, column=0, row=1, sticky=W)
    e2=Entry(tl, textvariable=nombre_socio)
    e2.grid(padx=5, pady=5, column=1, row=1, sticky=W)

    l3=Label(
        tl, text="Apellido del socio: ", anchor= W, 
        bg="#49A", fg='#ffffff', font=("Arial", 10)
        )
    l3.grid(padx=5, pady=5, column=0, row=2, sticky=W)
    e3=Entry(tl, textvariable=apellido_socio)
    e3.grid(padx=5, pady=5, column=1, row=2, sticky=W)

    l1=Label(
        tl, text="Edad del socio: ", anchor= W, bg="#49A", 
        fg='#ffffff', font=("Arial", 10)
        )
    l1.grid(padx=5, pady=5, column=0, row=3, sticky=W)
    e1=Entry(tl, textvariable=edad_socio)
    e1.grid(padx=5, pady=5, column=1, row=3, sticky=W)

    l4=Label(
        tl, text="Vencimiento apto médico: ", anchor= W, bg="#49A", 
        fg='#ffffff', font=("Arial", 10)
        )
    l4.grid(padx=5, pady=5, column=0, row=4, sticky=W)
    e4=Entry(tl, textvariable=vencimiento_apto_medico)
    e4.grid(padx=5, pady=5, column=1, row=4, sticky=W)

    boton = Button(
        tl, text = "Dar de alta", bg='#0052cc', fg='#ffffff', 
        command=lambda:[guardar_nuevo_socio(), borrar_variables_control(),
        tl.destroy()]
        )
    boton.grid(padx=5, pady=5, column=0, row=5)

    boton = Button(
        tl, text = "Cerrar", bg='#0052cc', fg='#ffffff', 
        command=lambda:[borrar_variables_control(), tl.destroy()]
        )
    boton.grid(padx=5, pady=5, column=1, row=5)
#------------------------------------------------------------------------------
"""
Ventana hija para modificar un socio existente
"""
def abm_socios_modificar_win():
    tl = Toplevel(root, bg="white")
    tl.title("Modificar socio")
    tl.geometry('310x170')
    tl['bg'] = '#49A'
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    l2=Label(
        tl, text="Nombre del socio: ", anchor= W, bg="#49A", 
        fg='#ffffff', font=("Arial", 10)
        )
    l2.grid(padx=5, pady=5, column=0, row=1, sticky=W)
    e2=Entry(tl, textvariable=nombre_socio)
    e2.grid(padx=5, pady=5, column=1, row=1, sticky=W)

    l3=Label(
        tl, text="Apellido del socio: ", anchor= W, bg="#49A", 
        fg='#ffffff', font=("Arial", 10)
        )
    l3.grid(padx=5, pady=5, column=0, row=2, sticky=W)
    e3=Entry(tl, textvariable=apellido_socio)
    e3.grid(padx=5, pady=5, column=1, row=2, sticky=W)

    l1=Label(
        tl, text="Edad del socio: ", anchor= W, bg="#49A", fg='#ffffff', 
        font=("Arial", 10)
        )
    l1.grid(padx=5, pady=5, column=0, row=3, sticky=W)
    e1=Entry(tl, textvariable=edad_socio)
    e1.grid(padx=5, pady=5, column=1, row=3, sticky=W)

    l4=Label(
        tl, text="Vencimiento apto médico: ", anchor= W, bg="#49A", 
        fg='#ffffff', font=("Arial", 10)
        )
    l4.grid(padx=5, pady=5, column=0, row=4, sticky=W)
    e4=Entry(tl, textvariable=vencimiento_apto_medico)
    e4.grid(padx=5, pady=5, column=1, row=4, sticky=W)

    boton = Button(
        tl, text = "Modificar", height=1, width=10, bg='#0052cc', 
        fg='#ffffff', command=lambda:[modificar_socio_existente(), 
        borrar_variables_control(), tl.destroy()]
        )
    boton.grid(padx=5, pady=5, column=0, row=5)

    boton = Button(
        tl, text = "Cerrar", height=1, width=10, bg='#0052cc', 
        fg='#ffffff', command=lambda:[ borrar_variables_control(), 
        tl.destroy()]
        )
    boton.grid(padx=5, pady=5, column=1, row=5)
#------------------------------------------------------------------------------
def exportar_base_txt():
    cantidad_de_registros_local = cantidad_registros(db)
    archivo = open("base_de_datos_socios.txt","w")
    for counter in range(1, cantidad_de_registros_local+1):
        data_from_db = seleccionar(db, counter)
        if data_from_db != ():
            str = f"Numero de socio: {data_from_db[0]},"
            str = str + f"nombre: {data_from_db[1]}, apellido: {data_from_db[2]},"
            str = str + f"edad: {data_from_db[3]},"
            str = str + f"vencimiento apto medico: {data_from_db[4]},"
            str = str + f"estado apto medico: {data_from_db[5]}\n"
            archivo.write(str)
    archivo.close()
#------------------------------------------------------------------------------
"""
Ventana hija para exportar la base de datos a un archivo txt
"""
def base_de_datos_win():
    global Numero_de_socio
    tl = Toplevel(root)
    tl.title("Exportar base de datos a txt")
    tl.geometry('320x100')
    tl['bg'] = '#49A'
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    l1=Label(
        tl, text="¿Desea exportar la base de datos a un archivo txt? ", 
        anchor= W, bg="#49A", fg='#ffffff', font=("Arial", 10)
        )
    l1.place(x = 10, y = 15)

    boton1 = Button(
        tl, text = "Exportar base", height=1, width=10, 
        bg='#0052cc', fg='#ffffff', command=lambda:[exportar_base_txt(), 
        tl.destroy()]
        )
    boton1.place(x = 60, y = 50)

    boton2 = Button(
        tl, text = "Cerrar", height=1, width=10, bg='#0052cc', 
        fg='#ffffff', command=lambda:[tl.destroy()]
        )
    boton2.place(x = 180, y = 50)
#------------------------------------------------------------------------------
def salirAplicacion():
    valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
    if valor=="yes":
        root.destroy()
#------------------------------------------------------------------------------
menubar=Menu(root)

menu_db = Menu(menubar, tearoff=0)
menu_db.add_command(
    label = "Exportar base de datos", command = base_de_datos_win
    )
menubar.add_cascade(label = "Base de datos", menu = menu_db)

menu_abm_socios = Menu(menubar, tearoff=0)
menu_abm_socios.add_command(
    label = "Nuevo socio", command = abm_socios_alta_win
    )
menu_abm_socios.add_command(
    label = "Baja de socio", command = abm_socios_baja_win
    )
menu_abm_socios.add_command(label = "Modificación información de socio", 
    command = abm_socios_modificar_win)
menubar.add_cascade(label = "Socios", menu = menu_abm_socios)

menu_ayuda = Menu(menubar, tearoff=0)
menu_ayuda.add_command(label = "Acerca de...", command = help_acercade_win)
menubar.add_cascade(label = "Ayuda", menu = menu_ayuda)

root.config(menu = menubar)

tree = ttk.Treeview(root)
#Crea un estilo para ajustar la fuente de los encabezados de columna
estilo = ttk.Style()
estilo.configure("Treeview.Heading", font=("Arial", 10, BOLD))

#Establece una ID a cada columna
tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
#Estilo para ajustar la fuente al Treeview
tree.tag_configure('fuente', font=("Arial", 10))
#Crea las Columnas del Treeview
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=80, minwidth=50, anchor=W)
tree.column("col2", width=100, minwidth=50, anchor=W)
tree.column("col3", width=80, minwidth=50, anchor=W)
tree.column("col4", width=180, minwidth=50, anchor=W)
tree.column("col5", width=180, minwidth=50, anchor=W)

#Encabezados de Columnas del Treeview
tree.heading("#0", text="Socio")
tree.heading("col1", text="Nombre")
tree.heading("col2", text="Apellido")
tree.heading("col3", text="Edad")
tree.heading("col4", text="Vencimiento apto médico")
tree.heading("col5", text="Estado apto médico")

tree.place(x = 10, y = 10)

boton = Button(root, text = "Salir", height=1, width=10, bg='#0052cc', 
    fg='#ffffff', command=salirAplicacion
    )
boton.place(x = 600, y = 245)

# Inicializo el treeview con los datos de la base de datos 
# Entra al loop una unica vez
if inicio == FALSE:
    inicio = TRUE
    actualizar_treeview(tree)

root.mainloop()
#------------------------------------------------------------------------------
#----------------------------- Fin de programa --------------------------------
#------------------------------------------------------------------------------