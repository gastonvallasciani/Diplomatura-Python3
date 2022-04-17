#----------------------------------- Imports ----------------------------------
#------------------------------------------------------------------------------
from pickle import FALSE, TRUE

from tkinter import Tk
from tkinter import StringVar
from tkinter import Toplevel
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import Menu
from tkinter import ttk
from tkinter import W, messagebox
from tkinter.font import BOLD

from modelo import actualizar_treeview

from modelo import modificar_socio_existente
from modelo import borrar_socio
from modelo import borrar_variables_control
from modelo import guardar_nuevo_socio
from modelo import exportar_base_txt

from sqlite3_module.sqlite_mod import crear_base
from sqlite3_module.sqlite_mod import crear_tabla
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
#----------------------------------------------------------------------------
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
        fg='#ffffff', command=lambda:[borrar_socio(tree, db), 
        borrar_variables_control(nombre_socio, apellido_socio, edad_socio, 
            vencimiento_apto_medico), tl.destroy()]
        )
    boton1.place(x = 60, y = 60)

    boton2 = Button(
        tl, text = "Cerrar", height=1, width=10, bg='#0052cc', 
        fg='#ffffff', 
        command=lambda:[borrar_variables_control(nombre_socio, apellido_socio, 
            edad_socio, vencimiento_apto_medico), tl.destroy()]
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
        command=lambda:[guardar_nuevo_socio(tree, db, nombre_socio.get(), 
            apellido_socio.get(), edad_socio.get(), 
            vencimiento_apto_medico.get()), 
            borrar_variables_control(nombre_socio, apellido_socio, 
            edad_socio, vencimiento_apto_medico),
        tl.destroy()]
        )
    boton.grid(padx=5, pady=5, column=0, row=5)

    boton = Button(
        tl, text = "Cerrar", bg='#0052cc', fg='#ffffff', 
        command=lambda:[borrar_variables_control(nombre_socio, apellido_socio, 
            edad_socio, vencimiento_apto_medico), tl.destroy()]
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
        fg='#ffffff', command=lambda:[modificar_socio_existente(tree, db, 
            nombre_socio.get(), apellido_socio.get(), edad_socio.get(), 
            vencimiento_apto_medico.get()), 
        borrar_variables_control(nombre_socio, apellido_socio, 
            edad_socio, vencimiento_apto_medico), tl.destroy()]
        )
    boton.grid(padx=5, pady=5, column=0, row=5)

    boton = Button(
        tl, text = "Cerrar", height=1, width=10, bg='#0052cc', 
        fg='#ffffff', command=lambda:[borrar_variables_control(nombre_socio, 
            apellido_socio, edad_socio, vencimiento_apto_medico), 
        tl.destroy()]
        )
    boton.grid(padx=5, pady=5, column=1, row=5)
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
        bg='#0052cc', fg='#ffffff', command=lambda:[exportar_base_txt(db), 
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
    actualizar_treeview(tree, db)

root.mainloop()
#------------------------------------------------------------------------------
#----------------------------- Fin de programa --------------------------------
#------------------------------------------------------------------------------