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

from modelo import borrar_variables_control

from modelo import Abmc
#------------------------------------------------------------------------------
app_version = "1.0.0"
inicio = FALSE
#-----------------------------------------------------------------------------
class Panel():
    def __init__(self, window):
        self.root = window
        self.abmc = Abmc()

        try:
            self.db = self.abmc.objeto_db.crear_base()
            self.abmc.objeto_db.crear_tabla(self.db)
        except:
            print("error")
        #-----------------------------------------------------------------------------
        global  app_version 
        global inicio

        self.root.title("GYM MANAGER")
        self.root.geometry("690x285")
        self.root['bg'] = '#49A'
    #------------------------------------------------------------------------------
    # Declaro variables de tkinter
        self.edad_socio = StringVar() 
        self.nombre_socio = StringVar()
        self.apellido_socio = StringVar()
        self.vencimiento_apto_medico = StringVar()
    #------------------------------------------------------------------------------
        """
        Ventana hija para dar de baja un socio
        """
        def abm_socios_baja_win():
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
                fg='#ffffff', command=lambda:[self.abmc.borrar_socio(self.tree, self.db), 
                borrar_variables_control(self.nombre_socio, self.apellido_socio, self.edad_socio, 
                    self.vencimiento_apto_medico), self.tl.destroy()]
                )
            self.boton1.place(x = 60, y = 60)

            self.boton2 = Button(
                self.tl, text = "Cerrar", height=1, width=10, bg='#0052cc', 
                fg='#ffffff', 
                command=lambda:[borrar_variables_control(self.nombre_socio, self.apellido_socio, 
                    self.edad_socio, self.vencimiento_apto_medico), self.tl.destroy()]
                )
            self.boton2.place(x = 180, y = 60)
        #------------------------------------------------------------------------------
        """
        Ventana hija para dar de alta al nuevo socio
        """
        def abm_socios_alta_win():
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
                command=lambda:[self.abmc.guardar_nuevo_socio(self.tree, self.db, self.nombre_socio.get(), 
                    self.apellido_socio.get(), self.edad_socio.get(), 
                    self.vencimiento_apto_medico.get()), 
                    borrar_variables_control(self.nombre_socio, self.apellido_socio, 
                    self.edad_socio, self.vencimiento_apto_medico),
                self.tl.destroy()]
                )
            self.boton.grid(padx=5, pady=5, column=0, row=5)

            self.boton = Button(
                self.tl, text = "Cerrar", bg='#0052cc', fg='#ffffff', 
                command=lambda:[borrar_variables_control(self.nombre_socio, self.apellido_socio, 
                    self.edad_socio, self.vencimiento_apto_medico), self.tl.destroy()]
                )
            self.boton.grid(padx=5, pady=5, column=1, row=5)
        #------------------------------------------------------------------------------
        """
        Ventana hija para modificar un socio existente
        """
        def abm_socios_modificar_win():
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
                fg='#ffffff', command=lambda:[self.abmc.modificar_socio_existente(self.tree, self.db, 
                    self.nombre_socio.get(), self.apellido_socio.get(), self.edad_socio.get(), 
                    self.vencimiento_apto_medico.get()), 
                borrar_variables_control(self.nombre_socio, self.apellido_socio, 
                    self.edad_socio, self.vencimiento_apto_medico), self.tl.destroy()]
                )
            self.boton.grid(padx=5, pady=5, column=0, row=5)

            self.boton = Button(
                self.tl, text = "Cerrar", height=1, width=10, bg='#0052cc', 
                fg='#ffffff', command=lambda:[borrar_variables_control(self.nombre_socio, 
                    self.apellido_socio, self.edad_socio, self.vencimiento_apto_medico), 
                self.tl.destroy()]
                )
            boton.grid(padx=5, pady=5, column=1, row=5)
        #------------------------------------------------------------------------------
        """
        Ventana hija para exportar la base de datos a un archivo txt
        """
        def base_de_datos_win():
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
                bg='#0052cc', fg='#ffffff', command=lambda:[self.abmc.exportar_base_txt(self.db), 
                self.tl.destroy()]
                )
            self.boton1.place(x = 60, y = 50)

            self.boton2 = Button(
                self.tl, text = "Cerrar", height=1, width=10, bg='#0052cc', 
                fg='#ffffff', command=lambda:[self.tl.destroy()]
                )
            self.boton2.place(x = 180, y = 50)
        #------------------------------------------------------------------------------
        self.menubar=Menu(self.root)

        self.menu_db = Menu(self.menubar, tearoff=0)
        self.menu_db.add_command(
            label = "Exportar base de datos", command = base_de_datos_win
            )
        self.menubar.add_cascade(label = "Base de datos", menu = self.menu_db)

        self.menu_abm_socios = Menu(self.menubar, tearoff=0)
        self.menu_abm_socios.add_command(
            label = "Nuevo socio", command = abm_socios_alta_win
            )
        self.menu_abm_socios.add_command(
            label = "Baja de socio", command = abm_socios_baja_win
            )
        self.menu_abm_socios.add_command(label = "Modificación información de socio", 
            command = abm_socios_modificar_win)
        self.menubar.add_cascade(label = "Socios", menu = self.menu_abm_socios)

        self.menu_ayuda = Menu(self.menubar, tearoff=0)
        self.menu_ayuda.add_command(label = "Acerca de...", command = lambda:[help_acercade_win()])
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

        boton = Button(self.root, text = "Salir", height=1, width=10, bg='#0052cc', 
            fg='#ffffff', command=lambda:[salirAplicacion()]
            )
        boton.place(x = 600, y = 245)

        # Inicializo el treeview con los datos de la base de datos 
        # Entra al loop una unica vez
        if inicio == FALSE:
            inicio = TRUE
            self.abmc.actualizar_treeview(self.tree, self.db)

        #----------------------------------------------------------------------------
        """
        Ventana hija para preguntar la version de software
        """
        def help_acercade_win():
            global app_version

            self.tl =Toplevel(self.root)
            self.tl['bg'] = '#49A'
            self.tl.title("Acerca de...")
            self.tl.geometry('195x150')
            self.tl.focus_set()
            self.tl.grab_set()
            self.tl.transient(master=self.root)
            
            str1 = "Python 3 - Nivel Inicial\n\n Autor: Gaston Vallasciani"
            str2 = f"\n\n Versión de software: {app_version}" 
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
        #------------------------------------------------------------------------------
        def salirAplicacion():
            valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")
            if valor=="yes":
                self.root.destroy()