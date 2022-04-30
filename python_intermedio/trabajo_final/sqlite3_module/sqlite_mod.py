import sqlite3

class DatabaseManager():
    def __init__(self) -> None:
        pass
         
    def crear_base(self,):
        con = sqlite3.connect("socios.db")
        return con

    def cerrar_base(self, con):
        con.close()

    def crear_tabla(self, con):
        cursor = con.cursor()
        sql = "CREATE TABLE IF NOT EXISTS socios(num_socio integer PRIMARY KEY, nombre text, apellido text, edad text, vencimiento_apto_medico text, estado_apto_medico text)"
        cursor.execute(sql)
        con.commit()

    def insertar(self, con, nombre, apellido, edad, vencimiento_apto_medico, estado_apto_medico):
        cursor = con.cursor()
        data = (str(nombre), str(apellido), str(edad), str(vencimiento_apto_medico), str(estado_apto_medico))
        sql = "INSERT INTO socios(nombre, apellido, edad, vencimiento_apto_medico, estado_apto_medico) VALUES(?, ?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()

    def borrar(self, con, num_socio):
        cursor = con.cursor()
        num_socio = int(num_socio)
        data = (num_socio,)
        sql = "DELETE from socios where num_socio = ?;"
        cursor.execute(sql, data)
        con.commit()

    def seleccionar(self, con, num_socio):
        row = ()
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

    def seleccionar_todos(self, con):
        sql = "SELECT * FROM socios ORDER BY num_socio ASC"
        cursor = con.cursor()
        data = cursor.execute(sql)
        return data.fetchall()

    def cantidad_registros(self, con):
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

    def actualizar(self, con, num_socio, nombre, apellido, edad, vencimiento_apto_medico, estado_apto_medico):
        cursor = con.cursor()
        num_socio = int(num_socio)
        data = (str(nombre), str(apellido), str(edad), str(vencimiento_apto_medico), str(estado_apto_medico), num_socio)
        sql = "UPDATE socios SET nombre=?, apellido=?, edad=?, vencimiento_apto_medico=?, estado_apto_medico=? WHERE num_socio=?;"
        cursor.execute(sql, data)
        con.commit()

