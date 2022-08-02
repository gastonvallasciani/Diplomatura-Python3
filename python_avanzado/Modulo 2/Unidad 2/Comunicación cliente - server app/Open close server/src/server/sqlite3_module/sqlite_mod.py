"""
sqlite_mod.py

Modulo utilizado para interactuar con la base de datos SQLite3.
"""
import sqlite3
#------------------------------------------------------------------------------
__author__ = "Gastón Vallasciani"
__maintainter__ = "Gastón Vallasciani"
__email__ = "gastonvallasciani@gmail.com"
__copyright__ = "Copyright 2022"
__version__ = "0.1"
#------------------------------------------------------------------------------
class DatabaseManager():
    def __init__(self):
        pass

    def __str__(self,):
        return("Clase DatabaseMaanger()")
         
    def crear_base(self,):
        """
        Se conecta con la base de datos de nobmre socios.db.

        :returns: objeto de conexion
        """
        con = sqlite3.connect("socios.db")
        return con

    def cerrar_base(self):
        con = self.crear_base()
        con.close()

    def crear_tabla(self):
        """
        Crea la tabla de nombre "socios" en la base de datos si no existe.
        """
        con = self.crear_base()
        cursor = con.cursor()
        sql = "CREATE TABLE socios(num_socio integer PRIMARY KEY, nombre text, apellido text, edad text, vencimiento_apto_medico text, estado_apto_medico text)"
        cursor.execute(sql)
        con.commit()

    def iniciar_base(self, ):
        """
        Inicia la base de datos.
        """
        print("Iniciando base de datos")
        try:
            self.crear_base()
            self.crear_tabla()
        except sqlite3.OperationalError as op_error:
            print("Error capturado: ", op_error)
        else:
            print("Base de datos y tabla creadas correctamente")
        finally:
            print("Finalizo el inicio de la base de datos")

    def insertar(self, nombre, apellido, edad, vencimiento_apto_medico, estado_apto_medico):
        """
        Inserta un nuevo registro en la base de datos.

        :nombre: nombre de socio a insertar en la tabla de la base de datos.
        :apellido: apellido de socio a insertar en la tabla de la base de datos.
        :vencimiento_apto_medico: vencimiento del apto medico a insertar en la tabla de la base de datos.
        :estado_apto_medico: estado del apto medico a insertar en la tabla de la base de datos.
        """
        con = self.crear_base()
        cursor = con.cursor()
        data = (str(nombre), str(apellido), str(edad), str(vencimiento_apto_medico), str(estado_apto_medico))
        sql = "INSERT INTO socios(nombre, apellido, edad, vencimiento_apto_medico, estado_apto_medico) VALUES(?, ?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
    
    def borrar(self, num_socio):
        """
        Borra un registro de la tabla "socios" de la base de datos.

        :num_socio: numero de socio a borrar.
        """
        con = self.crear_base()
        cursor = con.cursor()
        num_socio = int(num_socio)
        data = (num_socio,)
        sql = "DELETE from socios where num_socio = ?;"
        cursor.execute(sql, data)
        con.commit()

    def seleccionar(self, num_socio):
        """
        Selecciona un registro de la tabla "socios" de la base de datos.

        :num_socio: numero de socio a borrar.
        """
        row = ()
        con = self.crear_base()
        cursor = con.cursor()
        num_socio = int(num_socio)
        data = (num_socio,)
        # Ejecuta el fetch todas las columnas de la tabla de la fila num_socio
        sql = "SELECT * FROM socios WHERE num_socio =?;"
        cursor.execute(sql, data)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
        #if row == ():
        # devuelvo la tupla vacia porque no hay info en la posicion del registro
        # de la base de datos
        #    row = (num_socio,"","","","","")
        return row

    def seleccionar_todos(self,):
        """
        selecciona todos registros de la tabla "socios" de la base de datos.
        """
        sql = "SELECT * FROM socios ORDER BY num_socio ASC"
        con = self.crear_base()
        cursor = con.cursor()
        data = cursor.execute(sql)
        return data.fetchall()

    def cantidad_registros(self,):
        """
        Calcula y devuelve la cantidad de registros presentes en la tabla "socios" de la base de datos.

        :returns: cantidad de rergistros en la base de datos si no es vacio.
        """
        con = self.crear_base()
        cursor = con.cursor()
        #sql = "SELECT COUNT(*) FROM socios;"
        sql = "SELECT MAX(num_socio) FROM socios;"
        cursor.execute(sql)
        cantidad_de_registros = cursor.fetchone()
        print(f"La cantidad de registros en la base de datos es: {cantidad_de_registros}", cantidad_de_registros)
        if cantidad_de_registros != (None,):
            return cantidad_de_registros[0]
        else:
            return 0
    def actualizar(self, num_socio, nombre, apellido, edad, vencimiento_apto_medico, estado_apto_medico):
        """
        Actualiza un registro en la tabla "socios" de la base de datos.

        :num_socio: numero de socio a modificar.
        :nombre: nombre de socio a modificar.
        :apellido: apellido de socio a modificar.
        :vencimiento_apto_medico: vencimiento del apto medico a modificar.
        :estado_apto_medico: estado del apto medico a modificar.
        """
        con = self.crear_base()
        cursor = con.cursor()
        num_socio = int(num_socio)
        data = (str(nombre), str(apellido), str(edad), str(vencimiento_apto_medico), str(estado_apto_medico), num_socio)
        sql = "UPDATE socios SET nombre=?, apellido=?, edad=?, vencimiento_apto_medico=?, estado_apto_medico=? WHERE num_socio=?;"
        cursor.execute(sql, data)
        con.commit()
#------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Version del modulo: ", __version__)
    print("Autor: ", __author__)
#------------------------------------------------------------------------------
