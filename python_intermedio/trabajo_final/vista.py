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

from modelo import Abmc
from system_app_module.system_app_mod import SystemApp

#------------------------------------------------------------------------------
class Panel():
    def __init__(self, window):

        self.root = window
        self.abmc = Abmc()
        self.system_app = SystemApp("1.0.0.1", FALSE)

        self.root.title("GYM MANAGER")
        self.root.geometry("690x285")
        self.root['bg'] = '#49A'
    
        self.edad_socio = StringVar() 
        self.nombre_socio = StringVar()
        self.apellido_socio = StringVar()
        self.vencimiento_apto_medico = StringVar()
    
        self.menubar=Menu(self.root)

        self.menu_db = Menu(self.menubar, tearoff=0)
        self.menu_db.add_command(
            label = "Exportar base de datos", command = self.base_de_datos_win
            )
        self.menubar.add_cascade(label = "Base de datos", menu = self.menu_db)

        self.menu_abm_socios = Menu(self.menubar, tearoff=0)
        self.menu_abm_socios.add_command(
            label = "Nuevo socio", command = self.abm_socios_alta_win
            )
        self.menu_abm_socios.add_command(
            label = "Baja de socio", command = self.abm_socios_baja_win
            )
        self.menu_abm_socios.add_command(label = "Modificación información de socio", 
            command = self.abm_socios_modificar_win)
        self.menubar.add_cascade(label = "Socios", menu = self.menu_abm_socios)

        self.menu_ayuda = Menu(self.menubar, tearoff=0)
        self.menu_ayuda.add_command(label = "Acerca de...", command = lambda:[self.help_acercade_win()])
        self.menubar.add_cascade(label = "Ayuda", menu = self.menu_ayuda)

        self.root.config(menu = self.menubar)

        self.tree = ttk.Treeview(self.root)
        #Crea un estilo para ajustar la fuente de los encabezados de columna
        self.estilo = ttk.Style()
        self.estilo.configure("Treeview.Heading", font=("Arial", 10, BOLD))

        #Establece una ID a cada columna
        self.tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
        #Estilo para ajustar la fuente al Treeview
        self.tree.tag_configure('fuente', font=("Arial", 10))
        #Crea las Columnas del Treeview
        self.tree.column("#0", width=50, minwidth=50, anchor=W)
        self.tree.column("col1", width=80, minwidth=50, anchor=W)
        self.tree.column("col2", width=100, minwidth=50, anchor=W)
        self.tree.column("col3", width=80, minwidth=50, anchor=W)
        self.tree.column("col4", width=180, minwidth=50, anchor=W)
        self.tree.column("col5", width=180, minwidth=50, anchor=W)

        #Encabezados de Columnas del Treeview
        self.tree.heading("#0", text="Socio")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Apellido")
        self.tree.heading("col3", text="Edad")
        self.tree.heading("col4", text="Vencimiento apto médico")
        self.tree.heading("col5", text="Estado apto médico")

        self.tree.place(x = 10, y = 10)

        self.boton = Button(self.root, text = "Salir", height=1, width=10, bg='#0052cc', 
            fg='#ffffff', command=lambda:[self.salirAplicacion()]
            )
        self.boton.place(x = 600, y = 245)

        # Inicializo el treeview con los datos de la base de datos 
        # Entra al loop una unica vez
        if self.system_app.inicio == FALSE:
            self.system_app.inicio = TRUE
            self.abmc.actualizar_treeview(self.tree)
          
    def borrar_variables_control(self, ):
        self.nombre_socio.set("")
        self.apellido_socio.set("")
        self.edad_socio.set("")
        self.vencimiento_apto_medico.set("")

    def abm_socios_alta_win(self, ):
        self.tl = Toplevel(self.root, bg="white")
        self.tl.title("Alta socio")
        self.tl.geometry('310x170')
        self.tl['bg'] = '#49A'
        self.tl.focus_set()
        self.tl.grab_set()
        self.tl.transient(master=self.root)

        self.l2=Label(
            self.tl, text="Nombre del socio: ", anchor= W, bg="#49A", 
            fg='#ffffff', font=("Arial", 10)
            )
        self.l2.grid(padx=5, pady=5, column=0, row=1, sticky=W)
        self.e2=Entry(self.tl, textvariable=self.nombre_socio)
        self.e2.grid(padx=5, pady=5, column=1, row=1, sticky=W)

        self.l3=Label(
            self.tl, text="Apellido del socio: ", anchor= W, 
            bg="#49A", fg='#ffffff', font=("Arial", 10)
            )
        self.l3.grid(padx=5, pady=5, column=0, row=2, sticky=W)
        self.e3=Entry(self.tl, textvariable=self.apellido_socio)
        self.e3.grid(padx=5, pady=5, column=1, row=2, sticky=W)

        self.l1=Label(
            self.tl, text="Edad del socio: ", anchor= W, bg="#49A", 
            fg='#ffffff', font=("Arial", 10)
            )
        self.l1.grid(padx=5, pady=5, column=0, row=3, sticky=W)
        self.e1=Entry(self.tl, textvariable=self.edad_socio)
        self.e1.grid(padx=5, pady=5, column=1, row=3, sticky=W)

        self.l4=Label(
            self.tl, text="Vencimiento apto médico: ", anchor= W, bg="#49A", 
            fg='#ffffff', font=("Arial", 10)
            )
        self.l4.grid(padx=5, pady=5, column=0, row=4, sticky=W)
        self.e4=Entry(self.tl, textvariable=self.vencimiento_apto_medico)
        self.e4.grid(padx=5, pady=5, column=1, row=4, sticky=W)

        self.boton = Button(
            self.tl, text = "Dar de alta", bg='#0052cc', fg='#ffffff', 
            command=lambda:[self.abmc.guardar_nuevo_socio(self.tree, self.nombre_socio.get(), 
                self.apellido_socio.get(), self.edad_socio.get(), 
                self.vencimiento_apto_medico.get()), 
                self.borrar_variables_control(),
            self.tl.destroy()]
            )
        self.boton.grid(padx=5, pady=5, column=0, row=5)

        self.boton = Button(
            self.tl, text = "Cerrar", bg='#0052cc', fg='#ffffff', 
            command=lambda:[self.borrar_variables_control(), self.tl.destroy()]
            )
        self.boton.grid(padx=5, pady=5, column=1, row=5) 

    def abm_socios_baja_win(self, ):
        self.tl = Toplevel(self.root, bg="white")
        self.tl.title("Baja socio")
        self.tl.geometry('320x100')
        self.tl['bg'] = '#49A'
        self.tl.focus_set()
        self.tl.grab_set()
        self.tl.transient(master=self.root)

        self.l1=Label(
            self.tl, text="¿Desea dar de baja al socio seleccionado? ", 
            anchor= W, bg="#49A", fg='#ffffff', font=("Arial", 10)
            )
        self.l1.place(x = 27, y = 20)

        self.boton1 = Button(
            self.tl, text = "Dar de baja", height=1, width=10, bg='#0052cc', 
            fg='#ffffff', command=lambda:[self.abmc.borrar_socio(self.tree), 
            self.borrar_variables_control(), self.tl.destroy()]
            )
        self.boton1.place(x = 60, y = 60)

        self.boton2 = Button(
            self.tl, text = "Cerrar", height=1, width=10, bg='#0052cc', 
            fg='#ffffff', 
            command=lambda:[self.borrar_variables_control(), self.tl.destroy()]
            )
        self.boton2.place(x = 180, y = 60)

    def abm_socios_modificar_win(self, ):
        self.tl = Toplevel(self.root, bg="white")
        self.tl.title("Modificar socio")
        self.tl.geometry('310x170')
        self.tl['bg'] = '#49A'
        self.tl.focus_set()
        self.tl.grab_set()
        self.tl.transient(master=self.root)

        self.l2=Label(
            self.tl, text="Nombre del socio: ", anchor= W, bg="#49A", 
            fg='#ffffff', font=("Arial", 10)
            )
        self.l2.grid(padx=5, pady=5, column=0, row=1, sticky=W)
        self.e2=Entry(self.tl, textvariable=self.nombre_socio)
        self.e2.grid(padx=5, pady=5, column=1, row=1, sticky=W)

        self.l3=Label(
            self.tl, text="Apellido del socio: ", anchor= W, bg="#49A", 
            fg='#ffffff', font=("Arial", 10)
            )
        self.l3.grid(padx=5, pady=5, column=0, row=2, sticky=W)
        self.e3=Entry(self.tl, textvariable=self.apellido_socio)
        self.e3.grid(padx=5, pady=5, column=1, row=2, sticky=W)

        self.l1=Label(
            self.tl, text="Edad del socio: ", anchor= W, bg="#49A", fg='#ffffff', 
            font=("Arial", 10)
            )
        self.l1.grid(padx=5, pady=5, column=0, row=3, sticky=W)
        self.e1=Entry(self.tl, textvariable=self.edad_socio)
        self.e1.grid(padx=5, pady=5, column=1, row=3, sticky=W)

        self.l4=Label(
            self.tl, text="Vencimiento apto médico: ", anchor= W, bg="#49A", 
            fg='#ffffff', font=("Arial", 10)
            )
        self.l4.grid(padx=5, pady=5, column=0, row=4, sticky=W)
        self.e4=Entry(self.tl, textvariable=self.vencimiento_apto_medico)
        self.e4.grid(padx=5, pady=5, column=1, row=4, sticky=W)

        self.boton = Button(
            self.tl, text = "Modificar", height=1, width=10, bg='#0052cc', 
            fg='#ffffff', command=lambda:[self.abmc.modificar_socio_existente(self.tree, 
                self.nombre_socio.get(), self.apellido_socio.get(), self.edad_socio.get(), 
                self.vencimiento_apto_medico.get()), 
            self.borrar_variables_control(), self.tl.destroy()]
            )
        self.boton.grid(padx=5, pady=5, column=0, row=5)

        self.boton = Button(
            self.tl, text = "Cerrar", height=1, width=10, bg='#0052cc', 
            fg='#ffffff', command=lambda:[self.borrar_variables_control(), 
            self.tl.destroy()]
            )
        self.boton.grid(padx=5, pady=5, column=1, row=5) 

    def base_de_datos_win(self, ):
        self.tl = Toplevel(self.root)
        self.tl.title("Exportar base de datos a txt")
        self.tl.geometry('320x100')
        self.tl['bg'] = '#49A'
        self.tl.focus_set()
        self.tl.grab_set()
        self.tl.transient(master=self.root)

        self.l1=Label(
            self.tl, text="¿Desea exportar la base de datos a un archivo txt? ", 
            anchor= W, bg="#49A", fg='#ffffff', font=("Arial", 10)
            )
        self.l1.place(x = 10, y = 15)

        self.boton1 = Button(
            self.tl, text = "Exportar base", height=1, width=10, 
            bg='#0052cc', fg='#ffffff', command=lambda:[self.abmc.exportar_base_txt(), 
            self.tl.destroy()]
            )
        self.boton1.place(x = 60, y = 50)

        self.boton2 = Button(
            self.tl, text = "Cerrar", height=1, width=10, bg='#0052cc', 
            fg='#ffffff', command=lambda:[self.tl.destroy()]
            )
        self.boton2.place(x = 180, y = 50)

    def help_acercade_win(self, ):
        self.tl =Toplevel(self.root)
        self.tl['bg'] = '#49A'
        self.tl.title("Acerca de...")
        self.tl.geometry('195x150')
        self.tl.focus_set()
        self.tl.grab_set()
        self.tl.transient(master=self.root)
        
        str1 = "Python 3 - Nivel Intermedio\n\n Autor: Gaston Vallasciani"
        str2 = f"\n\n Versión de software: {self.system_app.version}" 
        str = str1 + str2
        self.label1 = Label(
            self.tl, text = str, anchor= W, bg="#49A", fg='#ffffff', 
            font=("Arial", 10)
            )
        self.label1.place(x = 15, y = 15)

        self.boton = Button(
            self.tl, text = "Cerrar" ,bg='#0052cc', fg='#ffffff',
            command=self.tl.destroy
            )
        self.boton.place(x = 75, y = 110)

    def salirAplicacion(self, ):
        valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
        if valor=="yes":
            self.root.destroy()
#------------------------------------------------------------------------------