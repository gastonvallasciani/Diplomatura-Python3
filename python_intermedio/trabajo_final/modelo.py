#------------------------------------------------------------------------------
from sqlite3_module.sqlite_mod import DatabaseManager
from data_validation_module.data_validation_mod import dataValidationManager

from tkinter import messagebox

from pickle import TRUE
from pickle import FALSE

import datetime as date
#------------------------------------------------------------------------------
class Abmc():
    def __init__(self) -> None:
        self.objeto_db = DatabaseManager()
        self.objeto_data_val = dataValidationManager()

    def actualizar_treeview(self, mitreeview, db_local):
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)
        
        resultado = self.objeto_db.seleccionar_todos(db_local)

        for fila in resultado:
            print(fila)
            mitreeview.insert(
                "", " 0", text=fila[0], tag = 'fuente', 
                values=(fila[1], fila[2], fila[3], fila[4], fila[5])
                )

    def item_seleccionado_treeview(self, mitreeview):
        item = mitreeview.focus()
        if item != "":
            num_socio = mitreeview.item(item, option="text")
            return num_socio

    def modificar_socio_existente(self, treeview, db_local, nombre_socio_local, 
        apellido_socio_local, edad_socio_local, 
        vencimiento_apto_medico_local = None):

        estado_apto_medico_local = "NO PRESENTADO"
        
        guardar_cliente = FALSE
        
        num_socio_a_modificar = self.item_seleccionado_treeview(treeview)
        if num_socio_a_modificar:
            str_aux = vencimiento_apto_medico_local

            if self.objeto_data_val.validar_letras(nombre_socio_local) == FALSE:
                guardar_cliente = FALSE
                str_aux_2 = " No se ha cargado el nombre del socio de forma correcta"
                messagebox.showwarning(message=str_aux_2)
            elif self.objeto_data_val.validar_letras(nombre_socio_local) == FALSE:
                guardar_cliente = FALSE
                str_aux_2 = " No se ha cargado el apellido del socio de forma correcta"
                messagebox.showwarning(message=str_aux_2)
            elif self.objeto_data_val.validar_numeros(edad_socio_local) == FALSE:
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
                if self.objeto_data_val.validar_fecha(str_aux) == TRUE:
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
                        estado_apto_medico_local = "VENCIDO"
                    else:
                        estado_apto_medico_local = "VIGENTE"
                else:
                    guardar_cliente = FALSE
                    str_aux_2 = " El formato de fecha ingresado es incorrecto"
                    messagebox.showwarning(message=str_aux_2)
        else:
            str_aux_2 = "No se ha modificado el socio "
            str_aux_2 = str_aux_2 + "ya que no ha seleccionado ninguno!"
            messagebox.showwarning(message=str_aux_2)

        if(guardar_cliente == TRUE):
            self.objeto_db.actualizar(
                db_local, num_socio_a_modificar, nombre_socio_local, 
                apellido_socio_local, edad_socio_local, 
                vencimiento_apto_medico_local, estado_apto_medico_local
                )
            self.actualizar_treeview(treeview, db_local)
            messagebox.showinfo(message="El socio ha sido modificado exitosamente!")
        else:
            str_aux_2 = " El socio no ha sido modificado "
            str_aux_2 = str_aux_2 + "por un error en la carga de datos"
            messagebox.showwarning(message=str_aux_2)

    def borrar_socio(self, treeview, db_local):
        num_socio_a_borrar = self.item_seleccionado_treeview(treeview)
        if num_socio_a_borrar:
            self.objeto_db.borrar(db_local, num_socio_a_borrar)
            self.actualizar_treeview(treeview, db_local)
        else:
            str_aux = "No se ha borrado el socio ya que no ha seleccionado ninguno!"
            messagebox.showwarning(message=str_aux)

    def guardar_nuevo_socio(self, treeview, db_local, nombre_socio_local, 
        apellido_socio_local, edad_socio_local, 
        vencimiento_apto_medico_local = None):
    
        guardar_cliente = FALSE

        estado_apto_medico_local = "NO PRESENTADO"

        str_aux = vencimiento_apto_medico_local

        if self.objeto_data_val.validar_letras(nombre_socio_local) == FALSE:
            guardar_cliente = FALSE
            str_aux_2 = " No se ha cargado el nombre del socio de forma correcta"
            messagebox.showwarning(message=str_aux_2)
        elif self.objeto_data_val.validar_letras(nombre_socio_local) == FALSE:
            guardar_cliente = FALSE
            str_aux_2 = " No se ha cargado el apellido del socio de forma correcta"
            messagebox.showwarning(message=str_aux_2)
        elif self.objeto_data_val.validar_numeros(edad_socio_local) == FALSE:
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
            if self.objeto_data_val.validar_fecha(str_aux) == TRUE:
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
                # estado_apto_medico_local.set("VENCIDO")
                    estado_apto_medico_local = "VENCIDO"
                else:
                # estado_apto_medico_local.set("VIGENTE")
                    estado_apto_medico_local = "VIGENTE"
            else:
                guardar_cliente = FALSE
                str_aux_2 = " El formato de fecha ingresado es incorrecto"
                messagebox.showwarning(message=str_aux_2)

        if(guardar_cliente == TRUE):
            self.objeto_db.insertar(
                db_local, nombre_socio_local, apellido_socio_local, 
                edad_socio_local, vencimiento_apto_medico_local, 
                estado_apto_medico_local
                )
            self.actualizar_treeview(treeview, db_local)
            messagebox.showinfo(message="El socio ha sido guardado exitosamente!")
        else:
            str_aux_2=" El socio no ha sido cargado "
            str_aux_2 = str_aux_2 + "por un error en la carga de datos"
            messagebox.showwarning(message=str_aux_2)
    
    def exportar_base_txt(self, db_local):
        cantidad_de_registros_local = self.objeto_db.cantidad_registros(db_local)
        archivo = open("base_de_datos_socios.txt","w")
        for counter in range(1, cantidad_de_registros_local+1):
            data_from_db = self.objeto_db.seleccionar(db_local, counter)
            if data_from_db != ():
                str = f"Numero de socio: {data_from_db[0]},"
                str = str + f"nombre: {data_from_db[1]}, apellido: {data_from_db[2]},"
                str = str + f"edad: {data_from_db[3]},"
                str = str + f"vencimiento apto medico: {data_from_db[4]},"
                str = str + f"estado apto medico: {data_from_db[5]}\n"
                archivo.write(str)
        archivo.close()
#------------------------------------------------------------------------------
